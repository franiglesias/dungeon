class ShowOutput:
    def put(self, message):
        pass


class FakeShowOutput(ShowOutput):
    def __init__(self):
        self._contents = ""

    def put(self, scene):
        self._contents = self._contents + scene.title() + "\n"
        self._contents = self._contents + scene.command() + "\n"
        self._contents = self._contents + scene.description() + "\n"
        self._contents = self._contents + scene.energy() + ""

    def contents(self):
        return self._contents


class MirrorUserCommand(ShowOutput):
    def put(self, scene):
        print("{} [{}]: {}".format(scene.command(), scene.title(), scene.description()))
