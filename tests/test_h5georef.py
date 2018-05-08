# -*- coding: utf-8 -*-
"""
tests.test_h5georef description
"""
import unittest
import os
from h5georef import H5Georef

__author__ = 'jph'
__email__ = 'j.huart@cra.wallonie.be'
__copyright__ = 'Copyright 2018, Jean Pierre Huart'
__license__ = 'GPLv3'
__date__ = '2018-05-08'
__version__ = '1.0'
__status__ = 'Development'


class Test(unittest.TestCase):


    def setUp(self):
        self.hdf5 = os.path.join('../data', 'HDF5_LSASAF_MSG_DSSF_MSG-Disk_201510251200')
        return


    def tearDown(self):
        pass


    def test_H5Georef(self):
        h5g = H5Georef(self.hdf5)
        self.assertIsInstance(h5g, H5Georef)
        self.assertEqual(h5g.coff, 1856)       
        print(h5g.GEOSProjString) 
        samples = h5g.get_sample_coords(numSamples=2)
        print(samples)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()