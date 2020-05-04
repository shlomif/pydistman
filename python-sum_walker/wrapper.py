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
            "version": "0.8.0",
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
    _append("sum_walker/sum_walker/iterator_wrapper.py",
            "code/sum_walker/iterator_wrapper.py")
    chglog = "sum_walker/CHANGELOG.rst"

    def _re_mutate(fn, pattern, repl_fn, prefix='', suffix=''):
        txt = open(fn, "rt").read()
        import re
        txt, count = re.subn(pattern, (prefix + open(
            repl_fn, "rt").read() + suffix).replace('\\', '\\\\'),
            txt, 1, re.M | re.S)
        # print(count)
        assert count == 1
        open(fn, "wt").write(txt)
    _re_mutate(chglog, "\n0\\.1\\.0\n.*", "code/CHANGELOG.rst.base.txt", "\n")
    s = "COPYRIGHT\n"
    for fn in ["sum_walker/README", "sum_walker/README.rst",
               "sum_walker/docs/README.rst", ]:
        _re_mutate(fn, "^PURPOSE\n.*?\n" + s, "code/README.part.rst", '', s)

    testfn = "sum_walker/tests/test_sum_walker.py"
    _append(testfn,
            "code/tests/test_sum_walker.py")
    open("sum_walker/tox.ini", "wt").write(
        "[tox]\nenvlist = py38\n\n" +
        """[testenv]\ndeps =\n\tpytest\n\tpytest-cov\ncommands = pytest\n""")
    import os
    os.chmod(testfn, 0o755)
    from subprocess import check_call
    check_call(["bash", "-c", "cd sum_walker && tox"])


main()
