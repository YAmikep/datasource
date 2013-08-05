# Python stdlib
# Let's use only StringIO because cStringIO seems to duplicate the data in memory
# when using getvalue() to create a new stream.
# try:
#    from cStringIO import StringIO as _StringIO
# except ImportError:
#    from StringIO import StringIO as _StringIO
from StringIO import StringIO as _StringIO

# Internal
from ..interface import DataSourceInterface
from ..utils import helpers


class StringDataSource(DataSourceInterface):

    def __init__(self, data, **kwargs):
        self._data = data
        self._readers = []

    @property
    def is_loaded(self):
        return True

    def load(self):
        pass

    def size(self, *args, **kwargs):
        return len(self._data)

    def get_reader(self):
        r = _StringIO(self._data)
        self._readers.append(r)
        return r

    def __repr__(self):
        name = self.__class__.__name__
        return u'<{}: {}>'.format(name, helpers.truncate(self._data, size=50))

    def __del__(self):
        for r in self._readers:
            r.close()
