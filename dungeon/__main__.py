import sys

from dungeon.application import Application
from dungeon.obtain_user_command import ConsoleObtainUserCommand
from dungeon.show_output import ConsoleShowOutput


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    application = Application(
        ConsoleObtainUserCommand(),
        ConsoleShowOutput()
    )
    application.run()


if __name__ == "__main__":
    sys.exit(main())
