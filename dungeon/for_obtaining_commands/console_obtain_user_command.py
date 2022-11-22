from dungeon.app.command.command_factory import CommandFactory
from dungeon.app.obtain_user_command import ObtainUserCommand


class ConsoleObtainUserCommand(ObtainUserCommand):

    def command(self):
        raw = input("What should I do? >")
        user_input = " ".join(raw.lower().strip().split())
        return CommandFactory.from_user_input(user_input)
