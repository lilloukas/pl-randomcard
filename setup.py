from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'randomcard',
    version          = '0.1',
    description      = 'Download random card info',
    long_description = readme,
    author           = 'lilloukas',
    author_email     = 'colejh@bu.edu',
    url              = 'http://wiki',
    packages         = ['randomcard'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'randomcard = randomcard.__main__:main'
            ]
        }
)
