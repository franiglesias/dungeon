class EnergyUnit:
    def __init__(self, value):
        self._value = value

    def is_lower_than(self, other):
        return self._value < other.value()

    def value(self):
        return self._value

    def subtract(self, delta):
        return EnergyUnit(self._value - delta.value())

    def __eq__(self, other):
        return self._value == other.value()


class Energy:
    def __init__(self, starting_energy):
        self._energy = starting_energy

    def is_dead(self):
        return self._energy.is_lower_than(EnergyUnit(1))

    def decrease(self, delta):
        self._energy = self._energy.subtract(delta)

    def __str__(self):
        return str(self._energy.value())

    def current(self):
        return self._energy
