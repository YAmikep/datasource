# Testing toolbox
import unittest
from nose_parameterized import parameterized

# Sets of data test
import test_data as td

from datasource import *


class DataSourceGlobalTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        td.setup_files_data_tests()

    @classmethod        
    def tearDownClass(cls):
        td.clean_files_data_tests()


    @parameterized.expand(td.load_data_tests)
    def test_size(self, name, target, klass, data, datasize_before_load, datasize):

        s = DataSource(target)  # By default, preload must be equal to False so check the size.
        
        # Do not fetch the data if it is an URL.
        if not isinstance(s, RemoteDataSource):
            self.assertEqual(s.size(), datasize_before_load)
            self.assertEqual(s.size(force_load=True), datasize)
        
        # Do not fetch the data if it is an URL.
        # TODO: find a way to test remote sources: a static file on bitbucket?
        if not isinstance(s, RemoteDataSource):
            r = s.get_reader()
            size = len(r.read())
            self.assertEqual(size, datasize)


    @parameterized.expand(td.load_data_tests)
    def test_get_reader(self, name, target, klass, data, datasize_before_load, datasize):

        s = DataSource(target)
        
        # Do not fetch the data if it is an URL.
        # TODO: find a way to test remote sources: a static file on bitbucket?
        if not isinstance(s, RemoteDataSource):
            # Size before loading
            self.assertEqual(s.size(), datasize_before_load)

            r1 = s.get_reader()
            r2 = s.get_reader()

            # Size after getting a reader
            self.assertEqual(s.size(), datasize)

            # Is loaded
            self.assertEqual(s.is_loaded, True)
            
            # Size of the data
            self.assertEqual(len(r1.read()), datasize)
            self.assertEqual(len(r2.read()), datasize)

            # Set the reader position back to the beginning
            r1.seek(0)
            self.assertEqual(len(r1.read()), datasize)

            # Do not set the reader position back to the beginning
            self.assertEqual(len(r2.read()), 0)             

            # Check the data
            r1.seek(0)
            self.assertEqual(r1.read(), data)

            r1.seek(0)
            r2.seek(0)
            self.assertEqual(r1.read(), r2.read())
