#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_sum_walker
----------------------------------

Tests for `sum_walker` module.
"""

import pickle

import pytest  # noqa: F401

import sum_walker
import sum_walker.iterator_wrapper
from sum_walker import StreamCombiner, StreamGrouper, SumStream


def test_sum_walker():
    """Sample pytest test function with the pytest fixture as an argument.
    """
    seq = list(range(1, 100))
    cnt = 2

    def request_more():
        nonlocal seq
        seq.append(seq[-1] + 1)

    def _next(w):
        sum_, coords = next(w)
        return (sum_, coords)

    def create1():
        return StreamGrouper(StreamCombiner(
            [SumStream(cnt, seq, request_more)]))

    def create2():
        return sum_walker.DWIM_SumWalker(cnt, seq, request_more)

    def test_next(w):
        assert _next(w) == (2, [[0, 0]])
        assert _next(w) == (3, [[0, 1]])
        assert _next(w) == (4, [[0, 2], [1, 1], ])

    def test_for(w):
        i = 0
        for sum_, coords in w:
            pair = (sum_, coords)
            if i == 0:
                assert pair == (2, [[0, 0]])
            elif i == 1:
                assert pair == (3, [[0, 1]])
            elif i == 2:
                assert pair == (4, [[0, 2], [1, 1], ])
            else:
                break
            i += 1
    for tester in [test_next, test_for]:
        for builder in [create1, create2]:
            tester(builder())

    def _calc_state():
        walker = create2()
        for i in range(3):
            next(walker)
        return pickle.dumps(walker)

    state = _calc_state()
    newwalker = pickle.loads(state)
    newwalker.set_request_more(request_more, seq)
    assert next(newwalker) == (5, [[0, 3], [1, 2], ])


def test_iterator_wrapper():
    def natural_nums_iter():
        ret = 1
        while True:
            yield ret
            ret += 1

    def mytest(walker, wanted_sum, wanted_combis):
        sum2, elems2 = next(walker)
        assert sum2 == wanted_sum
        assert len(elems2) == len(wanted_combis)
        for (idx, want), have in zip(enumerate(wanted_combis), elems2):
            assert len(want) == len(have)
            for elem_idx, (w, h) in enumerate(zip(want, have)):
                assert h.coord == w['c']
                assert h.value == w['v']

    walker = sum_walker.iterator_wrapper.Walker(
        counts=[2], iterator=natural_nums_iter())

    mytest(walker, 2, [[{"c": 0, "v": 1}, {"c": 0, "v": 1}]])
    mytest(walker, 3, [[{"c": 0, "v": 1}, {"c": 1, "v": 2}]])

    walker = sum_walker.iterator_wrapper.Walker(
        counts=[2, 3], iterator=natural_nums_iter())

    mytest(walker, 2, [[{"c": 0, "v": 1}, {"c": 0, "v": 1}]])
    mytest(walker, 3, [
        [{"c": 0, "v": 1}, {"c": 0, "v": 1}, {"c": 0, "v": 1}, ],
        [{"c": 0, "v": 1}, {"c": 1, "v": 2}, ],
        ])
    mytest(walker, 4, [
        [{"c": 0, "v": 1}, {"c": 0, "v": 1}, {"c": 1, "v": 2}, ],
        [{"c": 0, "v": 1}, {"c": 2, "v": 3}, ],
        [{"c": 1, "v": 2}, {"c": 1, "v": 2}, ],
        ])
