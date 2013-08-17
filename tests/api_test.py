# Testing toolbox
import unittest
from nose_parameterized import parameterized

# Sets of data test
import _test_datasets as tds

import datasource
import datasource.api as ds_api # need it for the __all__ variable
from datasource.exceptions import DataSourceError


endpoints = ['DataSource', 'StringDataSource', 'IterableDataSource', 'FileDataSource', 'RemoteDataSource']

class APITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        tds.setup_files_data_tests()

    @classmethod        
    def tearDownClass(cls):
        tds.clean_files_data_tests()

    @parameterized.expand(endpoints)
    def test_endpoints_all_exists(self, endpoint):        
        self.assertIn(endpoint, ds_api.__all__)

    @parameterized.expand(ds_api.__all__)
    def test_endpoints_discover(self, endpoint):        
        self.assertIn(endpoint, endpoints)        
        
    @parameterized.expand(tds.load_data_tests)
    def test_created_class_based_on_target(self, name, target, klass, data, datasize_lazy, datasize):

        s = datasource.DataSource(target)
        self.assertIsInstance(s, klass)

    def test_not_existing_file(self):
        target = "not_exiting_file"
        self.assertRaises(DataSourceError, datasource.DataSource, target=target, is_file=True)
