from dungeon.app.command.action_result import ActionResult


class Command:

    def __init__(self, argument):
        self._argument = argument

    @staticmethod
    def from_user_input(user_input):
        try:
            command, argument = user_input.split(" ", 1)
        except ValueError:
            command = user_input
            argument = "around"

        if command == "go":
            return GoCommand(argument)
        if command == "look":
            return LookCommand(argument)

        return InvalidCommand(user_input)

    def do(self, receiver):
        pass

    def __str__(self) -> str:
        return "You said: {} {}".format(self._name(), self._argument)

    def _name(self):
        pass


class GoCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def do(self, receiver):
        return receiver.go(self._argument)

    def _name(self):
        return "go"


class LookCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def do(self, receiver):
        return receiver.look(self._argument)

    def _name(self):
        return "look"


class InvalidCommand(Command):
    def __init__(self, user_input):
        super().__init__(user_input)

    def do(self, dungeon):
        return ActionResult.player_acted("I don't understand")

    def __str__(self) -> str:
        return "You said: {}".format(self._argument)
