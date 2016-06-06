"""
 * Copyright (c) 2016. Mingyu Gao
 * All rights reserved.
 *
"""
import numpy as np
import matplotlib.ticker


# Inches per point.
INCHES_PER_PT = 1.0 / 72


# Golden ratio, 0.618...
_GOLDEN_RATIO = (np.sqrt(5) - 1) / 2.


def turn_off_box(axes):
    """ Turn off the top and right spines of the plot box of the axes.

    axes: axes of the box.
    """
    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)
    axes.xaxis.set_ticks_position('bottom')
    axes.yaxis.set_ticks_position('left')


def paper_plot(fontsize=9):
    """ Initialize the settings of the plot, including font, fontsize, etc..

    fontsize: fontsize for legends and labels.

    Ref:
    http://damon-is-a-geek.com/publication-ready-the-first-time-beautiful-reproducible-plots-with-matplotlib.html
    """
    matplotlib.rcParams['font.family'] = 'serif'
    matplotlib.rcParams['font.size'] = fontsize
    matplotlib.rcParams['legend.fontsize'] = fontsize
    matplotlib.rcParams['axes.labelsize'] = fontsize
    matplotlib.rcParams['xtick.labelsize'] = fontsize
    matplotlib.rcParams['ytick.labelsize'] = fontsize
    matplotlib.rcParams['lines.linewidth'] = 0.75
    matplotlib.rcParams['lines.markersize'] = 4
    #matplotlib.rcParams['font.serif'] = ['Times New Roman']
    #matplotlib.rcParams['text.usetex'] = True


def get_fig_dims(width_in_pt):
    """ Get the figure dimension in inches with golden ratio.

    width_in_pt: figure width in points.
    """
    width = width_in_pt * INCHES_PER_PT
    height = width * _GOLDEN_RATIO
    return [width, height]


def resize_ax_box(axes, wratio=1, hratio=1, to_right=False, to_bottom=False):
    """ Resize the axes box.

    axes: axes to be resized.
    wratio: width ratio, should be (0, 1].
    hratio: height ratio, should be (0, 1].
    to_right: if True, shrink left side. Otherwise shrink right side.
    to_bottom: if True, shrink top side. Otherwise shrink bottom side.
    """
    box = axes.get_position()
    assert wratio <= 1 and wratio > 0
    assert hratio <= 1 and hratio > 0
    x0 = box.x0 + box.width * (1 - wratio) if to_right else box.x0
    width = box.width * wratio
    y0 = box.y0 if to_bottom else box.y0 + box.height * (1 - hratio)
    height = box.height * hratio
    axes.set_position([x0, y0, width, height])


def set_axis_to_percent(axis):
    """ Make axis to display percentage ticker.

    axis: a single axis, such as ax.yaxis.
    """
    def cb_to_percent(value, position):
        """ Callback, arguments are value and tick position
        """
        s = str(int(100 * value))
        # The percent symbol needs escaping in latex
        if matplotlib.rcParams['text.usetex']:
            return s + r'$\%$'
        else:
            return s + '%'

    axis.set_major_formatter(matplotlib.ticker.FuncFormatter(cb_to_percent))


