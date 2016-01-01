"""
Clock implementations for testing.

This module *is* public API.

---11------11------11----9------9------9----9------9-----9----8-----8-----8----
-----11------11------11---11-----11-----11---11-----11----11---9-----9-----9---
-------12-------12----------10-----10----------10-----10--------10----10-------
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------


"""

from characteristic import Attribute, attributes


class EndOfTime(Exception):
    pass


@attributes(
    [
        Attribute(name="_time", default_value=0),
        Attribute(
            name="_iterations",
            default_value=1,
            exclude_from_cmp=True,
            exclude_from_repr=True,
        ),
        Attribute(
            name="_step",
            default_value=1,
            exclude_from_cmp=True,
            exclude_from_repr=True,
        ),
    ],
)
class Finite(object):
    """
    A finite clock.

    """

    def time(self):
        time, self._time = self._time, self._time + self._step
        self._iterations -= 1
        if self._iterations < 0:
            raise EndOfTime(self)
        return time
