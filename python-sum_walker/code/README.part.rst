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

::

    # Finding sums of 2 powers of 3:
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

