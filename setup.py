#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ree",
    version="2.2.2",
    author="blackleg",
    author_email="hectorespertpardo@gmail.com",
    description="UNOFFICIAL Red Eléctrica de España data client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blackleg/ree",
    packages=setuptools.find_packages(),
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
