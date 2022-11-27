from dungeon.app.command.action_result import ActionResult, WithCost
from dungeon.app.command.command import Command
from dungeon.app.domain.player import EnergyUnit


class InvalidCommand(Command):
    def __init__(self, user_input):
        super().__init__(user_input)

    def do(self, dungeon):
        return WithCost(ActionResult.player_acted("I don't understand"), EnergyUnit(1))

    def __str__(self) -> str:
        return "You said: {}".format(self._argument)
