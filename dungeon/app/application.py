from dungeon.app.command.action_result import ActionResult
from dungeon.app.domain.game import Game


class Application:
    def __init__(self, obtain_user_command, show_output, factory, toggles):
        self._toggles = toggles
        self._obtain_user_command = obtain_user_command
        self._show_output = show_output
        self._factory = factory

    def run(self, dungeon='game'):
        if not self._toggles.is_active('with_player'):
            self.run_with_game(dungeon)
        else:
            self.run_with_game(dungeon)

    def run_with_game(self, dungeon):
        self._show_message("Welcome to the Dungeon")
        game = self._prepare_game_with_dungeon(dungeon)
        action_result = ActionResult.player_acted("")
        while not action_result.is_finished():
            command = self._obtain_command()
            action_result = game.do_command(command)
            self._show_message(str(command))
            self._show_message(action_result.message())

    def _prepare_game_with_dungeon(self, dungeon):
        return Game(self._build_dungeon(dungeon))

    def _obtain_command(self):
        return self._obtain_user_command.command()

    def _show_message(self, message):
        self._show_output.put(message)

    def _build_dungeon(self, dungeon):
        return self._factory.make(dungeon)
