"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

setup(
    name='shmeehub',
    version='0.1.0',
    description='a stub for KeyHub',
    author='Sander Evers',
    packages=find_packages(),
    install_requires=['Flask','Authlib>=0.6'],
    entry_points={
        'console_scripts': [
            'shmeehub=shmeehub.__main__:main',
        ],
    },
)