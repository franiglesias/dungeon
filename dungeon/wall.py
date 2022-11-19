from dungeon.command.action_result import ActionResult
from dungeon.dir import Dir


class Wall:
    def go(self):
        return ActionResult.player_acted("You hit a wall")

    def look(self):
        return ActionResult.player_acted("There is a wall")


class Exit(Wall):
    def go(self):
        return ActionResult.player_exited("Congrats. You're out")

    def look(self):
        return ActionResult.player_acted("There is a door")


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
