import unittest

from dungeon.app.domain.dir import Dir
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.wall import Exit
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class DungeonAsSubjectTestCase(unittest.TestCase):
    def test_supports_current_room_changed_event(self):
        fake_observer = FakeObserver()

        builder = DungeonBuilder()
        builder.add('start')
        builder.add('other')
        builder.connect('start', Dir.N, 'other')
        dungeon = builder.build()

        dungeon.register(fake_observer)

        dungeon.go(Dir.N)

        self.assertTrue(fake_observer.is_aware_of("player_moved"))

    def test_supports_player_exited_event(self):
        fake_observer = FakeObserver()

        builder = DungeonBuilder()
        builder.add('start')
        builder.set('start', Dir.N, Exit())
        dungeon = builder.build()

        dungeon.register(fake_observer)

        dungeon.go(Dir.N)

        self.assertTrue(fake_observer.is_aware_of("player_exited"))


if __name__ == '__main__':
    unittest.main()
