import unittest

from dungeon.app.domain.player.backpack import Backpack
from dungeon.app.domain.thing import Thing


class Hand:
    def __init__(self):
        pass

    def holds(self):
        raise NotImplementedError

    def get(self, thing_name):
        raise NotImplementedError


class FullHand(Hand):
    def __init__(self, holds: Thing, backpack: Backpack) -> None:
        self._holds = holds
        self._backpack = backpack

    def holds(self) -> Thing:
        return self._holds

    def get(self, thing_name):
        try:
            thing = self._backpack.exchange(self._holds, thing_name)
            return FullHand(thing, self._backpack)
        except IndexError:
            return self


class EmptyHand(Hand):
    def __init__(self, backpack: Backpack) -> None:
        self._backpack = backpack

    def get(self, thing_name) -> FullHand:
        thing = self._backpack.get_safe(thing_name)
        return FullHand(thing, self._backpack)



class HandTestCase(unittest.TestCase):
    def test_empty_hand_can_get_object_from_backpack(self):
        backpack = Backpack()
        something = Thing.from_raw("Something")
        backpack.keep(something)
        hand = EmptyHand(backpack)
        full_hand = hand.get("Something")
        self.assertEqual(something, full_hand.holds())

    def test_full_hand_exchanges_object_from_backpack(self):
        backpack = Backpack()
        first = Thing.from_raw("First")
        second = Thing.from_raw("Second")
        backpack.keep(first)
        backpack.keep(second)

        hand = EmptyHand(backpack)
        full_hand = hand.get("Second")
        full_hand = full_hand.get("First")
        self.assertEqual(first, full_hand.holds())
        self.assertEqual(second, backpack.get("Second"))

    def test_full_hand_keeps_same_object_getting_not_existing_one(self):
        backpack = Backpack()
        first = Thing.from_raw("First")
        backpack.keep(first)

        hand = EmptyHand(backpack)
        full_hand = hand.get("First")
        full_hand = full_hand.get("Another")
        self.assertEqual(first, full_hand.holds())
        with self.assertRaises(IndexError):
            backpack.get_safe("First")


if __name__ == '__main__':
    unittest.main()
