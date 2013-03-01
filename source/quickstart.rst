=================================
Getting Started with PredictionIO
=================================

.. index:: 
   single: quickstart

Overview
--------

| PredictionIO is an open-source prediction server: Data In, Prediction Out.
| You can setup PredictionIO easily within a few minutes.

.. image:: static/systemchart.jpg
    :alt: system chart

5 Simple Steps to Use PredictionIO:

1. Register your web/mobile app to obtain an *app key*
2. Create an *engine* of the prediction service you need
3. Integrate your data into PredictionIO for this app 
4. Optionally select an algorithm for this engine
5. Make Prediction

.. note::

   - You need to register your app once only.
   - You can create multiple prediction engines for an app to serve different prediction purposes.
   - You can integrate all kind of data into this app. Data will be shared among all engines.
   - For each engine, an algorithm is selected by default. You may manually select another one if there is more than one algorithm. 


.. index::
   single: installation
   single: installation guides
   single: installation tutorials
    
Install PredictionIO
--------------------
    
PredictionIO runs on JVM, so it can be installed on most platforms.
`TappingStone <http://www.tappingstone.com>`_, the PredictionIO makers, provides both binaries
and packages. Choose your platform below:

.. _quickstart-installation:

.. toctree::
   :maxdepth: 1

   installation/install-predictionio-on-aws-private-instance
   installation/install-predictionio-on-red-hat-centos-or-fedora-linux
   installation/install-predictionio-on-ubuntu
   installation/install-predictionio-on-debian
   installation/install-predictionio-on-linux
   installation/install-predictionio-on-os-x
   installation/install-predictionio-on-windows

Register a Website or an Mobile App
-----------------------------------
Go to http://yourhost:8000/. Follow the instruction.

Now an app key can be obtained from the control panel. You need this key for all PredictionIO API/SDK calls.

Create a Prediction Engine
--------------------------

After you have registered your app, it is time to create a Prediction Engine for the prediction service you need. You can create more than one prediction engine.
For first-time users, you may simply create one to start with.

A prediction engine can be created on the control panel or through API call.


Integrate Data into PredictionIO
---------------------------------

Before you can use the prediction engine you have just created, you need to integrate data into PredictionIO for your app.
You can import all kind of data. It will be accessible among all prediction engines.

There are two way:

Batch Import
~~~~~~~~~~~~

This approach is especially useful to import your existing data into PredictionIO.

Real-time Import
~~~~~~~~~~~~~~~~

To ensure you have the latest data in PredictionIO,
you should also submit the data from your app to PredictionIO in real-time.
We have efficient SDKs in different languages which support both asynchronized and synchronized calls.

Please refer to :doc:`dataintegration` for more information.


Make Prediction
-------------------

.. code-block:: python

   engine.("rec1", uid=1, n=10)


Download PredictionIO SDKs
--------------------------
We provide various SDK libraries for your developments, which means that you could easily integrate PredictionIO into your Apps by adding a few function calls! Please check out the following SDK documentations for more details.

- Python

  - `Python SDK Documentation <http://api.prediction.io/>`_
  - `Download Phar <http://api.prediction.io/>`_
  
- Ruby

  - (coming soon)

- PHP

  - (coming soon)
  
- Java

  - (coming soon)


Release Notes
-------------

Stable Releases are suitable for production-use. You should always install the latest version of PredictionIO.
Development releases are relatively unstable, however, they contain some of the latest features.

- Current Stable Releases

  - None
  
- Current Development Release

  - :doc:`/release-notes/0.1dev`
