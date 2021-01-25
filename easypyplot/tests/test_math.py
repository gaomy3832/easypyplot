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
import numpy as np

from easypyplot import math as m  # avoid conflict with built-in.

class TestMath(unittest.TestCase):
    ''' Tests for math module. '''

    def setUp(self):
        self.data = np.linspace(1, 3 * 2 * 4, num=3 * 2 * 4, endpoint=True).reshape(3, 2, 4) / 10.

    def test_parse_expected_tuple(self):
        ''' _parse_expected_tuple. '''
        # pylint: disable=protected-access
        self.assertTupleEqual((3,), m._parse_expected_tuple(3))
        self.assertTupleEqual((-1,), m._parse_expected_tuple(-1))
        self.assertTupleEqual((2, 3, -1,), m._parse_expected_tuple([2, 3, -1]))
        self.assertTupleEqual(tuple(), m._parse_expected_tuple(None))

    def test_normalize(self):
        ''' normalize. '''
        # Normalize all together.
        result1 = m.normalize(self.data)
        expect1 = self.data * 10
        np.testing.assert_allclose(expect1, result1)
        self.assertTupleEqual(expect1.shape, result1.shape)

        # Normalize along innermost axis of size 4.
        result2 = m.normalize(self.data, axis=-1)
        expect2 = self.data / (np.array([[1, 5], [9, 13], [17, 21]]) / 10.)[..., np.newaxis]
        np.testing.assert_allclose(expect2, result2)
        self.assertTupleEqual(expect2.shape, result2.shape)

        # Normalize along outermost axis of size 3.
        result3 = m.normalize(self.data, axis=0)
        expect3 = self.data / (np.array([range(1, 1+4), range(5, 5+4)]) / 10.)
        np.testing.assert_allclose(expect3, result3)
        self.assertTupleEqual(expect3.shape, result3.shape)

        # Normalize along outermost axis of size 3, using the second index.
        result4 = m.normalize(self.data, axis=0, index=1)
        expect4 = self.data / (np.array([range(9, 9+4), range(13, 13+4)]) / 10.)
        np.testing.assert_allclose(expect4, result4)
        self.assertTupleEqual(expect4.shape, result4.shape)

        # Normalize along two innermost axes of size (2, 4), using the last index.
        result5 = m.normalize(self.data, axis=(-1, -2), index=(-1, -1))
        expect5 = self.data / (np.array([8, 16, 24]) / 10.)[..., np.newaxis, np.newaxis]
        np.testing.assert_allclose(expect5, result5)
        self.assertTupleEqual(expect5.shape, result5.shape)

        # Normalize along none axis, i.e., each is normalized individually and becomes 1.
        result6 = m.normalize(self.data, axis=tuple())
        expect6 = np.ones(self.data.shape)
        np.testing.assert_allclose(expect6, result6)
        self.assertTupleEqual(expect6.shape, result6.shape)

    def test_geomean(self):
        ''' geomean. '''
        # Geomean along all.
        result1 = m.geomean(self.data)
        expect1 = np.prod(self.data.reshape(None)) ** (1. / self.data.size)
        np.testing.assert_allclose(expect1, result1)
        self.assertTupleEqual(expect1.shape, result1.shape)

        # Geomean along innermost axis of size 4.
        result2 = m.geomean(self.data, axis=-1)
        expect2 = np.array(
            [np.prod(range(i, i + 4)) ** (1. / 4) for i in range(1, 1 + 24, 4)]).reshape(3, 2) / 10.
        np.testing.assert_allclose(expect2, result2)
        self.assertTupleEqual(expect2.shape, result2.shape)

        # Geomean along outermost axis of size 3.
        result3 = m.geomean(self.data, axis=0)
        expect3 = np.array(
            [np.prod([i, i + 8, i + 16]) ** (1. / 3) for i in range(1, 1 + 8)]).reshape(2, 4) / 10.
        np.testing.assert_allclose(expect3, result3)
        self.assertTupleEqual(expect3.shape, result3.shape)

        # Geomean along two innermost axes of size (2, 4).
        result4 = m.geomean(self.data, axis=(-1, -2))
        expect4 = np.array(
            [np.prod(range(i, i + 8)) ** (1. / 8) for i in range(1, 1 + 24, 8)]) / 10.
        np.testing.assert_allclose(expect4, result4)
        self.assertTupleEqual(expect4.shape, result4.shape)

