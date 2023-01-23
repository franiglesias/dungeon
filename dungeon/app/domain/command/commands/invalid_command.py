from dungeon.app.domain.command.command import Command


class InvalidCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def __str__(self) -> str:
        return "You said: {}".format(self._argument)
