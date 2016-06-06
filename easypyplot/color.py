"""
 * Copyright (c) 2016. Mingyu Gao
 * All rights reserved.
 *
"""
import numpy as np
import matplotlib.colors


# Colors from http://www.colorbrewer2.org/, 8-class, qualitative, Accent
COLOR_SET = ['#386cb0', '#7fc97f', '#f0027f', '#beaed4', \
             '#bf5b17', '#fdc086', '#666666', '#ffff99']

def color_scale(refhex, num, low=0.4, high=0.9):
    """ Get a color scale from shallow to dark.

    refhex: referenced color in HEX format.
    num: number of colors in the scale.
    low: low brightness.
    high: high brightness.
    """
    refc = matplotlib.colors.hex2color(refhex)
    maxrefc = max(refc)
    refc = [x / maxrefc for x in refc]
    colors = [matplotlib.colors.rgb2hex([x * s for x in refc])
              for s in np.linspace(low, high, num)]
    return colors

