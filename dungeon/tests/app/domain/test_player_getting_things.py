import unittest

from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.thing import Thing


class PlayerGettingThingsTestCase(unittest.TestCase):
    def test_player_get_object_removes_from_room(self):
        player = Player.awake()
        dungeon = self.dungeon_with_object(Thing("Food"))
        player.awake_in(dungeon)
        get_command = GetCommand("food")
        player.do(get_command)
        description = dungeon.look('objects')
        self.assertIn("There are no objects", description.get("message"))

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
