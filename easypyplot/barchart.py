"""
 * Copyright (c) 2016. Mingyu Gao
 * All rights reserved.
 *
"""
import numpy as np
import matplotlib
from .color import COLOR_SET
from .util import matplotlib_version_tuple


def draw(axes,
         data, group_names=None, entry_names=None,
         breakdown=True,
         xticks=None, width=None, cluster_bar_shrink=None,
         colors=None, edgecolor='k', linewidth=0.5,
         hatchs=None, hatchcolor='k',
         legendloc='upper right', log=False,
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

    log: whether the y-axis should be in log scale.

    xticklabelfontsize: the fontsize of the xtick labels.
    xticklabelrotation: the rotation control of the xtick labels.

    return: handlers associated with entries.
    """

    # pylint: disable=too-many-branches

    ############################################################################
    # data contains num_groups groups, each group has num_entries entries
    data = np.array(data)
    dim = data.shape
    if len(dim) != 2:
        raise ValueError('[barchart] data must be 2-dimension')
    num_groups = dim[0]
    num_entries = dim[1]

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

    # In matplotlib 2.0.0, xleft argument in bar() function call actually mean
    # the center of the bars! How crazy!
    bar_xleft_arg = np.copy(xlefts)  # deep copy
    if matplotlib_version_tuple() >= (2, 0, 0):
        bar_xleft_arg += cluster_bar_shrink * width / 2.0

    ############################################################################
    # Each time draw each entry for all groups
    hdls = []
    for eid in range(num_entries):
        d = data[:, eid]

        c = colors[eid]

        p = axes.bar(bar_xleft_arg, d, width*cluster_bar_shrink, bottom=ybottoms,
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
            bar_xleft_arg += width

        hdls.append(p)

    ############################################################################
    # Axes options

    # Remove xticks
    # http://stackoverflow.com/questions/12998430/remove-xticks-in-a-matplot-lib-plot
    axes.tick_params( \
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom='off',      # ticks along the bottom edge are off
            top='off')         # ticks along the top edge are off

    if group_names is not None:
        axes.set_xticks(xticks)
        axes.set_xticklabels(group_names, \
                fontsize=xticklabelfontsize, rotation=xticklabelrotation)

    if entry_names is not None:
        axes.legend(hdls, entry_names, legendloc)

    axes.set_xlim([xticks[0]-1, xticks[-1]+1])

    return hdls


