from dungeon.app.command.action_result import ActionResult
from dungeon.app.domain.dir import Dir
from dungeon.app.domain.player.player_events import PlayerExited, PlayerMoved
from dungeon.app.events.subject import Subject


class Wall:
    def go(self):
        return ActionResult.player_acted("You hit a wall")

    def look(self):
        return ActionResult.player_acted("There is a wall")


class Exit(Wall):
    def __init__(self):
        self._subject = Subject()

    def go(self):
        self._notify_observers(PlayerExited())
        return ActionResult.player_exited("Congrats. You're out")

    def look(self):
        return ActionResult.player_acted("There is a door")

    def register(self, observer):
        self._subject.register(observer)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)


class Door(Wall):
    def __init__(self, destination):
        self._destination = destination
        self._subject = Subject()

    def go(self):
        self._notify_observers(PlayerMoved(self._destination))
        return ActionResult.player_moved("", self._destination)

    def look(self):
        return ActionResult.player_acted("There is a door")

    def register(self, observer):
        self._subject.register(observer)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)


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
            response += str(dirs.value).capitalize() + ": " + self._walls[dirs].look().get("message") + "\n"

        response += "That's all" + "\n"
        return response

    def register(self, observer):
        for d, wall in self._walls.items():
            if hasattr(wall, "register"):
                wall.register(observer)
