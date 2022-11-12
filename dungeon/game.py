from dungeon.command.command import Command
from dungeon.dungeon import Dungeon


class Game:
    def __init__(self):
        self.dungeon = None

    def start(self):
        self.dungeon = Dungeon()

    def execute(self, instruction):
        c = Command.from_user_input(instruction)

        result = c.do(self.dungeon)

        return result
