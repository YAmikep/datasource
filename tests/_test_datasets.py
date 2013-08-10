# -*- coding: utf-8 -*- 
# set encoding to use u'abé' in the data test
# Use '_' prefix to this module to hide it from the auto discovering mode of nosetests

# Sets of data test
# Tuples (name, target, klass, data, datasize when lazy, real datasize)

import os as _os
import shutil as _shutil

from datasource import api as ds_api


def load_string_data_tests():
    return  [
        ('string', 'abc', ds_api.StringDataSource, 'abc', 3, 3),
        ('ustring', u'abé', ds_api.StringDataSource, u'abé', 3, 3),
    ]

def load_iterable_data_tests():
    # name, target, data, datasize lazy, datasize
    return  [
        ('iterable', ('a' for i in xrange(10)), ds_api.IterableDataSource, 'a'*10, 0, 10),
        ('iterable_ustring', (u'aé' for i in xrange(10)), ds_api.IterableDataSource, u'aé'*10, 0, 20),
    ]

folders = ['./tests_tmp/']
filenames = ['test.txt', './tests_tmp/test_file.txt']
filepaths = [_os.path.abspath(n) for n in filenames]    
filedatas = ['abc'*100, 'abc'*10000]
filesizes = [len(d) for d in filedatas]    

def load_files_data_tests():
    tests = []

    for i, name in enumerate(filenames):
        tests.extend([
            ('filename', filenames[i], ds_api.FileDataSource, filedatas[i], filesizes[i], filesizes[i]),
            ('filepath', filepaths[i], ds_api.FileDataSource, filedatas[i], filesizes[i], filesizes[i]),
            ('filepath_uri', 'file://{}'.format(filepaths[i]), ds_api.FileDataSource, filedatas[i], filesizes[i], filesizes[i])
        ])

    return  tests

def setup_files_data_tests():
    for path in folders:
        try:
            _os.makedirs(path)
        except:
            pass

    for i, name in enumerate(filenames):
        with open(name, 'w') as f:
            f.write(filedatas[i])

def clean_files_data_tests():
    for name in filenames:
        _os.remove(name)

    for path in folders:
        _shutil.rmtree(path)    

def load_remote_data_tests():
    #('url', 'http://www.test.com', 0, 0), # TODO: find a way to test remote sources
    return []       

def load_data_tests():
    return load_string_data_tests() + load_iterable_data_tests() + load_files_data_tests() + load_remote_data_tests()
