# Testing toolbox
import unittest
from nose_parameterized import parameterized
# Use these tools when assertEqual, etc from unittest.TestCase are not defined ? It seemed to appear once when using @parameterized.expand 
#from nose.tools import assert_equal, assert_is_instance, assert_raises, assert_in

# Sets of data test
import test_data as td

from datasource import api as ds_api
from datasource.exceptions import DataSourceError


endpoints = ['DataSource', 'StringDataSource', 'IterableDataSource', 'FileDataSource', 'RemoteDataSource']

class DataSourceAPITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        td.setup_files_data_tests()

    @classmethod        
    def tearDownClass(cls):
        td.clean_files_data_tests()

    @parameterized.expand(endpoints)
    def test_endpoints_all_exists(self, endpoint):        
        self.assertIn(endpoint, ds_api.__all__)

    @parameterized.expand(ds_api.__all__)
    def test_endpoints_discover(self, endpoint):        
        self.assertIn(endpoint, endpoints)        
        
    @parameterized.expand(td.load_data_tests)
    def test_created_class_based_on_target(self, name, target, klass, data, datasize_lazy, datasize):

        s = ds_api.DataSource(target)
        self.assertIsInstance(s, klass)

    def test_not_existing_file(self):
        target = "not_exiting_file"
        self.assertRaises(DataSourceError, ds_api.DataSource, target=target, is_file=True)
