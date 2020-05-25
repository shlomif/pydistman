==============================================================================
Sum walker.  Iterate over sums of a certain number of elements
==============================================================================
:Info: This is the README file for Sum walker.
:Author: Shlomi Fish <shlomif@cpan.org>
:Copyright: © 2020, Shlomi Fish.
:Date: 2020-02-25
:Version: 0.6.1

.. index: README
.. image:: https://travis-ci.org/shlomif/sum_walker.svg?branch=master
   :target: https://travis-ci.org/shlomif/sum_walker

PURPOSE
-------

The sum_walker PyPI distribution allows one to iterate over increasing
sums of a certain count (e.g: 2 or 3) of elements out of a stream of
increasing integers.

This repository also serves as a test bed for an experimental distribution
generator for python, inspired by Perl 5's `Dist::Zilla <http://dzil.org/>`_
, which is “Maximum Overkill” and "don't repeat yourself". Currently,
there is still a lot of way for this vision to materialise, but you can
see the work-in-progress at `wrapper.py <./python-sum_walker/wrapper.py>`_ .

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

COPYRIGHT
---------
Copyright © 2020, Shlomi Fish.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions, and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions, and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

3. Neither the name of the author of this software nor the names of
   contributors to this software may be used to endorse or promote
   products derived from this software without specific prior written
   consent.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
