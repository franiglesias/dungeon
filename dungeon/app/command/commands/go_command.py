from dungeon.app.command.command import Command
from dungeon.app.domain.player.energy import EnergyUnit


class GoCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def do(self, receiver):
        return receiver.go(self._argument)

    def cost(self):
        return EnergyUnit(5)

    def name(self):
        return "go"
