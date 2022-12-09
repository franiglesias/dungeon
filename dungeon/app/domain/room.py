from dungeon.app.command.action_result import ActionResult


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

    def go(self, direction):
        wall = self._walls.get(direction)
        return wall.go()

    def look(self, argument):
        if argument == "objects":
            return self._look_objects()
        return self._look_around()

    def _look_objects(self):
        response = self._things.look()
        return ActionResult.player_acted(response)

    def _look_around(self):
        response = self._things.look()
        response += self._walls.look()
        return ActionResult.player_acted(response)

    def register(self, observer):
        self._walls.register(observer)

    def put(self, an_object):
        self._things.put(an_object)


class Things:
    def __init__(self):
        self._things = dict()

    def put(self, a_thing):
        self._things[a_thing.name()] = a_thing

    def look(self):
        if len(self._things) > 0:
            response = "There are:\n"
            for thing in self._things.values():
                response += "* {}\n".format(thing.name())
        else:
            response = "There are no objects\n"
        return response
