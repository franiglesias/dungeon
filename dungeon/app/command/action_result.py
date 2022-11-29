class Result:
    def message(self):
        pass

    def is_finished(self):
        pass

    def moved_to(self):
        pass

    def cost(self):
        pass


class ResultBag():
    def __init__(self):
        self._results = dict()

    def set(self, key, data):
        self._results[key] = data

    def get(self, key):
        return self._results[key]


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
        self._bag = ResultBag()
        self._bag.set("message", message)
        self._bag.set("destination", destination)
        self._bag.set("exited", exited)

    def message(self):
        return self._bag.get("message")

    def is_finished(self):
        return self._bag.get("exited")

    def moved_to(self):
        return self._bag.get("destination")

    def get(self, key):
        return self._bag.get(key)

    def set(self, key, data):
        self._bag.set(key, data)


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
