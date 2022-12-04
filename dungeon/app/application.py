from dungeon.app.Scene import Scene
from dungeon.app.domain.player import Player
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
        dungeon = self._build_dungeon(dungeon_name)
        player = Player.awake()
        player.register(self._printer)
        dungeon.register(self._printer)
        while player.is_alive() and not player.has_won():
            command = self._obtain_command()
            player.do(command, dungeon)
            self._printer.draw()

    def _obtain_command(self):
        return self._obtain_user_command.command()

    def _show_scene(self, scene):
        self._show_output.put(scene)

    def _build_dungeon(self, dungeon):
        return self._factory.make(dungeon)
