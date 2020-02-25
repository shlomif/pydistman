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


main()
