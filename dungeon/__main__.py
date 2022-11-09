import sys

from dungeon.game import Game


def main(args=None):
    if args is None:
        args = sys.argv[1:]

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


if __name__ == "__main__":
    sys.exit(main())
