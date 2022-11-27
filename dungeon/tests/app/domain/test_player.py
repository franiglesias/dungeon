import unittest

from dungeon.app.command.action_result import ActionResult
from dungeon.app.command.command import Command
from dungeon.app.domain.player import Player


class ExitDungeonCommand(Command):
    def do(self, receiver):
        return ActionResult.player_exited("You're out")


class PlayerTestCase(unittest.TestCase):
    def test_player_should_be_ready_for_action(self):
        player = Player.awake()

        self.assertTrue(player.is_alive())
        self.assertFalse(player.has_won())
        self.assertEqual("I'm ready", player.said())

    def test_player_should_be_able_to_exit_dungeon(self):
        player = Player.awake()

        player.do(ExitDungeonCommand(""), player)

        self.assertTrue(player.is_alive())
        self.assertTrue(player.has_won())
        self.assertEqual("You're out", player.said())


if __name__ == '__main__':
    unittest.main()
