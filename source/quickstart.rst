===========
Quick Start
===========

.. index::
   single: quickstart

Let's try to get a sample app up and running in a few steps: 

1. Install PredictionIO
-----------------------

Please follow the steps at :doc:`installation`. When it is done, go to web admin panel at ``http://<yourhost>:9000/``.

2. Create an App
----------------
Follow on-screen instruction to add the first app.
Now an **app key** can be obtained from the control panel. You need this key for all PredictionIO API/SDK calls.

3. Create a Prediction Engine
-----------------------------

Next, you need to create a **Prediction Engine** under the new app. Each engine deals with one specific prediction problem.
Let's start by creating an **Item Recommendation Engine** (itemrec) and name it **engine1**.


4. Write Client Code
--------------------

Your engine is now ready for use! Try to write the first piece of client code to interact with PredictionIO Server using your preferred language:

.. toctree::
   :maxdepth: 1

   First Client Code in PHP <quickstart/quickstart-php>
   First Client Code in Python <quickstart/quickstart-python>


.. note::

   - You can create multiple prediction engines for an app to serve different prediction purposes.
   - You can import all kind of data into this app. Data will be shared among all engines.
   - For each engine, an algorithm is selected by default. You may manually select another one.
   - Pay attention to the engine status on the web admin panel. You can retrieve prediction only if its status is *running*.