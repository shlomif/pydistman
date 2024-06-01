#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2024 Shlomi Fish < https://www.shlomifish.org/ >
#
# Licensed under the terms of the MIT license.

"""

"""

import subprocess

subprocess.check_call([
    "bash", "-e", "-x", "-c",
    ("cd pydistman/ && python3 python_pypi_dist_manager.py test &&" +
     "cat dest/README.rst > ../README.rst"),
])