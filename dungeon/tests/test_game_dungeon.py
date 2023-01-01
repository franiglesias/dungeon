import unittest

from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.command.commands.go_command import GoCommand
from dungeon.app.command.commands.open_command import OpenCommand
from dungeon.app.domain.dungeon_factory import DungeonFactory
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.player.player_events import PlayerExited
from dungeon.tests.decorators import expect_event
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class GameDungeonTestCase(unittest.TestCase):
    def setUp(self):
        self.observer = FakeObserver()

    @expect_event(PlayerExited)
    def test_we_can_complete_dungeon(self):
        dungeon = DungeonFactory().make('game')
        dungeon.register(self.observer)
        player = Player()
        player.register(self.observer)
        player.awake_in(dungeon)

        player.do(GoCommand('north'))
        player.do(GoCommand('north'))
        player.do(GoCommand('north'))
        player.do(GoCommand('east'))
        player.do(GoCommand('north'))
        player.do(GoCommand('east'))
        player.do(GoCommand('east'))
        player.do(GoCommand('south'))
        player.do(GoCommand('west'))
        player.do(GetCommand('RedKey'))
        player.do(GoCommand('east'))
        player.do(GoCommand('south'))
        player.do(OpenCommand('east'))
        player.do(GoCommand('east'))


if __name__ == '__main__':
    unittest.main()
