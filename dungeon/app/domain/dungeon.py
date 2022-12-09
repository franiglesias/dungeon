from dungeon.app.domain.dir import Dir
from dungeon.app.events.subject import Subject


class Dungeon:
    def __init__(self, rooms):
        self._rooms = rooms
        self._current = 'start'
        self._subject = Subject()
        self._rooms.register(self)

    def go(self, direction):
        result = self._current_room().go(Dir(direction))
        return result

    def look(self, focus):
        return self._current_room().look(focus)

    def _current_room(self):
        return self._rooms.get(self._current)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)

    def register(self, observer):
        self._subject.register(self)
        self._rooms.register(observer)

    def notify(self, event):
        if event.name() == "player_moved":
            self._current = event.room()
