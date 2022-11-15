from dungeon.dungeon import Dungeon


class Game:
    def __init__(self):
        self.dungeon = None

    def start(self, dungeon=Dungeon()):
        self.dungeon = dungeon

    def do_command(self, command):
        return command.do(self.dungeon)
