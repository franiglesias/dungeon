import unittest

from dungeon.app.domain.command.commands.bye_command import ByeCommand
from dungeon.app.domain.dungeon import Dungeon
from dungeon.app.domain.player.player import Player, EnergyUnit
from dungeon.app.domain.player.player_events import PlayerEnergyChanged, PlayerSentCommand, PlayerDied, PlayerAwake, \
    PlayerFinishedGame
from dungeon.app.domain.room import Rooms
from dungeon.tests.decorators import expect_event
from dungeon.app.domain.command.command import FakeCommand, FakeObserver


class PlayerAsSubjectTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.observer = FakeObserver()
        self.player.register(self.observer)

    @expect_event(PlayerEnergyChanged)
    def test_can_register_an_observer_and_notify(self):
        self.player.do(FakeCommand(EnergyUnit(50)))

    @expect_event(PlayerSentCommand)
    def test_notifies_player_sent_command_event(self):
        self.player.do(FakeCommand(EnergyUnit(50)))

    @expect_event(PlayerDied)
    def test_notifies_player_died_event_when_energy_is_0(self):
        self.player.do(FakeCommand(EnergyUnit(100)))

    @expect_event(PlayerAwake)
    def test_notifies_player_awake(self):
        self.player.awake_in(Dungeon(Rooms()))

    @expect_event(PlayerFinishedGame)
    def test_wants_to_finish_game(self):
        self.player.do(ByeCommand())


if __name__ == '__main__':
    unittest.main()
