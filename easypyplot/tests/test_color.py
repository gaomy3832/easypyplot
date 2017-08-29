"""
 * Copyright (c) 2016. Mingyu Gao
 * All rights reserved.
 *
"""
import numpy as np
from matplotlib import pyplot as plt

from easypyplot import color

from . import image_comparison

@image_comparison(baseline_images=['color_set'])
def test_color_set():
    ''' color set. '''
    fig = plt.figure()
    ax = fig.gca()

    x = np.linspace(0, 2 * np.pi, 500)
    yy = [np.sin(x + phi) for phi
          in np.linspace(0, 2 * np.pi, len(color.COLOR_SET), endpoint=False)]

    for y, c in zip(yy, color.COLOR_SET):
        ax.plot(x, y, color=c)


@image_comparison(baseline_images=['color_scale'])
def test_color_scale():
    ''' color scale. '''
    fig = plt.figure()
    ax = fig.gca()
    ax.set_axis_off()

    cnt = 5

    for idx, base_color in enumerate(color.COLOR_SET + ['k', (0, 0, 1.)]):
        colors = color.color_scale(base_color, cnt)

        for jdx, c in enumerate(colors):
            ax.plot([idx], [jdx], marker='o', markersize=jdx * 5,
                    color=c, markeredgecolor='none')

