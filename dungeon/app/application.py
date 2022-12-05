from dungeon.app.Scene import Scene
from dungeon.app.domain.player import Player
from dungeon.app.printer import Printer


class Game:
    def __init__(self, player, input, printer, dungeon):
        self._dungeon = dungeon
        self._player = player
        self._input = input
        self._printer = printer

    def run(self):
        while self.not_finished():
            command = self._input.command()
            self._player.do(command, self._dungeon)
            self._printer.draw()

    def not_finished(self):
        return self._player.is_alive() and not self._player.has_won()


class Application:
    def __init__(self, obtain_user_command, show_output, factory, toggles):
        self._toggles = toggles
        self._obtain_user_command = obtain_user_command
        self._show_output = show_output
        self._printer = Printer(show_output)
        self._factory = factory

    def run(self, dungeon_name='game'):
        self._show_scene(Scene(title="Welcome to the Dungeon", command="", description="", energy="100"))
        dungeon = self._build_dungeon(dungeon_name)
        player = Player.awake()
        player.register(self._printer)
        dungeon.register(self._printer)
        game = Game(player=player, printer=self._printer, input=self._obtain_user_command, dungeon=dungeon)
        game.run()

    def _show_scene(self, scene):
        self._show_output.put(scene)

    def _build_dungeon(self, dungeon):
        return self._factory.make(dungeon)
