class Command:

    def __init__(self, argument):
        self._argument = argument

    def do(self, receiver):
        pass

    def __str__(self) -> str:
        return "You said: {} {}".format(self._name(), self._argument)

    def _name(self):
        pass

    def _to_str(self):
        return "{} {}".format(self._name(), self._argument)
