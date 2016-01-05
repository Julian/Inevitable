import random
import transaction

from inevitable.core import Reactor


def callback():
    for i in xrange(10000):
        answer = i ** 3
    if random.random() > 0.00001:
        reactor.call_later(seconds=0, callback=callback)


reactor = Reactor(clock=transaction)
reactor.call_later(seconds=0, callback=callback)
reactor.call_later(seconds=0, callback=callback)
reactor.run_until_idle()
