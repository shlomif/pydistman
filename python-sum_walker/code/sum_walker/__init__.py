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

import heapq


class _MyIterable(object):
    def __iter__(self):
        return self


class StreamCombiner(_MyIterable):
    """Combines several non-decreasing streams of sums into one
    non-decreasing stream of sums.

    st = StreamGrouper(StreamCombiner([
        SumStream(cnt, seq, request_more) for cnt in range(1, 3+1)]))
    """
    def __init__(self, streams):
        self._queue = []
        for stream in streams:
            sum_, coords, _ = next(stream)
            self._queue.append((sum_, coords, stream))
        heapq.heapify(self._queue)

    def add(self, stream):
        sum_, coords, _ = next(stream)
        heapq.heappush(self._queue, (sum_, coords, stream))

    def __next__(self):
        if not len(self._queue):
            raise StopIteration()
        sum_, coords, stream = heapq.heappop(self._queue)
        try:
            newsum, newcoords, _ = next(stream)
            heapq.heappush(self._queue, (newsum, newcoords, stream))
        except StopIteration:
            pass
        return (sum_, coords, stream)


class StreamGrouper(_MyIterable):
    """Groups sums together and returns tuples with the sums and lists of
    coordinates lists.
    :param stream: the base stream of coordinates
    :type stream: SumStream
    """
    def __init__(self, stream):
        self._stream = stream
        self._current = next(self._stream)

    def __next__(self):
        sum_, coords0, _ = self._current
        retcoords = [coords0]
        nextsum_, newcoords, stream = next(self._stream)
        while nextsum_ == sum_:
            retcoords.append(newcoords)
            nextsum_, newcoords, stream = next(self._stream)
        self._current = (nextsum_, newcoords, stream)
        return (sum_, sorted(retcoords))


class _PrivateWrapper(_MyIterable):
    def __init__(self, _delegate):
        self._delegate = _delegate

    def __next__(self):
        sum_, coords, _ = self._delegate._private_next()
        return (sum_, coords, self)


class _InternalSumStream(_MyIterable):
    def __init__(self, seq, coords, coord_idx, request_more):
        self._coords = coords
        self._seq = seq
        self._coord_idx = coord_idx
        self._request_more = request_more
        self._current = (
            sum([self._seq[x] for x in self._coords]), self._coords[:], self)
        self.combiner = StreamCombiner([_PrivateWrapper(self)])

    def _update_current(self):
        _coord_idx = self._coord_idx
        _coords = self._coords
        if _coord_idx:
            if _coords[_coord_idx-1] < _coords[_coord_idx]:
                newcoords = [0]*(_coord_idx-1)+[_coords[_coord_idx-1]+1] +\
                    _coords[_coord_idx:]
                self.combiner.add(
                    _InternalSumStream(
                        self._seq, newcoords,
                        _coord_idx-1, self._request_more))
        if _coord_idx == len(_coords) - 1:
            if _coords[-1] == len(self._seq) - 1:
                self._request_more()

    def _recalc(self):
        self._current = (
            sum([self._seq[x] for x in self._coords]), self._coords[:], self)

    def _private_next(self):
        if self._current == 0:
            idx = self._coord_idx
            if idx == len(self._coords) - 1:
                self._update_current()
                if self._coords[-1] == len(self._seq) - 1:
                    self._request_more()
                self._coords[idx] += 1
                for i in range(self._coord_idx):
                    self._coords[i] = 0
                self._recalc()
            else:
                if self._coords[idx] == self._coords[idx+1]:
                    self._current = None
                self._update_current()
                if self._coords[idx] < self._coords[idx+1]:
                    self._coords[idx] += 1
                    for i in range(self._coord_idx):
                        self._coords[i] = 0
                    self._recalc()
        if self._current:
            ret = self._current
            self._current = 0
            return ret
        else:
            raise StopIteration()

    def __next__(self):
        return next(self.combiner)


def SumStream(cnt, seq, request_more):
    """Creates a stream of non-decreasing sums of cnt elements out of seq.

    :param cnt: the count of elements
    :type cnt: int
    :param seq: a list of increasing integers
    :type seq: list
    :param request_more: a callback to request that more elements should be
    added to seq
    :type request_more: function

    """
    return _InternalSumStream(seq, [0]*cnt, cnt-1, request_more)


def DWIM_SumWalker(cnt, seq, request_more):
    """Creates a stream of non-decreasing sums of cnt elements out of seq.
    While handling the grouping and combining.

    :param cnt: the count of elements
    :type cnt: int
    :param seq: a list of increasing integers
    :type seq: list
    :param request_more: a callback to request that more elements should be
    added to seq
    :type request_more: function

    """
    return StreamGrouper(StreamCombiner(
            [SumStream(cnt, seq, request_more)]))
