from dungeon.app.command.command import Command
from dungeon.app.domain.dir import Dir
from dungeon.app.domain.player.backpack import Backpack
from dungeon.app.domain.player.energy import EnergyUnit, Energy
from dungeon.app.domain.player.hand import EmptyHand, ObjectNotFound
from dungeon.app.domain.player.player_events import PlayerDied, PlayerEnergyChanged, PlayerSentCommand, \
    ActionNotCompleted, PlayerAwake, BackpackChanged, PlayerGotThing, PlayerCollectedThing, ThingInHandChanged, \
    PlayerFinishedGame
from dungeon.app.domain.thing import Key
from dungeon.app.events.subject import CanBeObserved, Observer
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
        command.do(self)
        command.do(receiver)
        self._last_command = command
        self._notify_observers(PlayerSentCommand(command.name(), command.argument()))

    def holds(self):
        if self._toggles.is_active("hand"):
            return self._hand.holds()
        else:
            return self._holds

    def use(self, thing_name):
        if self._toggles.is_active("hand"):
            pass
        else:
            if self._holds is None:
                self._notify_observers(ActionNotCompleted("You need an object to use it."))
                return
            if self._is_a_different_object(thing_name):
                return
            self._holds = self._holds.apply_on(self)

    def open(self, door_dir):
        if self._toggles.is_active("hand"):
            pass
        else:
            if self._holds is None:
                self._notify_observers(ActionNotCompleted("You need a key to open something."))
                return
            if not isinstance(self._holds, Key):
                self._notify_observers(ActionNotCompleted("You need a key to open something."))
                return
            self._holds = self._holds.apply_on(self._receiver.door(Dir(door_dir)))

    def _is_a_different_object(self, thing_name):
        return not self._holds.is_named(thing_name)

    def get(self, thing_name):
        if self._toggles.is_active("hand"):
            try:
                self._hand = self._hand.get_from(self._backpack, thing_name)
                self._notify_observers(BackpackChanged(self._backpack.inventory()))
                self._notify_observers(ThingInHandChanged(self._hand.holds().name()))
            except ObjectNotFound:
                try:
                    self._hand = self._hand.get_from(self._receiver, thing_name)
                    self._notify_observers(ThingInHandChanged(self._hand.holds().name()))
                except ObjectNotFound:
                    self._notify_observers(ActionNotCompleted("{} not in backpack or cell".format(thing_name)))
        else:
            thing = self._backpack.get(thing_name)
            if thing is None:
                return
            if self._holds is not None:
                try:
                    self._backpack.keep(self._holds)
                    self._holds = None
                except IndexError:
                    self._notify_observers(ActionNotCompleted("Your backpack is full."))
            self._holds = thing
            self._notify_observers(BackpackChanged(self._backpack.inventory()))
            self._notify_observers(ThingInHandChanged(self._holds.name()))

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
        if event.of_type(PlayerGotThing):
            self._do_get_thing(event)
        if event.of_type(PlayerCollectedThing):
            self.do_collect_thing(event)

    def do_collect_thing(self, event):
        try:
            self._backpack.keep(event.thing())
            self._notify_observers(BackpackChanged(self._backpack.inventory()))
        except IndexError:
            self._notify_observers(ActionNotCompleted("Your backpack is full."))

    def _do_get_thing(self, event):
        if self._toggles.is_active("hand"):
            pass
        else:
            if self._holds is not None:
                self._receiver.drop(self._holds)
                self._holds = None
            self._holds = event.thing()
            self._notify_observers(ThingInHandChanged(self._holds.name()))
