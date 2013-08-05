# Python stdlib
import os as _os

# Internal
from ..interface import DataSourceInterface


class FileDataSource(DataSourceInterface):

    def __init__(self, filepath, **kwargs):
        self._filepath = _os.path.abspath(filepath)
        self._readers = []

    @property
    def is_loaded(self):
        return True

    def load(self):
        pass        

    def size(self, *args, **kwargs):
        return _os.path.getsize(self._filepath)

    def get_reader(self):
        r = open(self._filepath, 'r')
        self._readers.append(r)
        return r

    def __repr__(self):
        name = self.__class__.__name__
        return '<{}: {}>'.format(name, self._filepath)

    def __del__(self):
        for r in self._readers:
            r.close()
