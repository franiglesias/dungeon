from dungeon.app.domain.command.command import Command


class ByeCommand(Command):
    def __init__(self, *args):
        pass

    def name(self):
        return "bye"
