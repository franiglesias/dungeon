from unittest import TestCase

from dungeon.app.domain.thing import ThingName, ThingId, Thing


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
