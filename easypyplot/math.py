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

import numpy as np

def _parse_expected_tuple(arg, default=tuple()):
    """ Parse the argument into an expected tuple.

    The argument can be None (i.e., using the default), a single element (i.e.,
    a length-1 tuple), or a tuple
    """
    try:
        _ = iter(arg)
    except TypeError:
        tpl = tuple(default) if arg is None else (arg,)
    else:
        tpl = tuple(arg)
    return tpl


def normalize(data, axis=None, index=None):
    """ Normalize data on the given axis

    data: a multi-dim array.
    axis: axis or axes which makes subarrays to be normalized together.
        E.g., axis=-1 means to normalize the innermost dimension.
        None (i.e., all axes) or int or tuple of int.
    index: index or indices of the elements used for normalization along the
        normalization axis or axes.
        None or int or tuple of int.

    Example:
    data = [[.1, .4, .7], [.2, .5, .8], [.3, .6, .9]]
    normalize(data) = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    normalize(data, axis=-1) = [[1, 4, 7], [1, 2.5, 4], [1, 2, 3]]
    normalize(data, axis=0) = [[1, 1, 1], [2, 1.25, 1.143], [3, 1.5, 1.286]]
    normalize(data, axis=0, index=1) =
            [[0.5, 0.8, 0.875], [1, 1, 1], [1.5, 1.2, 1.125]]
    """
    din = np.asarray(data)
    ndim = din.ndim
    shape = din.shape

    # Parse arguments.
    axes = _parse_expected_tuple(axis, default=range(ndim))
    indices = _parse_expected_tuple(index)
    # Pad with zero indices, or ignore unused indices.
    indices += (0,) * (len(axes) - len(indices))

    # Constrcut the denominator array through an index array.
    # The denominator array has the same shape as the data array, except the
    # normalization axes whose dimensions are 1 and elements are the indexed
    # elements used for normalization that will be broadcast.
    # The index array selects the elements used for normalization, using the
    # given indice along the normalization axes, and a full slice along the
    # other axes.
    didx = [slice(None) for _ in range(ndim)]
    sidx = list(shape)  # indexing loses axis, restore through reshape
    for d, i in zip(axes, indices):
        didx[d] = i
        sidx[d] = 1
    dnorm = din[tuple(didx)].reshape(tuple(sidx))

    return din / dnorm


def geomean(data, axis=None):
    """ Get the geometric mean along the given axis.

    data: a multi-dim array.
    axis: axis or axes along which the geomean is performed.
        None (i.e., all axes) or int or tuple of int.
    """
    din = np.asarray(data)
    prod = np.prod(din, axis=axis)
    num = din.size // prod.size
    return prod ** (1. / num)

