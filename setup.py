#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='reescraper',
    version='1.5.0',
    packages=['reescraper', 'reescraper/core', 'reescraper/response', 'reescraper/canary', 'reescraper/balearic'],
    install_requires=[
        'arrow',
        'requests'
      ],
    url='https://github.com/blackleg/reescraper',
    license='MIT',
    author='blackleg',
    author_email='hectorespertpardo@gmail.com',
    description='Red Eléctrica de España data scraper'
)
