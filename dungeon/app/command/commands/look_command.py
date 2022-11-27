from dungeon.app.command.action_result import WithCost
from dungeon.app.command.command import Command
from dungeon.app.domain.player import EnergyUnit


class LookCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def do(self, receiver):
        return WithCost(receiver.look(self._argument), EnergyUnit(1))

    def _name(self):
        return "look"
