#-*- coding:utf-8 -*-
u'''
embedding gist to sphinx

usage:

First of all, add `sphinx_gist_embed` to sphinx extension list in conf.py

.. code-block:: python

   extensions = ['sphinxcontrib.gist']


then use `gist` directive.

.. code-block:: rst

   .. gist:: https://gist.github.com/shomah4a/5149412


finally, build your sphinx project.

.. code-block:: sh

   $ make html

'''

__version__ = '0.1.0'
__author__ = '@shomah4a'
__license__ = 'LGPLv3'



def setup(app):

    from . import gist

    app.add_node(gist.gist,
                 html=(gist.visit, gist.depart))
    app.add_directive('gist', gist.GistDirective)

