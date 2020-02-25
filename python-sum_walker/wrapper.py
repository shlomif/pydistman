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
        overwrite_if_exists=True,
        extra_context={
            'full_name':'Shlomi Fish',
            },
        )


main()
