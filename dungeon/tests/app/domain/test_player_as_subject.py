import unittest

from dungeon.app.command.action_result import ActionResult
from dungeon.app.command.command import Command
from dungeon.app.domain.player import Player, EnergyUnit


class TestCommand(Command):
    def __init__(self, energy_consumption):
        self._energy_consumption = energy_consumption

    def do(self, receiver):
        result = ActionResult.player_acted("You did something")
        result.set('cost', self._energy_consumption)
        result.set('command', "test command")
        return result


class FakeObserver:
    def __init__(self):
        self._events = dict()

    def notify(self, event):
        self._events[event.name()] = event

    def is_aware_of(self, event_name):
        return event_name in self._events.keys()


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

    def test_notifies_player_got_description_event(self):
        fake_observer = FakeObserver()

        player = Player.awake_with_energy(EnergyUnit(100))
        player.register(fake_observer)

        player.do(TestCommand(EnergyUnit(50)))

        self.assertTrue(fake_observer.is_aware_of("player_got_description"))


if __name__ == '__main__':
    unittest.main()
