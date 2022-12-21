import unittest

from dungeon.app.command.commands.collect_command import CollectCommand
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.player.player_events import PlayerCollectedThing, PlayerGotDescription, BackpackChanged
from dungeon.app.domain.thing import Thing
from dungeon.tests.decorators import expect_event_containing, expect_event
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class CollectingThingsTestCase(unittest.TestCase):
    def setUp(self):
        self.thing = Thing("Food")
        self.builder = DungeonBuilder()
        self.observer = FakeObserver()
        self.player = Player()
        self.player.register(self.observer)

    @expect_event_containing(PlayerGotDescription, "description", "There are no objects")
    def test_player_collect_object_removes_from_room(self):
        dungeon = self.dungeon_with_object(Thing("Food"))
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(CollectCommand("food"))
        dungeon.look('objects')

    @expect_event(PlayerCollectedThing)
    def test_dungeon_raises_event(self):
        dungeon = self.dungeon_with_object(Thing("Food"))
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(CollectCommand("food"))

    @expect_event_containing(BackpackChanged, "content", "Food")
    def test_player_added_item_to_backpack(self):
        dungeon = self.dungeon_with_object(Thing("Food"))
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(CollectCommand("food"))

    def dungeon_with_object(self, thing=Thing("Food")):
        builder = DungeonBuilder()
        builder.add('start')
        builder.put('start', thing)
        return builder.build()


if __name__ == '__main__':
    unittest.main()
