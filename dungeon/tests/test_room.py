from unittest import TestCase

from dungeon.room import Room, Dir


class TestRoom(TestCase):
    def test_wall_in_all_directions(self):
        room = Room()
        result = room.go(Dir.N)
        self.assertEqual("Congrats. You're out", result.message())
        result = room.go(Dir.E)
        self.assertEqual('You hit a wall', result.message())
        result = room.go(Dir.S)
        self.assertEqual('You hit a wall', result.message())
        result = room.go(Dir.W)
        self.assertEqual('You hit a wall', result.message())

    def test_can_provide_description(self):
        description = """North: There is a door
East: There is a wall
South: There is a wall
West: There is a wall
That's all
"""

        room = Room()
        result = room.look('around')

        self.assertEqual(description, result.message())
