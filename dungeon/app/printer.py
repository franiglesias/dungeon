from dungeon.app.Scene import Scene


class Printer:
    def __init__(self, show_output):
        self.show_output = show_output
        self._command = ""
        self._description = ""
        self._energy = ""

    def notify(self, event):
        if event.name() == "player_energy_changed":
            self._energy = str(event.energy().value())
        elif event.name() == "player_got_description":
            self._description = event.description()
        else:
            self._command = "{} {}".format(event.command(), event.argument())

    def draw(self):
        scene = Scene(
            title="",
            command=self._command,
            description=self._description,
            energy=self._energy
        )

        return self.show_output.put(scene)
