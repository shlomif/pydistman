# The Expat License
#
# Copyright (c) 2020, Shlomi Fish
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from collections import namedtuple

from sum_walker import StreamCombiner, StreamGrouper, SumStream

CoordValue = namedtuple('CoordValue', 'coord value')


class Walker(object):

    def __iter__(self):
        return self
    """Creates a stream of non-decreasing sums of counts elements out of the iterator.

    :param counts: the counts of elements
    :type counts: list
    :param iterator: an iterator that returns increasing and positive integers
    :type iterator: an iterable

    This is a wrapper around sum_walker.

    Iterating it returns a sum followed by a list of lists of items
    containing .coord and .value .
    """
    def __init__(self, counts, iterator):
        self._values = []

        def request_more():
            nonlocal self
            self._values.append(next(iterator))

        request_more()
        self._stream = StreamGrouper(StreamCombiner(
                [SumStream(c, self._values, request_more) for c in counts]))

    def __next__(self):
        sum_, coords = next(self._stream)
        return sum_, [
            [CoordValue(c, self._values[c]) for c in x]
            for x in coords]
