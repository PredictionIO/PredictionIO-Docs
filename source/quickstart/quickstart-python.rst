=============================
First Python PredictionIO App
=============================

It's a quickstart guide of using PredictionIO Python SDK to write a very simple app.  It assumes that you have installed PredictionIO server.

Let's create a new project directory:

.. code-block:: console

    mkdir pydemo
    cd pydemo
        
Install Python SDK
------------------

(coming soon)

Generate and Import Data
------------------------

In the same directory, create import.py as below.

Replace **<your app key>** with your app key string.

.. code-block:: python

    (coming soon)

And execute it to generate user, item and random view actions.

.. code-block:: console

    python import.py


Check Engine Status
-------------------

On the dashboard of your web admin panel, you can check the number of users, items and actions being imported.

In the Item Recommendation Engine that you have created, namely **engine1**, please take a look at the engine status.
You cannot retrieve prediction result until engine status becomes **Running**.

You may check if the training jobs are running properly through the PredictionIO server log files:

(assume your PredictionIO server is installed in your home directory)

.. code-block:: console

    cd ~/PredictionIO-{current version}
    
    tail -f logs/scheduler.err -f logs/scheduler.log

If you see the some hadoop jobs are running, then your setup is probably okay. Ctrl+C to exit log viewing.

.. note::

    Please be patience. It may take a long time to train the data model the first time even for very small dataset.
    It is normal because PredictionIO implements an distributed algorithm by default, which is not optimized for small dataset.
    You can change that later.


Retrieve Prediction
-------------------

Create a file 'show.py' with this code:

Replace **<engine name>** with your engine name. It should be named '**engine1**' in this example.

.. code-block:: python

    (coming soon)
    
Execute it AFTER your engine status becomes **Running** or you may not see any recommendation.

.. code-block:: console

    python show.py
    
    
Congratulations! You have just create a "hello world" of PredictionIO in Python.
