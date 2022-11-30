from dungeon.app.command.command import Command
from dungeon.app.domain.player import EnergyUnit


class GoCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def do(self, receiver):
        result = receiver.go(self._argument)
        result.set('cost', EnergyUnit(5))
        return result

    def _name(self):
        return "go"
