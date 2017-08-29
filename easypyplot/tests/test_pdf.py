"""
 * Copyright (c) 2016. Mingyu Gao
 * All rights reserved.
 *
"""
from easypyplot import pdf

from . import sin_plot
from . import image_comparison

@image_comparison(baseline_images=['pdf_base'], extensions=['pdf'],
                  saved_as=['pdf_base'])
def test_base():
    ''' pdf base. '''
    pdfpage, fig = pdf.plot_setup('pdf_base')
    try:
        sin_plot(fig.gca())
    finally:
        pdf.plot_teardown(pdfpage)


@image_comparison(baseline_images=['pdf_name_suffix'], extensions=['pdf'],
                  saved_as=['pdf_name_suffix'])
def test_name_suffix():
    ''' pdf name suffix. '''
    pdfpage, fig = pdf.plot_setup('pdf_name_suffix.pdf')
    try:
        sin_plot(fig.gca())
    finally:
        pdf.plot_teardown(pdfpage)


@image_comparison(baseline_images=['pdf_figsize'], extensions=['pdf'],
                  saved_as=['pdf_figsize'])
def test_figsize():
    ''' pdf figsize. '''
    pdfpage, fig = pdf.plot_setup('pdf_figsize', figsize=(16, 12))
    try:
        sin_plot(fig.gca())
    finally:
        pdf.plot_teardown(pdfpage)


@image_comparison(baseline_images=['pdf_fontsize'], extensions=['pdf'],
                  saved_as=['pdf_fontsize'])
def test_fontsize():
    ''' pdf fontsize. '''
    pdfpage, fig = pdf.plot_setup('pdf_fontsize', fontsize=14)
    try:
        sin_plot(fig.gca(), remove_text=False)
        fig.gca().set_title('My title')
    finally:
        pdf.plot_teardown(pdfpage)


@image_comparison(baseline_images=['pdf_context'], extensions=['pdf'],
                  saved_as=['pdf_context'])
def test_context():
    ''' pdf context. '''
    with pdf.plot_open('pdf_context', figsize=(16, 12), fontsize=14) as fig:
        sin_plot(fig.gca())

