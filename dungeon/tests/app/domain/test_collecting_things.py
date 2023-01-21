import unittest

from dungeon.app.command.commands.collect_command import CollectCommand
from dungeon.app.command.commands.look_command import LookCommand
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.player.player_events import PlayerCollectedThing, PlayerGotDescription, BackpackChanged
from dungeon.app.domain.thing import Thing
from dungeon.tests.decorators import expect_event_containing, expect_event
from dungeon.app.command.command import FakeObserver
from dungeon.app.domain.dungeon_builder import DungeonMother

OBJECT = "Food"


class CollectingThingsTestCase(unittest.TestCase):
    def setUp(self):
        self.observer = FakeObserver()
        dungeon = DungeonMother.with_objects(Thing.from_raw(OBJECT))
        dungeon.register(self.observer)
        self.player = Player()
        self.player.register(self.observer)
        self.player.awake_in(dungeon)

    @expect_event_containing(PlayerGotDescription, "description", "There are no objects")
    def test_collecting_thing_removes_it_from_room(self):
        self.player.do(CollectCommand(OBJECT))
        self.player.do(LookCommand('objects'))

    @expect_event_containing(BackpackChanged, "content", OBJECT)
    def test_collecting_thing_keeps_it_into_backpack(self):
        self.player.do(CollectCommand(OBJECT))

    @expect_event(PlayerCollectedThing)
    def test_collecting_thing_is_notified(self):
        self.player.do(CollectCommand(OBJECT))


if __name__ == '__main__':
    unittest.main()
