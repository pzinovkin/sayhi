#!/usr/bin/env python
from setuptools import setup

from sayhi import __version__


setup(
    name='sayhi',
    version=__version__,
    packages=['sayhi'],
    # packages required for your module
    install_requires=[
        'termcolor==1.1.0',
    ],
    entry_points={
        'console_scripts': ['sayhi = sayhi.main:main', ]
    }
)
