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

import os
import shutil
import locale
import numpy as np
import matplotlib.ticker
from cycler import cycler

from .color import COLOR_SET
from .util import __mpl_version__

# Inches per point.
INCHES_PER_PT = 1.0 / 72

# Golden ratio, 0.618...
_GOLDEN_RATIO = (np.sqrt(5) - 1) / 2.

def turn_off_box(axes, twinx_axes=None):
    """ Turn off the top and right spines of the plot box of the axes.

    axes: axes of the box.
    twinx_axes: twinx axes.
    """
    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)
    axes.xaxis.set_ticks_position('bottom')
    axes.yaxis.set_ticks_position('left')
    if twinx_axes is not None:
        twinx_axes.spines['top'].set_visible(False)
        twinx_axes.spines['left'].set_visible(False)
        twinx_axes.xaxis.set_ticks_position('bottom')
        twinx_axes.yaxis.set_ticks_position('right')


def paper_plot(fontsize=9, font='paper'):
    """ Initialize the settings of the plot, including font, fontsize, etc..
    Also refer to the changes in
    https://matplotlib.org/users/dflt_style_changes.html

    fontsize: fontsize for legends and labels.
    font: font for legends and labels, 'paper' uses Times New Roman, 'default'
    uses default, a tuple of (family, font, ...) customizes font.
    """
    # Set locale for unicode signs (e.g., minus sign).
    try:
        locale.setlocale(locale.LC_ALL, 'C.UTF-8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        except locale.Error:
            pass

    # Clear font cache (in case of switching host machines).
    # On Mac OS, cache directory and config directory is the same, avoid remove
    # the rc file.
    for e in os.listdir(matplotlib.get_cachedir()):
        if str(e) != 'matplotlibrc':
            fe = os.path.join(matplotlib.get_cachedir(), e)
            try:
                os.remove(fe)
            except OSError:
                shutil.rmtree(fe, ignore_errors=True)

    if font == 'paper':
        matplotlib.rcParams['font.family'] = 'serif'
        matplotlib.rcParams['font.serif'] = ['Times New Roman']
        matplotlib.rcParams['mathtext.fontset'] = 'stix'  # to blend well with Times
        matplotlib.rcParams['mathtext.rm'] = 'serif'
    elif font == 'default':
        pass
    else:
        if not isinstance(font, (tuple, list)) or len(font) < 2:
            raise ValueError('[format] font must be a tuple of (family, font)')
        matplotlib.rcParams['font.family'] = font[0]
        matplotlib.rcParams['font.{}'.format(font[0])] = list(font[1:])
        matplotlib.rcParams['mathtext.rm'] = font[0]

    matplotlib.rcParams['font.size'] = fontsize

    # Use TrueType fonts.
    matplotlib.rcParams['ps.fonttype'] = 42
    matplotlib.rcParams['pdf.fonttype'] = 42

    matplotlib.rcParams['legend.loc'] = 'upper right'
    matplotlib.rcParams['legend.fontsize'] = fontsize
    matplotlib.rcParams['legend.fancybox'] = False
    matplotlib.rcParams['legend.shadow'] = False
    matplotlib.rcParams['legend.numpoints'] = 2
    matplotlib.rcParams['legend.scatterpoints'] = 3
    matplotlib.rcParams['legend.borderpad'] = 0.4
    try:
        matplotlib.rcParams['legend.facecolor'] = 'inherit'
        matplotlib.rcParams['legend.edgecolor'] = 'inherit'
    except KeyError:
        assert __mpl_version__ < (2, 0)  # Changed from 2.0
    try:
        matplotlib.rcParams['legend.framealpha'] = 1.0
    except KeyError:
        assert __mpl_version__ < (1, 5)  # Changed from 1.5
    matplotlib.rcParams['axes.linewidth'] = 1.0
    matplotlib.rcParams['axes.facecolor'] = 'w'
    matplotlib.rcParams['axes.edgecolor'] = 'k'
    matplotlib.rcParams['axes.labelsize'] = fontsize
    matplotlib.rcParams['axes.axisbelow'] = True
    try:
        matplotlib.rcParams['axes.prop_cycle'] = cycler('color', COLOR_SET)
    except KeyError:
        assert __mpl_version__ < (1, 5)  # Changed from 1.5
        matplotlib.rcParams['axes.color_cycle'] = COLOR_SET
    matplotlib.rcParams['xtick.labelsize'] = fontsize
    matplotlib.rcParams['ytick.labelsize'] = fontsize
    matplotlib.rcParams['grid.linestyle'] = ':'
    matplotlib.rcParams['grid.linewidth'] = 0.5
    matplotlib.rcParams['grid.alpha'] = 1.0
    matplotlib.rcParams['grid.color'] = 'k'
    matplotlib.rcParams['lines.linewidth'] = 1.0
    try:
        matplotlib.rcParams['lines.color'] = 'C0'
    except ValueError:
        assert __mpl_version__ < (2, 0)  # Changed from 2.0
    matplotlib.rcParams['lines.markeredgewidth'] = 0.5
    matplotlib.rcParams['lines.markersize'] = 4
    try:
        matplotlib.rcParams['lines.dashed_pattern'] = [4, 4]
        matplotlib.rcParams['lines.dashdot_pattern'] = [4, 2, 1, 2]
        matplotlib.rcParams['lines.dotted_pattern'] = [1, 3]
    except KeyError:
        assert __mpl_version__ < (2, 0)  # Changed from 2.0
    matplotlib.rcParams['patch.linewidth'] = 0.5
    try:
        matplotlib.rcParams['patch.facecolor'] = 'C0'
        matplotlib.rcParams['patch.force_edgecolor'] = True
    except ValueError:
        assert __mpl_version__ < (2, 0)  # Changed from 2.0
    matplotlib.rcParams['patch.edgecolor'] = 'k'
    try:
        matplotlib.rcParams['hatch.linewidth'] = 0.5
        matplotlib.rcParams['hatch.color'] = 'k'
    except KeyError:
        assert __mpl_version__ < (2, 0)  # Changed from 2.0
    try:
        matplotlib.rcParams['errorbar.capsize'] = 3
    except KeyError:
        assert __mpl_version__ < (1, 5)  # Changed from 1.5
    matplotlib.rcParams['xtick.direction'] = 'out'
    matplotlib.rcParams['ytick.direction'] = 'out'
    matplotlib.rcParams['xtick.major.width'] = 0.8
    matplotlib.rcParams['xtick.minor.width'] = 0.6
    matplotlib.rcParams['ytick.major.width'] = 0.8
    matplotlib.rcParams['ytick.minor.width'] = 0.6
    try:
        matplotlib.rcParams['xtick.top'] = False
        matplotlib.rcParams['ytick.right'] = False
    except KeyError:
        assert __mpl_version__ < (2, 0)  # Changed from 2.0


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


def set_axis_to_percent(axis, precision=0):
    """ Make axis to display percentage ticker.

    axis: a single axis, such as ax.yaxis.
    precision: a number indicating how many digits should be displayed after
    the decimal point, as in string format for f/F or g/G.
    """
    def cb_to_percent(value, position):
        """ Callback, arguments are value and tick position
        """
        s = ('{' + ':.{}f'.format(precision) + '}').format(value * 100)
        s = s.format(value * 100)
        # Use Tex for better minus sign. Tex is directly supported in
        # matplotlib even without Tex installed. See
        # https://matplotlib.org/users/mathtext.html
        return r'${}\%$'.format(s)

    axis.set_major_formatter(matplotlib.ticker.FuncFormatter(cb_to_percent))


def set_group_xticklabels(axes, grouplabels, xvals, yval,
                          horizontalalignment='center', verticalalignment='center',
                          **kwargs):
    """ Set group labels along x axis.

    axes: axes to be added with group labels.
    grouplabels: group labels to be added.
    xvals: list of x positions to add group labels. It could have the same length
        as grouplabels (in which case it is directly used as the positions), or
        a multiple (in which case the positions are inferred from it).
    yval: y position to add group labels.
    horizontalalignment: horizontal alignment, e.g., 'center', 'left'.
    verticalalignment: vertical alignment, e.g., 'center', 'top', 'bottom', 'baseline'.
    kwargs: additional kw arguments passed to axes.text().
    """
    gnum = len(grouplabels)
    xnum = len(xvals)
    if xnum == 0 or xnum % gnum != 0:
        raise ValueError('[format] set_group_xticklabels: '
                         'xvals length must be a multiple of grouplabels length. '
                         '({} vs. {})'
                         .format(xnum, gnum))

    # Infer positions for group labels.
    gsize = xnum // gnum
    gvals = []
    for g in range(gnum):
        gxs = xvals[g * gsize : (g + 1) * gsize]
        # Use the center of the first and last positions.
        gval = (gxs[0] + gxs[-1]) / 2.
        gvals.append(gval)

    for gval, label in zip(gvals, grouplabels):
        axes.text(gval, yval, label, ha=horizontalalignment, va=verticalalignment, **kwargs)

