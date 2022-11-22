from dungeon.app.command.commands.go_command import GoCommand
from dungeon.app.command.commands.invalid_command import InvalidCommand
from dungeon.app.command.commands.look_command import LookCommand


class CommandFactory:

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
