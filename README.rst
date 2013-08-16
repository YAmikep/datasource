=====================================================================
DataSource - A simple wrapper for fetching data no matter where it is
=====================================================================

.. image:: https://secure.travis-ci.org/YAmikep/datasource.png
    :target: https://travis-ci.org/YAmikep/datasource

.. image:: https://coveralls.io/repos/YAmikep/datasource/badge.png
   :target: https://coveralls.io/r/YAmikep/datasource  

.. image:: https://pypip.in/v/datasource/badge.png
    :target: https://crate.io/packages/datasource/

.. image:: https://pypip.in/d/datasource/badge.png
    :target: https://crate.io/packages/datasource/


DataSource is a simple wrapper for fetching data with a uniform API regardless how the data should be fetched.

The purpose of this library is to remove the pain of thinking of the required approach based on where the data is:

- a file on disk
- a remote file reachable via an URL
- a string in memory
- or even an iterable / a callable that generates data.

It takes care of fetching the data and provides "readers" (file-like objects) to actually get the data.
It can handle huge amount of data by keeping a low memory footprint. (See the section "Working with huge amount of data")



Docs
----

.. http://datasource.readthedocs.org/en/latest/



Install
-------

From PyPI (stable)::

    pip install datasource

From Github (unstable)::

    pip install git+git://github.com/YAmikep/datasource.git#egg=datasource

DataSource currently requires the `requests <http://docs.python-requests.org/>`_ library to fetch URLs.



Main API
---------

- ``datasource.DataSource(target, **kwargs)``: a DataSource object

The only mandatory argument is ``target`` which defines where the data is. It can be a string, a callable or an iterable.

There are a couple of possible keyword arguments:

- ``is_file``: a boolean to ensure that the string target is actually considered as a filepath so that an error is raised if the file cannot be found. By default, a string target is considered as a raw string data if the file does no exist.


The following four parameters are useful only when the data is not locally available, i.e. has to be downloaded or generated.

- ``preload``: a boolean to trigger data loading when the object is created (Default: False). A DataSource object is lazy by default.
- ``max_memory``: the maximum size of the data to store in memory. This threshold triggers the creation of a temporary file.
- ``buffer_size``: the buffer size
- ``dir_tmp``: the directory where to create temporary files



DataSource objects
------------------

A ``DataSource`` object has a simple API:

- ``is_loaded`` property: tells whether the source is loaded, meaning that the data is available locally
- ``load(self)``: will load the data if it has not been done yet
- ``size(self, force_load=False)``: the size of the data. If the data is not loaded yet, the size is 0, it will not load it unless you set force_load to True to make sure it is loaded before it returns the size.
- ``get_reader(self)``: returns a "reader" which is a file-like object from which you will actually get the data with the read method.


A DataSource object is lazy by default (preload=False). For example, when providing a URL, the data will not be downloaded when the object is created but when the data is first needed, which is to say when calling get_reader().


Working with huge amount of data will not make you run out of memory
--------------------------------------------------------------------
When using an in-memory string or a file, the data is already stored locally so there is no extra work to fetch and store the data.
However, when fetching a remote file or using a generator, you do not know the size of the data.
The data is by default downloaded into memory for a performance concern. However, to avoid running out of memory because of a huge amount of data, you can tell the maximum memory to use (max_memory kwarg) so that a temporary file will automatically be created when reaching this threshold (default: 5 MB), freeing the memory. This features ensures that you can keep control of your memory while fetching data of unknown size. The temporary file is managed behind the scene and will be deleted when the DataSource object is deleted.

You can also have control over the buffer (buffer_size kwarg, default: 512 KB) and the directory where temporary files should be created (dir_tmp kwarg, default: the default temporary folder of the OS).

Note that a DataSource object is lazy so, unless you set preload to True at the creation of the object, the data will actually be fetched and stored only when you call get_reader for the first time.


Usage and examples
------------------

.. code:: python

    >>> import datasource as ds

    # Directly an in-memory string
    >>> data = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> source = ds.DataSource(data)
    >>> print source.is_loaded, source.size()
    True 26
    >>> reader = source.get_reader()
    >>> print reader.read()
    ABCDEFGHIJKLMNOPQRSTUVWXYZ

    # A string as a filepath: absolute path, relative path or path defined with "file://"
    >>> filepath = 'tests/data/afile.txt'
    >>> source = ds.DataSource(filepath)
    >>> print source.is_loaded, source.size()
    True 26
    >>> reader = source.get_reader()
    >>> print reader.read()
    ABCDEFGHIJKLMNOPQRSTUVWXYZ

    # A string as a filepath: use is_file to make sure it is considered as a file to raise an Error if the file does not exist
    >>> filepath = 'file_does_not_exist.txt'
    >>> try:
    ...     source = ds.DataSource(filepath, is_file=True)
    ... except Exception as e:
    ...     print e
    File not found: file_does_not_exist.txt

    # A callable
    >>> f = lambda: (chr(c) for c in xrange(65, 91))
    >>> callable(f)
    True
    >>> source = ds.DataSource(f)
    >>> print source.is_loaded, source.size()  # A DataSource is lazy by default so it is not loaded yet
    False 0
    >>> reader = source.get_reader()  # get_reader triggers data loading
    >>> print source.is_loaded, source.size()
    True 26
    >>> print reader.read()
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    >>> source = ds.DataSource(f, preload=True)  # Set preload to True to load the data at the creation
    >>> print source.is_loaded, source.size()
    True 26

    # A generator
    >>> gen = (chr(c) for c in xrange(65, 91))
    >>> type(gen)
    <type 'generator'>
    >>> source = ds.DataSource(gen)
    >>> print source.size(force_load=True), source.is_loaded  # A DataSource is lazy so use force_load to make sure it is loaded
    26 True
    >>> reader = source.get_reader()
    >>> print source.is_loaded, source.size()
    True 26
    >>> print reader.read()
    ABCDEFGHIJKLMNOPQRSTUVWXYZ

    # An URL
    >>> url = 'https://bitbucket.org/YAmikep/datasource/raw/master/tests/data/afile.txt'
    >>> source = ds.DataSource(url)
    >>> print source.is_loaded, source.size()  # A DataSource is lazy by default
    False 0
    >>> reader = source.get_reader()  # get_reader triggers data loading
    >>> print source.is_loaded, source.size()
    True 26
    >>> print reader.read()
    ABCDEFGHIJKLMNOPQRSTUVWXYZ



Contribute
----------

Clone and install testing dependencies::

    $ python setup.py develop 
    $ pip install -r requirements_tests.txt

Ensure tests pass::

    $ ./runtests.sh

Or using tox::

    $ tox
