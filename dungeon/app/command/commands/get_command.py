from dungeon.app.command.action_result import ActionResult
from dungeon.app.command.command import Command


class GetCommand(Command):
    def __init__(self, argument):
        super().__init__(argument)

    def do(self, receiver):
        receiver.get(self._argument)

    def name(self):
        return "get"
