# -*- coding: utf-8 -*-
import os.path as osp
import setuptools

this_dir = osp.abspath(osp.dirname(__file__))


def find_tests():
    import unittest

    loader = unittest.TestLoader()
    return loader.discover('tests', pattern='*.py', top_level_dir=True)


setuptools.setup(
    name="testing_selenium_extras",
    version="0.1.0",
    url="https://github.com/mykulyak/testing_selenium_extras",

    author="Andriy Mykulyak",
    author_email="mykulyak@gmail.com",

    description="Stuff that simplifies writing Selenium tests in Python.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=open(osp.join(this_dir, 'requirements.txt'), 'r').read().splitlines(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
