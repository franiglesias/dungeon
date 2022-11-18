from dungeon.room import Room, Dir


class Dungeon:
    def __init__(self):
        self.start = Room()

    def go(self, direction):
        return self.start.go(Dir(direction))

    def look(self, focus):
        return self.start.look(focus)


class DungeonBuilder:
    def __init__(self):
        pass

    def build(self):
        return Dungeon()
