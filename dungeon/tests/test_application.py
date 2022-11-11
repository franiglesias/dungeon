from unittest import TestCase

from dungeon.application import Application
from dungeon.show_output import ShowOutput


class ObtainUserCommand:
    def command(self):
        return "go north"


class TestApplication(TestCase):
    def test_should_show_title(self):
        obtain_user_command = ObtainUserCommand()
        show_output = ShowOutput()

        app = Application(obtain_user_command, show_output)
        app.run()

        self.assertIn("Welcome to the Dungeon", show_output.contents())
