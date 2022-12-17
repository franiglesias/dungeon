from dungeon.app.command.command_factory import CommandFactory, Autodiscover
from dungeon.app.obtain_user_command import ObtainUserCommand


class ConsoleObtainUserCommand(ObtainUserCommand):
    def __init__(self, command_factory):
        self._command_factory = command_factory

    def command(self):
        raw = input("What should I do? >")
        user_input = " ".join(raw.lower().strip().split())
        return self._command_factory.from_user_input(user_input)
