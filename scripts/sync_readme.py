#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2024 Shlomi Fish < https://www.shlomifish.org/ >
#
# Licensed under the terms of the MIT license.

"""

"""

import os
import subprocess

os.chdir("pydistman")
subprocess.check_call([
    "python3", "python_pypi_dist_manager.py", "test",
])

bn = "README.rst"
with open("dest/{bn}".format(bn=bn,), "rt") as in_fh:
    with open("../{bn}".format(bn=bn,), "wt") as out_fh:
        out_fh.write(in_fh.read())
