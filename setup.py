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

import os
import re
import setuptools

PACKAGE = 'easypyplot'
DESC = 'Lightweight utilities and wrappers for Python matplotlib.'

def _get_version():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, PACKAGE, '__init__.py'), 'r') as fh:
        matches = re.findall(r'^\s*__version__\s*=\s*[\'"]([^\'"]+)[\'"]',
                             fh.read(), re.M)
        if matches:
            return matches[-1]
    return '0.0.0'

def _readme():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'README.rst'), 'r') as fh:
        return fh.read()

setuptools.setup(
    name=PACKAGE,
    version=_get_version(),
    description=DESC,

    author='Mingyu Gao',
    author_email='gaomy@tsinghua.edu.cn',
    long_description=_readme(),
    url='https://github.com/gaomy3832/easypyplot',
    license='BSD 3-clause',

    packages=setuptools.find_packages(),

    install_requires=[
        'coverage>=4',
        'matplotlib>=1.3',
        'cycler>=0.10',
        'nose>=1.3',
        'pytest>=3',
        'pytest-cov>=2',
        'pytest-xdist>=1',
    ],

    include_package_data=True,

    keywords='matplotlib python-plot',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Utilities',
    ],
)

