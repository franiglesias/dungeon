from dungeon.app.command.command import Command
from dungeon.app.command.command_factory import CommandFactory


class ObtainUserCommand:

    def command(self) -> Command:
        pass


class FixedObtainUserCommand(ObtainUserCommand):
    def __init__(self, instruction):
        self._instruction = instruction

    def command(self) -> Command:
        factory = CommandFactory()
        return factory.from_user_input(self._instruction)
