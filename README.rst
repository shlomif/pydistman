==============================================================================
Python Dist Manager.  "Maximum Overkill DRY" PyPI distribution manager (WiP)
==============================================================================
:Info: This is the README file for Python Dist Manager.
:Author: Shlomi Fish <shlomif@cpan.org>
:Copyright: © 2020, Shlomi Fish.
:Date: 2023-12-31
:Version: 0.0.10

.. index: README
.. image:: https://travis-ci.org/shlomif/pydistman.svg?branch=master
   :target: https://travis-ci.org/shlomif/pydistman

PURPOSE
-------

A work-in-progress manager for PyPI-like python distributions which aims to
be a "maximum overkill" don't-repeat yourself manager with a user
experience similar to Dist Zilla ( http://dzil.org/ ).

Currently it is functional, but a far cry from our vision.

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
