"""
 * Copyright (c) 2016. Mingyu Gao
 * All rights reserved.
 *
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

