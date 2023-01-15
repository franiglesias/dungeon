import unittest

from dungeon.app.domain.player.backpack import Backpack
from dungeon.app.domain.player.hand import EmptyHand, ObjectNotFound
from dungeon.app.domain.thing import Thing


class HandTestCase(unittest.TestCase):
    def test_empty_hand_can_get_object_from_backpack(self):
        backpack = Backpack()
        something = Thing.from_raw("Something")
        backpack.keep(something)
        hand = EmptyHand()
        full_hand = hand.get_from(backpack, "Something")
        self.assertEqual(something, full_hand.holds())

    def test_full_hand_exchanges_object_from_backpack(self):
        backpack = Backpack()
        first = Thing.from_raw("First")
        second = Thing.from_raw("Second")
        backpack.keep(first)
        backpack.keep(second)

        hand = EmptyHand()
        full_hand = hand.get_from(backpack, "Second")
        full_hand = full_hand.get_from(backpack, "First")
        self.assertEqual(first, full_hand.holds())
        self.assertEqual(second, backpack.get("Second"))

    def test_full_hand_keeps_same_object_getting_not_existing_one(self):
        backpack = Backpack()
        first = Thing.from_raw("First")
        backpack.keep(first)

        hand = EmptyHand()
        full_hand = hand.get_from(backpack, "First")
        with self.assertRaises(ObjectNotFound):
            full_hand.get_from(backpack, "Another")

    def test_empty_hand_keeps_being_empty_getting_not_existing_object(self):
        backpack = Backpack()
        hand = EmptyHand()
        with self.assertRaises(ObjectNotFound):
            hand.get_from(backpack, "Another")


if __name__ == '__main__':
    unittest.main()
