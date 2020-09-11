#! /bin/bash
#
# ww.bash
# Copyright (C) 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under the MIT/Expat license.
#

# rm -fr ~/.cookiecutters/python-project-template/
# rm -fr sum_walker/
exec python3 python_pypi_dist_manager.py "$@"
