from unittest import TestCase

from dungeon.command.command import Command


class TestCommand(TestCase):
    def test_allow_look_command_with_no_parameter(self):
        command = Command.from_user_input('look')
        expected = Command('look', 'around')
        self.assertEquals(CommandMatcher(expected), command)


class CommandMatcher:
    def __init__(self, expected):
        self.expected = expected

    def __eq__(self, other):
        return self.expected._command == other._command and \
               self.expected._argument == other._argument
