from dungeon.command.command import Command
from dungeon.game import Game


class Application:
    def __init__(self, obtain_user_command, show_output):
        self._obtain_user_command = obtain_user_command
        self._show_output = show_output

    def run(self):
        self._show_output.put("Welcome to the Dungeon")
        print("-")
        game = Game()
        game.start()
        finished = False
        while not finished:
            instruction = self._obtain_user_command.command()
            command = Command.from_user_input(instruction)
            result = game.execute(instruction)
            self._show_output.put(str(command))
            print(result)
            print("-")
            finished = result == "Congrats. You're out"
        print("-")
