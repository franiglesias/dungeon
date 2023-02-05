from dungeon.app.domain.command.command import Command
from dungeon.app.domain.dir import Dir
from dungeon.app.domain.player.backpack import Backpack
from dungeon.app.domain.player.energy import EnergyUnit, Energy
from dungeon.app.domain.player.hand import EmptyHand, ObjectNotFound, DoNotHaveThatObject, ObjectIsNotKey
from dungeon.app.domain.player.player_events import PlayerDied, PlayerEnergyChanged, PlayerSentCommand, \
    ActionNotCompleted, PlayerAwake, BackpackChanged, PlayerCollectedThing, ThingInHandChanged, \
    PlayerFinishedGame
from dungeon.app.domain.events.subject import CanBeObserved, Observer
from dungeon.app.toggles.toggles import Toggles


class Player(CanBeObserved, Observer):
    def __init__(self, starting_energy=EnergyUnit(100), toggles=Toggles()):
        super().__init__()
        self._toggles = toggles
        self._energy = Energy(starting_energy)
        self._receiver = None
        self._holds = None
        self._last_command = None
        self._backpack = Backpack()
        self._hand = EmptyHand()

    def awake_in(self, dungeon):
        dungeon.register(self)
        self._receiver = dungeon
        self._notify_observers(PlayerAwake())

    def do(self, command: Command):
        self._execute_command(command, self._receiver)
        self._update_energy()

    def bye(self, *args):
        self._notify_observers(PlayerFinishedGame())

    def _execute_command(self, command, receiver):
        if not hasattr(command, 'do'):
            return
        command.do(self)
        command.do(receiver)
        self._last_command = command
        self._notify_observers(PlayerSentCommand(command.name(), command.argument()))

    def holds(self):
        return self._hand.holds()

    def use(self, thing_name):
        try:
            self._hand = self._hand.use_thing_with(thing_name, self)
        except ObjectNotFound:
            self._notify_observers(ActionNotCompleted("You need an object to use it."))
        except DoNotHaveThatObject:
            self._notify_observers(ActionNotCompleted("You don't have that object."))

    def open(self, door_dir):
        try:
            self._hand.open_with_key(self._receiver.door(Dir(door_dir)))
        except DoNotHaveThatObject:
            self._notify_observers(ActionNotCompleted("You need the right key."))
        except ObjectIsNotKey:
            self._notify_observers(ActionNotCompleted("You need a key to open doors."))

    def get(self, thing_name):
        try:
            self._hand = self._hand.get_from(self._backpack, thing_name)
            self._notify_observers(BackpackChanged(self._backpack.inventory()))
            self._notify_observers(ThingInHandChanged(self._hand.holds().name().to_s()))
        except ObjectNotFound:
            try:
                self._hand = self._hand.get_from(self._receiver, thing_name)
                self._notify_observers(ThingInHandChanged(self._hand.holds().name().to_s()))
            except ObjectNotFound:
                self._notify_observers(ActionNotCompleted("{} not in backpack or cell".format(thing_name)))

    def increase_energy(self, delta_energy):
        self._energy.increase(delta_energy)

    def _update_energy(self):
        self._energy.decrease(self._last_action_cost())
        self._notify_observers(PlayerEnergyChanged(self._energy.current()))
        if self._energy.is_dead():
            self._notify_observers(PlayerDied())

    def _last_action_cost(self):
        if self._last_command is not None:
            if hasattr(self._last_command, "cost"):
                return self._last_command.cost()

    def notify(self, event):
        if event.of_type(PlayerCollectedThing):
            self.do_collect_thing(event)

    def do_collect_thing(self, event):
        try:
            self._backpack.keep(event.thing())
            self._notify_observers(BackpackChanged(self._backpack.inventory()))
        except IndexError:
            self._notify_observers(ActionNotCompleted("Your backpack is full."))
