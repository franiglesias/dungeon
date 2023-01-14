from dungeon.app.domain.player.backpack import Backpack
from dungeon.app.domain.thing import Thing


class ObjectNotFound(Exception):
    pass


class Hand:
    def __init__(self):
        pass

    def holds(self):
        raise NotImplementedError

    def get(self, thing_name):
        raise NotImplementedError


class FullHand(Hand):
    def __init__(self, holds: Thing, backpack: Backpack) -> None:
        self._holds = holds
        self._backpack = backpack

    def holds(self) -> Thing:
        return self._holds

    def get(self, thing_name):
        try:
            thing = self._backpack.exchange(self._holds, thing_name)
            return FullHand(thing, self._backpack)
        except IndexError:
            raise ObjectNotFound


class EmptyHand(Hand):
    def __init__(self, backpack: Backpack) -> None:
        self._backpack = backpack

    def get(self, thing_name) -> FullHand:
        try:
            thing = self._backpack.get_safe(thing_name)
            return FullHand(thing, self._backpack)
        except IndexError:
            raise ObjectNotFound

    def holds(self):
        pass
