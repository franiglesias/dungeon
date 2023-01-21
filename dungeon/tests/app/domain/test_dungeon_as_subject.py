import unittest

from dungeon.app.domain.dir import Dir
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.player.player_events import PlayerMoved, PlayerExited
from dungeon.app.domain.wall import Exit
from dungeon.tests.decorators import expect_event
from dungeon.app.command.command import FakeObserver


class DungeonAsSubjectTestCase(unittest.TestCase):
    def setUp(self):
        self.builder = DungeonBuilder()
        self.observer = FakeObserver()

    @expect_event(PlayerMoved)
    def test_supports_current_room_changed_event(self):
        self.builder.add('start')
        self.builder.add('other')
        self.builder.connect('start', Dir.N, 'other')
        dungeon = self.builder.build()

        dungeon.register(self.observer)
        dungeon.go(Dir.N)

    @expect_event(PlayerExited)
    def test_supports_player_exited_event(self):
        self.builder.add('start')
        self.builder.set('start', Dir.N, Exit())
        dungeon = self.builder.build()

        dungeon.register(self.observer)
        dungeon.go(Dir.N)


if __name__ == '__main__':
    unittest.main()
