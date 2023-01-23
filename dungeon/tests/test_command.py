from unittest import TestCase

from dungeon.app.domain.command.command_factory import CommandFactory
from dungeon.app.domain.command.commands.look_command import LookCommand


class TestCommand(TestCase):
    def test_allow_look_command_with_no_parameter(self):
        factory = CommandFactory()
        command = factory.from_user_input("look")
        expected = LookCommand('around')
        self.assertEqual(CommandMatcher(expected), command)


class CommandMatcher:
    def __init__(self, expected):
        self.expected = expected

    def __eq__(self, other):
        return self.expected.name() == other.name() and \
               self.expected.argument() == other.argument()
