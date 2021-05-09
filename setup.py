#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ree",
    version_config=True,
    setup_requires=['setuptools-git-versioning'],
    author="blackleg",
    author_email="hectorespertpardo@gmail.com",
    description="UNOFFICIAL Red Eléctrica de España data client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blackleg/ree",
    packages=find_packages(),
    install_requires=[
        'arrow',
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
