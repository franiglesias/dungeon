from dungeon.app.domain.dir import Dir
from dungeon.app.domain.player.container import Container
from dungeon.app.domain.player.player_events import PlayerCollectedThing, PlayerMoved, \
    ActionNotCompleted
from dungeon.app.domain.thing import Thing
from dungeon.app.events.subject import CanBeObserved, Observer


class Dungeon(CanBeObserved, Observer, Container):
    def __init__(self, rooms):
        super().__init__()
        self._rooms = rooms
        self._current = 'start'
        self._rooms.register(self)

    def go(self, direction):
        try:
            self._current_room().go(Dir(direction))
        except ValueError:
            self._notify_observers(ActionNotCompleted("I don't know how to go {}.".format(direction)))

    def look(self, focus):
        self._current_room().look(focus)

    def get_safe(self, thing_name) -> Thing:
        thing = self._current_room().get(thing_name)
        if thing is None:
            raise IndexError
        return thing

    def exchange(self, to_keep: Thing, thing_name) -> Thing:
        try:
            thing = self.get_safe(thing_name)
            self.drop(to_keep)
            return thing
        except IndexError:
            raise

    def collect(self, thing_name):
        thing = self._current_room().get(thing_name)
        self._notify_observers(PlayerCollectedThing(thing))

    def drop(self, thing):
        self._current_room().put(thing)

    def door(self, direction):
        return self._current_room().door(direction)

    def _current_room(self):
        return self._rooms.get(self._current)

    def register(self, observer):
        super().register(observer)
        self._rooms.register(observer)

    def notify(self, event):
        if event.of_type(PlayerMoved):
            self._current = event.room()
