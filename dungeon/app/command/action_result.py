class ResultBag():
    def __init__(self):
        self._results = dict()

    def set(self, key, data):
        self._results[key] = data

    def get(self, key):
        return self._results[key]


class ActionResult:
    @classmethod
    def player_acted(cls, message):
        return cls(message, None, False)

    def __init__(self, message, destination=None, exited=False):
        self._bag = ResultBag()
        self._bag.set("message", message)

    def get(self, key):
        return self._bag.get(key)

    def set(self, key, data):
        self._bag.set(key, data)
