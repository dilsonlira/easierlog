import pathlib
from setuptools import find_packages, setup

from easierlog import VERSION

HERE = pathlib.Path(__file__).parent
PACKAGE_NAME = 'easierlog'
AUTHOR = 'Manoel Lira'
AUTHOR_EMAIL = 'dilsonlira@gmail.com'
URL = 'https://github.com/dilsonlira/easierlog'
LICENSE = 'MIT'
DESCRIPTION = 'The easy way to inspect variables in Python'
LONG_DESCRIPTION = (HERE / 'README.md').read_text()
LONG_DESC_TYPE = 'text/markdown'
CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]
REQUIRES_PYTHON = '>=3.6.0'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages()
    )
