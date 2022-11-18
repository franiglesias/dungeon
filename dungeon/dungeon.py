from dungeon.room import Room, Dir, Rooms


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
        rooms.set('start', Room())
        return Dungeon(rooms)
