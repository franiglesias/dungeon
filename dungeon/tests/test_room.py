from unittest import TestCase

from dungeon.room import Room, Dir, Rooms


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


class TestRooms(TestCase):
    def setUp(self):
        self.rooms = Rooms()

    def test_new_collection_created_empty(self):
        self.assertEqual(0, self.rooms.count())

    def test_can_set_rooms_with_identifier(self):
        room = Room()
        rooms = self.rooms.set('aRoom', room)
        self.assertEqual(1, rooms.count())

    def test_can_get_specific_room(self):
        first = Room()
        second = Room()

        self.rooms = self.rooms \
            .set('first', first) \
            .set('second', second)

        self.assertEqual(first, self.rooms.get('first'))
        self.assertEqual(second, self.rooms.get('second'))
