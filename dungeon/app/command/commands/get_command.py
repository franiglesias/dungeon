from dungeon.app.command.action_result import ActionResult
from dungeon.app.command.command import Command
from dungeon.app.domain.player.energy import EnergyUnit


class GetCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def do(self, receiver):
        receiver.get(self._argument)
        result = ActionResult("Got thing")
        result.set('cost', EnergyUnit(1))
        return result

    def name(self):
        return "get"
