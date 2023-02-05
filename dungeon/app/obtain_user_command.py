from dungeon.app.domain.command.command import Command
from dungeon.app.domain.command.command_factory import CommandFactory, Autodiscover


class ObtainUserCommand:

    def command(self) -> Command:
        pass


class FixedObtainUserCommand(ObtainUserCommand):
    def __init__(self, instruction):
        self._instruction = instruction

    def command(self) -> Command:
        factory = CommandFactory()
        return factory.from_user_input(self._instruction)


class SequenceObtainUserCommand(ObtainUserCommand):
    def __init__(self, commands):
        self._factory = CommandFactory(Autodiscover("dungeon.app.domain.command.commands"))
        self._generator = (command for command in commands)

    def command(self) -> Command:
        for instruction in self._generator:
            return self._factory.from_user_input(instruction)
