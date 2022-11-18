from dungeon.room import Room, Rooms
from dungeon.dir import Dir
from dungeon.wall import Walls, Exit


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
        pass

    def build(self):
        rooms = Rooms()
        walls = Walls()
        walls.set(Dir.N, Exit())
        rooms.set('start', Room(walls))
        return Dungeon(rooms)
