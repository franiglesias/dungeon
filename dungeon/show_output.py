class ShowOutput:
    def __init__(self):
        self._contents = ""

    def put(self, message):
        self._contents = self._contents + message + "\n"

    def contents(self):
        return self._contents
