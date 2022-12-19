from dungeon.app.domain.dir import Dir
from dungeon.app.domain.player.player_events import PlayerGotThing, PlayerCollectedThing
from dungeon.app.events.subject import Subject


class Dungeon:
    def __init__(self, rooms):
        self._rooms = rooms
        self._current = 'start'
        self._subject = Subject()
        self._rooms.register(self)

    def go(self, direction):
        self._current_room().go(Dir(direction))

    def look(self, focus):
        self._current_room().look(focus)

    def get(self, thing_name):
        thing = self._current_room().get(thing_name)
        if thing is not None:
            self._notify_observers(PlayerGotThing(thing))

    def collect(self, thing_name):
        thing = self._current_room().get(thing_name)
        self._notify_observers(PlayerCollectedThing(thing))

    def _current_room(self):
        return self._rooms.get(self._current)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)

    def register(self, observer):
        self._subject.register(observer)
        self._rooms.register(observer)

    def notify(self, event):
        if event.name() == "player_moved":
            self._current = event.room()
