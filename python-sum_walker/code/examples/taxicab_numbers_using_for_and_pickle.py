#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under the terms of the MIT license.
#
# This program finds numbers that are expressible as the sum of two integer
# cubes in two or more ways.
#
# See:
# https://en.wikipedia.org/wiki/Taxicab_number

import os.path
import pickle

from six import print_

from sum_walker import DWIM_SumWalker


class Seq:
    def __init__(self):
        self.seq = [0, 1]
        self.reached = 2

    def request_more(self):
        self.seq.append(self.reached ** 3)
        self.reached += 1


def main():
    fn = 'taxicab.pykl'
    if os.path.exists(fn):
        with open(fn, 'rb') as f:
            [it, seq] = pickle.load(f)

            def request_more():
                return seq.request_more()
            it.set_request_more(request_more, seq.seq)
    else:
        seq = Seq()

        def request_more():
            return seq.request_more()
        it = DWIM_SumWalker(2, seq.seq, request_more)
    count = init_count = 1000
    for sum_, coords in it:
        len_ = len(coords)
        if len_ > 1:
            print_("{}\t{}\t{}".format(
                len_, sum_, " ; ".join(
                    [" + ".join(["{} ** 3".format(x) for x in c])
                     for c in coords])))
        count -= 1
        if count == 0:
            count = init_count
            with open(fn, 'wb') as f:
                pickle.dump([it, seq], f)


main()
