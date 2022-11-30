from unittest import TestCase

from dungeon.app.command.action_result import ActionResult
from dungeon.app.domain.player import EnergyUnit


class TestActionResult(TestCase):
    def test_generic_action_result(self):
        result = ActionResult.player_acted("message")

        self.assertFalse(result.get("exited"))
        self.assertIsNone(result._bag.get("destination"))

    def test_moving_action_result(self):
        result = ActionResult.player_moved("message", 'room')

        self.assertFalse(result.get("exited"))
        self.assertEqual('room', result._bag.get("destination"))

    def test_exit_action_result(self):
        result = ActionResult.player_exited("message")

        self.assertTrue(result.get("exited"))
        self.assertIsNone(result._bag.get("destination"))

    def test_game_started_result(self):
        result = ActionResult.game_started()

        self.assertFalse(result._bag.get("exited"))
        self.assertIsNone(result._bag.get("destination"))

    def test_action_result_with_cost(self):
        result = ActionResult.player_acted("Action")
        result.set('cost', EnergyUnit(3))
        self.assertEqual(EnergyUnit(3), result._bag.get("cost"))
