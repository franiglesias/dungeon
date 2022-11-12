from unittest import TestCase

from mock.mock import patch

from dungeon.obtain_user_command import ConsoleObtainUserCommand


class TestConsoleObtainUserCommand(TestCase):
    def test_should_show_a_prompt(self):
        with patch('builtins.input', return_value="go north") as mock_input:
            obtain_user_command = ConsoleObtainUserCommand()
            instruction = obtain_user_command.command()
            self.assertEqual("go north", instruction)
            self.assertEqual("What should I do? >", mock_input.call_args.args[0])
