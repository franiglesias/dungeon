from dungeon.app.domain.dir import Dir


class Dungeon:
    def __init__(self, rooms):
        self._rooms = rooms
        self._current = 'start'

    def go(self, direction):
        result = self._current_room().go(Dir(direction))
        if result.moved_to() is not None:
            self._current = result.moved_to()
        return result

    def look(self, focus):
        return self._current_room().look(focus)

    def _current_room(self):
        return self._rooms.get(self._current)
