from dungeon.app.command.command import Command
from dungeon.app.obtain_user_command import ObtainUserCommand


class ConsoleObtainUserCommand(ObtainUserCommand):

    def command(self):
        raw = input("What should I do? >")
        user_input = " ".join(raw.lower().strip().split())
        return Command.from_user_input(user_input)
