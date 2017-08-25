"""
 * Copyright (c) 2016. Mingyu Gao
 * All rights reserved.
 *
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


def plot_teardown(pdfpage):
    """ Tear down a PDF page after plotting.

    pdfpage: PDF page.
    """
    pdfpage.savefig()
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
    plot_teardown(pdfpage)

