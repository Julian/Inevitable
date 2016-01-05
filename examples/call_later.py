import random
import transaction

from inevitable.core import Reactor


class Looper(object):
    def __init__(self, iterations):
        self.iterations = iterations

    def run(self):
        for i in xrange(10000):
            answer = i ** 3
        if self.iterations > 0:
            self.iterations -= 1
            reactor.call_later(seconds=0, callback=self.run)


reactor = Reactor(clock=transaction)
reactor.call_later(seconds=0, callback=Looper(iterations=1000).run)
reactor.call_later(seconds=0, callback=Looper(iterations=1000).run)
reactor.run_until_idle()
