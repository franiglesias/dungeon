from unittest import TestCase

from dungeon.app.domain.dir import Dir
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.thing import Thing
from dungeon.app.domain.wall import Exit
from dungeon.tests.fakes.observers.fake_observer import FakeObserver


class TestDungeonBuilder(TestCase):
    def test_can_add_room_with_exit_to_North(self):
        fake_observer = FakeObserver()
        builder = DungeonBuilder()
        builder.add('start')
        builder.set('start', Dir.N, Exit())

        dungeon = builder.build()
        dungeon.register(fake_observer)

        dungeon.go('north')
        self.assertTrue(fake_observer.is_aware_of("player_exited"))

    def test_can_add_room_with_several_doors(self):
        fake_observer = FakeObserver()
        builder = DungeonBuilder()
        builder.add('start')
        builder.set('start', Dir.N, Exit())
        builder.set('start', Dir.S, Exit())

        dungeon = builder.build()
        dungeon.register(fake_observer)

        dungeon.go('north')
        self.assertTrue(fake_observer.is_aware_of("player_exited"))

        dungeon.go('south')
        self.assertTrue(fake_observer.is_aware_of("player_exited"))

    def test_can_add_several_rooms(self):
        fake_observer = FakeObserver()
        builder = DungeonBuilder()
        builder.add('101')
        builder.add('start')
        builder.set('101', Dir.S, Exit())
        builder.set('start', Dir.N, Exit())

        dungeon = builder.build()
        dungeon.register(fake_observer)

        dungeon.go('north')
        self.assertTrue(fake_observer.is_aware_of("player_exited"))

    def test_can_connect_rooms(self):
        builder = DungeonBuilder()
        builder.add('101')
        builder.add('start')
        builder.connect('start', Dir.N, '101')
        builder.set('101', Dir.E, Exit())

        fake_observer = FakeObserver()

        dungeon = builder.build()

        dungeon.register(fake_observer)

        dungeon.go('north')
        dungeon.go('south')
        dungeon.go('north')
        dungeon.go('east')

        self.assertTrue(fake_observer.is_aware_of("player_exited"))

    def test_can_put_things_in_rooms(self):
        fake_observer = FakeObserver()

        builder = DungeonBuilder()
        builder.add('101')
        builder.add('start')
        builder.connect('start', Dir.N, '101')
        builder.put('101', Thing("Sword"))
        builder.set('101', Dir.E, Exit())

        dungeon = builder.build()
        dungeon.register(fake_observer)

        dungeon.go('north')
        dungeon.look('objects')

        last_event = fake_observer.last("player_got_description")
        self.assertIn("Sword", last_event.description())
