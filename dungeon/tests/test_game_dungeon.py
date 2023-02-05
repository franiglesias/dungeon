import unittest

from dungeon.app.application import Application
from dungeon.app.domain.command.command import FakeObserver
from dungeon.app.domain.dungeon_factory import DungeonFactory
from dungeon.app.obtain_user_command import SequenceObtainUserCommand
from dungeon.app.show_output import MirrorUserCommand
from dungeon.app.toggles.toggles import Toggles


class GameDungeonTestCase(unittest.TestCase):
    def setUp(self):
        self.observer = FakeObserver()

    def test_using_commands(self):
        commands = [
            'go north',
            'go north',
            'go north',
            'go east',
            'go north',
            'go east',
            'go east',
            'go south',
            'go west',
            'get RedKey',
            'go east',
            'go south',
            'open east',
            'go east'
        ]

        obtain_user_command = SequenceObtainUserCommand(commands)
        show_output = MirrorUserCommand()
        toggles = Toggles()

        application = Application(obtain_user_command, show_output, DungeonFactory(), toggles)
        application.run(dungeon_name='game')


if __name__ == '__main__':
    unittest.main()
