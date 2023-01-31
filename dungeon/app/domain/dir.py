from enum import Enum


class Dir(Enum):
    N = "north"
    E = "east"
    S = "south"
    W = "west"

    def opposite(self):
        return self._opposite_dir()

    def _opposite_dir(self):
        opposites = {
            Dir.N: Dir.S,
            Dir.S: Dir.N,
            Dir.E: Dir.W,
            Dir.W: Dir.E
        }

        return opposites[self]
