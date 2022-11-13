from dungeon.command.command import Command
from dungeon.game import Game


class Application:
    def __init__(self, obtain_user_command, show_output):
        self._obtain_user_command = obtain_user_command
        self._show_output = show_output

    def run(self):
        self._show_output.put("Welcome to the Dungeon")
        game = Game()
        game.start()
        finished = False
        while not finished:
            command = self._obtain_user_command.command()
            result = game.do_command(command)
            self._show_output.put(str(command))
            self._show_output.put(result)
            finished = result == "Congrats. You're out"
