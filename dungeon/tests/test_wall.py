from unittest import TestCase

from dungeon.app.domain.dir import Dir
from dungeon.app.domain.wall import Wall, Exit, Door, Walls


class TestWalls(TestCase):
    def setUp(self):
        self.walls = Walls()

    def test_walls_collection_starts_with_all_walls(self):
        self.assertIsInstance(self.walls.get(Dir.N), Wall)
        self.assertIsInstance(self.walls.get(Dir.S), Wall)
        self.assertIsInstance(self.walls.get(Dir.E), Wall)
        self.assertIsInstance(self.walls.get(Dir.W), Wall)

    def test_can_set_a_wall(self):
        self.walls = self.walls.set(Dir.N, Exit())
        self.assertIsInstance(self.walls.get(Dir.N), Exit)

    def test_door_go_moves_player_to_another_room(self):
        door = Door('destination')
        result = door.go()

        self.assertEqual('destination', result._bag.get("destination"))
