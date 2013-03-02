===========
Quick Start
===========

.. index:: 
   single: quickstart

Overview
--------

| PredictionIO is an open-source prediction server: Data In, Prediction Out.
| You can setup PredictionIO easily within a few minutes.

5 Simple Steps to Use PredictionIO:

1. Install PredictionIO
2. Create a new *application* on PredictionIO to obtain an *app key*
3. Create an *engine* of the prediction service you need
4. Integrate your data into PredictionIO for this app 
5. Make Prediction

.. note::

   - You can create multiple prediction engines for an app to serve different prediction purposes.
   - You can integrate all kind of data into this app. Data will be shared among all engines.
   - For each engine, an algorithm is selected by default. You may manually select another one. 

1. Install PredictionIO
-----------------------

Please follow the steps at :doc:`installation`.

2. Obtain an App Key
--------------------
Go to http://yourhost:8000/. Follow the instruction.

Now an app key can be obtained from the control panel. You need this key for all PredictionIO API/SDK calls.

3. Create a Prediction Engine
-----------------------------

After you have created your app on PredictionIO, it is time to create a Prediction Engine for the prediction service you need. You can create more than one prediction engine.
For first-time users, you may simply create one to start with.

A prediction engine can be created on the control panel or through API call.


4. Integrate Data into PredictionIO
------------------------------------

Before you can use the prediction engine you have just created, you need to integrate data into PredictionIO for your app.
You can import all kind of data. It will be accessible among all prediction engines.

There are two way:

Batch Import
~~~~~~~~~~~~

This approach is especially useful to import your existing data into PredictionIO.
*Instruction coming soon *

Real-time Import
~~~~~~~~~~~~~~~~

To ensure you have the latest data in PredictionIO, you should also submit the data from your app to PredictionIO in real-time.
We have efficient SDKs in different languages which support both asynchronized and synchronized calls.

Please refer to :ref:`api_data`.

5. Make Prediction
-------------------

To make a prediction through the engine you have created, please refer to the specific API of your engine's :ref:`api_prediction`.
