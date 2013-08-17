"""
See README.rst for further information

"""
import os
import urlparse

from .impl.string import StringDataSource
from .impl.iterable import IterableDataSource
from .impl.file import FileDataSource
from .impl.remote import RemoteDataSource

from .exceptions import DataSourceError

# Define the API
__all__ = ['DataSource', 'StringDataSource', 'IterableDataSource', 'FileDataSource', 'RemoteDataSource']


def DataSource(target, is_file=None, **kwargs):
    """
    Inspects the target and returns the convenient DataSource implementation.
    
    :param boolean is_file: when the target is a filepath and the file does not exist, the target is considered as a StringDataSource by default.
        Set is_file to True to make sure an Exception is raised if the file does not exist instead of considering the target as a String. 
    
    """
    if isinstance(target, basestring):
        target_head = target[0:10].lower()

        is_remote = target_head.startswith('http://') or target_head.startswith('https://')
        if is_remote:
            return RemoteDataSource(target, **kwargs)

        if target_head.startswith('file://'):
            p = urlparse.urlparse(target)
            filepath = os.path.abspath(os.path.join(p.netloc, p.path))
            return FileDataSource(filepath, **kwargs)

        if os.path.exists(target):
            return FileDataSource(target, **kwargs)
        elif is_file:
            raise DataSourceError('File not found: {}'.format(target))

        return StringDataSource(target, **kwargs)

    # Not a string
    return IterableDataSource(target, **kwargs)
