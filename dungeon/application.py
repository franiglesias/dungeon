from dungeon.command.action_result import ActionResult
from dungeon.dungeon_pkg.dungeon_factory import DungeonFactory
from dungeon.game import Game


class Application:
    def __init__(self, obtain_user_command, show_output, dungeon_name='game'):
        self._obtain_user_command = obtain_user_command
        self._show_output = show_output
        self._dungeon_name = dungeon_name

    def run(self):
        self._show_output.put("Welcome to the Dungeon")
        dungeon = self._build_dungeon()
        game = Game()
        game.start(dungeon)
        action_result = ActionResult.player_acted("")
        while not action_result.is_finished():
            command = self._obtain_user_command.command()
            action_result = game.do_command(command)
            self._show_output.put(str(command))
            self._show_output.put(action_result.message())

    def _build_dungeon(self):
        factory = DungeonFactory()
        return factory.make(self._dungeon_name)
