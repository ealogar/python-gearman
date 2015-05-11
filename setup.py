#!/usr/bin/env python

from setuptools import setup


setup(
    name = 'gearman',
    version = '2.0.4',
    author = 'Matthew Tai',
    author_email = 'mtai@yelp.com',
    description = 'Gearman API - Client, worker, and admin client interfaces',
    long_description=open('README.txt').read(),
    install_requires=['six'],
    url = 'http://github.com/Yelp/python-gearman/',
    packages = ['gearman'],
    license='Apache',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
