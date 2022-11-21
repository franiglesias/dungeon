from unittest import TestCase

from dungeon.app.domain.dir import Dir
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.wall import Exit


class TestDungeonBuilder(TestCase):
    def test_can_add_room_with_exit_to_North(self):
        builder = DungeonBuilder()
        builder.add('start')
        builder.set('start', Dir.N, Exit())

        dungeon = builder.build()
        result = dungeon.go('north')
        self.assertTrue(result.is_finished())

    def test_can_add_room_with_several_doors(self):
        builder = DungeonBuilder()
        builder.add('start')
        builder.set('start', Dir.N, Exit())
        builder.set('start', Dir.S, Exit())

        dungeon = builder.build()

        result = dungeon.go('north')
        self.assertTrue(result.is_finished())
        result = dungeon.go('south')
        self.assertTrue(result.is_finished())

    def test_can_add_several_rooms(self):
        builder = DungeonBuilder()
        builder.add('101')
        builder.add('start')
        builder.set('101', Dir.S, Exit())
        builder.set('start', Dir.N, Exit())

        dungeon = builder.build()

        result = dungeon.go('north')
        self.assertTrue(result.is_finished())

    def test_can_connect_rooms(self):
        builder = DungeonBuilder()
        builder.add('101')
        builder.add('start')
        builder.connect('start', Dir.N, '101')
        builder.set('101', Dir.E, Exit())

        dungeon = builder.build()
        dungeon.go('north')
        dungeon.go('south')
        dungeon.go('north')
        result = dungeon.go('east')

        self.assertTrue(result.is_finished())
