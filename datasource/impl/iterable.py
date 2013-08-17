# Internal
from ..interface import DataSourceInterface, MAX_MEMORY, BUFFER_SIZE
from ..utils.tempfile import SpooledTemporaryFile as _SpooledTemporaryFile
from ..utils import helpers


class IterableDataSource(DataSourceInterface):

    def __init__(self, data, preload=False, max_memory=MAX_MEMORY, buffer_size=BUFFER_SIZE, dir_tmp=None, **kwargs):
        """
        :param data: an object that is iterable or callable

        """
        self._tmp_file = None

        # IMPORTANT: do not use lambda functions with self because it leads to circular references and prevents the object to get deleted.
        #self._lazy_load = lambda: self._load(data, max_memory, buffer_size, dir_tmp)
        self._tmp_args = [data, max_memory, buffer_size, dir_tmp]

        if preload is True:
            self.load()
        
    @property
    def is_loaded(self):
        return self._tmp_file is not None

    def load(self):
        if self.is_loaded is False:
            data = self._tmp_args.pop(0) # pop the target out of the list arguments

            self._tmp_file = self._create_tmp_file(*self._tmp_args)      
            del self._tmp_args

            if callable(data):
                data = data()

            for chunk in data:
                self._tmp_file.write(chunk)

    def size(self, force_load=False):
        if self.is_loaded is False:
            if force_load is False:
                return 0

            self.load()
            
        return self._tmp_file._file.tell()

    def get_reader(self):
        if self.is_loaded is False:
            self.load()

        return self._tmp_file.get_reader()

    def __repr__(self):
        name = self.__class__.__name__
        excerpt = None
        if self._tmp_file is not None:
            r = self.get_reader()
            excerpt = helpers.truncate(r.read(60), size=50)
        return '<{}: {}>'.format(name, excerpt)

    def __del__(self):
        del self._tmp_file  # will be closed and deleted

    def _create_tmp_file(self, max_memory, buffer_size, dir_tmp):
        return _SpooledTemporaryFile(max_size=max_memory, bufsize=buffer_size, dir=dir_tmp)
