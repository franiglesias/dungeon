from dungeon.game import Game


class Application:
    def run(self):
        print("Welcome to the Dungeon")
        print("-")
        game = Game()
        game.start()
        finished = False
        while not finished:
            command = input()
            result = game.execute(command)
            print(result)
            print("-")
            finished = result == "Congrats. You're out"
        print("-")
