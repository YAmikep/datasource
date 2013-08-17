# Third party
import requests

# Internal
from .iterable import IterableDataSource, MAX_MEMORY, BUFFER_SIZE


class RemoteDataSource(IterableDataSource):
    """
    Use an IterableDataSource to load the data.
    """

    def __init__(self, url, preload=False, max_memory=MAX_MEMORY, buffer_size=BUFFER_SIZE, dir_tmp=None, **kwargs):
        self._tmp_file = None
        self._url = url
        self._buffer_size = buffer_size

        # IMPORTANT: do not use lambda functions with self because it leads to circular references and prevents the object to get deleted.
        #self._lazy_load = lambda: self._load(data, max_memory, buffer_size, dir_tmp)
        self._tmp_args = [self._iter_fetch, max_memory, buffer_size, dir_tmp]

        if preload is True:
            self.load()

    def __repr__(self):
        return '<RemoteDataSource: {}>'.format(self._url)

    def _iter_fetch(self):
        """Loads the source.
        If data exists, it will be used to load it. Data can be a string or an iterable (list, generator, etc.).
        If already loaded, it will be reset first.
        """
        # Fetches the URI. It does not download it in one shot in case there is
        # a huge amount of data.
        # stream=True to not download it in one shot
        r = requests.get(self._url, stream=True)
        return r.iter_content(chunk_size=self._buffer_size)