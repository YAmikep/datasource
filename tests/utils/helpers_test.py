# Testing toolbox
import unittest
from nose_parameterized import parameterized

from datasource.utils import helpers
 
class UtilsHelpersTests(unittest.TestCase):
    
    @parameterized.expand([
        ('string', 'abc'*20, 10, '...', 'abcabca...'),
        ('string', 'abc'*20, 2, '...', '..'),
        ('string', 'abc'*20, 0, '...', ''),
        ('string', 'abc'*20, 60, '...', 'abc'*20),
        ('string', 'abc'*20, 70, '...', 'abc'*20),
    ])    
    def test_truncate(self, name, s, size, tail, expected):
        trunc = helpers.truncate(s, size, tail)
        self.assertEqual(trunc, expected)
        self.assertEqual(len(trunc), len(expected))
