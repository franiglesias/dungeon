from dungeon.app.Scene import Scene
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
        player = self.set_up_player(dungeon_name)
        game = Game(player=player, obtain_input=self._obtain_user_command, printer=self._printer)
        game.run()

    def set_up_player(self, dungeon_name):
        dungeon = self._build_dungeon(dungeon_name)
        player = Player.awake()
        player.register(self._printer)
        dungeon.register(self._printer)
        player.awake_in(dungeon)
        return player

    def _show_scene(self, scene):
        self._show_output.put(scene)

    def _build_dungeon(self, dungeon):
        return self._factory.make(dungeon)
