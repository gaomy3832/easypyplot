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
import matplotlib.colors

from .util import __mpl_version__

# Colors from http://www.colorbrewer2.org/, 8-class, qualitative, Accent
COLOR_SET = ['#386cb0', '#7fc97f', '#f0027f', '#beaed4', \
             '#bf5b17', '#fdc086', '#666666', '#ffff99']

def color_scale(ref, num, low=0.2, high=0.9):
    """ Get a color scale from shallow to dark.

    ref: referenced color.
    num: number of colors in the scale.
    low: low brightness.
    high: high brightness.
    """
    # Saturate the color.
    try:
        rgb = matplotlib.colors.to_rgb(ref)
    except AttributeError:
        assert __mpl_version__ < (2, 0)  # Changed from 2.0
        rgb = matplotlib.colors.ColorConverter().to_rgb(ref)
    if max(rgb) < 1e-4:
        # All 0, black.
        rgb = (1.,) * len(rgb)
    else:
        rgb = tuple(v / max(rgb) for v in rgb)

    # Make a colormap.
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        'cm', [(0, 0, 0), rgb])

    # Linearly select the colors.
    colors = [cmap(x) for x in np.linspace(low, high, num)]

    return colors

