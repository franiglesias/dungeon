from dungeon.app.command.action_result import ActionResult
from dungeon.app.command.command import Command
from dungeon.app.domain.player import EnergyUnit


class InvalidCommand(Command):
    def __init__(self, user_input):
        super().__init__(user_input)

    def do(self, dungeon):
        result = ActionResult.player_acted("I don't understand")
        result.set('cost', EnergyUnit(1))
        return result

    def __str__(self) -> str:
        return "You said: {}".format(self._argument)
