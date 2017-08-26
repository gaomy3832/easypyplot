"""
 * Copyright (c) 2016. Mingyu Gao
 * All rights reserved.
 *
"""
import matplotlib

def matplotlib_version_tuple():
    """ Get the matplotlib version as a 3-tuple. """
    return tuple([int(x) for x in matplotlib.__version__.split('.')])

__mpl_version__ = matplotlib_version_tuple()

