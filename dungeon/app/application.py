from dungeon.app.scene import Scene
from dungeon.app.domain.player.player import Player
from dungeon.app.game import Game
from dungeon.app.printer import Printer


class Application:
    def __init__(self, obtain_user_command, show_output, factory, toggles):
        self._toggles = toggles
        self._obtain_user_command = obtain_user_command
        self._show_output = show_output
        self._printer = Printer(show_output)
        self._factory = factory

    def run(self, dungeon_name='game'):
        self._show_scene(Scene(title="Welcome to the Dungeon", command="", description="", energy="100"))
        game = Game(obtain_input=self._obtain_user_command, printer=self._printer)
        dungeon = self._build_dungeon(dungeon_name, game)
        player = self._setup_player(dungeon)
        game.run(player)

    def _setup_player(self, dungeon):
        player = Player.awake()
        player.register(self._printer)
        player.awake_in(dungeon)
        return player

    def _build_dungeon(self, dungeon_name, game):
        dungeon = self._factory.make(dungeon_name)
        dungeon.register(self._printer)
        dungeon.register(game)
        return dungeon

    def _show_scene(self, scene):
        self._show_output.put(scene)
