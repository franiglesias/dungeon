from dungeon.app.command.command_factory import CommandFactory
from dungeon.app.obtain_user_command import ObtainUserCommand


class FixedObtainUserCommand(ObtainUserCommand):
    def __init__(self, instruction):
        self._instruction = instruction

    def command(self):
        factory = CommandFactory()
        return factory.from_user_input(self._instruction)
