#!/usr/bin/env python3

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup
import os

def get_file_path(name):
    return os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        name))

def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]\

with open(get_file_path('fi2fa/version.py')) as f:
    exec(f.read())

# read requirements from requirements.txt
requirements = parse_requirements(get_file_path('requirements.txt'))

setup(
    name = 'fi2fa',
    py_modules = ['version'],
    packages = ['fi2fa'],
    install_requires = requirements,
    include_package_data=True,
    version = __version__,
    description = 'Finglish-to-Persian converter.',
    author = 'Iman Sarraf',
    license = '...',
    author_email = 'sarraf@yahoo.com',
    url = '',
    download_url = '' + __version__,
    keywords = ['persian', 'finglish'],
    classifiers = [
        'Programming Language :: Python :: 3'
    ],
    entry_points = {
        'console_scripts': [
            'f2p=fi2fa.f2p:main',
        ],
    },
)
