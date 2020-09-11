#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_use
----------------------------------

Tests for pydistman
"""

import re

import pytest  # noqa: F401

import pydistman


def test_pydistman():
    assert pydistman.DistManager
    with open("README.rst", "rt") as readme_fh:
        txt = readme_fh.read()
        # Should be changed if the copyright holder
        # changes.
        assert re.search(
            '\\n:Author: Shlomi Fish <shlomif\\@cpan\\.org>\\n',
            txt,
            re.M | re.S
        )
