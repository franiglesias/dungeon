import sys

from dungeon.app.application import Application
from dungeon.app.domain.dungeon_factory import DungeonFactory
from dungeon.app.toggles.toggles import Toggles
from dungeon.for_obtaining_commands.console_obtain_user_command import ConsoleObtainUserCommand
from dungeon.for_showing_output.console_show_output import ConsoleShowOutput


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    toggles = Toggles()
    application = Application(ConsoleObtainUserCommand(), ConsoleShowOutput(), DungeonFactory(), toggles)
    application.run()


if __name__ == "__main__":
    sys.exit(main())
