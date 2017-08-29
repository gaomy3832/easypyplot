""" $lic$
Copyright (c) 2017, Mingyu Gao
All rights reserved.

This program is free software: you can redistribute it and/or modify it under
the terms of the Modified BSD-3 License as published by the Open Source
Initiative.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the BSD-3 License for more details.

You should have received a copy of the Modified BSD-3 License along with this
program. If not, see <https://opensource.org/licenses/BSD-3-Clause>.
"""

from contextlib import contextmanager
import matplotlib.backends.backend_pdf

from .format import paper_plot

def plot_setup(name, figsize=None, fontsize=9):
    """ Setup a PDF page for plot.

    name: PDF file name. If not ending with .pdf, will automatically append.
    figsize: dimension of the plot in inches, should be an array of length two.
    fontsize: fontsize for legends and labels.
    """
    paper_plot(fontsize)
    if not name.endswith('.pdf'):
        name += '.pdf'
    pdfpage = matplotlib.backends.backend_pdf.PdfPages(name)
    fig = matplotlib.pyplot.figure(figsize=figsize)
    return pdfpage, fig


def plot_teardown(pdfpage, fig=None):
    """ Tear down a PDF page after plotting.

    pdfpage: PDF page.
    fig: the figure to save.
    """
    pdfpage.savefig(fig)
    pdfpage.close()


@contextmanager
def plot_open(name, figsize=None, fontsize=9):
    """ Open a context of PDF page for plot, used for the `with` statement.

    name: PDF file name. If not ending with .pdf, will automatically append.
    figsize: dimension of the plot in inches, should be an array of length two.
    fontsize: fontsize for legends and labels.
    """
    pdfpage, fig = plot_setup(name, figsize=figsize, fontsize=fontsize)
    yield fig
    plot_teardown(pdfpage, fig)

