from unittest import TestCase

from dungeon.app.domain.player.player_events import PlayerMoved, Event
from dungeon.app.domain.thing import ThingName, ThingId, Thing, Key, ThingKey
from dungeon.app.domain.wall import Door, Wall
from dungeon.app.events.subject import Subject
from dungeon.tests.decorators import expect_event
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class TestThingName(TestCase):
    def test_should_not_be_created_empty(self):
        with self.assertRaises(ValueError):
            ThingName("")


class TestThingId(TestCase):
    def test_should_not_be_created_empty(self):
        with self.assertRaises(ValueError):
            ThingId("")

    def test_should_be_normalized_to_lowercase(self):
        identifier = ThingId.normalized("SomeIdForThing")
        self.assertEqual("someidforthing", identifier.to_s())

    def test_could_be_derived_from_ThingName(self):
        identifier = ThingId.from_name(ThingName("A Thing"))
        self.assertEqual("a thing", identifier.to_s())

    def test_could_compare_for_equality(self):
        an_id = ThingId("example")
        another_id = ThingId("example")

        self.assertEqual(an_id, another_id)


class TestThing(TestCase):
    def test_could_be_created_from_raw_name(self):
        a_thing = Thing.from_raw("Food")
        self.assertEqual("food", a_thing.id().to_s())


class DoorWasLocked(Event):
    pass


class Locked(Wall):
    def __init__(self, door, secret):
        self._door = door
        self._secret = secret
        self._is_locked = True
        self._subject = Subject()

    def go(self):
        if self._is_locked:
            self._notify_observers(DoorWasLocked())
        else:
            self._door.go()

    def unlock_with(self, key):
        self._is_locked = not key.match(self._secret)
        return

    def register(self, observer):
        super().register(observer)
        self._door.register(observer)


class TestLockedDoor(TestCase):

    def setUp(self) -> None:
        self.observer = FakeObserver()

    @expect_event(DoorWasLocked)
    def test_should_be_locked_if_no_key(self):
        locked_door = Locked(Door("another_place"), ThingKey("supersecret"))
        locked_door.register(self.observer)
        locked_door.go()

    @expect_event(PlayerMoved)
    def test_should_be_unlocked_with_the_right_key(self):
        locked_door = Locked(Door("another_place"), ThingKey("supersecret"))
        locked_door.register(self.observer)
        key = Key.from_raw("TheKey", "supersecret")
        key.apply_on(locked_door)
        locked_door.go()
