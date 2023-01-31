from dungeon.app.domain.player.energy import EnergyUnit
from dungeon.app.domain.events.subject import Observer


class Command:

    def __init__(self, argument):
        self._argument = argument

    def do(self, receiver):
        if hasattr(receiver, self.name()):
            getattr(receiver, self.name())(self.argument())

    def name(self):
        return ""

    def cost(self):
        return EnergyUnit(1)

    def argument(self):
        if hasattr(self, "_argument"):
            return self._argument

        return ""


class FakeCommand(Command):
    def __init__(self, energy_consumption):
        self._energy_consumption = energy_consumption

    def cost(self):
        return self._energy_consumption

    def name(self):
        return "fake"


class FakeObserver(Observer):
    def __init__(self):
        self._events = dict()

    def notify(self, event):
        self._events[event.name()] = event

    def is_aware_of(self, event_class):
        return event_class.__name__ in self._events.keys()

    def last(self, event_class):
        if self.is_aware_of(event_class):
            return self._events[event_class.__name__]
