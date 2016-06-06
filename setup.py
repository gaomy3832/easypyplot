"""
 * Copyright (c) 2016. Mingyu Gao
 * All rights reserved.
 *
"""
import os
import re
# To use a consistent encoding
from codecs import open
# Always prefer setuptools over distutils
import setuptools

here = os.path.abspath(os.path.dirname(__file__))

package = 'easypyplot'
version = '0.0.0'
desc = 'Python matplotlib utilities and wrappers'

# Get version number
with open(os.path.join(here, package, '__init__.py'), encoding='utf-8') as fh:
    matches = re.findall(r'^\s*__version__\s*=\s*[\'"]([^\'"]+)[\'"]',
            fh.read(), re.M)
    if matches:
        version = matches[-1]

setuptools.setup(
    name=package,
    version=version,

    description=desc,

    author='Mingyu Gao',
    author_email='mgao12@stanford.edu',

    #long_description='',
    #url='',
    #license='',

    packages=[package],

    #install_requires=[],
)
