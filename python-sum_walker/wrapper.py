#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.

import cookiecutter.main
import os
import os.path
import re
import shutil
import sys
from subprocess import check_call


repo_name = "sum_walker"
base_dir = "python-" + repo_name


class DistGenerator(object):
    """docstring for DistGenerator"""
    def __init__(self, dist_name, base_dir):
        self.dist_name = dist_name
        self.base_dir = base_dir

    def _myformat(self, mystring):
        return mystring.format(
            dist_name=self.dist_name, base_dir=self.base_dir, )

    def command__build(self):
        self.command__build_only()
        self.command__test()

    def command__build_only(self):
        if os.path.exists(self.dist_name):
            shutil.rmtree(self.dist_name)
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
                "repo_name": self.dist_name,
                "version": "0.8.2",
                "year": "2020",
                'aur_email': "shlomif@cpan.org",
                'email': "shlomif@cpan.org",
                'full_name': 'Shlomi Fish',
                'github_username': "shlomif",
                },
            )

        def _append(to, from_):
            open(to, "at").write(open(from_, "rt").read())

        _append("sum_walker/sum_walker/__init__.py",
                "code/sum_walker/__init__.py")
        _append("sum_walker/sum_walker/iterator_wrapper.py",
                "code/sum_walker/iterator_wrapper.py")
        chglog = "sum_walker/CHANGELOG.rst"

        def _re_mutate(fn, pattern, repl_fn, prefix='', suffix=''):
            txt = open(fn, "rt").read()
            txt, count = re.subn(pattern, (prefix + open(
                repl_fn, "rt").read() + suffix).replace('\\', '\\\\'),
                txt, 1, re.M | re.S)
            # print(count)
            assert count == 1
            open(fn, "wt").write(txt)
        _re_mutate(
            chglog, "\n0\\.1\\.0\n.*",
            "code/CHANGELOG.rst.base.txt", "\n")
        s = "COPYRIGHT\n"
        for fn in ["sum_walker/README", "sum_walker/README.rst",
                   "sum_walker/docs/README.rst", ]:
            _re_mutate(
                fn, "^PURPOSE\n.*?\n" + s, "code/README.part.rst", '', s)

        testfn = "sum_walker/tests/test_sum_walker.py"
        _append(testfn,
                "code/tests/test_sum_walker.py")
        open("sum_walker/tox.ini", "wt").write(
            "[tox]\nenvlist = py38\n\n" +
            "[testenv]\ndeps =\n\tpytest\n\t" +
            "pytest-cov\ncommands = pytest\n")
        os.chmod(testfn, 0o755)

    def command__test(self):
        check_call(["bash", "-c", self._myformat("cd {dist_name} && tox")])

    def command__gen_travis_yaml(self):
        import yaml

        with open("travis.yml", "wt") as f:
            f.write(yaml.dump({
                'install':
                [
                    'pip install cookiecutter',
                    self._myformat(
                        '( cd {base_dir} && ' +
                        'python3 wrapper.py command__build_only )'),
                    self._myformat(
                        '( cd {base_dir} && cd {dist_name} && ' +
                        'pip install -r requirements.txt && pip install . )')
                ],
                'script': [
                    self._myformat(
                        '( cd {base_dir} && cd {dist_name} && ' +
                        'py.test --cov {dist_name} ' +
                        '--cov-report term-missing tests/ )')
                ],
                'language': 'python',
                'python': ['3.5', '3.6', '3.7', '3.8', 'pypy3', ],
                }))


try:
    cmd = sys.argv.pop(1)
except IndexError:
    cmd = 'build'

obj = DistGenerator(dist_name="sum_walker", base_dir=base_dir)

if cmd == 'travis':
    obj.command__gen_travis_yaml()
elif cmd == 'build':
    obj.command__build()
elif cmd == 'command__build_only':
    obj.command__build_only()
else:
    raise BaseException("Unknown sub-command")
