import unittest

from dungeon.app.domain.dungeon_builder import DungeonMother
from dungeon.app.domain.thing import Thing, ThingMother

UNAVAILABLE_OBJECT = "OtherThing"
OBJECT_IN_CELL = "Food"


class DungeonAsContainerTestCase(unittest.TestCase):
    def setUp(self):
        self.thing = Thing.from_raw(OBJECT_IN_CELL)
        self.dungeon = DungeonMother.with_objects(self.thing)

    def test_we_can_grab_object_from_dungeon(self):
        self.assertGotTheThingFromCell(self.dungeon.get_safe(OBJECT_IN_CELL))

    def test_cannot_grab_non_existing_object(self):
        with self.assertRaises(IndexError):
            self.dungeon.get_safe(UNAVAILABLE_OBJECT)

    def test_we_can_exchange_object_from_dungeon(self):
        self.assertGotTheThingFromCell(self.dungeon.exchange(Thing.random(), OBJECT_IN_CELL))

    def test_cannot_exchange_with_not_existing_object(self):
        with self.assertRaises(IndexError):
            self.dungeon.exchange(Thing.random(), UNAVAILABLE_OBJECT)

    def assertGotTheThingFromCell(self, got_thing):
        self.assertEqual(self.thing, got_thing)


if __name__ == '__main__':
    unittest.main()
