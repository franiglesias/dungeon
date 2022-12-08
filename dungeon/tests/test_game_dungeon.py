import unittest

from dungeon.app.domain.dungeon_factory import DungeonFactory
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class GameDungeonTestCase(unittest.TestCase):
    def test_we_can_complete_dungeon(self):
        fake_observer = FakeObserver()

        dungeon = DungeonFactory().make('game')

        dungeon.register(fake_observer)

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

        self.assertTrue(fake_observer.is_aware_of("player_exited"))


if __name__ == '__main__':
    unittest.main()
