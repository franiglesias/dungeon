from enum import Enum


class Dir(Enum):
    N = "north"
    S = "south"
    E = "east"
    W = "west"

    def opposite(self):
        if self == Dir.N:
            return Dir.S
        elif self == Dir.S:
            return Dir.N
        elif self == Dir.E:
            return Dir.W
        return Dir.E
