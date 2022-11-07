class Wall:
    def go(self):
        return "You hit a wall"

    def look(self):
        return "There is a wall"


class Exit(Wall):
    def go(self):
        return "Congrats. You're out"

    def look(self):
        return "There is a door"
