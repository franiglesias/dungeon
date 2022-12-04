from unittest import TestCase

from dungeon.app.application import Application
from dungeon.app.domain.dungeon_factory import DungeonFactory
from dungeon.app.toggles.toggles import Toggles
from dungeon.tests.fakes.obtain_user_command.fixed_obtain_user_command import FixedObtainUserCommand
from dungeon.tests.fakes.show_output.fake_show_output import FakeShowOutput


class TestApplication(TestCase):

    def setUp(self) -> None:
        self.obtain_user_command = FixedObtainUserCommand("go north")
        self.show_output = FakeShowOutput()
        self.toggles = Toggles()

        self.application = Application(self.obtain_user_command, self.show_output, DungeonFactory(), self.toggles)

    def test_should_show_title(self):
        self.application.run('test')
        self.assertIn("Welcome to the Dungeon", self.show_output.contents())

    def test_should_show_command_echo(self):
        self.application.run('test')
        self.assertIn("go north", self.show_output.contents())

    def test_should_show_ending_message(self):
        self.application.run('test')
        self.assertIn("Congrats. You're out", self.show_output.contents())
