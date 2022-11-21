import unittest

from dungeon.app.command.command import Command
from dungeon.app.domain.dir import Dir
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.wall import Exit
from dungeon.app.domain.game import Game


class OneRoomDungeonTestCase(unittest.TestCase):
    def setUp(self):
        builder = DungeonBuilder()
        builder.add('start')
        builder.set('start', Dir.N, Exit())
        dungeon = builder.build()
        self.game = Game()
        self.game.start(dungeon)

    def execute_user_action(self, action):
        return self.game.do_command(Command.from_user_input(action)).message()

    def test_player_finds_easy_way_out(self):
        self.assertEqual("Congrats. You're out", self.execute_user_action("go north"))

    def test_player_tries_closed_wall(self):
        self.assertEqual("You hit a wall", self.execute_user_action("go south"))

    def test_player_tries_another_closed_wall(self):
        self.assertEqual("You hit a wall", self.execute_user_action("go east"))

    def test_unknown_command(self):
        self.assertEqual("I don't understand", self.execute_user_action("foo bar"))

    def test_player_can_look_around(self):
        description = """North: There is a door
East: There is a wall
South: There is a wall
West: There is a wall
That's all
"""
        self.assertEqual(description, self.execute_user_action("look around"))


if __name__ == '__main__':
    unittest.main()
