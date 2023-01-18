import unittest

from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.command.commands.go_command import GoCommand
from dungeon.app.command.commands.open_command import OpenCommand
from dungeon.app.domain.dir import Dir
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.player.player_events import ActionNotCompleted, PlayerExited
from dungeon.app.toggles.toggles import Toggles
from dungeon.tests.decorators import expect_event
from dungeon.tests.fakes.observers.fake_observer import FakeObserver
from mothers.dungeon import DungeonMother


class PlayerOpeningDoorsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.toggle = Toggles()
        self.player = Player(toggles=self.toggle)
        self.observer = FakeObserver()
        self.dungeon = DungeonMother.with_locked_exit(Dir.N)
        self.dungeon.register(self.observer)
        self.player.awake_in(self.dungeon)
        self.player.register(self.observer)

    @expect_event(ActionNotCompleted)
    def test_not_having_key_does_not_open_doors(self):
        self.player.do(OpenCommand("north"))

    @expect_event(ActionNotCompleted)
    def test_object_that_is_not_a_key_does_not_open_doors(self):
        self.player.do(GetCommand("food"))
        self.player.do(OpenCommand("north"))

    @expect_event(PlayerExited)
    def test_key_allows_open_door_and_go_through_it(self):
        self.player.do(GetCommand("key"))
        self.player.do(OpenCommand("north"))
        self.player.do(GoCommand("north"))


if __name__ == '__main__':
    unittest.main()
