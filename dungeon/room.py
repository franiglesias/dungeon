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
        response += "North: " + self.north.look() + "\n"
        response += "East: " + self.east.look() + "\n"
        response += "South: " + self.south.look() + "\n"
        response += "West: " + self.west.look() + "\n"

        response += "That's all" + "\n"
        return response
