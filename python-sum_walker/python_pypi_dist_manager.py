#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.

import sys

from pydistman import DistManager

try:
    cmd = sys.argv.pop(1)
except IndexError:
    cmd = 'build'

dist_name = "sum_walker"

obj = DistManager(
    dist_name=dist_name,
    dist_version="0.8.2",
    project_name="Sum Walker",
    project_short_description=(
        "Iterate over sums of a certain" +
        " number of elements"
    ),
    release_date="2020-02-25",
    project_year="2020",
    aur_email="shlomif@cpan.org",
    project_email="shlomif@cpan.org",
    full_name="Shlomi Fish",
    github_username="shlomif",
)
obj.run_command(cmd=cmd, args=[])
