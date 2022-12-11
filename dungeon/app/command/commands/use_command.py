from dungeon.app.command.command import Command


class UseCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def name(self):
        return "use"

    def do(self, receiver):
        receiver.use(self._argument)
