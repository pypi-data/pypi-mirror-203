# -*- coding: utf-8 -*-
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Extension
# To use a consistent encoding
from codecs import open
from os import path
import os
from glob import glob

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

reqs = []


setup_args = {
    'name': 'pyhfst',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    'version': '1.1.0',

    'description': 'A pure Python implementation of HFST for using HFST optimized lookup transducers (with or without weights)',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',

    # The project's main homepage.
    'url': 'https://github.com/Rootroo-ltd/pyhfst',
    # Author details
    'author': 'Khalid Alnajjar and Mika Hämäläinen',
    'author_email': 'hello@rootroo.com',
    "zip_safe":False,
    # Choose your license
    'license': "Apache-2.0",

    # See https://pypi.python.org/pypi?%3Aaction':list_classifiers
    'classifiers': [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        "Topic :: Text Processing :: Linguistic",

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',

    ],

    # What does your project relate to?
    'keywords': 'hfst, fst, optimized lookup, hfstol, transducers',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    'packages': ["c_pyhfst", "pyhfst"],
    'package_dir': {'pyhfst': 'pyhfst', 'c_pyhfst': 'c_pyhfst'},

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    'install_requires': reqs,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    'extras_require': {},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    'package_data': {"c_pyhfst": [x.split("/")[-1]  for x in list(glob("./c_pyhfst/*.pyx")) + list(glob("./c_pyhfst/*.pxd")) + list(glob("./c_pyhfst/*.h"))]},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    'data_files': [],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    'entry_points': {},
    'project_urls': {  # Optional
        'Bug Reports': 'https://github.com/Rootroo-ltd/pyhfst/issues',
        'Developer': 'https://rootroo.com/',
    },
}

try:
    from Cython.Build import cythonize
    setup(ext_modules=cythonize("c_pyhfst/*.pyx", language_level=3), **setup_args)
except Exception as e:
    setup(**setup_args)