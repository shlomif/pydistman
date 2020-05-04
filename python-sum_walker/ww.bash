#! /bin/bash
#
# ww.bash
# Copyright (C) 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.
#

rm -fr ~/.cookiecutters/python-project-template/
rm -fr sum_walker/
exec python3 wrapper.py "$@"
