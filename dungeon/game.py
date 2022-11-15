from dungeon.command.action_result import ActionResult
from dungeon.command.command import Command
from dungeon.dungeon import Dungeon


class Game:
    def __init__(self):
        self.dungeon = None

    def start(self):
        self.dungeon = Dungeon()

    def do_command_deprecate(self, command):
        return command.do(self.dungeon)

    def do_command(self, command):
        result = self.do_command_deprecate(command)
        return ActionResult(result)
