class Printer:
    def __init__(self):
        self._command = ""
        self._energy = ""

    def notify(self, event):
        if event.name() == "player_energy_changed":
            self._energy = str(event.energy().value())
        else:
            self._command = "{} {}".format(event.command(), event.argument())

    def draw(self):
        output = self._command
        output += self._energy
        return output
