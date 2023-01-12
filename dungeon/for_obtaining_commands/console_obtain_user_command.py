from dungeon.app.command.command import Command
from dungeon.app.obtain_user_command import ObtainUserCommand


class ConsoleObtainUserCommand(ObtainUserCommand):
    def __init__(self, command_factory):
        self._command_factory = command_factory

    def command(self) -> Command:
        raw = input("What should I do? >")
        user_input = " ".join(raw.lower().strip().split())
        return self._command_factory.from_user_input(user_input)
