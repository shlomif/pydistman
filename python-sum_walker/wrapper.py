#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.

import cookiecutter.main


def main():
    cookiecutter.main.cookiecutter(
        'gh:Kwpolska/python-project-template',
        no_input=True,
        overwrite_if_exists=True,
        extra_context={
            "entry_point": ["none", "cli", "gui", ],
            "project_name": "Sum walker",
            "project_short_description":
                ("Iterate over sums of a certain" +
                 " number of elements"),
            "release_date": "2020-02-25",
            "repo_name": "sum_walker",
            "version": "0.2.0",
            "year": "2020",
            'aur_email': "shlomif@cpan.org",
            'email': "shlomif@cpan.org",
            'full_name': 'Shlomi Fish',
            'github_username': "shlomif",
            },
        )

    def _append(to, from_):
        open(to, "at").write(open(from_, "rt").read())

    _append("sum_walker/sum_walker/__init__.py", "code/sum_walker/__init__.py")
    testfn = "sum_walker/tests/test_sum_walker.py"
    _append(testfn,
            "code/tests/test_sum_walker.py")
    import os
    os.chmod(testfn, 0o755)
    from subprocess import check_call
    check_call(["bash", "-c", "cd sum_walker && tox"])


main()
