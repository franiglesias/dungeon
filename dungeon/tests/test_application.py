from unittest import TestCase

from dungeon.app.application import Application
from dungeon.app.command.command_factory import CommandFactory
from dungeon.app.domain.dungeon_factory import DungeonFactory
from dungeon.app.obtain_user_command import ObtainUserCommand
from dungeon.app.show_output import ShowOutput


class FixedObtainUserCommand(ObtainUserCommand):
    def __init__(self, instruction):
        self._instruction = instruction

    def command(self):
        return CommandFactory.from_user_input(self._instruction)


class TestShowOutput(ShowOutput):
    def __init__(self):
        self._contents = ""

    def put(self, message):
        self._contents = self._contents + message + "\n\n"

    def contents(self):
        return self._contents


class TestApplication(TestCase):
    def test_should_show_title(self):
        obtain_user_command = FixedObtainUserCommand("go north")
        show_output = TestShowOutput()

        app = Application(obtain_user_command, show_output, DungeonFactory())
        app.run('test')

        self.assertIn("Welcome to the Dungeon", show_output.contents())

    def test_should_show_command_echo(self):
        obtain_user_command = FixedObtainUserCommand("go north")
        show_output = TestShowOutput()

        app = Application(obtain_user_command, show_output, DungeonFactory())
        app.run('test')

        self.assertIn("You said: go north", show_output.contents())

    def test_should_show_ending_message(self):
        obtain_user_command = FixedObtainUserCommand("go north")
        show_output = TestShowOutput()

        app = Application(obtain_user_command, show_output, DungeonFactory())
        app.run('test')

        self.assertIn("Congrats. You're out", show_output.contents())
