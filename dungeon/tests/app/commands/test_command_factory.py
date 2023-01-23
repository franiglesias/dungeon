from unittest import TestCase

from dungeon.app.domain.command.command_factory import Autodiscover
from dungeon.app.domain.command.commands.go_command import GoCommand
from dungeon.app.domain.command.commands.invalid_command import InvalidCommand


class TestCommandFactoryAutodiscoveryEngine(TestCase):
    def test_autodiscover_commands(self):
        autodiscover = Autodiscover("dungeon.app.domain.command.commands")
        command = autodiscover.by_name("go", "argument")
        self.assertIsInstance(command, GoCommand)

    def test_fallback_to_invalid_if_no_command_found(self):
        autodiscover = Autodiscover("dungeon.app.domain.command.commands")
        command = autodiscover.by_name("yadayadayada", "argument")
        self.assertIsInstance(command, InvalidCommand)
