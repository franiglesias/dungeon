from dungeon.app.domain.player.player_events import PlayerExited, PlayerDied


class Game:
    def __init__(self, obtain_input, printer):
        self._finished = False
        self._input = obtain_input
        self._printer = printer

    def run(self, player, dungeon):
        dungeon.register(self)
        player.awake_in(dungeon)
        self._printer.draw()
        while not self.finished():
            player.do(self._input.command())
            self._printer.draw()

    def notify(self, event):
        if event.of_type(PlayerExited):
            self._finished = True
        if event.of_type(PlayerDied):
            self._finished = True

    def finished(self):
        return self._finished
