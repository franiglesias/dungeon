from dungeon.command.command import Command


class ObtainUserCommand:

    def command(self):
        pass


class ConsoleObtainUserCommand(ObtainUserCommand):

    def command(self):
        raw = input("What should I do? >")
        user_input = " ".join(raw.lower().strip().split())
        return Command.from_user_input(user_input)
