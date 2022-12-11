class FakeObserver:
    def __init__(self):
        self._events = dict()

    def notify(self, event):
        self._events[event.name()] = event

    def is_aware_of(self, event_name):
        return event_name in self._events.keys()

    def last(self, event_name):
        if self.is_aware_of(event_name):
            return self._events[event_name]
