from dungeon.dungeon import Dungeon


class Game:
    def __init__(self):
        self.dungeon = None

    def start(self):
        self.dungeon = Dungeon()

    def execute(self, instruction):
        result = "I don't understand"
        command, argument = instruction.split(" ", 1)
        if command == "go":
            print("You said: {c} {a}".format(c=command, a=argument))
            result = self.dungeon.go(argument)
        if command == "look":
            print("You said: {c} {a}".format(c=command, a=argument))
            result = self.dungeon.look(argument)
        return result
