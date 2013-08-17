from setuptools import setup, find_packages

from datasource.version import __version__

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
    install_requires=['requests>1.2,<1.3'],
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
