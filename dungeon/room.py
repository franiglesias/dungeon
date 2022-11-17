
from dungeon.command.action_result import ActionResult
from dungeon.wall import Exit, Wall
from enum import Enum


class Room:
    def __init__(self):
        self._walls = {
            Dir.N: Exit(),
            Dir.E: Wall(),
            Dir.S: Wall(),
            Dir.W: Wall()
        }

    def go(self, direction):
        wall = self._walls[direction]
        return wall.go()

    def look(self, argument):
        response = ""
        response += "North: " + self._walls[Dir.N].look().message() + "\n"
        response += "East: " + self._walls[Dir.E].look().message() + "\n"
        response += "South: " + self._walls[Dir.S].look().message() + "\n"
        response += "West: " + self._walls[Dir.W].look().message() + "\n"

        response += "That's all" + "\n"
        return ActionResult(response)


class Dir(Enum):
    N = "north"
    S = "south"
    E = "east"
    W = "west"
