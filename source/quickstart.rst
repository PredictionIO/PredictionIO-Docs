===========
Quick Start
===========

.. index::
   single: quickstart


| PredictionIO is an open-source prediction server: Data In, Prediction Out.
| You can try out PredictionIO easily with a few steps:

1. Install PredictionIO
-----------------------

Please follow the steps at :doc:`installation`.
Then go to web admin panel at `http://<yourhost>:9000/`.

2. Obtain an App Key
--------------------
Follow on-screen instruction to add the first app. 
Now an **app key** can be obtained from the control panel. You need this key for all PredictionIO API/SDK calls.

3. Create a Prediction Engine
-----------------------------

Next, you need to create a **Prediction Engine** under the new app. Each engine deals with one specific prediction problem. 
Let's start by creating an **Item Recommendation Engine** (itemrec) and name it **engine1**.


4. Write your First App
-----------------------

Your first engine is ready to use! Try to write the first piece of code to interact with it using your preferred language: 

.. toctree::
   :maxdepth: 1

   First PredictionIO App in PHP <quickstart/quickstart-php>
   First PredictionIO App in Python <quickstart/quickstart-python>
   
Things to Know
--------------
 
.. note::

   - You can create multiple prediction engines for an app to serve different prediction purposes.
   - You can import all kind of data into this app. Data will be shared among all engines.
   - For each engine, an algorithm is selected by default. You may manually select another one.
 
Pay attention to the engine status on the web admin panel. You can retrieve prediction only if its status is *running*.