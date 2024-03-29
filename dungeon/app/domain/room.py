from dungeon.app.domain.player.player_events import PlayerGotDescription
from dungeon.app.domain.things_collection import ThingsCollection
from dungeon.app.domain.events.subject import CanBeObserved


class Rooms:
    def __init__(self):
        self._rooms = dict()

    def get(self, key):
        return self._rooms[key]

    def count(self):
        return len(self._rooms)

    def set(self, key, room):
        cloned = self
        cloned._rooms[key] = room
        return cloned

    def register(self, observer):
        for name, room in self._rooms.items():
            room.register(observer)


class Room(CanBeObserved):
    def __init__(self, walls):
        super().__init__()
        self._walls = walls
        self._things = Things()

    def go(self, direction):
        wall = self._walls.get(direction)
        wall.go()

    def door(self, direction):
        return self._walls.get(direction)

    def look(self, argument):
        if argument == "objects":
            return self._look_objects()
        return self._look_around()

    def _look_objects(self):
        response = self._things.inventory()
        self._notify_observers(PlayerGotDescription(response))

    def _look_around(self):
        response = self._things.inventory()
        response += self._walls.look()
        self._notify_observers(PlayerGotDescription(response))

    def register(self, observer):
        super().register(observer)
        self._walls.register(observer)

    def put(self, an_object):
        self._things.append(an_object)

    def get(self, thing_name):
        return self._things.get(thing_name)


class Things:
    def __init__(self):
        self._collection = ThingsCollection()

    def append(self, a_thing):
        self._store_thing(a_thing)

    def _store_thing(self, a_thing):
        self._collection.store(a_thing)

    def inventory(self):
        return self._things_inventory(
            prefix="There are:\n",
            item_format="* {}",
            item_join="\n",
            empty="There are no objects\n"
        )

    def _things_inventory(self, prefix, item_format, item_join, empty):
        return self._collection.inventory(prefix, item_format, item_join, empty)

    def get(self, thing_name):
        return self._retrieve_thing(thing_name)

    def _retrieve_thing(self, thing_name):
        return self._collection.retrieve(thing_name)
