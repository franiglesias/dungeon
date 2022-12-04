from dungeon.app.command.action_result import ActionResult
from dungeon.app.events.subject import Subject


class EnergyUnit:
    def __init__(self, value):
        self._value = value

    def is_greater_than(self, other):
        return self._value > other.value()

    def value(self):
        return self._value

    def subtract(self, delta):
        return EnergyUnit(self._value - delta.value())

    def __eq__(self, other):
        return self._value == other.value()


class Energy:
    def __init__(self, starting_energy):
        self._energy = starting_energy

    def is_alive(self):
        return self._energy.is_greater_than(EnergyUnit(0))

    def decrease(self, delta):
        self._energy = self._energy.subtract(delta)

    def __str__(self):
        return str(self._energy.value())

    def current(self):
        return self._energy


class Player:
    def __init__(self, starting_energy):
        self._energy = Energy(starting_energy)
        self._last_result = ActionResult.player_acted("I'm ready")
        self._subject = Subject()

    @classmethod
    def awake(cls):
        return cls(EnergyUnit(100))

    @classmethod
    def awake_with_energy(cls, starting_energy):
        return cls(starting_energy)

    def do(self, command, receiver):
        self._execute_command(command, receiver)
        self._update_energy()

    def _execute_command(self, command, receiver):
        self._last_result = command.do(receiver)
        self._notify_observers(PlayerSentCommand(command.name(), command.argument()))
        self._notify_observers(PlayerGotDescription(self._last_result.get('message')))

    def _update_energy(self):
        self._energy.decrease(self._last_action_cost())
        self._notify_observers(PlayerEnergyChanged(self._energy.current()))
        self._last_result.set("energy", str(self._energy))

    def _last_action_cost(self):
        return self._last_result.get("cost")

    def last_result(self):
        return self._last_result

    def is_alive(self):
        return self._energy.is_alive()

    def has_won(self):
        return self._last_result.get("exited")

    def register(self, observer):
        self._subject.register(observer)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)


class PlayerEnergyChanged:
    def __init__(self, updated_energy):
        self._updated_energy = updated_energy

    def name(self):
        return "player_energy_changed"

    def energy(self):
        return self._updated_energy


class PlayerSentCommand:
    def __init__(self, command, argument):
        self._command = command
        self._argument = argument

    def name(self):
        return "player_sent_command"

    def command(self):
        return self._command

    def argument(self):
        return self._argument


class PlayerGotDescription:
    def __init__(self, description):
        self._description = description

    def name(self):
        return "player_got_description"

    def description(self):
        return self._description
