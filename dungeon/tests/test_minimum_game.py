import unittest

from dungeon.game import Game


class OneRoomDungeonTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.start()

    def test_player_finds_easy_way_out(self):
        self.assertEqual("Congrats. You're out", self.game.execute("go north"))

    def test_player_tries_closed_wall(self):
        self.assertEqual("You hit a wall", self.game.execute("go south"))

    def test_player_tries_another_closed_wall(self):
        self.assertEqual("You hit a wall", self.game.execute("go east"))

    def test_unknown_command(self):
        self.assertEqual("I don't understand", self.game.execute("foo bar"))

    def test_player_can_look_around(self):
        description = """North: There is a door
East: There is a wall
South: There is a wall
West: There is a wall
That's all
"""
        self.assertEqual(description, self.game.execute("look around"))


if __name__ == '__main__':
    unittest.main()
