from setuptools import setup, find_packages

# Dirty hack for error when using vagrant
# $ python setup.py sdist
# making hard links in foo-0.1...
# hard linking README.txt -> foo-0.1
# error: Operation not permitted
import os
if 'vagrant' in str(os.environ):
    del os.link


__version_info__ = (0, 2, 0)
__version__ = '.'.join((str(i) for i in __version_info__))

with open('README.rst') as f:
    long_description = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='datasource',
    version=__version__,
    description="DataSource is a simple wrapper for fetching data with a uniform API regardless how the data should be fetched.",
    long_description=long_description,
    license=license,
    url='https://bitbucket.org/YAmikep/datasource',
    author="Michael Palumbo",
    author_email="michael.palumbo87@gmail.com",
    packages=find_packages(exclude=('tests', 'tests.*')), # tests.* is important to exclude all packages under tests
    install_requires=['requests>1.2,<2.4.0'],
    include_package_data=True,
    package_data={'': ['AUTHORS', 'LICENSE']},    
    classifiers=[ # All possible values here: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
