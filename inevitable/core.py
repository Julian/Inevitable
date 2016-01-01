from characteristic import Attribute, attributes
from pyrsistent import s as pset


@attributes(
    [
        Attribute(name="clock"),
    ],
)
class Reactor(object):
    def __init__(self):
        self._waiting = pset()

    def call_later(self, callback, seconds):
        clock = self.clock
        waitable = CallAt(clock=clock, time=clock.time() + seconds)
        self._waiting = self._waiting.add((waitable, callback))

    def run_until_idle(self):
        while self._waiting:
            for waitable, callback in self._waiting:
                if waitable.is_ready():
                    self._waiting = self._waiting.remove((waitable, callback))
                    callback()


@attributes(
    [
        Attribute(name="time"),
        Attribute(name="clock", exclude_from_cmp=True),
    ],
)
class CallAt(object):
    def is_ready(self):
        return self.time <= self.clock.time()
