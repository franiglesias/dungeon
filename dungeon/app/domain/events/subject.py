class Event:
    def name(self):
        return self.__class__.__name__

    def of_type(self, cls):
        return isinstance(self, cls)


class Observer:
    def notify(self, event: Event):
        pass


class CanBeObserved:
    def __init__(self):
        self._observers = []

    def register(self, observer: Observer):
        if observer in self._observers:
            return
        self._observers.append(observer)

    def notify_observers(self, event: Event):
        for observer in self._observers:
            observer.notify(event)

    def _notify_observers(self, event: Event):
        return self.notify_observers(event)
