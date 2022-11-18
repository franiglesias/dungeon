from dungeon.dir import Dir
from dungeon.room import Room, Rooms
from dungeon.wall import Walls


class Dungeon:
    def __init__(self, rooms):
        self._rooms = rooms
        self._current = 'start'

    def go(self, direction):
        return self._current_room().go(Dir(direction))

    def look(self, focus):
        return self._current_room().look(focus)

    def _current_room(self):
        return self._rooms.get(self._current)


class DungeonBuilder:
    def __init__(self):
        self._names = []
        self._walls = dict()

    def build(self):
        rooms = Rooms()
        for name in self._names:
            walls = Walls()
            for direction, wall in self._walls[name].items():
                walls.set(direction, wall)
            rooms = rooms.set(name, Room(walls))

        return Dungeon(rooms)

    def add(self, room_name):
        self._names.append(room_name)
        self._walls[room_name] = dict()

    def set(self, room_name, direction, wall):
        self._walls[room_name][direction] = wall
