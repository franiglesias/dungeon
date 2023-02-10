import sys

from dungeon.app.application import Application
from dungeon.app.domain.command.command_factory import CommandFactory, Autodiscover
from dungeon.app.domain.dungeon_factory import DungeonFactory
from dungeon.app.printer import Printer
from dungeon.app.toggles.toggles import Toggles
from dungeon.for_obtaining_commands.console_obtain_user_command import ConsoleObtainUserCommand
from dungeon.for_showing_output.rich_console_show_output import RichConsoleShowOutput


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    command_factory = CommandFactory(Autodiscover("dungeon.app.domain.command.commands"))
    obtain_user_command = ConsoleObtainUserCommand(command_factory)
    printer = Printer(RichConsoleShowOutput())
    toggles = Toggles()
    application = Application(obtain_user_command, printer, DungeonFactory(), toggles)
    application.run()


if __name__ == "__main__":
    sys.exit(main())
