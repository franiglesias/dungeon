class ActionResult:
    def __init__(self, message):
        self._message = message

    def message(self):
        return self._message

    def is_finished(self):
        return self._message == "Congrats. You're out"
