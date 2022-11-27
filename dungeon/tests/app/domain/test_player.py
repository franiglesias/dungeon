import unittest

from dungeon.app.command.action_result import ActionResult, WithCost
from dungeon.app.command.command import Command
from dungeon.app.domain.player import Player, EnergyUnit


class ExitDungeonCommand(Command):
    def do(self, receiver):
        return WithCost(ActionResult.player_exited("You're out"), EnergyUnit(1))


class KillerCommand(Command):
    def __init__(self, energy_consumption):
        self._energy_consumption = energy_consumption

    def do(self, receiver):
        return WithCost(ActionResult.player_acted("You're dead!"), self._energy_consumption)


class PlayerTestCase(unittest.TestCase):
    def test_player_should_be_ready_for_action(self):
        player = Player.awake()

        self.assertTrue(player.is_alive())
        self.assertFalse(player.has_won())
        self.assertIn("I'm ready", player.said())
        self.assertIn("Remaining energy: 100", player.said())

    def test_player_should_be_able_to_exit_dungeon(self):
        player = Player.awake()

        player.do(ExitDungeonCommand(""), player)

        self.assertTrue(player.is_alive())
        self.assertTrue(player.has_won())
        self.assertIn("You're out", player.said())
        self.assertIn("Remaining energy: 99", player.said())

    def test_player_dies_if_action_consumes_all_energy(self):
        player = Player.awake_with_energy(EnergyUnit(10))
        player.do(KillerCommand(EnergyUnit(15)), player)
        self.assertFalse(player.is_alive())
        self.assertFalse(player.has_won())
        self.assertIn("You're dead!", player.said())
        self.assertIn("Remaining energy: -5", player.said())

    def test_player_does_not_die_if_action_does_not_consume_all_energy(self):
        player = Player.awake_with_energy(EnergyUnit(10))
        player.do(KillerCommand(EnergyUnit(5)), player)
        self.assertTrue(player.is_alive())


if __name__ == '__main__':
    unittest.main()
