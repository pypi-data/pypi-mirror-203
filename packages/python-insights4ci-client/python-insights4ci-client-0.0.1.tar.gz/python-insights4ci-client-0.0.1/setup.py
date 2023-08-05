#!/usr/bin/env python3
"""
Python Insights4CI' client library
Copyright (c) 2022 Beraldo Leal for Red Hat, Inc.
"""

import sys
import setuptools
import pkg_resources

from setuptools.command import bdist_egg


class bdist_egg_guard(bdist_egg.bdist_egg):
    def run(self):
        sys.exit('Please use `pip install .` instead.')


def main():
    # https://medium.com/@daveshawley/safely-using-setup-cfg-for-metadata-1babbe54c108
    pkg_resources.require('setuptools>=39.2')

    kwargs = {
        'cmdclass': {'bdist_egg': bdist_egg_guard}
    }

    setuptools.setup(**kwargs)


if __name__ == '__main__':
    main()
