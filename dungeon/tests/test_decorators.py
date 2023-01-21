from unittest import TestCase

from dungeon.app.events.subject import Event
from dungeon.tests.decorators import expect_event
from dungeon.app.command.command import FakeObserver


class FakeEvent(Event):
    pass


class Test(TestCase):
    def setUp(self) -> None:
        self.observer = FakeObserver()

    @expect_event(FakeEvent)
    def test_something(self):
        self.observer.notify(FakeEvent())
