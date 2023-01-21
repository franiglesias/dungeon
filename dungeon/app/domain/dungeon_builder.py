from dungeon.app.domain.dir import Dir
from dungeon.app.domain.dungeon import Dungeon
from dungeon.app.domain.room import Rooms, Room
from dungeon.app.domain.thing import ThingKey, Key, Food
from dungeon.app.domain.wall import Door, Walls, Locked, Exit


class DungeonBuilder:
    def __init__(self):
        self._names = []
        self._walls = dict()
        self._things = dict()

    def build(self):
        rooms = Rooms()
        for name in self._names:
            walls = Walls()
            for direction, wall in self._walls[name].items():
                walls = walls.set(direction, wall)

            room = Room(walls)
            for thing in self._things[name]:
                room.put(thing)
            rooms = rooms.set(name, room)

        return Dungeon(rooms)

    def add(self, room_name):
        self._names.append(room_name)
        self._walls[room_name] = dict()
        self._things[room_name] = []

    def set(self, room_name, direction, wall):
        self._walls[room_name][direction] = wall

    def connect(self, origin, direction, target):
        self.set(origin, direction, Door(target))
        self.set(target, direction.opposite(), Door(origin))

    def put(self, room_name, thing):
        self._things[room_name].append(thing)


class DungeonMother:
    @staticmethod
    def with_objects(*things) -> Dungeon:
        builder = DungeonBuilder()
        builder.add('start')
        for thing in things:
            builder.put('start', thing)
        return builder.build()

    @staticmethod
    def with_locked_exit(direction=Dir.N) -> Dungeon:
        builder = DungeonBuilder()
        builder.add('start')
        builder.set('start', direction, Locked(Exit(), ThingKey("super-secret")))
        builder.put('start', Key.from_raw("key", "super-secret"))
        builder.put('start', Food.from_raw("food"))
        return builder.build()
