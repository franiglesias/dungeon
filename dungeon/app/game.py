class Game:
    def __init__(self, player, obtain_input, printer):
        self._finished = False
        self._player = player
        self._input = obtain_input
        self._printer = printer

    def run(self):
        while not self.finished():
            self._player.do(self._input.command())
            self._printer.draw()

    def notify(self, event):
        if event.name() == "player_exited":
            self._finished = True
        if event.name() == "player_died":
            self._finished = True

    def finished(self):
        return self._finished
