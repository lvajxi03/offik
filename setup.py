#!/usr/bin/env python3

"""
Setup module for packaging
(required by setuptools)
"""

import os
from setuptools import setup


def read(file_name):
    """
    Read file content.
    Utility function for setup, below
    :param file_name: Name of the file to read
    :return: file content (string)
    """
    return open(
        os.path.join(
            os.path.dirname(__file__),
            file_name),
        encoding="UTF-8").read()


setup(
    name="offik",
    version="xTAGx",
    author="Marcin Bielewicz",
    author_email="marcin.bielewicz@gmail.com",
    description="Simple 'walk/collect/destroy enemies in your office' game",
    license="GPL",
    keywords="pyglet office game arcade",
    packages=['offik'],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://iostream.pl/offik-en",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    install_requires=['pyglet']
)
