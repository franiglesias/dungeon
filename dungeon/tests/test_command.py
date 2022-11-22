from unittest import TestCase

from dungeon.app.command.command_factory import CommandFactory
from dungeon.app.command.commands.look_command import LookCommand


class TestCommand(TestCase):
    def test_allow_look_command_with_no_parameter(self):
        command = CommandFactory.from_user_input('look')
        expected = LookCommand('around')
        self.assertEqual(CommandMatcher(expected), command)


class CommandMatcher:
    def __init__(self, expected):
        self.expected = expected

    def __eq__(self, other):
        return self.expected._name() == other._name() and \
               self.expected._argument == other._argument
