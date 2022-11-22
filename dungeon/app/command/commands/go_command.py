from dungeon.app.command.command import Command


class GoCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def do(self, receiver):
        return receiver.go(self._argument)

    def _name(self):
        return "go"
