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
import matplotlib
from matplotlib import pyplot as plt

from easypyplot import format as fmt  # avoid conflict with built-in.

from . import sin_plot, skip_if_without_tex
from . import image_comparison

@image_comparison(baseline_images=['format_turn_off_box'])
def test_turn_off_box():
    ''' format turn off box. '''
    fig = plt.figure()
    ax = fig.gca()

    fmt.turn_off_box(ax)

    sin_plot(ax)


@image_comparison(baseline_images=['format_turn_off_box_twinx'])
def test_turn_off_box_twinx():
    ''' format turn off box with twinx. '''
    fig = plt.figure()
    ax = fig.gca()
    ax2 = ax.twinx()

    fmt.turn_off_box(ax, twinx_axes=ax2)

    sin_plot(ax2)


@image_comparison(baseline_images=['format_paper_plot'])
def test_paper_plot():
    ''' format paper plot. '''
    # Must be before figure creation.
    fmt.paper_plot(font='default')

    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax, remove_text=False)
    sin_plot(ax, phi=0.5 * np.pi, fmt='--', remove_text=False)
    sin_plot(ax, phi=1 * np.pi, fmt='-.', remove_text=False)
    sin_plot(ax, phi=1.5 * np.pi, fmt=':', remove_text=False)

    x = np.linspace(0, 6, 13)
    y = x / -6
    ax.plot(x, y, 's')

    ax.scatter([1, 2, 3], [0, -0.5, 0.5])

    ax.set_xlabel('My x label')
    ax.set_ylabel('My y label')
    ax.set_xticks(np.linspace(0, 6, 7, endpoint=True))
    ax.set_yticks(np.linspace(-1, 1, 9, endpoint=True))
    ax.set_xlim([0, 6])
    ax.set_ylim([-1, 1])
    ax.yaxis.grid(True)
    ax.legend(['My data 1-1', 'My data 1-2', 'My data 1-3', 'My data 1-4',
               'My data 2', 'My points'])


@image_comparison(baseline_images=['format_paper_plot_mono'])
def test_paper_plot_mono():
    ''' format paper plot with monospace font. '''
    # Must be before figure creation.
    fmt.paper_plot(font=('monospace', 'DejaVu Sans Mono'))

    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax, remove_text=False)

    ax.set_xlabel('My x label')
    ax.set_ylabel('My y label')


@image_comparison(baseline_images=['format_paper_plot_mathtext'],
                  remove_text=False)
def test_paper_plot_mathtext():
    ''' format paper plot and use mathtext. '''
    # Must be before figure creation.
    fmt.paper_plot(font='default')

    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax)
    ax.set_yticks(np.linspace(-100, 100, 11, endpoint=True) / 100.)

    ax.set_yticklabels([r'$e^{' + '{}'.format(x) + r'}$' for x in range(11)])


@image_comparison(baseline_images=['format_resize_ax_box_w_r'])
def test_resize_ax_box_w_r():
    ''' format resize axes box, width to right. '''
    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax)

    fmt.resize_ax_box(ax, wratio=0.8, to_right=True)


@image_comparison(baseline_images=['format_resize_ax_box_w_l'])
def test_resize_ax_box_w_l():
    ''' format resize axes box, width to left. '''
    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax)

    fmt.resize_ax_box(ax, wratio=0.6, to_right=False)


@image_comparison(baseline_images=['format_resize_ax_box_h_b'])
def test_resize_ax_box_h_b():
    ''' format resize axes box, height to bottom. '''
    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax)

    fmt.resize_ax_box(ax, hratio=0.85, to_bottom=True)


@image_comparison(baseline_images=['format_resize_ax_box_h_t'])
def test_resize_ax_box_h_t():
    ''' format resize axes box, height to top. '''
    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax)

    fmt.resize_ax_box(ax, hratio=0.7, to_bottom=False)


@image_comparison(baseline_images=['format_resize_ax_box_both'])
def test_resize_ax_box_both():
    ''' format resize axes box, both width and height. '''
    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax)

    fmt.resize_ax_box(ax, wratio=0.6, hratio=0.8)


@image_comparison(baseline_images=['format_set_axis_to_percent'],
                  remove_text=False)
def test_set_axis_to_percent():
    ''' format set axis tick to percentage. '''
    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax)
    ax.set_yticks(np.linspace(-100, 100, 11, endpoint=True) / 100.)

    fmt.set_axis_to_percent(ax.yaxis)


@image_comparison(baseline_images=['format_set_axis_to_percent_pcs'],
                  remove_text=False)
def test_set_axis_to_percent_pcs():
    ''' format set axis tick to percentage with precision. '''
    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax)
    ax.set_yticks(np.linspace(-100, 100, 11, endpoint=True) / 100.)

    fmt.set_axis_to_percent(ax.yaxis, precision=2)


@image_comparison(baseline_images=['format_set_axis_to_percent_tex'],
                  extensions=['pdf'], remove_text=False)
def test_set_axis_to_percent_tex():
    ''' format set axis tick to percentage with Tex. '''
    skip_if_without_tex()
    # Must be before figure creation.
    matplotlib.rcParams['text.usetex'] = True

    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax)
    ax.set_yticks(np.linspace(-100, 100, 11, endpoint=True) / 100.)

    fmt.set_axis_to_percent(ax.yaxis)


@image_comparison(baseline_images=['format_set_axis_to_percent_pplot'],
                  remove_text=False)
def test_set_axis_to_percent_pplot():
    ''' format set axis tick to percentage with paper plot. '''
    fmt.paper_plot()

    fig = plt.figure()
    ax = fig.gca()

    sin_plot(ax)
    ax.set_yticks(np.linspace(-100, 100, 11, endpoint=True) / 100.)

    fmt.set_axis_to_percent(ax.yaxis)


@image_comparison(baseline_images=['format_set_group_xticklabels'],
                  remove_text=False)
def test_set_group_xticklabels():
    ''' format set group labels along x axis. '''
    fig = plt.figure()
    ax = fig.add_subplot(211)

    gnum = 4
    xnum = 12
    xs = list(range(xnum))
    y = 0.2

    ax.set_ylim([0, 1])
    ax.axhline(y, xmin=xs[0], xmax=xs[-1])

    ax.set_xticks(xs)

    grouplabels = ['g{}'.format(i) for i in range(gnum)]
    xvals = range((xnum // gnum - 1) // 2, xnum, xnum // gnum)
    fmt.set_group_xticklabels(ax, grouplabels, xvals, -y)


@image_comparison(baseline_images=['format_set_group_xticklabels'],
                  remove_text=False, save_suffix='_orig_xvals')
def test_set_group_xticklabels_orig_xvals():
    ''' format set group labels along x axis, with original xvals. '''
    # pylint: disable=invalid-name
    fig = plt.figure()
    ax = fig.add_subplot(211)

    gnum = 4
    xnum = 12
    xs = list(range(xnum))
    y = 0.2

    ax.set_ylim([0, 1])
    ax.axhline(y, xmin=xs[0], xmax=xs[-1])

    ax.set_xticks(xs)

    grouplabels = ['g{}'.format(i) for i in range(gnum)]
    fmt.set_group_xticklabels(ax, grouplabels, xs, -y)


class TestFormat(unittest.TestCase):
    ''' Tests for format module. '''

    def test_get_fig_dims(self):
        ''' get_fig_dims(). '''
        figsize = fmt.get_fig_dims(100)
        self.assertEqual(len(figsize), 2)
        self.assertAlmostEqual(figsize[0], 1.3889, places=4)
        self.assertAlmostEqual(figsize[1] / figsize[0], 0.618, places=3)

        figsize = fmt.get_fig_dims(250)
        self.assertEqual(len(figsize), 2)
        self.assertAlmostEqual(figsize[0], 3.4722, places=4)
        self.assertAlmostEqual(figsize[1] / figsize[0], 0.618, places=3)

    def test_paper_plot_invalid_font(self):
        ''' paper_plot invalid font. '''
        with self.assertRaisesRegexp(ValueError, r'\[format\] .*font.*'):
            fmt.paper_plot(font='DejaVu Serif')

    def test_set_group_xticklabels_invalid_xvals(self):
        ''' set_group_xticklabels invalid xvals. '''
        # pylint: disable=invalid-name
        fig = plt.figure()
        ax = fig.gca()

        with self.assertRaisesRegexp(ValueError, r'\[format\] .*xvals.*'):
            fmt.set_group_xticklabels(ax, ['a', 'b'], [0, 1, 2], -1)

