#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under the terms of the MIT license.
#
# This program displays increasing sums of two positive integers

from six import print_
import sum_walker.iterator_wrapper


def main():
    def natural_nums_iter():
        ret = 1
        while True:
            yield ret
            ret += 1

    walker = sum_walker.iterator_wrapper.Walker(
        counts=[2], iterator=natural_nums_iter())

    def print_next():
        nonlocal walker
        sum_, coords = next(walker)
        print_("{} = {}".format(
            sum_, " ; ".join(
                [" + ".join([str(x.value) for x in permutation])
                 for permutation in coords])))

    # Prints «2 = 1 + 1»
    print_next()

    # Prints «3 = 1 + 2»
    print_next()

    # Prints «4 = 1 + 3 ; 2 + 2»
    print_next()

    # Prints «5 = 1 + 4 ; 2 + 3»
    print_next()

    # Prints «6 = 1 + 5 ; 2 + 4 ; 3 + 3»
    print_next()


main()
