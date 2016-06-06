"""
 * Copyright (c) 2016. Mingyu Gao
 * All rights reserved.
 *
"""
import matplotlib.backends.backend_pdf
from .format import paper_plot


def plot_setup(name, dims, fontsize=9):
    """ Setup a PDF page for plot.

    name: PDF file name. If not ending with .pdf, will automatically append.
    dims: dimension of the plot, should be an array of length two.
    fontsize: fontsize for legends and labels.
    """
    paper_plot(fontsize)
    if not name.endswith('.pdf'):
        name += '.pdf'
    pdfpage = matplotlib.backends.backend_pdf.PdfPages(name)
    fig = matplotlib.pyplot.figure(figsize=dims)
    return pdfpage, fig


def plot_teardown(pdfpage):
    """ Tear down a PDF page after plotting.

    pdfpage: PDF page.
    """
    pdfpage.savefig()
    pdfpage.close()


