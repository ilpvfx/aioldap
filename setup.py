#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'ldap3 >=2.5, <3',
    'async_timeout >=4.0.2, <5',
]

setup(
    name='ilp-aioldap',
    version='0.4.5',
    description="Async ldap library sorta based off ldap3",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    author="Terry Cain",
    author_email='terry@terrys-home.co.uk',
    url='https://github.com/ilpvfx/aioldap',
    packages=find_packages(include=['aioldap*']),
    include_package_data=True,
    install_requires=requirements,
    license="Apache 2",
    zip_safe=False,
    keywords='aioldap',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests'
)
