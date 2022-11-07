from dungeon.room import Room


class Dungeon:
    def __init__(self):
        self.start = Room()

    def go(self, direction):
        return self.start.go(direction)

    def look(self, focus):
        return self.start.look(focus)
