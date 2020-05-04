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

    walker = sum_walker.iterator_wrapper.Walker(
        counts=[2], iterator=natural_nums_iter())
    sum1, elems1 = next(walker)
    assert sum1 == 2
    assert len(elems1) == 1
    assert len(elems1[0]) == 2
    for x in elems1[0]:
        assert x.coord == 0
        assert x.value == 1
