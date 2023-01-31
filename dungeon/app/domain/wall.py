from dungeon.app.domain.dir import Dir
from dungeon.app.domain.player.player_events import PlayerExited, PlayerMoved, PlayerHitWall, PlayerGotDescription, \
    DoorWasLocked, DoorWasUnlocked
from dungeon.app.domain.events.subject import CanBeObserved


class Boundary:
    def go(self):
        raise NotImplementedError

    def look(self):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError


class Wall(Boundary, CanBeObserved):
    def __init__(self):
        super().__init__()

    def go(self):
        self._notify_observers(PlayerHitWall())

    def look(self):
        self._notify_observers(PlayerGotDescription(self.description()))

    def description(self):
        return "There is a wall"


class Door(Boundary, CanBeObserved):
    def __init__(self, destination):
        self._destination = destination
        super().__init__()

    def go(self):
        self._notify_observers(PlayerMoved(self._destination))

    def description(self):
        return "There is a door"


class Exit(Boundary, CanBeObserved):
    def __init__(self):
        super().__init__()

    def go(self):
        self._notify_observers(PlayerExited())

    def description(self):
        return "There is a door"


class Locked(Boundary, CanBeObserved):
    def __init__(self, door, secret):
        self._door = door
        self._secret = secret
        self._is_locked = True
        super().__init__()

    def go(self):
        if self._is_locked:
            self._notify_observers(DoorWasLocked())
        else:
            self._door.go()

    def description(self):
        template = "{} (locked)" if self._is_locked else "{} (unlocked)"
        return template.format(self._door.description())

    def unlock_with(self, key):
        self._is_locked = not key.match(self._secret)
        what_happened = DoorWasLocked() if self._is_locked else DoorWasUnlocked()
        self._notify_observers(what_happened)

    def register(self, observer):
        super().register(observer)
        self._door.register(observer)


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
