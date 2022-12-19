from dungeon.app.domain.player.energy import EnergyUnit, Energy
from dungeon.app.domain.player.player_events import PlayerDied, PlayerEnergyChanged, PlayerSentCommand, \
    ActionNotCompleted, PlayerAwake, BackPackChanged
from dungeon.app.events.subject import Subject


class Backpack:
    def __init__(self):
        self._items = dict()

    def append(self, item):
        self._items[item.name().lower()] = item

    def content(self):
        content = []
        for key, item in self._items.items():
            content.append(item.name())

        return ", ".join(content)

    def get(self, thing_name):
        if thing_name.lower() in self._items.keys():
            return self._items.pop(thing_name.lower())

class Player:
    def __init__(self, starting_energy=EnergyUnit(100)):
        self._energy = Energy(starting_energy)
        self._subject = Subject()
        self._receiver = None
        self._holds = None
        self._last_command = None
        self._backpack = Backpack()

    def awake_in(self, dungeon):
        dungeon.register(self)
        self._receiver = dungeon
        self._notify_observers(PlayerAwake())

    def do(self, command):
        self._execute_command(command, self._receiver)
        self._update_energy()

    def _execute_command(self, command, receiver):
        command.do(self)
        command.do(receiver)
        self._last_command = command
        self._notify_observers(PlayerSentCommand(command.name(), command.argument()))

    def holds(self):
        return self._holds

    def use(self, thing_name):
        if self._holds is None:
            self._notify_observers(ActionNotCompleted("You need an object to use it."))
            return
        if self._holds.name().lower() != thing_name.lower():
            return
        self._holds.apply_on(self)
        self._holds = None

    def get(self, thing_name):
        self._holds = self._backpack.get(thing_name)

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

    def register(self, observer):
        self._subject.register(observer)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)

    def notify(self, event):
        if "player_got_thing" == event.name():
            self._holds = event.thing()
        if "player_collected_thing" == event.name():
            self._backpack.append(event.thing())
            self._notify_observers(BackPackChanged(self._backpack.content()))
