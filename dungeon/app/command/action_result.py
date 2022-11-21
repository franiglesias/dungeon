class ActionResult:
    @classmethod
    def player_acted(cls, message):
        return cls(message)

    @classmethod
    def player_moved(cls, message, destination):
        return cls(message, destination)

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
