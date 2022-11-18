from unittest import TestCase

from dungeon.dir import Dir
from dungeon.dungeon import DungeonBuilder
from dungeon.wall import Exit


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
