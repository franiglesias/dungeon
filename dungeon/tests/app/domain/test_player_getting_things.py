import unittest

from dungeon.app.command.commands.collect_command import CollectCommand
from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.command.commands.look_command import LookCommand
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.player.player_events import PlayerGotDescription, BackpackChanged
from dungeon.app.domain.thing import Thing
from dungeon.tests.decorators import expect_event_containing, expect_event_equal
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class PlayerGettingThingsTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.observer = FakeObserver()
        self.player.register(self.observer)

    @expect_event_containing(PlayerGotDescription, "description", "There are no objects")
    def test_player_get_object_removes_from_room(self):
        dungeon = self.dungeon_with_object(Thing.from_raw("Food"))
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(GetCommand("food"))
        dungeon.look('objects')

    def test_player_get_object_and_holds(self):
        thing = Thing.from_raw("Food")
        dungeon = self.dungeon_with_object(thing)
        self.player.awake_in(dungeon)
        self.player.do(GetCommand("food"))
        self.assertEqual(thing, self.player.holds())

    def test_player_get_object_from_backpack_and_holds(self):
        thing = Thing.from_raw("Food")
        dungeon = self.dungeon_with_object(thing)
        self.player.awake_in(dungeon)
        self.player.do(CollectCommand("food"))
        self.player.do(GetCommand("food"))
        self.assertEqual(thing, self.player.holds())

    @expect_event_containing(BackpackChanged, "content", "")
    def test_player_get_object_removes_from_backpack(self):
        dungeon = self.dungeon_with_object(Thing.from_raw("Food"))
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(CollectCommand("food"))
        self.player.do(GetCommand("food"))

    @expect_event_containing(PlayerGotDescription, "description", "Food")
    def test_player_get_two_objects_and_holds_the_last_one(self):
        first = Thing.from_raw("Food")
        second = Thing.from_raw("Sword")
        dungeon = self.dungeon_with_objects(first, second)
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(GetCommand("food"))
        self.player.do(GetCommand("sword"))
        self.player.do(LookCommand("objects"))
        self.assertEqual(second, self.player.holds())

    @expect_event_equal(BackpackChanged, "content", "Sword")
    def test_player_collects_two_objects_and_holds_the_last_one(self):
        food = Thing.from_raw("Food")
        sword = Thing.from_raw("Sword")
        dungeon = self.dungeon_with_objects(food, sword)
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(CollectCommand("food"))
        self.player.do(CollectCommand("sword"))
        self.player.do(GetCommand("sword"))
        self.player.do(GetCommand("food"))
        self.assertEqual(food, self.player.holds())

    def dungeon_with_object(self, thing=Thing.from_raw("Food")):
        builder = DungeonBuilder()
        builder.add('start')
        builder.put('start', thing)
        return builder.build()

    def dungeon_with_objects(self, first, second):
        builder = DungeonBuilder()
        builder.add('start')
        builder.put('start', first)
        builder.put('start', second)
        return builder.build()


if __name__ == '__main__':
    unittest.main()
