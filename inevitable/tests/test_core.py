from unittest import TestCase

from inevitable.core import Reactor
from inevitable.tests import clocks


class TestReactor(TestCase):

    called = 0

    def callback(self):
        self.called += 1

    def test_it_can_call_things_later_when_time_elapses(self):
        """
        When time passes beyond a scheduled call_later, the callback is called.

        """

        reactor = Reactor(clock=clocks.Finite(iterations=3))
        reactor.call_later(callback=self.callback, seconds=2)
        reactor.run_until_idle()
        self.assertTrue(self.called)

    def test_it_can_call_things_later_when_time_elapses_inexactly(self):
        reactor = Reactor(clock=clocks.Finite(iterations=2, step=0.63))
        reactor.call_later(callback=self.callback, seconds=0.25)
        reactor.run_until_idle()
        self.assertTrue(self.called)

    def test_it_does_not_call_things_later_until_time_elapses(self):
        reactor = Reactor(clock=clocks.Finite(iterations=1))
        reactor.call_later(callback=self.fail, seconds=2)
        with self.assertRaises(clocks.EndOfTime):
            reactor.run_until_idle()
        self.assertFalse(self.called)

    def test_it_calls_things_later_only_once(self):
        reactor = Reactor(clock=clocks.Finite(iterations=10))
        reactor.call_later(callback=self.callback, seconds=2)
        reactor.run_until_idle()
        self.assertEqual(self.called, 1)

    def test_ready_waitable_things_are_run(self):
        class Thing(object):
            def is_ready(self):
                return True

        reactor = Reactor()
        reactor.wait_on(Thing(), callback=self.callback)
        reactor.run_until_idle()

        self.assertTrue(self.called)
