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

