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
    def test_can_append_room_to_rooms_collection(self):
        room = Room()
        rooms = Rooms()

        self.assertEqual(0, rooms.count())
        rooms = rooms.append(room)

        self.assertEqual(1, rooms.count())

    def test_can_get_specific_room(self):
        first = Room()
        second = Room()
        rooms = Rooms()

        rooms = rooms.append(first)
        rooms = rooms.append(second)

        self.assertEqual(first, rooms.get(0))
        self.assertEqual(second, rooms.get(1))
