from unittest import TestCase

from dungeon.app.command.action_result import ActionResult


class TestActionResult(TestCase):
    def test_generic_action_result(self):
        result = ActionResult.player_acted("message")

        self.assertFalse(result.is_finished())
        self.assertIsNone(result.moved_to())

    def test_moving_action_result(self):
        result = ActionResult.player_moved("message", 'room')

        self.assertFalse(result.is_finished())
        self.assertEqual('room', result.moved_to())

    def test_exit_action_result(self):
        result = ActionResult.player_exited("message")

        self.assertTrue(result.is_finished())
        self.assertIsNone(result.moved_to())

    def test_game_started_result(self):
        result = ActionResult.game_started()

        self.assertFalse(result.is_finished())
        self.assertIsNone(result.moved_to())
