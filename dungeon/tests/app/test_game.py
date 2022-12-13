import unittest

from dungeon.app.domain.dungeon_factory import DungeonFactory
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.player.player_events import PlayerExited, PlayerDied
from dungeon.app.game import Game
from dungeon.app.printer import Printer
from dungeon.tests.fakes.obtain_user_command.fixed_obtain_user_command import FixedObtainUserCommand
from dungeon.tests.fakes.show_output.fake_show_output import FakeShowOutput


class GameTestCase(unittest.TestCase):
    def test_game_handles_player_exited_event(self):
        dungeon = DungeonFactory().make('test')
        player = Player()
        player.awake_in(dungeon)

        game = Game(obtain_input=FixedObtainUserCommand("go north"), printer=Printer(FakeShowOutput()))
        game.notify(PlayerExited())

        self.assertTrue(game.finished())

    def test_game_handles_player_died_event(self):
        dungeon = DungeonFactory().make('test')
        player = Player()
        player.awake_in(dungeon)

        game = Game(obtain_input=FixedObtainUserCommand("go north"), printer=Printer(FakeShowOutput()))
        game.notify(PlayerDied())

        self.assertTrue(game.finished())


if __name__ == '__main__':
    unittest.main()
