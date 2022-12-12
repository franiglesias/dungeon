import unittest

from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.thing import Thing
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class PlayerGettingThingsTestCase(unittest.TestCase):
    def test_player_get_object_removes_from_room(self):
        fake_observer = FakeObserver()
        player = Player.awake()
        dungeon = self.dungeon_with_object(Thing("Food"))
        dungeon.register(fake_observer)
        player.awake_in(dungeon)
        get_command = GetCommand("food")
        player.do(get_command)
        dungeon.look('objects')
        last_event = fake_observer.last("player_got_description")
        self.assertIn("There are no objects", last_event.description())

    def test_player_get_object_and_holds(self):
        thing = Thing("Food")
        player = Player.awake()
        dungeon = self.dungeon_with_object(thing)
        player.awake_in(dungeon)
        get_command = GetCommand("food")
        player.do(get_command)
        self.assertEqual(thing, player.holds())

    def dungeon_with_object(self, thing=Thing("Food")):
        builder = DungeonBuilder()
        builder.add('start')
        builder.put('start', thing)
        return builder.build()


if __name__ == '__main__':
    unittest.main()
