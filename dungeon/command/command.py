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

    def do_deprecated(self, dungeon):
        result = ""

        if self._command == "go":
            result = dungeon.go(self._argument)
        if self._command == "look":
            result = dungeon.look(self._argument)

        return result

    def do(self, dungeon):
        result = self.do_deprecated(dungeon)
        return ActionResult(result)

    def __str__(self) -> str:
        return "You said: {} {}".format(self._command, self._argument)


class InvalidCommand(Command):
    def __init__(self, user_input):
        self._user_input = user_input

    def do_deprecated(self, dungeon):
        return "I don't understand"

    def __str__(self) -> str:
        return "You said: {}".format(self._user_input)
