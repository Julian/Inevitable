from unittest import TestCase

from inevitable.core import Reactor
from inevitable.tests import clocks


def run(reactor):
    try:
        reactor.run()
    except clocks.EndOfTime:
        pass


class TestReactor(TestCase):
    def test_it_can_call_things_later_when_time_elapses(self):
        """
        When time passes beyond a scheduled call_later, the callback is called.

        """

        reactor = Reactor(clock=clocks.Finite(iterations=3))

        reactor.call_later(
            callback=lambda : setattr(self, "called", True),
            seconds=2,
        )
        run(reactor)

        self.assertEqual(getattr(self, "called", None), True)

    def test_it_can_call_things_later_when_time_elapses_inexactly(self):
        reactor = Reactor(clock=clocks.Finite(iterations=2, step=0.63))

        reactor.call_later(
            callback=lambda : setattr(self, "called", True),
            seconds=0.25,
        )
        run(reactor)

        self.assertEqual(getattr(self, "called", None), True)

    def test_it_does_not_call_things_later_until_time_elapses(self):
        reactor = Reactor(clock=clocks.Finite(iterations=1))
        reactor.call_later(callback=self.fail, seconds=2)
        run(reactor)

    def test_it_calls_things_later_only_once(self):
        reactor = Reactor(clock=clocks.Finite(iterations=10))

        reactor.call_later(
            seconds=2,
            callback=lambda : setattr(
                self, "called", getattr(self, "called", 0) + 1
            ),
        )
        run(reactor)

        self.assertEqual(getattr(self, "called", None), 1)
