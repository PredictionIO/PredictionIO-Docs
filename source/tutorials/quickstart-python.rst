=============================
First Python PredictionIO App
=============================

This is a quickstart guide of using PredictionIO Python SDK to write a very simple app.  It assumes that you have installed PredictionIO server.

Register an App with PredictionIO
---------------------------------

Go to the web admin panel of PredictionIO Server at ``http://<yourhost>:9000/``.
Follow on-screen instruction to add the first app.
Now an **app key** can be obtained from the control panel. You need this key for all PredictionIO API/SDK calls.

Create a Prediction Engine
-----------------------------

Next, you need to create a **Prediction Engine** under the new app. Each engine deals with one specific prediction problem.
Let's start by creating an **Item Recommendation Engine** (itemrec) and name it **engine1**.

Create PHP Project
------------------

Let's create a new project directory:

.. code-block:: console

    mkdir pydemo
    cd pydemo

Install Python SDK
------------------

To install the module from PyPI, you may

.. code-block:: console

    pip install predictionio

or

.. code-block:: console

    easy_install predictionio

If you have cloned the repository and want to install directly from there,
do the following in the root directory of the repository:

.. code-block:: console

    python setup.py install

This will install the ``predictionio`` module to your Python distribution.

Generate and Import Data
------------------------

In the same directory, create import.py as below.

Replace **<your app key>** with your app key string.

.. code-block:: python

    import predictionio
    import random

    client = predictionio.Client(appkey="<your app key>")

    # generate 10 users, with user ids 1,2,....,10
    for i in range(10):
        i = i + 1
        print "Add user", i
        client.create_user(i)

    # generate 50 items, with item ids 1,2,....,50
    # assign type id 1 to all of them
    for i in range(50):
        i = i + 1
        print "Add item", i
        client.create_item(i, ('1',))

    # each user randomly views 10 items
    random.seed()
    for u in range(10):
        u = u + 1
        for count in range(10):
            i = random.randint(1, 50)
            print "User", u, "views item", i
            client.identify(u)
            client.record_action_on_item("view", i)

    client.close()

And execute it to generate users, items and random view actions.

.. code-block:: console

    python import.py

Check Engine Status
-------------------

On the dashboard of your web admin panel, you can check the number of users, items and actions being imported.

In the Item Recommendation Engine that you have created, namely **engine1**, please take a look at the engine status.
You cannot retrieve prediction result until engine status becomes **Running**.

**Speed up the training:**

PredictionIO server updates data model periodically. You can trigger the training immediately:

1.  On web admin panel, go Manage for **engine1**.

2.  Click the **Algorithms** tab.

3.  In the **Deployed Algorithm** area, click the **Running** small button next to the algorithm description.

4.  Click **Train Data Model Now**

You may check if the training jobs are running properly through the PredictionIO server log files:

(assume your PredictionIO server is installed in your home directory)

.. code-block:: console

    cd ~/PredictionIO-{current version}

    tail -f logs/scheduler.err -f logs/scheduler.log

If you see the some Hadoop jobs are running, then your setup is probably okay. Press Ctrl+C to exit log viewing.

.. note::

    Please be patient. It may take a long time to train the data model the first time even for very small dataset.
    It is normal because PredictionIO implements an distributed algorithm by default, which is not optimized for small dataset.
    You can change that later.


Retrieve Prediction
-------------------

Create a file 'show.py' with this code:

Replace **<engine name>** with your engine name. It should be named '**engine1**' in this example.

.. code-block:: python

    import predictionio

    client = predictionio.Client(appkey="<your app key>")

    # Recommend 5 items to each user
    for u in range(5):
        u = u + 1
        print "Retrieve top 5 recommendations for user", u
        try:
            client.identify(u)
            rec = client.get_itemrec_topn("<engine name>", 5)
            print rec
        except predictionio.ItemRecNotFoundError as e:
            print 'Caught exception:', e.strerror()

Execute it AFTER your engine status becomes **Running** or you may not see any recommendation.

.. code-block:: console

    python show.py


Congratulations! You have just create a "hello world" of PredictionIO in Python.


.. note::

   - You can create multiple prediction engines for an app to serve different prediction purposes.
   - You can import all kind of data into this app. Data will be shared among all engines.
   - For each engine, an algorithm is selected by default. You may manually select another one.
   - Pay attention to the engine status on the web admin panel. You can retrieve prediction only if its status is *running*.
   
