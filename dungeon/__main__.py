import sys

from dungeon.application import Application
from dungeon.game import Game


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    application = Application()
    application.run()


if __name__ == "__main__":
    sys.exit(main())
