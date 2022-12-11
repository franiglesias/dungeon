import unittest

from dungeon.app.command.command import Command
from dungeon.app.domain.player.player import Player, EnergyUnit
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class TestCommand(Command):
    def __init__(self, energy_consumption):
        self._energy_consumption = energy_consumption

    def cost(self):
        return self._energy_consumption


class PlayerAsSubjectTestCase(unittest.TestCase):
    def test_can_register_an_observer_and_notify(self):
        fake_observer = FakeObserver()

        player = Player.awake_with_energy(EnergyUnit(100))
        player.register(fake_observer)

        player.do(TestCommand(EnergyUnit(50)))

        self.assertTrue(fake_observer.is_aware_of("player_energy_changed"))

    def test_notifies_player_sent_command_event(self):
        fake_observer = FakeObserver()

        player = Player.awake_with_energy(EnergyUnit(100))
        player.register(fake_observer)

        player.do(TestCommand(EnergyUnit(50)))

        self.assertTrue(fake_observer.is_aware_of("player_sent_command"))

    def test_notifies_player_died_event_when_energy_is_0(self):
        fake_observer = FakeObserver()

        player = Player.awake_with_energy(EnergyUnit(100))
        player.register(fake_observer)

        player.do(TestCommand(EnergyUnit(100)))

        self.assertTrue(fake_observer.is_aware_of("player_died"))


if __name__ == '__main__':
    unittest.main()
