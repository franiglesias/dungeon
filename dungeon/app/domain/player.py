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
        self._last_message = "I'm ready"
        self._energy = Energy(starting_energy)
        self._exited = False

    @classmethod
    def awake(cls):
        return cls(EnergyUnit(100))

    @classmethod
    def awake_with_energy(cls, starting_energy):
        return cls(starting_energy)

    def do(self, command, receiver):
        result = command.do(receiver)
        self._energy.decrease(result.cost())
        self._exited = result.is_finished()
        self._last_message = result.get("message")

    def is_alive(self):
        return self._energy.is_alive()

    def has_won(self):
        return self._exited

    def said(self):
        return "{message}\nRemaining energy: {energy}".format(message=self._last_message, energy=self._energy)
