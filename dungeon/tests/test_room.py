from unittest import TestCase

from dungeon.app.domain.dir import Dir
from dungeon.app.domain.room import Rooms, Room
from dungeon.app.domain.thing import Thing
from dungeon.app.domain.wall import Exit, Walls
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class TestRoom(TestCase):
    def setUp(self):
        walls = Walls()
        walls.set(Dir.N, Exit())

        self.room = Room(walls)

        self.fake_observer = FakeObserver()
        self.room.register(self.fake_observer)

    def test_wall_in_all_directions(self):
        self.room.go(Dir.N)
        self.assertTrue(self.fake_observer.is_aware_of("player_exited"))

        self.room.go(Dir.E)
        self.assertTrue(self.fake_observer.is_aware_of("player_hit_wall"))

        self.room.go(Dir.S)
        self.assertTrue(self.fake_observer.is_aware_of("player_hit_wall"))

        self.room.go(Dir.W)
        self.assertTrue(self.fake_observer.is_aware_of("player_hit_wall"))

    def test_can_provide_description(self):
        self.room.look('around')

        event = self.fake_observer.last("player_got_description")
        description = event.description()

        self.assertIn("North: There is a door", description)
        self.assertIn("East: There is a wall", description)
        self.assertIn("South: There is a wall", description)
        self.assertIn("West: There is a wall", description)

    def test_can_provide_description_of_objects_in_empty_room(self):
        self.room.look('objects')

        event = self.fake_observer.last("player_got_description")
        description = event.description()

        self.assertIn("There are no objects", description)

    def test_can_put_objects_in_a_room(self):
        self.room.put(Thing("Food"))
        self.room.put(Thing("Wood Sword"))
        self.room.put(Thing("Gold Coin"))
        self.room.look('objects')

        event = self.fake_observer.last("player_got_description")
        description = event.description()

        self.assertIn("Food", description)
        self.assertIn("Wood Sword", description)
        self.assertIn("Gold Coin", description)

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
