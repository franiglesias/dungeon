from dungeon.app.domain.player import EnergyUnit


class Result:
    def message(self):
        pass

    def is_finished(self):
        pass

    def moved_to(self):
        pass

    def cost(self):
        pass


class ActionResult(Result):
    @classmethod
    def player_acted(cls, message):
        return cls(message, None, False)

    @classmethod
    def player_moved(cls, message, destination):
        return cls(message, destination, False)

    @classmethod
    def player_exited(cls, message):
        return cls(message, None, True)

    @classmethod
    def game_started(cls):
        return cls("")

    def __init__(self, message, destination=None, exited=False):
        self._message = message
        self._destination = destination
        self._exited = exited

    def message(self):
        return self._message

    def is_finished(self):
        return self._exited

    def moved_to(self):
        return self._destination


class WithCost(Result):
    def __init__(self, origin, cost):
        self._origin = origin
        self._cost = cost

    def message(self):
        return self._origin.message()

    def is_finished(self):
        return self._origin.is_finished()

    def moved_to(self):
        return self._origin.moved_to()

    def cost(self):
        return self._cost
