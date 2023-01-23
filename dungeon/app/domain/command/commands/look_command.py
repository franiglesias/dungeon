from dungeon.app.domain.command.command import Command


class LookCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def name(self):
        return "look"
