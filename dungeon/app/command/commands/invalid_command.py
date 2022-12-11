from dungeon.app.command.action_result import ActionResult
from dungeon.app.command.command import Command


class InvalidCommand(Command):
    def __init__(self, user_input):
        super().__init__(user_input)

    def do(self, dungeon):
        return ActionResult.player_acted("I don't understand")

    def __str__(self) -> str:
        return "You said: {}".format(self._argument)
