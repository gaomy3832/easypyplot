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
import matplotlib

from .color import COLOR_SET

def draw(axes,
         data, group_names=None, entry_names=None,
         breakdown=True,
         xticks=None, width=None, cluster_bar_shrink=None,
         colors=None, edgecolor='k', linewidth=0.5,
         hatchs=None, hatchcolor='k',
         legendloc='upper right', legendncol=1, log=False,
         xticklabelfontsize=None, xticklabelrotation='horizontal'):
    """ A super flexible bar chart drawing wrapper.

    axes: the axes instance to be drawn on.

    data: 2-dimension, grouped into groups, each of which has entries.
    group_names, entry_names: names of all groups/entries.

    breakdown: if True, draw each group as stacked bar; otherwise as clustered
        bars.

    xticks: the positions of the centers of stacked/clustered bars on x axis.
        xticks can be used to further cluster groups. Default to be
        range(num_groups).
    width: the width for one stacked bar (if breakdown) or the total width of
        one clustered bar. Default to be 0.8.
    cluster_bar_shrink: shrinks each individual bar in the clustered bar by the
        given factor to leave some space between bars in the same cluster. Only
        valid for clustered bars.

    colors: the colors in HEX format used for entries across all groups. Length
        should be equal to the number of entries.
    edgecolor: the color of the bar edges.
    linewidth: the width of the bar edges.

    hatchs: the hatch patterns for entries. Length should be equal to the
        number of entries.
    hatchcolor: the color of all hatches.

    legendloc: the location of the legend.
    legendncol: number of columns of the legend.

    log: whether the y-axis should be in log scale.

    xticklabelfontsize: the fontsize of the xtick labels.
    xticklabelrotation: the rotation control of the xtick labels.

    return: handlers associated with entries.
    """
    # pylint: disable=too-many-branches

    ############################################################################
    # data contains num_groups groups, each group has num_entries entries
    try:
        data = np.array(data, dtype=np.float64)
    except ValueError:
        raise ValueError('[barchart] data cannot be convert to an array. '
                         'Dimension mismatch?\n{}'.format(data))
    dim = data.shape
    if len(dim) != 2:
        raise ValueError('[barchart] data must be 2-dimension')
    num_groups = dim[0]
    num_entries = dim[1]

    if group_names is not None and len(group_names) != num_groups:
        raise ValueError('[barchart] group names must have {} elements'
                         .format(num_groups))

    if entry_names is not None and len(entry_names) != num_entries:
        raise ValueError('[barchart] entry names must have {} elements'
                         .format(num_entries))

    ############################################################################
    # Parse and adjust plot parameters
    if width is None:
        width = 0.8
    if not breakdown:
        width /= num_entries

    if breakdown:
        cluster_bar_shrink = 1
    else:
        if cluster_bar_shrink is None:
            cluster_bar_shrink = 1
    if cluster_bar_shrink > 1:
        raise ValueError('[barchart] cluster_bar_shrink must be no more than 1')

    if xticks is None:
        xticks = np.arange(num_groups)
    elif len(xticks) != num_groups:
        raise ValueError('[barchart] xticks size does not match data')
    else:
        xticks = np.array(xticks)

    if colors is None:
        if num_entries > len(COLOR_SET):
            raise ValueError('[barchart] Not enough default colors')
        colors = COLOR_SET[:num_entries]
    if len(colors) < num_entries:
        raise ValueError('[barchart] Not enough colors')

    if edgecolor is None:
        edgecolor = 'none'

    if hatchs is not None:
        if len(hatchs) != num_entries:
            raise ValueError('[barchart] Given hatchs do not match the data')
    else:
        hatchs = [None for eid in range(num_entries)]


    ############################################################################
    # Coordinates of bars

    # ybottoms is the bottom y coordinates of each bar
    ybottoms = np.zeros(num_groups)
    # xlefts are the left x coordinates of each bar
    if breakdown:
        xlefts = xticks - width/2.0
    else:
        xlefts = xticks - width * num_entries / 2.0 \
                + (1 - cluster_bar_shrink) * width / 2.0

    ############################################################################
    # Each time draw each entry for all groups
    hdls = []
    for eid in range(num_entries):
        d = data[:, eid]

        c = colors[eid]

        p = axes.bar(xlefts, d, width * cluster_bar_shrink,
                     bottom=ybottoms, align='edge',
                     color=c, log=log,
                     edgecolor=edgecolor, linewidth=linewidth)

        if hatchs is not None:
            for (x, y, d1) in zip(xlefts, ybottoms, d):
                polygon = [[x, y], [x, y+d1],
                           [x+width*cluster_bar_shrink, y+d1],
                           [x+width*cluster_bar_shrink, y]]
                axes.add_patch(matplotlib.patches.Polygon( \
                               polygon,
                               hatch=hatchs[eid], color=hatchcolor,
                               linewidth=0, fill=False))

        if breakdown:
            ybottoms += d
        else:
            xlefts += width

        hdls.append(p)

    ############################################################################
    # Axes options

    # Remove xticks
    axes.xaxis.set_ticks_position('none')

    if group_names is not None:
        axes.set_xticks(xticks)
        axes.set_xticklabels(group_names, \
                fontsize=xticklabelfontsize, rotation=xticklabelrotation)

    if entry_names is not None:
        axes.legend(hdls, entry_names, loc=legendloc, ncol=legendncol)

    axes.set_xlim([xticks[0]-1, xticks[-1]+1])

    return hdls

