"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from dash_admin import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=dash_admin', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name = 'dash-admin',
    version = __version__,
    description = 'A CLI for starting Dash projects',
    long_description = long_description,
    url = 'https://github.com/gaw89/dash-admin',
    author = 'Gideon Whitehead',
    author_email = 'gideon.whitehead@uphs.upenn.edu',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'dash-admin=dash_admin.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)
