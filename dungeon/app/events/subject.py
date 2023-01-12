class CanBeObserved:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        if observer in self._observers:
            return
        self._observers.append(observer)

    def notify_observers(self, event):
        for observer in self._observers:
            observer.notify(event)

    def _notify_observers(self, event):
        return self.notify_observers(event)


class Observer:
    def notify(self, event):
        pass
