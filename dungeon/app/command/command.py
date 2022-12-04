class Command:

    def __init__(self, argument):
        self._argument = argument

    def do(self, receiver):
        pass

    def __str__(self) -> str:
        return "You said: {} {}".format(self._name(), self._argument)

    def _name(self):
        pass

    def name(self):
        return self._name()

    def argument(self):
        if hasattr(self, "_argument"):
            return self._argument

        return ""

    def _to_str(self):
        return "{} {}".format(self._name(), self._argument)
