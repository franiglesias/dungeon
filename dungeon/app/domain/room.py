from dungeon.app.domain.player.player_events import PlayerGotDescription
from dungeon.app.domain.thing import ThingId
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
        response = self._things.look()
        self._notify_observers(PlayerGotDescription(response))

    def _look_around(self):
        response = self._things.look()
        response += self._walls.look()
        self._notify_observers(PlayerGotDescription(response))

    def register(self, observer):
        self._walls.register(observer)
        self._subject.register(observer)

    def put(self, an_object):
        self._things.put(an_object)

    def get(self, thing_name):
        return self._things.get(thing_name)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)


class Things:
    def __init__(self):
        self._things = dict()

    def put(self, a_thing):
        self._things[a_thing.id()] = a_thing

    def look(self):
        if len(self._things) > 0:
            response = "There are:\n"
            for thing in self._things.values():
                response += "* {}\n".format(thing.name().to_s())
        else:
            response = "There are no objects\n"
        return response

    def get(self, thing_name):
        thing_id = ThingId.normalized(thing_name)
        if thing_id in self._things.keys():
            return self._things.pop(thing_id)
        return None
