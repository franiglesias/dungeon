class ObtainUserCommand:
    def command(self):
        pass


class ConsoleObtainUserCommand(ObtainUserCommand):
    def command(self):
        return input()
