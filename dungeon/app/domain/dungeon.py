from dungeon.app.domain.dir import Dir
from dungeon.app.events.subject import Subject


class Dungeon:
    def __init__(self, rooms):
        self._rooms = rooms
        self._current = 'start'
        self._subject = Subject()

    def go(self, direction):
        result = self._current_room().go(Dir(direction))
        if result.get("destination") is not None:
            self._current = result.get("destination")
            self._notify_observers(PlayerMoved(self._current))
        return result

    def look(self, focus):
        return self._current_room().look(focus)

    def _current_room(self):
        return self._rooms.get(self._current)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)

    def register(self, observer):
        self._subject.register(observer)
        self._rooms.register(observer)


class PlayerMoved:
    def __init__(self, room):
        self._room = room

    def room(self):
        return self._room

    def name(self):
        return "player_moved"
