#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.

import sys
sys.path.insert(0, "./code")

from pydistman import DistManager  # noqa: E402

dist_name = "pydistman"

obj = DistManager(
    dist_name=dist_name,
    dist_version="0.0.11",
    project_name="Python Dist Manager",
    project_short_description=(
        "\"Maximum Overkill DRY\" PyPI distribution manager (WiP)"
    ),
    release_date="2024-07-22",
    project_year="2020",
    aur_email="shlomif@cpan.org",
    project_email="shlomif@cpan.org",
    full_name="Shlomi Fish",
    github_username="shlomif",
)
obj.cli_run()
