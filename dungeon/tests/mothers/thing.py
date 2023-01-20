import random
import string

from dungeon.app.domain.thing import Thing


class ThingMother:
    @staticmethod
    def random():
        return Thing.from_raw(''.join(random.choice(string.ascii_letters)))
