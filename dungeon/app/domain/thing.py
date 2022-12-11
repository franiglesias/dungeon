from dungeon.app.domain.player.energy import EnergyUnit


class Thing:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def apply_on(self, user):
        user.increase_energy(EnergyUnit(10))
