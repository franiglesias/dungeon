import unittest

from dungeon.app.command.commands.get_command import GetCommand
from dungeon.app.command.commands.go_command import GoCommand
from dungeon.app.command.commands.open_command import OpenCommand
from dungeon.app.domain.dir import Dir
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.player.player import Player
from dungeon.app.domain.player.player_events import ActionNotCompleted, PlayerExited
from dungeon.app.domain.thing import Key, Food, Thing, ThingKey
from dungeon.app.domain.wall import Exit, Locked
from dungeon.tests.decorators import expect_event
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class PlayerOpeningDoorsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.observer = FakeObserver()

    @expect_event(ActionNotCompleted)
    def test_not_having_key_does_not_open_doors(self):
        dungeon = self.dungeon_with_locked_exit()
        dungeon.register(self.observer)
        player = Player()
        player.awake_in(dungeon)
        player.register(self.observer)
        player.do(OpenCommand("north"))

    @expect_event(ActionNotCompleted)
    def test_object_that_is_not_a_key_does_not_open_doors(self):
        dungeon = self.dungeon_with_locked_exit()
        dungeon.register(self.observer)
        player = Player()
        player.awake_in(dungeon)
        player.register(self.observer)
        player.do(GetCommand("food"))
        player.do(OpenCommand("north"))

    @expect_event(PlayerExited)
    def test_key_allows_open_door_and_go_through_it(self):
        dungeon = self.dungeon_with_locked_exit()
        dungeon.register(self.observer)
        player = Player()
        player.awake_in(dungeon)
        player.register(self.observer)
        player.do(GetCommand("key"))
        player.do(OpenCommand("north"))
        player.do(GoCommand("north"))

    def dungeon_with_locked_exit(self):
        builder = DungeonBuilder()
        builder.add('start')
        builder.set('start', Dir.N, Locked(Exit(), ThingKey("super-secret")))
        builder.put('start', Key.from_raw("key", "super-secret"))
        builder.put('start', Food.from_raw("food"))
        return builder.build()


if __name__ == '__main__':
    unittest.main()
