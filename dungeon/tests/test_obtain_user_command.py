from unittest import TestCase

from mock.mock import patch

from dungeon.obtain_user_command import ConsoleObtainUserCommand


class TestConsoleObtainUserCommand(TestCase):
    def test_should_show_a_prompt(self):
        with patch('builtins.input', return_value="go north") as mock_input:
            obtain_user_command = ConsoleObtainUserCommand()
            command = obtain_user_command.command()
            self.assertIn("go north", str(command))
            self.assertEqual("What should I do? >", mock_input.call_args.args[0])

    def test_should_normalize_case_to_lowercase(self):
        with patch('builtins.input', return_value="go NORTH"):
            obtain_user_command = ConsoleObtainUserCommand()
            command = obtain_user_command.command()
            self.assertIn("go north", str(command))

    def test_should_trim_spaces(self):
        with patch('builtins.input', return_value="  go north   "):
            obtain_user_command = ConsoleObtainUserCommand()
            command = obtain_user_command.command()
            self.assertIn("go north", str(command))

    def test_should_normalize_middle_spaces(self):
        with patch('builtins.input', return_value="go      north"):
            obtain_user_command = ConsoleObtainUserCommand()
            command = obtain_user_command.command()
            self.assertIn("go north", str(command))
