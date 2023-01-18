import unittest

from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.command.commands.use_command import UseCommand
from dungeon.app.domain.player.energy import EnergyUnit
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.player.player_events import ActionNotCompleted, PlayerEnergyChanged
from dungeon.app.domain.thing import Thing, Food
from dungeon.app.toggles.toggles import Toggles
from dungeon.tests.decorators import expect_event_equal, expect_event
from dungeon.tests.fakes.observers.fake_observer import FakeObserver
from mothers.dungeon import DungeonMother


class PlayerUsingFoodTestCase(unittest.TestCase):
    def setUp(self):
        self.toggle = Toggles()
        self.player = Player(EnergyUnit(50), toggles=self.toggle)
        self.observer = FakeObserver()

    @expect_event_equal(PlayerEnergyChanged, "energy", EnergyUnit(58))
    def test_using_food_makes_player_increase_energy(self):
        dungeon = DungeonMother.with_objects(Food.from_raw("Banana"))
        self.player.awake_in(dungeon)
        self.player.register(self.observer)

        self.player.do(GetCommand("Banana"))
        self.player.do(UseCommand("Banana"))

        self.assertIsNone(self.player.holds())

    @expect_event(ActionNotCompleted)
    @expect_event_equal(PlayerEnergyChanged, "energy", EnergyUnit(49))
    def test_trying_to_use_an_object_but_holding_none(self):
        dungeon = DungeonMother.with_objects(Thing.from_raw("Food"))
        self.player.awake_in(dungeon)
        self.player.register(self.observer)
        self.player.do(UseCommand("food"))

        self.assertIsNone(self.player.holds())


if __name__ == '__main__':
    unittest.main()
