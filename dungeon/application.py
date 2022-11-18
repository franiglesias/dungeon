from dungeon.command.action_result import ActionResult
from dungeon.dungeon import DungeonBuilder
from dungeon.game import Game


class Application:
    def __init__(self, obtain_user_command, show_output):
        self._obtain_user_command = obtain_user_command
        self._show_output = show_output

    def run(self):
        self._show_output.put("Welcome to the Dungeon")
        dungeon_builder = DungeonBuilder()
        dungeon = dungeon_builder.build()
        game = Game()
        game.start(dungeon)
        action_result = ActionResult("")
        while not action_result.is_finished():
            command = self._obtain_user_command.command()
            action_result = game.do_command(command)
            self._show_output.put(str(command))
            self._show_output.put(action_result.message())
