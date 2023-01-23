from unittest import TestCase

from dungeon.app.domain.dir import Dir
from dungeon.app.domain.player.player_events import PlayerMoved, DoorWasUnlocked, DoorWasLocked
from dungeon.app.domain.thing import ThingKey, Key
from dungeon.app.domain.wall import Wall, Exit, Door, Walls, Locked
from dungeon.tests.decorators import expect_event_containing, expect_event
from dungeon.app.domain.command.command import FakeObserver


class TestWalls(TestCase):
    def setUp(self):
        self.observer = FakeObserver()
        self.walls = Walls()

    def test_walls_collection_starts_with_all_walls(self):
        self.assertIsInstance(self.walls.get(Dir.N), Wall)
        self.assertIsInstance(self.walls.get(Dir.S), Wall)
        self.assertIsInstance(self.walls.get(Dir.E), Wall)
        self.assertIsInstance(self.walls.get(Dir.W), Wall)

    def test_can_set_a_wall(self):
        self.walls = self.walls.set(Dir.N, Exit())
        self.assertIsInstance(self.walls.get(Dir.N), Exit)

    @expect_event_containing(PlayerMoved, "room", "destination")
    def test_door_go_moves_player_to_another_room(self):
        door = Door('destination')
        door.register(self.observer)
        door.go()


class TestLocked(TestCase):

    def setUp(self) -> None:
        self.observer = FakeObserver()

    @expect_event(DoorWasUnlocked)
    def test_unlock_with_the_right_key(self):
        door = Door("dest")
        locked_door = Locked(door, ThingKey("secret"))
        locked_door.register(self.observer)
        key = Key.from_raw("Key", "secret")

        key.apply_on(locked_door)

    @expect_event(DoorWasLocked)
    def test_unlock_with_the_wrong_key(self):
        door = Door("dest")
        locked_door = Locked(door, ThingKey("secret"))
        locked_door.register(self.observer)
        key = Key.from_raw("Key", "wrong")

        key.apply_on(locked_door)
