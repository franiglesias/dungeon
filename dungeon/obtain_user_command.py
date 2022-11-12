class ObtainUserCommand:
    def command(self):
        pass


class ConsoleObtainUserCommand(ObtainUserCommand):
    def command(self):
        raw = input("What should I do? >")
        return " ".join(raw.lower().strip().split())
