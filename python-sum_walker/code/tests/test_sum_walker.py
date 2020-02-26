#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_sum_walker
----------------------------------

Tests for `sum_walker` module.
"""

import pytest

import sum_walker
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

    for builder in [create1, create2]:
        w = builder()

        assert _next(w) == (2, [[0, 0]])
        assert _next(w) == (3, [[0, 1]])
        assert _next(w) == (4, [[0, 2], [1, 1], ])
