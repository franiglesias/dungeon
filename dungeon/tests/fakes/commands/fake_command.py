from dungeon.app.command.command import Command


class FakeCommand(Command):
    def __init__(self, energy_consumption):
        self._energy_consumption = energy_consumption

    def cost(self):
        return self._energy_consumption

    def name(self):
        return "fake"
