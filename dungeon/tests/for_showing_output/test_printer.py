import unittest

from dungeon.app.domain.player import PlayerEnergyChanged, EnergyUnit, PlayerSentCommand
from dungeon.app.printer import Printer


class PrinterAsObserverTestCase(unittest.TestCase):
    def test_handles_energy_changed_event(self):
        event = PlayerEnergyChanged(EnergyUnit(50))

        printer = Printer()
        printer.notify(event)

        output = printer.draw()
        self.assertIn("50", output)

    def test_handles_different_energy_changed_event(self):
        event = PlayerEnergyChanged(EnergyUnit(60))

        printer = Printer()
        printer.notify(event)

        output = printer.draw()
        self.assertIn("60", output)

    def test_handles_command_sent_event(self):
        event = PlayerSentCommand("command", "argument")

        printer = Printer()
        printer.notify(event)

        output = printer.draw()
        self.assertIn("command argument", output)


if __name__ == '__main__':
    unittest.main()
