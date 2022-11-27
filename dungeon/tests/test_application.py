from unittest import TestCase

from dungeon.app.application import Application
from dungeon.app.command.command_factory import CommandFactory
from dungeon.app.domain.dungeon_factory import DungeonFactory
from dungeon.app.obtain_user_command import ObtainUserCommand
from dungeon.app.show_output import ShowOutput
from dungeon.app.toggles.toggles import Toggles


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

    def setUp(self) -> None:
        self.obtain_user_command = FixedObtainUserCommand("go north")
        self.show_output = TestShowOutput()
        self.toggles = Toggles()

        self.application = Application(self.obtain_user_command, self.show_output, DungeonFactory(), self.toggles)

    def test_should_show_title(self):
        self.application.run('test')
        self.assertIn("Welcome to the Dungeon", self.show_output.contents())

    def test_should_show_command_echo(self):
        self.application.run('test')
        self.assertIn("You said: go north", self.show_output.contents())

    def test_should_show_ending_message(self):
        self.application.run('test')
        self.assertIn("Congrats. You're out", self.show_output.contents())
