import unittest

from dungeon.app.domain.dungeon_factory import DungeonFactory
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

        dungeon.go('north')
        dungeon.go('north')
        dungeon.go('north')
        dungeon.go('east')
        dungeon.go('north')
        dungeon.go('east')
        dungeon.go('east')
        dungeon.go('south')
        dungeon.go('south')
        dungeon.go('east')


if __name__ == '__main__':
    unittest.main()
