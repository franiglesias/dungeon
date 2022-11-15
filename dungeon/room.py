from dungeon.command.action_result import ActionResult
from dungeon.wall import Exit, Wall


class Room:
    def __init__(self):
        self.north = Exit()
        self.south = Wall()
        self.east = Wall()
        self.west = Wall()

    def go(self, direction):
        wall = getattr(self, direction)
        return wall.go()

    def look(self, argument):
        response = ""
        response += "North: " + self.north.look().message() + "\n"
        response += "East: " + self.east.look().message() + "\n"
        response += "South: " + self.south.look().message() + "\n"
        response += "West: " + self.west.look().message() + "\n"

        response += "That's all" + "\n"
        return ActionResult(response)
