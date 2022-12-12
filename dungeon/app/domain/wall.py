from dungeon.app.domain.dir import Dir
from dungeon.app.domain.player.player_events import PlayerExited, PlayerMoved, PlayerHitWall, PlayerGotDescription
from dungeon.app.events.subject import Subject


class Wall:
    def __init__(self):
        self._subject = Subject()

    def go(self):
        self._notify_observers(PlayerHitWall())

    def look(self):
        self._notify_observers(PlayerGotDescription(self.description()))

    def description(self):
        return "There is a wall"

    def register(self, observer):
        self._subject.register(observer)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)


class Exit(Wall):
    def __init__(self):
        super().__init__()

    def go(self):
        self._notify_observers(PlayerExited())

    def description(self):
        return "There is a door"


class Door(Wall):
    def __init__(self, destination):
        super().__init__()
        self._destination = destination

    def go(self):
        self._notify_observers(PlayerMoved(self._destination))

    def description(self):
        return "There is a door"


class Walls:
    def __init__(self):
        self._walls = {
            Dir.N: Wall(),
            Dir.E: Wall(),
            Dir.S: Wall(),
            Dir.W: Wall()
        }

    def get(self, direction):
        return self._walls[direction]

    def set(self, direction, wall):
        cloned = self
        cloned._walls[direction] = wall
        return cloned

    def look(self):
        response = ""
        for dirs in Dir:
            response += "{0}: {1}\n".format(str(dirs.value).capitalize(), self._walls[dirs].description())

        response += "That's all" + "\n"
        return response

    def register(self, observer):
        for d, wall in self._walls.items():
            if hasattr(wall, "register"):
                wall.register(observer)
