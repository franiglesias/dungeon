from dungeon.app.domain.dir import Dir
from dungeon.app.domain.player.player_events import PlayerGotThing, PlayerCollectedThing, PlayerMoved, \
    ActionNotCompleted
from dungeon.app.events.subject import CanBeObserved


class Dungeon:
    def __init__(self, rooms):
        self._rooms = rooms
        self._current = 'start'
        self._subject = CanBeObserved()
        self._rooms.register(self)

    def go(self, direction):
        try:
            self._current_room().go(Dir(direction))
        except ValueError:
            self._notify_observers(ActionNotCompleted("I don't know how to go {}.".format(direction)))

    def look(self, focus):
        self._current_room().look(focus)

    def get(self, thing_name):
        thing = self._current_room().get(thing_name)
        if thing is not None:
            self._notify_observers(PlayerGotThing(thing))

    def collect(self, thing_name):
        thing = self._current_room().get(thing_name)
        self._notify_observers(PlayerCollectedThing(thing))

    def drop(self, thing):
        self._current_room().put(thing)

    def door(self, direction):
        return self._current_room().door(direction)

    def _current_room(self):
        return self._rooms.get(self._current)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)

    def register(self, observer):
        self._subject.register(observer)
        self._rooms.register(observer)

    def notify(self, event):
        if event.of_type(PlayerMoved):
            self._current = event.room()
