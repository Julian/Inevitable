from sys import argv
import random
import transaction

from inevitable.core import Reactor


class Looper(object):
    def __init__(self, iterations, reactor):
        self.iterations = iterations
        self.reactor = reactor

    def run(self):
        for i in xrange(10000):
            answer = i ** 3
        if self.iterations > 0:
            self.iterations -= 1
            self.reactor.call_later(seconds=0, callback=self.run)


def main(argv=argv[1:]):
    iterations, threads = map(int, argv)
    reactor = Reactor()
    for _ in xrange(threads):
        looper = Looper(iterations=iterations, reactor=reactor)
        reactor.call_later(seconds=0, callback=looper.run)
    reactor.run_until_idle()


main()
