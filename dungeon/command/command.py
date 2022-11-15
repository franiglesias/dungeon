from dungeon.command.action_result import ActionResult


class Command:

    def __init__(self, command, argument):
        self._argument = argument
        self._command = command

    @staticmethod
    def from_user_input(user_input):
        command, argument = user_input.split(" ", 1)
        if command != "go" and command != "look":
            return InvalidCommand(user_input)

        return Command(command, argument)

    def do(self, dungeon):
        if self._command == "go":
            return dungeon.go(self._argument)
        if self._command == "look":
            return dungeon.look(self._argument)

    def __str__(self) -> str:
        return "You said: {} {}".format(self._command, self._argument)


class InvalidCommand(Command):
    def __init__(self, user_input):
        self._user_input = user_input

    def do(self, dungeon):
        return ActionResult("I don't understand")

    def __str__(self) -> str:
        return "You said: {}".format(self._user_input)
