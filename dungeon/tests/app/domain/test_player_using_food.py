import unittest

from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.command.commands.use_command import UseCommand
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.player.energy import EnergyUnit
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.thing import Thing
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class PlayerUsingFoodTestCase(unittest.TestCase):
    def test_using_food_makes_player_increase_energy(self):
        thing = Thing("Food")
        fake_observer = FakeObserver()
        dungeon = self.dungeon_with_object(thing)

        player = Player.awake_with_energy(EnergyUnit(50))
        player.awake_in(dungeon)
        player.register(fake_observer)

        player.do(GetCommand("Food"))
        player.do(UseCommand("food"))

        last_energy_event = fake_observer.last("player_energy_changed")
        self.assertEqual(58, last_energy_event.energy().value())
        self.assertIsNone(player.holds())

    def dungeon_with_object(self, thing):
        builder = DungeonBuilder()
        builder.add('start')
        builder.put('start', thing)
        return builder.build()


if __name__ == '__main__':
    unittest.main()
