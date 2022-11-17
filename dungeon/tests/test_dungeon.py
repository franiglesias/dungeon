import unittest

from dungeon.dungeon import Dungeon


class DungeonTestCase(unittest.TestCase):
    @unittest.skip("temporary disabled")
    def test_something(self):
        dungeon = self.build_dungeon()

        dungeon.go('west')
        exited = dungeon.go('south')

        self.assertTrue(exited.is_finished())

    def build_dungeon(self):
        dungeon = Dungeon(2)
        dungeon.connect(0, 'east', 1)
        dungeon.connect(1, 'west', 0)
        dungeon.exit(0, 'south')
        dungeon.start(1)

        return dungeon


if __name__ == '__main__':
    unittest.main()
