from dungeon.app.command.action_result import ActionResult
from dungeon.app.domain.dir import Dir


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

    def go(self, direction):
        wall = self._walls.get(direction)
        return wall.go()

    def look(self, argument):
        response = ""
        response += "North: " + self._walls.get(Dir.N).look().get("message") + "\n"
        response += "East: " + self._walls.get(Dir.E).look().get("message") + "\n"
        response += "South: " + self._walls.get(Dir.S).look().get("message") + "\n"
        response += "West: " + self._walls.get(Dir.W).look().get("message") + "\n"

        response += "That's all" + "\n"
        return ActionResult.player_acted(response)

    def register(self, observer):
        self._walls.register(observer)
