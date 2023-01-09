from dungeon.app.domain.player.player_events import PlayerGotDescription
from dungeon.app.domain.thing import ThingId
from dungeon.app.domain.things_collection import ThingsCollection
from dungeon.app.events.subject import Subject


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


class Room:
    def __init__(self, walls):
        self._walls = walls
        self._things = Things()
        self._subject = Subject()

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
        self._walls.register(observer)
        self._subject.register(observer)

    def put(self, an_object):
        self._things.append(an_object)

    def get(self, thing_name):
        return self._things.get(thing_name)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)


class Things:
    def __init__(self):
        self._things = dict()
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

    def _item_listing(self, item_format, join_string):
        content = []
        for key, item in self._things.items():
            content.append(item_format.format(item.name().to_s()))
        return join_string.join(content)

    def get(self, thing_name):
        return self._retrieve_thing(thing_name)

    def _retrieve_thing(self, thing_name):
        return self._collection.retrieve(thing_name)
