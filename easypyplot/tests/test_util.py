""" $lic$
Copyright (c) 2016-2021, Mingyu Gao

This program is free software: you can redistribute it and/or modify it under
the terms of the Modified BSD-3 License as published by the Open Source
Initiative.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the BSD-3 License for more details.

You should have received a copy of the Modified BSD-3 License along with this
program. If not, see <https://opensource.org/licenses/BSD-3-Clause>.
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

