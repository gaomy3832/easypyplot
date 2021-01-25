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

from collections import OrderedDict
import functools
import os
import shutil
import unittest
import warnings

import numpy as np
import matplotlib
import matplotlib.font_manager as mlpfm
import matplotlib.pyplot as plt
import matplotlib.testing
import matplotlib.testing.compare as mplcmp
import matplotlib.ticker
import matplotlib.units
from matplotlib.testing.decorators import _image_directories
import pytest

import easypyplot.util

def remove_ticks_and_titles(figure):
    ''' Remove ticks and titles from figure. '''
    figure.suptitle('')
    null_formatter = matplotlib.ticker.NullFormatter()
    for ax in figure.get_axes():
        ax.set_title('')
        ax.xaxis.set_major_formatter(null_formatter)
        ax.xaxis.set_minor_formatter(null_formatter)
        ax.yaxis.set_major_formatter(null_formatter)
        ax.yaxis.set_minor_formatter(null_formatter)
        try:
            ax.zaxis.set_major_formatter(null_formatter)
            ax.zaxis.set_minor_formatter(null_formatter)
        except AttributeError:
            pass


def skip_if_without_fonts(fonts):
    ''' Skip the test if the system does not have the given fonts. '''
    __tracebackhide__ = True  # pylint: disable=unused-variable
    for font in fonts:
        # Use unicode string as font name.
        try:
            name = unicode(font)
        except NameError:
            name = font
        fp = matplotlib.font_manager.FontProperties(
            fname=matplotlib.font_manager.findfont(name))
        if fp.get_name() == name:
            # Find a font.
            return
    # No font found.
    raise unittest.SkipTest('Skip because fonts {} is not in this system.'
                            .format(fonts))


def skip_if_without_tex():
    ''' Skip the test if the system does not have TeX. '''
    __tracebackhide__ = True  # pylint: disable=unused-variable
    with warnings.catch_warnings():
        warnings.filterwarnings('error')
        try:
            if matplotlib.checkdep_usetex(True):
                return
        except UserWarning as e:
            if 'Agg' in str(e):
                # Filter the warning about using Tex with Agg backend.
                return
    raise unittest.SkipTest('Skip because Tex is not in this system.')


def sin_plot(axes, phi=0, fmt='', remove_text=True):
    ''' Plot a sin function in the axes. '''
    x = np.linspace(0, 2 * np.pi, 500)
    y = np.sin(x + phi)
    if fmt:
        axes.plot(x, y, fmt)
    else:
        axes.plot(x, y)
    if remove_text:
        remove_ticks_and_titles(axes.get_figure())
    else:
        families = matplotlib.rcParams['font.family']
        try:
            if isinstance(families, basestring):
                families = [families]
        except NameError:
            if isinstance(families, str):
                families = [families]
        fonts = sum([matplotlib.rcParams['font.{}'.format(f)]
                     for f in families], [])
        skip_if_without_fonts(fonts)


def setup():
    ''' Set up. '''
    plt.close('all')
    original_units_registry = matplotlib.units.registry.copy()
    original_settings = matplotlib.rcParams.copy()
    ver = easypyplot.util.matplotlib_version_tuple()
    # Setup routine introduced from 1.5.
    if ver >= (1, 5):
        matplotlib.testing.setup()
    # Style name has changed over matplotlib versions.
    # See changes from <matplotlib repo>/lib/matplotlib/testing/conftest.py:mpl_test_settings()
    if ver >= (3, 2):
        matplotlib.style.use(['classic', '_classic_test_patch'])
    elif ver >= (2, 0):
        matplotlib.style.use('_classic_test')
    elif ver >= (1, 5):
        matplotlib.style.use('classic')
    # Times bold bug.
    # https://stackoverflow.com/questions/33955900
    # https://github.com/matplotlib/matplotlib/issues/5574
    #
    # The proposed solution simply removes `'roman'` from `weight_dict`, which
    # may cause `KeyError` when `weight_dict['roman']` is used in other places.
    #
    # Instead we order `'roman'` after `'bold'`, so when matching weights,
    # "Times New Roman Bold" will first match `'bold'` and get its weight.
    #
    # Also we need to update the shortcut module method `findfont`. It may
    # already be imported in other modules, so instead of update its value, we
    # also need to update the font lists of the previous font manager, so that
    # those already imported can also use the new font lists.
    if ver >= (2, 0):
        # Order `'bold'` before `'roman'` in the weight list.
        roman_weight = mlpfm.weight_dict.pop('roman', None)
        mlpfm.weight_dict = OrderedDict(mlpfm.weight_dict)
        if roman_weight is not None:
            mlpfm.weight_dict['roman'] = roman_weight
        # Rebuild font manager and update existing font lists.
        fm = mlpfm.fontManager
        mlpfm._rebuild()  # pylint: disable=protected-access
        mlpfm.findfont = mlpfm.fontManager.findfont
        fm.ttflist = mlpfm.fontManager.ttflist
        fm.afmlist = mlpfm.fontManager.afmlist
    return original_units_registry, original_settings


def teardown(origs):
    ''' Tear down. '''
    plt.close('all')
    original_units_registry, original_settings = origs
    matplotlib.rcParams.clear()
    matplotlib.rcParams.update(original_settings)
    matplotlib.units.registry.clear()
    matplotlib.units.registry.update(original_units_registry)
    warnings.resetwarnings()


class _ImageComparisonBase(unittest.TestCase):
    '''
    Base TestCase class used to replace original test function.

    We use a different class for each individual test function, and use
    different tests to compare different image extensions. Thus, the setup and
    teardown methods are class-level fixtures, and the original test function
    to plot the figure is also executed in this class-level setup method (after
    derived).
    '''

    @classmethod
    def setUpClass(cls):
        cls.origs = setup()
        cls.baseline_dir, cls.result_dir = cls._image_directories()

    @classmethod
    def tearDownClass(cls):
        teardown(cls.origs)

    @staticmethod
    def mark_extension(extension):
        ''' Mark whether extension is supported. '''
        __tracebackhide__ = True  # pylint: disable=unused-variable

        if extension not in mplcmp.comparable_formats():
            raise unittest.SkipTest('Cannot compare {} files in this '
                                    'system'.format(extension))

    def compare(self, baseline_images, actual_suffix, extension, tol):
        ''' Compare actual images with baseline images. '''
        __tracebackhide__ = True  # pylint: disable=unused-variable

        cls = self.__class__

        for baseline in baseline_images:
            actual_fname = os.path.join(
                cls.result_dir, baseline + actual_suffix + '.' + extension)
            self.assertTrue(os.path.exists(actual_fname),
                            'Image does not exist: {}'.format(actual_fname))

            expected_fname = self._copy_baseline(baseline, extension)
            self.assertTrue(os.path.exists(expected_fname),
                            'Image does not exist: {}'.format(expected_fname))

            err = mplcmp.compare_images(expected_fname, actual_fname, tol)
            self.assertFalse(err, 'Images are not close\n{}'.format(err))

    @classmethod
    def _image_directories(cls):
        raise NotImplementedError('{}: _image_directories'
                                  .format(cls.__name__))

    def _copy_baseline(self, baseline, extension):
        ''' Copy baseline image with given extension to result directory. '''
        __tracebackhide__ = True  # pylint: disable=unused-variable

        cls = self.__class__

        base_ext = baseline + '.' + extension

        # Original baseline file.
        baseline_fname = os.path.join(cls.baseline_dir, base_ext)
        if extension == 'eps' and not os.path.exists(baseline_fname):
            baseline_fname = baseline_fname[:len('eps')] + 'pdf'

        # Copied expected file.
        expected_fname = mplcmp.make_test_filename(os.path.join(
            cls.result_dir, os.path.basename(baseline_fname)), 'expected')

        self.assertTrue(os.path.exists(baseline_fname),
                        'Do not have baseline image {0} '
                        'because this file does not exist: {1}'
                        .format(expected_fname, baseline_fname))
        shutil.copyfile(baseline_fname, expected_fname)
        return expected_fname


def image_comparison(baseline_images, extensions=None, tol=0,
                     remove_text=True, savefig_kwargs=None,
                     saved_as=None, save_suffix=''):
    '''
    Compare images generated by the test with those specified in
    `baseline_images`.

    Derived from matplotlib, lib/matplotlib/testing/decorators.py.

    Add `saved_as` option, which means that the test function has already saved
    the images to the locations, if not empty.

    Add `save_suffix` option, which is added to the baseline name before the
    extension to be used as the actual file name, so that multiple tests can
    share the same baseline image and still be stored as different files.
    '''
    __tracebackhide__ = True  # pylint: disable=unused-variable

    if not extensions:
        extensions = ['pdf', 'png', 'svg']

    if not savefig_kwargs:
        savefig_kwargs = {}

    if saved_as and len(baseline_images) != len(saved_as):
        raise ValueError('image_comparison: `saved_as` should have the same '
                         'length as `baseline_images` if not empty.')

    def decorator(func):
        ''' Decorator. '''
        __tracebackhide__ = True  # pylint: disable=unused-variable

        class ImageComparisonTest(_ImageComparisonBase):
            ''' TestCase class to compare image. '''

            @classmethod
            def _image_directories(cls):
                return _image_directories(func)

            @classmethod
            def setUpClass(cls):
                super(ImageComparisonTest, cls).setUpClass()
                func()

            __doc__ = func.__doc__  # __doc__ must be assigned at define time.
        # __name__ and __module__ are assigned after definition.
        ImageComparisonTest.__name__ = func.__name__
        ImageComparisonTest.__module__ = func.__module__

        def test(self, extension):
            ''' Common method to compare an image with extension. '''

            self.mark_extension(extension)

            # Save figures.
            kwargs = savefig_kwargs.copy()
            if extension == 'pdf':
                kwargs.setdefault('metadata',
                                  {'Creator': None,
                                   'Producer': None,
                                   'CreationDate': None})

            result_dir = self.__class__.result_dir

            if len(plt.get_fignums()) != len(baseline_images):
                raise ValueError('image_comparison: `baseline_images` should '
                                 'have the same length as the number of '
                                 'figures generated')

            for idx, baseline in enumerate(baseline_images):
                fignum = plt.get_fignums()[idx]
                figure = plt.figure(fignum)

                actual_fname = os.path.join(
                    result_dir, baseline + save_suffix + '.' + extension)

                if saved_as:
                    # Just copy local saved file to result directory.
                    saved_fname = saved_as[idx]
                    if not saved_fname.endswith('.' + extension):
                        saved_fname += '.' + extension
                    shutil.move(saved_fname, actual_fname)

                else:
                    if remove_text:
                        remove_ticks_and_titles(figure)
                    figure.savefig(actual_fname, **kwargs)

            # Decide the extra tolerance.
            extra_tol = 0.5

            def aggr_ticklabel(ticklabels):
                ''' Aggregate all ticklabels as a string. '''
                return ''.join(str(tl) for tl in ticklabels)

            for ax in figure.get_axes():
                xticklabels = aggr_ticklabel(ax.get_xticklabels()
                                             + ax.get_xticklabels(minor=True))
                yticklabels = aggr_ticklabel(ax.get_yticklabels()
                                             + ax.get_yticklabels(minor=True))

                if easypyplot.util.matplotlib_version_tuple() < (2, 0) \
                        and yticklabels:
                    # yaxis tick vertical alignment, fixed in 2.0.
                    # See https://github.com/matplotlib/matplotlib/pull/6200
                    extra_tol += 256 * min(0.15, 0.01 * len(yticklabels))

                elif extension == 'png':
                    # PNG backend is not accurate. Weird warning from libpng.
                    extra_tol += 256 * min(0.1, 0.005 * len(xticklabels
                                                            + yticklabels))

            # Compare images.
            self.compare(baseline_images, save_suffix, extension, tol + extra_tol)

        # Dynamically add test methods for each image extension.
        for extension in extensions:
            ext_tst_func = lambda self, ext=extension: test(self, ext)
            ext_tst_name = 'test_{}'.format(extension)
            ext_tst_func.__name__ = ext_tst_name
            ext_tst_func.__doc__ = ' Compare images for {}. '.format(extension)
            setattr(ImageComparisonTest, ext_tst_name, ext_tst_func)

        return ImageComparisonTest

    return decorator

