from unittest import TestCase

from dungeon.app.domain.dir import Dir
from dungeon.app.domain.room import Rooms, Room
from dungeon.app.domain.wall import Exit, Walls


class TestRoom(TestCase):
    def setUp(self):
        walls = Walls()
        walls.set(Dir.N, Exit())
        self.room = Room(walls)

    def test_wall_in_all_directions(self):
        result = self.room.go(Dir.N)
        self.assertEqual("Congrats. You're out", result.get("message"))
        result = self.room.go(Dir.E)
        self.assertEqual('You hit a wall', result.get("message"))
        result = self.room.go(Dir.S)
        self.assertEqual('You hit a wall', result.get("message"))
        result = self.room.go(Dir.W)
        self.assertEqual('You hit a wall', result.get("message"))

    def test_can_provide_description(self):
        description = """North: There is a door
East: There is a wall
South: There is a wall
West: There is a wall
That's all
"""

        result = self.room.look('around')

        self.assertEqual(description, result.get("message"))

    def test_can_provide_description_of_objects_in_empty_room(self):
        description = "There are no objects"
        result = self.room.look('objects')
        self.assertEqual(description, result.get("message"))


class TestRooms(TestCase):
    def setUp(self):
        self.rooms = Rooms()

    def test_new_collection_created_empty(self):
        self.assertEqual(0, self.rooms.count())

    def test_can_set_rooms_with_identifier(self):
        room = Room(Walls())
        rooms = self.rooms.set('aRoom', room)
        self.assertEqual(1, rooms.count())

    def test_can_get_specific_room(self):
        first = Room(Walls())
        second = Room(Walls())

        self.rooms = self.rooms \
            .set('first', first) \
            .set('second', second)

        self.assertEqual(first, self.rooms.get('first'))
        self.assertEqual(second, self.rooms.get('second'))
