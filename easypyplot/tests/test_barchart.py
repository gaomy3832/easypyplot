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
from matplotlib import pyplot as plt

from easypyplot import barchart

from . import image_comparison
from . import setup, teardown

def _data():
    return [[1, 3], [2, 4], [3.5, 1.5]]


@image_comparison(baseline_images=['barchart_base'],
                  remove_text=False)
def test_barchart_base():
    ''' bar chart base. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data())


@image_comparison(baseline_images=['barchart_nparray'],
                  remove_text=False)
def test_barchart_nparray():
    ''' bar chart with data np.array. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, np.array(_data()))


@image_comparison(baseline_images=['barchart_hdls'],
                  remove_text=False)
def test_barchart_hdls():
    ''' bar chart handlers. '''
    fig = plt.figure()
    ax = fig.gca()

    hdls = barchart.draw(ax, _data())

    ax.legend(hdls, ['E1', 'E2'])


@image_comparison(baseline_images=['barchart_group_names'],
                  remove_text=False)
def test_barchart_group_names():
    ''' bar chart group names. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), group_names=['Aa', 'Bb', '$Cc$'])


@image_comparison(baseline_images=['barchart_entry_names'],
                  remove_text=False)
def test_barchart_entry_names():
    ''' bar chart entry names. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), entry_names=['x', '$x^2$'])


@image_comparison(baseline_images=['barchart_nobkdn'],
                  remove_text=False)
def test_barchart_nobkdn():
    ''' bar chart without breakdown. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), breakdown=False)


@image_comparison(baseline_images=['barchart_width'],
                  remove_text=False)
def test_barchart_width():
    ''' bar chart width. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), width=0.5)


@image_comparison(baseline_images=['barchart_width_nobkdn'],
                  remove_text=False)
def test_barchart_width_nobkdn():
    ''' bar chart width without breakdown. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), width=0.5, breakdown=False)


@image_comparison(baseline_images=['barchart_cbshrk'],
                  remove_text=False)
def test_barchart_cbshrk():
    ''' bar chart cluster_bar_shrink. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), cluster_bar_shrink=0.5)


@image_comparison(baseline_images=['barchart_cbshrk_nobkdn'],
                  remove_text=False)
def test_barchart_cbshrk_nobkdn():
    ''' bar chart cluster_bar_shrink without breakdown. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), cluster_bar_shrink=0.5, breakdown=False)


@image_comparison(baseline_images=['barchart_xticks'],
                  remove_text=False)
def test_barchart_xticks():
    ''' bar chart xticks. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), xticks=[0, 2, 3])


@image_comparison(baseline_images=['barchart_xticks_nobkdn'],
                  remove_text=False)
def test_barchart_xticks_nobkdn():
    ''' bar chart xticks without breakdown. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), xticks=[0, 2, 3], breakdown=False)


@image_comparison(baseline_images=['barchart_colors'])
def test_barchart_colors():
    ''' bar chart colors. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), colors=['r', 'b'])


@image_comparison(baseline_images=['barchart_colors_nobkdn'])
def test_barchart_colors_nobkdn():
    ''' bar chart colors without breakdown. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), colors=['r', 'b'], breakdown=False)


@image_comparison(baseline_images=['barchart_edgecolor'])
def test_barchart_edgecolor():
    ''' bar chart edgecolor. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), edgecolor='y')


@image_comparison(baseline_images=['barchart_edgecolor_none'])
def test_barchart_edgecolor_none():
    ''' bar chart edgecolor. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), edgecolor=None)


@image_comparison(baseline_images=['barchart_hatchs'])
def test_barchart_hatchs():
    ''' bar chart hatchs. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), hatchs=['/', '//'])


@image_comparison(baseline_images=['barchart_linewidth'])
def test_barchart_linewidth():
    ''' bar chart linewidth. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), linewidth=5.0)


@image_comparison(baseline_images=['barchart_hatchcolor'])
def test_barchart_hatchcolor():
    ''' bar chart hatchcolor. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), hatchcolor='r', hatchs=['/', '//'])


@image_comparison(baseline_images=['barchart_legend_opts'],
                  remove_text=False)
def test_barchart_legend_opts():
    ''' bar chart legend options. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), legendloc='lower center', legendncol=2,
                  entry_names=['X', 'Y'])


@image_comparison(baseline_images=['barchart_yaxis_log'],
                  remove_text=False)
def test_barchart_yaxis_log():
    ''' bar chart yaxis log. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), log=True)


@image_comparison(baseline_images=['barchart_xticklabelfontsize'],
                  remove_text=False)
def test_barchart_xtlfontsize():
    ''' bar chart xticklabel fontsize. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), xticklabelfontsize=20,
                  group_names=['a', 'b', 'c'])


@image_comparison(baseline_images=['barchart_xticklabelrotation'],
                  remove_text=False)
def test_barchart_xtlrotation():
    ''' bar chart xticklabelrotation. '''
    fig = plt.figure()
    ax = fig.gca()

    barchart.draw(ax, _data(), xticklabelrotation=60,
                  group_names=['a', 'b', 'c'])


class TestBarchart(unittest.TestCase):
    ''' Tests for barchart module. '''

    def setUp(self):
        self.origs = setup()
        self.axes = plt.figure().gca()

    def tearDown(self):
        teardown(self.origs)

    def test_return_num_handlers(self):
        ''' Returned number of handlers. '''
        hdls = barchart.draw(self.axes, _data())
        self.assertEqual(len(hdls), len(_data()[0]))

    def test_invalid_data(self):
        ''' Invalid data. '''
        with self.assertRaisesRegexp(ValueError, r'\[barchart\] .*array.*'):
            barchart.draw(self.axes, [[1, 2], [1, 2, 3]])

    def test_invalid_data_dim(self):
        ''' Invalid data dimension. '''
        for d in [0, 1, 3, 4]:
            with self.assertRaisesRegexp(ValueError, r'\[barchart\] .*dim.*'):
                barchart.draw(self.axes, np.zeros([3] * d))

    def test_invalid_group_names(self):
        ''' Invalid group names. '''
        with self.assertRaisesRegexp(ValueError,
                                     r'\[barchart\] .*group names.*'):
            barchart.draw(self.axes, _data(), group_names=['a', 'b', 'c', 'd'])

    def test_invalid_entry_names(self):
        ''' Invalid entry names. '''
        with self.assertRaisesRegexp(ValueError,
                                     r'\[barchart\] .*entry names.*'):
            barchart.draw(self.axes, _data(), entry_names=['x', 'y', 'z'])

    def test_invalid_cluster_bar_shrink(self):
        ''' Invalid cluster_bar_shrink. '''
        with self.assertRaisesRegexp(ValueError,
                                     r'\[barchart\] .*cluster_bar_shrink.*'):
            barchart.draw(self.axes, _data(), breakdown=False,
                          cluster_bar_shrink=1.2)

    def test_invalid_xticks(self):
        ''' Invalid xticks. '''
        with self.assertRaisesRegexp(ValueError, r'\[barchart\] .*xticks.*'):
            barchart.draw(self.axes, _data(), xticks=['x'])

    def test_not_enough_def_colors(self):
        ''' Not enough default colors. '''
        with self.assertRaisesRegexp(ValueError,
                                     r'\[barchart\] .*default colors.*'):
            barchart.draw(self.axes, [[1] * 100])

    def test_invalid_colors(self):
        ''' Invalid colors. '''
        with self.assertRaisesRegexp(ValueError, r'\[barchart\] .*colors.*'):
            barchart.draw(self.axes, _data(), colors=['k'])

    def test_invalid_hatchs(self):
        ''' Invalid hatchs. '''
        with self.assertRaisesRegexp(ValueError, r'\[barchart\] .*hatchs.*'):
            barchart.draw(self.axes, _data(), hatchs=['/', '//', 'xx'])

