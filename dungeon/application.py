from dungeon.game import Game


class Application:
    def run(self):
        print("Welcome to the Dungeon")
        print("-")
        game = Game()
        game.start()
        print(game.execute("look around"))
        print("-")
        print(game.execute("go south"))
        print("-")
        print(game.execute("look around"))
        print("-")
        print(game.execute("go north"))
        print("-")
