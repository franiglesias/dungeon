from dungeon.app.show_output import ShowOutput


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
