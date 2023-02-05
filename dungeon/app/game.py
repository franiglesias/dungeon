from dungeon.app.domain.player.player_events import PlayerExited, PlayerDied, PlayerFinishedGame
from dungeon.app.domain.events.subject import Observer


class Game(Observer):
    def __init__(self, obtain_input, printer):
        self._finished = False
        self._input = obtain_input
        self._printer = printer

    def run(self, player, dungeon):
        player.register(self)
        dungeon.register(self)
        player.awake_in(dungeon)
        self._printer.welcome()
        while not self.finished():
            command = self._input.command()
            player.do(command)
            self._printer.draw()
        self._printer.goodbye()

    def notify(self, event):
        if event.of_type(PlayerExited):
            self._finished = True
        if event.of_type(PlayerDied):
            self._finished = True
        if event.of_type(PlayerFinishedGame):
            self._finished = True

    def finished(self):
        return self._finished
