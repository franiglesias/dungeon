import unittest

from dungeon.app.domain.dungeon_factory import DungeonFactory


class GameDungeonTestCase(unittest.TestCase):
    def test_we_can_complete_dungeon(self):
        dungeon = DungeonFactory().make('game')
        dungeon.go('north')
        dungeon.go('north')
        dungeon.go('north')
        dungeon.go('east')
        dungeon.go('north')
        dungeon.go('east')
        dungeon.go('east')
        dungeon.go('south')
        dungeon.go('south')
        result = dungeon.go('east')

        self.assertTrue(result.is_finished())


if __name__ == '__main__':
    unittest.main()
