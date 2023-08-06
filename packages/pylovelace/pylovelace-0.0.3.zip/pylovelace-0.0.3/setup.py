"""
PyLovelace
Python Obfuscation Tool

Copyright 2023 PyLovelace

Author - nshout
"""
from setuptools import setup
from os import path

directory = path.abspath(path.dirname(__file__))

with open(path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pylovelace',
    version="0.0.3",
    description='Python code obfuscation tool',
    long_description=long_description,
    author='nshout',
    url='https://github.com/pylovelace/pylovelace',
    keywords='obfuscate obfuscation distribute production tool',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Security',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
    packages=['pylovelace', 'pylovelace.core', 'pylovelace.core.cryptography'],
    package_dir={'pylovelace': 'source'},
    package_data={'pylovelace': ['core/*.py', 'core/*.pyd', 'core/cryptography/*.py', 'core/cryptography/*.pyd']},
    entry_points={'console_scripts': ['pylovelace=pylovelace.pylovelace:main']}
)
