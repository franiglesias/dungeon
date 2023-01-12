from dungeon.app.events.subject import Observer


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
