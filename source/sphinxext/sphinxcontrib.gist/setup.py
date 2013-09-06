#-*- coding:utf-8 -*-

import setuptools
from sphinxcontrib import gist as pkg

pkgname = pkg.__name__

setuptools.setup(
    name=pkgname,
    version=pkg.__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'sphinx'
        ],
    author=pkg.__author__,
    license=pkg.__license__,
    url='https://github.com/shomah4a/sphinx-gist-embed',
    description='''embedding gist to sphinx''',
    long_description=pkg.__doc__,
    namespace_packages=['sphinxcontrib'],
    classifiers='''
Programming Language :: Python
Development Status :: 4 - Beta
License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Topic :: Software Development :: Documentation
'''.strip().splitlines())

