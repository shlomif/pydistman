PURPOSE
-------

The sum_walker PyPI distribution allows one to iterate over increasing
sums of a certain number (e.g: 2 or 3) of elements out of a stream of
increasing integers.

INSTALLATION
------------

pip3 install sum_walker

USAGE
-----

A simple example of printing sums of two integers:

::

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

A more interesting example, this time using the more beaurocratic
sum_walker module:

::

    # Finding sums of two powers of 3 (= i**3 ) in two or more
    # different ways:
    #
    # https://en.wikipedia.org/wiki/Taxicab_number
    from sum_walker import DWIM_SumWalker

    seq = [0, 1]
    reached = 2

    def request_more():
        nonlocal reached
        nonlocal seq
        seq.append(reached ** 3)
        reached += 1

    it = DWIM_SumWalker(2, seq, request_more)
    for sum_, coords in it:
        len_ = len(coords)
        if len_ > 1:
            print("{}\t{}\t{}".format(
                len_, sum_, " ; ".join(
                    [" + ".join(["{} ** 3".format(x) for x in c])
                     for c in coords])))

NOTES
-----

