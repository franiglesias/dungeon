import unittest

from dungeon.dungeon import Dungeon, DungeonBuilder


class DungeonTestCase(unittest.TestCase):
    @unittest.skip("temporary disabled")
    def test_something(self):
        dungeon = self.build_dungeon()

        dungeon.go('west')
        exited = dungeon.go('south')

        self.assertTrue(exited.is_finished())

    def build_dungeon(self):
        builder = DungeonBuilder()
        dungeon = builder.build()
        # dungeon.connect(0, 'east', 1)
        # dungeon.connect(1, 'west', 0)
        # dungeon.exit(0, 'south')
        # dungeon.start(1)

        return dungeon


if __name__ == '__main__':
    unittest.main()
