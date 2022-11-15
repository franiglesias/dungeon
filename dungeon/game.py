from dungeon.command.action_result import ActionResult
from dungeon.dungeon import Dungeon


class Game:
    def __init__(self):
        self.dungeon = None

    def start(self):
        self.dungeon = Dungeon()

    def do_command(self, command):
        result = command.do_deprecated(self.dungeon)
        return ActionResult(result)
