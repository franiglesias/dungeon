from dungeon.app.domain.player.energy import EnergyUnit


class Command:

    def __init__(self, argument):
        self._argument = argument

    def do(self, receiver):
        pass

    def name(self):
        return None

    def cost(self):
        return EnergyUnit(1)

    def argument(self):
        if hasattr(self, "_argument"):
            return self._argument

        return ""
