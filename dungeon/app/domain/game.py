class Game:
    def __init__(self, dungeon=None):
        self.dungeon = dungeon

    def do_command(self, command):
        return command.do(self.dungeon)
