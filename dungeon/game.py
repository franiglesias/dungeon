from dungeon.dungeon import Dungeon


class Command:

    def __init__(self, command, argument):
        self._argument = argument
        self._command = command

    def do(self, dungeon):
        result = ""

        if self._command == "go":
            result = dungeon.go(self._argument)
        if self._command == "look":
            result = dungeon.look(self._argument)

        return result

    def __str__(self) -> str:
        return "You said: {} {}".format(self._command, self._argument)


class Game:
    def __init__(self):
        self.dungeon = None

    def start(self):
        self.dungeon = Dungeon()

    def execute(self, instruction):
        # obtain a valid command from player input
        command, argument = instruction.split(" ", 1)
        if command != "go" and command != "look":
            return "I don't understand"

        c = Command(command, argument)

        result = c.do(self.dungeon)

        print(c)
        return result
