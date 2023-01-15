from dungeon.app.domain.thing import Thing


class ObjectNotFound(Exception):
    pass


class Hand:
    def __init__(self):
        pass

    def holds(self):
        raise NotImplementedError

    def get_from(self, container, thing_name):
        raise NotImplementedError


class FullHand(Hand):
    def __init__(self, holds: Thing) -> None:
        self._holds = holds

    def holds(self) -> Thing:
        return self._holds

    def get_from(self, container, thing_name):
        try:
            thing = container.exchange(self._holds, thing_name)
            return FullHand(thing)
        except IndexError:
            raise ObjectNotFound


class EmptyHand(Hand):
    def __init__(self) -> None:
        pass

    def get_from(self, container, thing_name) -> FullHand:
        try:
            thing = container.get_safe(thing_name)
            return FullHand(thing)
        except IndexError:
            raise ObjectNotFound

    def holds(self):
        pass
