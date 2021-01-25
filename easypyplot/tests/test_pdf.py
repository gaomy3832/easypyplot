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

import sys
import pytest

from easypyplot import pdf
from easypyplot import util

from . import sin_plot
from . import image_comparison

@image_comparison(baseline_images=['pdf_base'], extensions=['pdf'],
                  saved_as=['pdf_base'])
def test_base():
    ''' pdf base. '''
    pdfpage, fig = pdf.plot_setup('pdf_base', font='default')
    try:
        sin_plot(fig.gca())
    finally:
        pdf.plot_teardown(pdfpage)


@image_comparison(baseline_images=['pdf_name_suffix'], extensions=['pdf'],
                  saved_as=['pdf_name_suffix'])
def test_name_suffix():
    ''' pdf name suffix. '''
    pdfpage, fig = pdf.plot_setup('pdf_name_suffix.pdf', font='default')
    try:
        sin_plot(fig.gca())
    finally:
        pdf.plot_teardown(pdfpage)


@image_comparison(baseline_images=['pdf_figsize'], extensions=['pdf'],
                  saved_as=['pdf_figsize'])
def test_figsize():
    ''' pdf figsize. '''
    pdfpage, fig = pdf.plot_setup('pdf_figsize', figsize=(16, 12),
                                  font='default')
    try:
        sin_plot(fig.gca())
    finally:
        pdf.plot_teardown(pdfpage)


@image_comparison(baseline_images=['pdf_fontsize'], extensions=['pdf'],
                  saved_as=['pdf_fontsize'])
def test_fontsize():
    ''' pdf fontsize. '''
    pdfpage, fig = pdf.plot_setup('pdf_fontsize', fontsize=14, font='default')
    try:
        sin_plot(fig.gca(), remove_text=False)
        fig.gca().set_title('My title')
    finally:
        pdf.plot_teardown(pdfpage)


@pytest.mark.xfail(util.__mpl_version__[:2] >= (2, 0)
                   and util.__mpl_version__[:2] < (2, 3)
                   and sys.version_info >= (3,),
                   reason='Python 3 with 2.x fails with Times unicode minus. '
                          'https://github.com/matplotlib/matplotlib/issues/9139'
                  )
@image_comparison(baseline_images=['pdf_fontsize_times'], extensions=['pdf'],
                  saved_as=['pdf_fontsize_times'])
def test_fontsize_times():
    ''' pdf fontsize with Times font. '''
    pdfpage, fig = pdf.plot_setup('pdf_fontsize_times', fontsize=14)
    try:
        sin_plot(fig.gca(), remove_text=False)
        fig.gca().set_title('My title')
    finally:
        pdf.plot_teardown(pdfpage)


@image_comparison(baseline_images=['pdf_context'], extensions=['pdf'],
                  saved_as=['pdf_context'])
def test_context():
    ''' pdf context. '''
    with pdf.plot_open('pdf_context', figsize=(16, 12), fontsize=14,
                       font='default') as fig:
        sin_plot(fig.gca())

