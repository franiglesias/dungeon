class Game:
    def __init__(self, obtain_input, printer):
        self._finished = False
        self._input = obtain_input
        self._printer = printer

    def run(self, player):
        while not self.finished():
            player.do(self._input.command())
            self._printer.draw()

    def notify(self, event):
        if event.name() == "player_exited":
            self._finished = True
        if event.name() == "player_died":
            self._finished = True

    def finished(self):
        return self._finished
