import unittest

from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.command.commands.use_command import UseCommand
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.player.energy import EnergyUnit
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.player.player_events import ActionNotCompleted, PlayerEnergyChanged
from dungeon.app.domain.thing import Thing
from dungeon.tests.decorators import expect_event_equal, expect_event
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class PlayerUsingFoodTestCase(unittest.TestCase):
    def setUp(self):
        self.observer = FakeObserver()

    @expect_event_equal(PlayerEnergyChanged, "energy", EnergyUnit(58))
    def test_using_food_makes_player_increase_energy(self):
        dungeon = self.dungeon_with_object(Thing("Food"))

        player = Player(EnergyUnit(50))
        player.awake_in(dungeon)
        player.register(self.observer)

        player.do(GetCommand("Food"))
        player.do(UseCommand("food"))

        self.assertIsNone(player.holds())

    @expect_event(ActionNotCompleted)
    @expect_event_equal(PlayerEnergyChanged, "energy", EnergyUnit(49))
    def test_trying_to_use_an_object_but_holding_none(self):
        dungeon = self.dungeon_with_object(Thing("Food"))

        player = Player(EnergyUnit(50))
        player.awake_in(dungeon)
        player.register(self.observer)
        player.do(UseCommand("food"))

        self.assertIsNone(player.holds())

    def dungeon_with_object(self, thing):
        builder = DungeonBuilder()
        builder.add('start')
        builder.put('start', thing)
        return builder.build()


if __name__ == '__main__':
    unittest.main()
