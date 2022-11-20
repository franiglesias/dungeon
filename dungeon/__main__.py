import sys

from dungeon.application import Application
from dungeon.dungeon_pkg.dungeon_factory import DungeonFactory
from dungeon.obtain_user_command import ConsoleObtainUserCommand
from dungeon.show_output import ConsoleShowOutput


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    application = Application(
        ConsoleObtainUserCommand(),
        ConsoleShowOutput(),
        DungeonFactory()
    )
    application.run()


if __name__ == "__main__":
    sys.exit(main())
