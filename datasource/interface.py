MAX_MEMORY = 5 * 1024 * 2 ** 10  # 5 MB
BUFFER_SIZE = 1 * 512 * 2 ** 10  # 512 KB

class DataSourceInterface(object):
    """Provides a uniform API regardless of how the data should be fetched."""

    def __init__(self, target, preload=False, **kwargs):
        raise NotImplementedError()

    @property
    def is_loaded(self):
        raise NotImplementedError()

    def load(self):
        """
        Loads the data if not already loaded.
        
        """
        raise NotImplementedError()        

    def size(self, force_load=False):
        """
        Returns the size of the data.
        If the datasource has not loaded the data yet (see preload argument in constructor), the size is by default equal to 0.
        Set force_load to True if you want to trigger data loading if not done yet.

        :param boolean force_load: if set to True will force data loading if not done yet.

        """
        raise NotImplementedError()

    def get_reader(self):
        """
        Returns an independent reader (with the read and seek methods).
        The data will be automatically loaded if not done yet.

        """
        raise NotImplementedError()
