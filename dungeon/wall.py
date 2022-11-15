from dungeon.command.action_result import ActionResult


class Wall:
    def go(self):
        return ActionResult("You hit a wall")

    def look(self):
        return ActionResult("There is a wall")


class Exit(Wall):
    def go(self):
        return ActionResult("Congrats. You're out")

    def look(self):
        return ActionResult("There is a door")
