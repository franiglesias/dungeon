from dungeon.app.command.action_result import ActionResult


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


class Player:
    def __init__(self, starting_energy):
        self._energy = Energy(starting_energy)
        self._last_result = ActionResult.player_acted("I'm ready")

    @classmethod
    def awake(cls):
        return cls(EnergyUnit(100))

    @classmethod
    def awake_with_energy(cls, starting_energy):
        return cls(starting_energy)

    def do(self, command, receiver):
        self._last_result = command.do(receiver)
        self._energy.decrease(self._last_action_cost())
        self._last_result.set("energy", str(self._energy))

    def _last_action_cost(self):
        return self._last_result.get("cost")

    def last_result(self):
        return self._last_result

    def is_alive(self):
        return self._energy.is_alive()

    def has_won(self):
        return self._last_result.get("exited")
