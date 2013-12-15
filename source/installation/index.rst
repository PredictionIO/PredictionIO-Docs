=======================
Installing PredictionIO
=======================

.. index::
   single: installation

To get started, install PredictionIO Server and choose a SDK for your application.


Installing PredictionIO Server
------------------------------

PredictionIO runs on JVM, so it runs on most platforms. Choose your platform below:

.. toctree::
   :maxdepth: 1

   install-predictionio-on-aws
   install-predictionio-with-virtualbox-vagrant
   install-predictionio-on-linux
   install-predictionio-from-source

..
   install-predictionio-on-aws-private-instance
   install-predictionio-on-red-hat-centos-or-fedora-linux
   install-predictionio-on-ubuntu
   install-predictionio-on-debian
   install-predictionio-on-linux
   install-predictionio-on-os-x
   install-predictionio-on-windows

.. note::

   To upgrade from a previous version properly, please run **bin/setup.sh** after you install the new binary.

If you run into any trouble, please take a look at the :doc:`troubleshooting guide <install-predictionio-troubleshooting>`.

.. toctree::
   :hidden:

   install-predictionio-troubleshooting


Installing an SDK
-----------------

We provide various SDKs to connect your software with PredictionIO Server:

- Java

  - `Installing Java SDK <https://github.com/PredictionIO/PredictionIO-Java-SDK>`_
  - `Java SDK Documentation </java/api>`_

- PHP

  - `Installing PHP SDK <https://github.com/PredictionIO/PredictionIO-PHP-SDK>`_
  - `PHP SDK Documentation </php/api>`_

- Python

  - `Installing Python SDK <https://github.com/PredictionIO/PredictionIO-Python-SDK>`_
  - `Python SDK Documentation <http://pythonhosted.org/PredictionIO/>`_

- Ruby

  - `Installing Ruby SDK <https://github.com/PredictionIO/PredictionIO-Ruby-SDK>`_
  - `Ruby SDK Documentation </ruby/api/PredictionIO.html>`_


First Steps with PredictionIO
-----------------------------

After you have installed PredictionIO, consider reading :doc:`../tutorials/quickstart` as the next step.
