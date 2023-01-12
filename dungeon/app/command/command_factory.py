from importlib import import_module

from dungeon.app.command.command import Command
from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.command.commands.go_command import GoCommand
from dungeon.app.command.commands.invalid_command import InvalidCommand
from dungeon.app.command.commands.look_command import LookCommand
from dungeon.app.command.commands.use_command import UseCommand


class CommandFactoryEngine:
    def by_name(self, command, argument) -> Command:
        pass


class Custom(CommandFactoryEngine):
    def by_name(self, command, argument) -> Command:
        if command == "go":
            return GoCommand(argument)
        if command == "look":
            return LookCommand(argument)
        if command == "get":
            return GetCommand(argument)
        if command == "use":
            return UseCommand(argument)

        return InvalidCommand("{} {}".format(command, argument))


class Autodiscover(CommandFactoryEngine):
    def __init__(self, path_to_commands):
        self._path_to_commands = path_to_commands

    def by_name(self, command, argument) -> Command:
        try:
            module = import_module("{path}.{command}_command".format(path=self._path_to_commands, command=command))
            command_class = getattr(module, "{name}Command".format(name=command.capitalize()))
        except ModuleNotFoundError:
            command_class = InvalidCommand
        return command_class(argument)


class CommandFactory:
    def __init__(self, engine=Custom()):
        self._engine = engine

    def from_user_input(self, user_input) -> Command:
        try:
            command, argument = user_input.split(" ", 1)
        except ValueError:
            command = user_input
            argument = "around"

        return self._engine.by_name(command, argument)
