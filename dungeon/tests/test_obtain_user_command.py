from unittest import TestCase

from mock.mock import patch

from dungeon.app.command.command_factory import CommandFactory
from dungeon.app.command.commands.go_command import GoCommand
from dungeon.for_obtaining_commands.console_obtain_user_command import ConsoleObtainUserCommand


class TestConsoleObtainUserCommand(TestCase):
    def setUp(self):
        factory = CommandFactory()
        self.obtain_user_command = ConsoleObtainUserCommand(factory)

    def test_should_show_a_prompt(self):
        with patch('builtins.input', return_value="go north") as mock_input:
            command = self.obtain_user_command.command()
            self.assertIsInstance(command, GoCommand)
            self.assertEqual("What should I do? >", mock_input.call_args.args[0])

    def test_should_normalize_case_to_lowercase(self):
        with patch('builtins.input', return_value="go NORTH"):
            command = self.obtain_user_command.command()
            self.assertIsInstance(command, GoCommand)
            self.assertEqual("north", command.argument())

    def test_should_trim_spaces(self):
        with patch('builtins.input', return_value="  go north   "):
            command = self.obtain_user_command.command()
            self.assertIsInstance(command, GoCommand)
            self.assertEqual("north", command.argument())

    def test_should_normalize_middle_spaces(self):
        with patch('builtins.input', return_value="go      north"):
            command = self.obtain_user_command.command()
            self.assertIsInstance(command, GoCommand)
            self.assertEqual("north", command.argument())
