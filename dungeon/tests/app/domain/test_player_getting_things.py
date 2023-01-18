import unittest

from dungeon.app.command.commands.collect_command import CollectCommand
from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.command.commands.look_command import LookCommand
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.player.player_events import PlayerGotDescription, BackpackChanged, ActionNotCompleted
from dungeon.app.domain.thing import Thing
from dungeon.app.toggles.toggles import Toggles
from dungeon.tests.decorators import expect_event_containing, expect_event_equal, expect_event
from dungeon.tests.fakes.observers.fake_observer import FakeObserver
from mothers.dungeon import DungeonMother
from mothers.things import ThingMother


class PlayerGettingThingsTestCase(unittest.TestCase):
    def setUp(self):
        self.toggle = Toggles()
        self.player = Player(toggles=self.toggle)
        self.observer = FakeObserver()
        self.player.register(self.observer)

    @expect_event_containing(PlayerGotDescription, "description", "There are no objects")
    def test_player_get_object_removes_from_room(self):
        dungeon = DungeonMother.with_objects(ThingMother.with_name("Food"))
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(GetCommand("food"))
        dungeon.look('objects')

    @expect_event(ActionNotCompleted)
    def test_player_tries_to_get_not_existing_thing(self):
        dungeon = DungeonMother.with_objects()
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(GetCommand("food"))

    def test_player_get_object_and_holds(self):
        food = ThingMother.with_name("Food")
        dungeon = DungeonMother.with_objects(food)
        self.player.awake_in(dungeon)
        self.player.do(GetCommand("food"))
        self.assertEqual(food, self.player.holds())

    def test_player_get_object_from_backpack_and_holds(self):
        food = ThingMother.with_name("Food")
        dungeon = DungeonMother.with_objects(food)
        self.player.awake_in(dungeon)
        self.player.do(CollectCommand("food"))
        self.player.do(GetCommand("food"))
        self.assertEqual(food, self.player.holds())

    @expect_event_containing(BackpackChanged, "content", "")
    def test_player_get_object_removes_from_backpack(self):
        dungeon = DungeonMother.with_objects(Thing.from_raw("Food"))
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(CollectCommand("food"))
        self.player.do(GetCommand("food"))

    @expect_event_containing(PlayerGotDescription, "description", "Food")
    def test_player_get_two_objects_and_holds_the_last_one(self):
        things = ThingMother.from_names("Food", "Sword")
        dungeon = DungeonMother.with_objects(*things)
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(GetCommand("food"))
        self.player.do(GetCommand("sword"))
        self.player.do(LookCommand("objects"))
        self.assertEqual(things[1], self.player.holds())

    @expect_event_equal(BackpackChanged, "content", "Sword")
    def test_player_collects_two_objects_and_holds_the_last_one(self):
        things = ThingMother.from_names("Food", "Sword")
        dungeon = DungeonMother.with_objects(*things)
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(CollectCommand("food"))
        self.player.do(CollectCommand("sword"))
        self.player.do(GetCommand("sword"))
        self.player.do(GetCommand("food"))
        self.assertEqual(things[0], self.player.holds())


if __name__ == '__main__':
    unittest.main()
