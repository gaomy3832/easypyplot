"""
 * Copyright (c) 2016. Mingyu Gao
 * All rights reserved.
 *
"""
import unittest
import matplotlib

from easypyplot import util

class TestUtil(unittest.TestCase):
    ''' Tests for util module. '''

    def test_matplotlib_version_tuple(self):
        ''' Get version tuple. '''
        vtpl = util.matplotlib_version_tuple()
        self.assertIsInstance(vtpl, tuple)
        for v in vtpl:
            self.assertIsInstance(v, int)
        self.assertLessEqual(len(vtpl), 3)
        self.assertEqual('.'.join(str(v) for v in vtpl), matplotlib.__version__)

