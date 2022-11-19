from dungeon.command.action_result import ActionResult
from dungeon.dir import Dir


class Room:
    def __init__(self, walls):
        self._walls = walls

    def go(self, direction):
        wall = self._walls.get(direction)
        return wall.go()

    def look(self, argument):
        response = ""
        response += "North: " + self._walls.get(Dir.N).look().message() + "\n"
        response += "East: " + self._walls.get(Dir.E).look().message() + "\n"
        response += "South: " + self._walls.get(Dir.S).look().message() + "\n"
        response += "West: " + self._walls.get(Dir.W).look().message() + "\n"

        response += "That's all" + "\n"
        return ActionResult.player_acted(response)


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
