import unittest

from dungeon.app.domain.player.backpack import Backpack, BackpackMother
from dungeon.app.domain.player.hand import EmptyHand, ObjectNotFound, FullHand, DoNotHaveThatObject, ObjectIsNotKey, \
    Hand
from dungeon.app.domain.thing import Thing, Key


class MyThing(Thing):
    def apply_on(self, some_object):
        some_object.register_call()
        return self


class MyKey(Key):
    def apply_on(self, door):
        door.register_call()
        return self


class HandUsingBackpackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.hand = None
        self.backpack = None

    def test_empty_hand_can_get_object_from_backpack(self):
        self.given_players_backpack_contains(Thing.random())
        self.when_player_gets_it_from_backpack()
        self.then_player_has_it_the_hand()

    def test_full_hand_exchanges_object_from_backpack(self):
        self.given_players_backpack_contains(Thing.random())
        self.given_player_holds(Thing.random())
        self.when_player_gets_it_from_backpack()
        self.then_player_has_it_the_hand()
        self.and_the_other_object_is_in_the_backpack()

    def test_full_hand_keeps_same_object_trying_to_get_not_existing_one(self):
        self.given_players_backpack_contains(Thing.random())
        self.given_player_holds(Thing.random())
        self.when_player_tries_to_get_an_object_not_in_backpack()
        self.then_player_keeps_original_object_in_the_hand()

    def test_empty_hand_keeps_being_empty_getting_not_existing_object(self):
        self.given_players_backpack_is_empty()
        self.when_player_tries_to_get_an_object_not_in_backpack()
        self.then_player_has_nothing_in_her_hand()

    def given_players_backpack_contains(self, *something):
        self.things = something
        self.backpack = BackpackMother.containing(*something)

    def given_players_backpack_is_empty(self):
        self.things = []
        self.backpack = Backpack.empty()

    def given_player_holds(self, other_thing):
        self.other_thing = other_thing
        self.hand = FullHand(other_thing)

    def when_player_gets_it_from_backpack(self):
        if self.hand is None:
            self.hand = Hand.empty()
        self.hand = self.hand.get_from(self.backpack, self.things[0].name().to_s())

    def when_player_tries_to_get_an_object_not_in_backpack(self):
        if self.hand is None:
            self.hand = Hand.empty()
        try:
            self.hand = self.hand.get_from(self.backpack, "another")
        except ObjectNotFound:
            pass

    def then_player_has_it_the_hand(self):
        self.assertEqual(self.things[0], self.hand.holds())

    def then_player_has_nothing_in_her_hand(self):
        self.assertEqual(None, self.hand.holds())

    def then_player_keeps_original_object_in_the_hand(self):
        self.assertEqual(self.other_thing, self.hand.holds())

    def and_the_other_object_is_in_the_backpack(self):
        self.assertEqual(self.other_thing, self.backpack.get(self.other_thing.name().to_s()))



class HandUsingThingsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calls = 0

    def test_empty_hand_cannot_use_thing(self):
        hand = EmptyHand()
        with self.assertRaises(ObjectNotFound):
            hand.use_thing_with("Food", self)

    def test_cannot_use_a_thing_that_is_not_in_your_hand(self):
        hand = FullHand(Thing.from_raw("Sword"))
        with self.assertRaises(DoNotHaveThatObject):
            hand.use_thing_with("Food", self)

    def test_can_use_the_thing_in_hand(self):
        hand = FullHand(MyThing.from_raw("Something"))
        hand.use_thing_with("Something", self)
        self.assertEqual(1, self.calls)

    def register_call(self):
        self.calls += 1


class HandOpeningDoorsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calls = 0

    def test_cannot_open_when_not_holding_key(self):
        hand = FullHand(MyThing.from_raw("Something"))
        with self.assertRaises(ObjectIsNotKey):
            hand.open_with_key(self)

    def test_can_open_with_a_key(self):
        hand = FullHand(MyKey.from_raw("Something", "secret"))
        hand.open_with_key(self)
        self.assertEqual(1, self.calls)

    def register_call(self):
        self.calls += 1


if __name__ == '__main__':
    unittest.main()
