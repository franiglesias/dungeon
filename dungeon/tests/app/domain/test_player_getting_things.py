import unittest

from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.thing import Thing
from dungeon.tests.decorators import expect_event_containing, expect_event
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class PlayerGettingThingsTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.observer = FakeObserver()
        self.player.register(self.observer)

    @expect_event_containing("player_got_description", "description", "There are no objects")
    def test_player_get_object_removes_from_room(self):
        dungeon = self.dungeon_with_object(Thing("Food"))
        dungeon.register(self.observer)
        self.player.awake_in(dungeon)
        self.player.do(GetCommand("food"))
        dungeon.look('objects')

    def test_player_get_object_and_holds(self):
        thing = Thing("Food")
        dungeon = self.dungeon_with_object(thing)
        self.player.awake_in(dungeon)
        get_command = GetCommand("food")
        self.player.do(get_command)
        self.assertEqual(thing, self.player.holds())

    def dungeon_with_object(self, thing=Thing("Food")):
        builder = DungeonBuilder()
        builder.add('start')
        builder.put('start', thing)
        return builder.build()


if __name__ == '__main__':
    unittest.main()
