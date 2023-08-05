import bisect
import typing
import unittest

class ValueCache:

    # T = typing.TypeVar('T', bound=Comparable)

    def __init__(self, key=None):
        self._values: typing.List = []
        self._key = key

    def get_idx(self, value) -> int:
        if len(self._values) == 0:
            self._values.append(value)
            return 0
        else:
            idx = bisect.bisect_left(self._values, value, key=self._key)
            if idx != len(self._values) and self._values[idx] != value:
                self._values.insert(idx, value)
            return idx


class TestValueCache(unittest.TestCase):

    def test_bla(self):
        cache = ValueCache()
        a = cache.get_idx('a')
        b = cache.get_idx('b')
        c = cache.get_idx('c')
        d = cache.get_idx('a')
        e = cache.get_idx('b')
        e = cache.get_idx('c')
