from dungeon.app.domain.player import Player


class Application:
    def __init__(self, obtain_user_command, show_output, factory, toggles):
        self._toggles = toggles
        self._obtain_user_command = obtain_user_command
        self._show_output = show_output
        self._factory = factory

    def run(self, dungeon='game'):
        self.run_with_player(dungeon)

    def run_with_player(self, dungeon_name):
        self._show_message("Welcome to the Dungeon")
        dungeon = self._build_dungeon(dungeon_name)
        player = Player()

        while player.is_alive() and not player.has_won():
            command = self._obtain_command()
            player.do(command, dungeon)
            self._show_message(str(command))
            self._show_message(player.said())

    def _obtain_command(self):
        return self._obtain_user_command.command()

    def _show_message(self, message):
        self._show_output.put(message)

    def _build_dungeon(self, dungeon):
        return self._factory.make(dungeon)
