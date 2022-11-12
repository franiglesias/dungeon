from unittest import TestCase

from dungeon.application import Application
from dungeon.obtain_user_command import ObtainUserCommand
from dungeon.show_output import ShowOutput


class FixedObtainUserCommand(ObtainUserCommand):
    def __init__(self, instruction):
        self._instruction = instruction

    def command(self):
        return self._instruction


class TestShowOutput(ShowOutput):
    def __init__(self):
        self._contents = ""

    def put(self, message):
        self._contents = self._contents + message + "\n"

    def contents(self):
        return self._contents


class TestApplication(TestCase):
    def test_should_show_title(self):
        obtain_user_command = FixedObtainUserCommand("go north")
        show_output = TestShowOutput()

        app = Application(obtain_user_command, show_output)
        app.run()

        self.assertIn("Welcome to the Dungeon", show_output.contents())

    def test_should_show_command_echo(self):
        obtain_user_command = FixedObtainUserCommand("go north")
        show_output = TestShowOutput()

        app = Application(obtain_user_command, show_output)
        app.run()

        self.assertIn("You said: go north", show_output.contents())
