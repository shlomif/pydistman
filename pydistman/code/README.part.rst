PURPOSE
-------

A work-in-progress manager for PyPI-like python distributions which aims to
be a "maximum overkill" don't-repeat yourself manager with a user
experience similar to Dist-Zilla ( http://dzil.org/ ).

Currently it is functional, but a far cry from our vision.

What pydistman does differently from many PyPI-distribution-generating "cookiecutters"
is generate a fresh-full-fledged (and possibly one with recent improvements) distribution
on every build-command, including ones to test local changes. Currently,
pydistman piggy-backs a lot-of-the heavy-lifting to Chris Warrick’s Python
Project Template ( https://chriswarrick.com/projects/python-project-template/ ) and
we thank him for his work.

INSTALLATION
------------

pip3 install pydistman

USAGE
-----

For some examples see:

* https://github.com/shlomif/black-hole-solitaire/tree/master/black-hole-solitaire/python-bindings/cffi

* https://github.com/shlomif/modint/tree/master/modint

* https://github.com/shlomif/pydistman

* https://github.com/shlomif/pysol_cards

* https://github.com/shlomif/rebookmaker/tree/master/epub_maker

* https://github.com/shlomif/sum_walker

* https://github.com/shlomif/python-vnu_validator

* https://github.com/shlomif/zenfilter


``python3 python_pypi_dist_manager.py test``

``python3 python_pypi_dist_manager.py release``

NOTES
-----

* https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

