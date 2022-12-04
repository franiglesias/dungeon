from dungeon.app.Scene import Scene


class Printer:
    def __init__(self, show_output):
        self.show_output = show_output
        self._command = ""
        self._energy = ""

    def notify(self, event):
        if event.name() == "player_energy_changed":
            self._energy = str(event.energy().value())
        else:
            self._command = "{} {}".format(event.command(), event.argument())

    def draw(self):
        scene = Scene(title="", command=self._command, description="", energy=self._energy)

        return self.show_output.put(scene)
