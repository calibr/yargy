# coding: utf-8
from __future__ import unicode_literals

from sys import version_info
from setuptools import setup, find_packages


REQUIREMENTS = [
    'pymorphy2==0.8',
    'backports.functools-lru-cache==1.3',
    'intervaltree==2.1.0',
    'jellyfish==0.5.6',
]

setup(
    name='yargy',
    version='0.8.0',
    description='Tiny rule-based facts extraction package',
    url='https://github.com/bureaucratic-labs/yargy',
    author='Dmitry Veselov',
    author_email='d.a.veselov@yandex.ru',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='natural language processing, russian morphology',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
)
