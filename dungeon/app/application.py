from dungeon.app.domain.player.player import Player
from dungeon.app.game import Game


class Application:
    def __init__(self, obtain_user_command, printer, factory, toggles):
        self._toggles = toggles
        self._obtain_user_command = obtain_user_command
        self._printer = printer
        self._factory = factory

    def run(self, dungeon_name='game'):
        player = self._setup_player()
        dungeon = self._setup_dungeon(dungeon_name)
        game = Game(obtain_input=self._obtain_user_command, printer=self._printer)
        game.run(player, dungeon)

    def _setup_player(self):
        player = Player(toggles=self._toggles)
        player.register(self._printer)
        return player

    def _setup_dungeon(self, dungeon_name):
        dungeon = self._factory.make(dungeon_name)
        dungeon.register(self._printer)
        return dungeon
