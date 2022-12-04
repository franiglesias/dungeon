import unittest

from dungeon.app.domain.dungeon import PlayerMoved
from dungeon.app.domain.player import PlayerEnergyChanged, EnergyUnit, PlayerSentCommand, PlayerGotDescription
from dungeon.app.printer import Printer
from dungeon.tests.fakes.show_output.fake_show_output import FakeShowOutput


class PrinterAsObserverTestCase(unittest.TestCase):
    def setUp(self):
        self.show_output = FakeShowOutput()
        self.printer = Printer(self.show_output)

    def test_handles_energy_changed_event(self):
        event = PlayerEnergyChanged(EnergyUnit(50))

        self.printer.notify(event)
        self.printer.draw()
        self.assertIn("50", self.show_output.contents())

    def test_handles_different_energy_changed_event(self):
        event = PlayerEnergyChanged(EnergyUnit(60))

        self.printer.notify(event)
        self.printer.draw()
        self.assertIn("60", self.show_output.contents())

    def test_handles_command_sent_event(self):
        event = PlayerSentCommand("command", "argument")

        self.printer.notify(event)
        self.printer.draw()
        self.assertIn("command argument", self.show_output.contents())

    def test_handles_got_description_event(self):
        event = PlayerGotDescription("scene description")

        self.printer.notify(event)
        self.printer.draw()
        self.assertIn("scene description", self.show_output.contents())

    def test_handles_player_moved_event(self):
        event = PlayerMoved("another room")

        self.printer.notify(event)
        self.printer.draw()
        self.assertIn("another room", self.show_output.contents())


if __name__ == '__main__':
    unittest.main()
