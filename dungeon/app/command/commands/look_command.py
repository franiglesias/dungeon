from dungeon.app.command.command import Command
from dungeon.app.domain.player.energy import EnergyUnit


class LookCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def do(self, receiver):
        result = receiver.look(self._argument)
        result.set('cost', EnergyUnit(1))
        return result

    def name(self):
        return "look"
