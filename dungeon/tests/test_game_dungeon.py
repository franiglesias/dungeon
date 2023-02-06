import unittest

from dungeon.app.application import Application
from dungeon.app.domain.command.command import FakeObserver
from dungeon.app.domain.dungeon_factory import DungeonFactory
from dungeon.app.obtain_user_command import SequenceObtainUserCommand
from dungeon.app.show_output import MirrorUserCommand
from dungeon.app.toggles.toggles import Toggles


class CommandSequenceMother:
    def __init__(self):
        self._dungeons = {
            'test': [
                "go south",
                "go north"
            ],
            'game': [
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
        }

    def for_dungeon(self, name):
        return self._dungeons[name]


class GameDungeonTestCase(unittest.TestCase):
    def setUp(self):
        self.observer = FakeObserver()
        dungeons = ["test", "game"]
        self._generator = (dungeon for dungeon in dungeons)

    def test_dungeon_can_be_resolved(self):
        for dungeon in self._generator:
            self.run_game_with_dungeon(dungeon)

    @staticmethod
    def run_game_with_dungeon(dungeon_to_test):
        commands = CommandSequenceMother().for_dungeon(dungeon_to_test)
        obtain_user_command = SequenceObtainUserCommand(commands)
        show_output = MirrorUserCommand()
        toggles = Toggles()
        application = Application(obtain_user_command, show_output, DungeonFactory(), toggles)
        application.run(dungeon_name=dungeon_to_test)


if __name__ == '__main__':
    unittest.main()
