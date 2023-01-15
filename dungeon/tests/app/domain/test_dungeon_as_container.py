import unittest

from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.thing import Thing


class DungeonAsContainerTestCase(unittest.TestCase):
    def test_we_can_grab_object_from_dungeon(self):
        thing = Thing.from_raw("Food")
        dungeon = self.dungeon_with_object(thing)

        got_thing = dungeon.get_safe("Food")
        self.assertEqual(thing, got_thing)

    def test_cannot_grab_non_existing_object(self):
        thing = Thing.from_raw("Food")
        dungeon = self.dungeon_with_object(thing)
        with self.assertRaises(IndexError):
            dungeon.get_safe("OtherThing")

    def test_we_can_exchange_object_from_dungeon(self):
        thing = Thing.from_raw("Food")
        to_keep = Thing.from_raw("Sword")
        dungeon = self.dungeon_with_object(thing)

        got_thing = dungeon.exchange(to_keep, "Food")
        self.assertEqual(thing, got_thing)

    def test_cannot_exchange_with_not_existing_object(self):
        thing = Thing.from_raw("Food")
        to_keep = Thing.from_raw("Sword")
        dungeon = self.dungeon_with_object(thing)

        with self.assertRaises(IndexError):
            dungeon.exchange(to_keep, "Another")

    def dungeon_with_object(self, thing=Thing.from_raw("Food")):
        builder = DungeonBuilder()
        builder.add('start')
        builder.put('start', thing)
        return builder.build()


if __name__ == '__main__':
    unittest.main()
