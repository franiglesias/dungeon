from dungeon.app.domain.player.backpack import Backpack
from dungeon.app.domain.thing import Thing


class BackpackMother:
    @staticmethod
    def full():
        max_capacity = 5
        backpack = Backpack(capacity=max_capacity)
        for i in range(0, max_capacity):
            backpack.keep(Thing.from_raw("Object {}".format(i + 1)))
        return backpack
