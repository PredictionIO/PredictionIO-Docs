=======================================
How to Build a Movie Recommendation App
=======================================

In this tutorial, we will show you how to build a simple command-line Python movie recommendation app using PredictionIO and real-world data. It assumes that you have successfully installed and started PredictionIO server and hadoop. It would be better if you have read our quickstart guide and know how to add an **App** and create an **Item Recommendation Engine** in the web admin panel, which are just a few easy clicks.

You also need to install the **PredictionIO Python SDK** in order to run this example. To install this SDK module from PyPI, you may

.. code-block:: console

    $ pip install predictionio

or

.. code-block:: console

    $ easy_install predictionio

All Python code of this example can be found in the **examples/itemrec/movies** directory of the **PredictionIO-Python-SDK** in github.

You can get the code of this example by doing:

.. code-block:: console

    $ git clone https://github.com/PredictionIO/PredictionIO-Python-SDK.git
    $ git checkout master

.. note:: 

    Please check out the master branch for the latest stable release.

Go to *PredictionIO-Python-SDK/examples/itemrec/movies/*, you will find 4 files:

* *app_config.py*: config data for the app such as App Key.
* *appdata.py*: data model structure which loads the data from the data set files.
* *batch_import.py*: app data batch import script.
* *movie_rec_app.py*: a simple command line based movie recommendation app.

More details of these files will be explained later.

1. Add a new App
----------------

Go to web admin panel. Create a new App named **My Movie App**.

2. Get The Data Set
-------------------

Now you need some data for the application. This example will use the `100K MovieLens Data Sets <http://www.grouplens.org/node/73#attachments>`_, which is collected by the GroupLens Rresearch from the MovieLens web site.

Go to *PredictionIO-Python-SDK/examples/itemrec/movies/*. Execute the following in the terminal:

.. code-block:: console

    $ wget http://www.grouplens.org/system/files/ml-100k.zip
    $ unzip ml-100k.zip

A new directory **ml-100k** is created, which contiains the data files of the real 100,000 ratings from 943 users on 1682 movies.

3. Import The Data
-------------------

Go to *PredictionIO-Python-SDK/examples/itemrec/movies/*. Open the file **app_config.py**. Replace the APP_KEY with the App Key of the app you just created in step 1.

.. code-block:: python

    APP_KEY = 'your app key here....'

If you are not using the *ml-100k* data set, you need to modify **appdata.py** accordingly.

Take a quick look at the file **batch_import.py**. Basically it is doing the following:

* Load the app data from the data set files:

.. code-block:: python

    app_data = AppData()

* Instantiate a PredictionIO Client object with the APP_KEY:

.. code-block:: python

   client = predictionio.Client(APP_KEY, 1, API_URL)

* Import each user to PredictionIO. Each user has an unique uid attribute:

.. code-block:: python

    for k, v in app_data.get_users().iteritems():
        client.create_user(v.uid)

* Import each item to PredictionIO. Each item has an unique iid and the itype is '*movie*':

.. code-block:: python

    for k, v in app_data.get_items().iteritems():
        client.create_item(v.iid, ("movie",))

* Import each rate action to PredictionIO. Each rate action has uid, iid, rating (which is 1 to 5) and the timestamp of this rate action:

.. code-block:: python

    for v in app_data.get_rate_actions():
        client.identify(v.uid)
        client.record_action_on_item("rate", v.iid, { "pio_rate": v.rating, "pio_t": v.t })

.. note:: 
    
    The attribute "pio_rate" is the rating value which is required for "rate" actions. The attribute "pio_t" is the optional timestamp.

In terminal, run the **batch_import.py** Python script:

.. code-block:: console

    $ python batch_import.py

You should see the following console outputs when it finishes:

.. code-block:: console

    $ python batch_import.py
    [Info] Initializing users...
    [Info] 943 users were initialized.
    [Info] Initializing items...
    [Info] 1682 items were initialized.
    [Info] Initializing rate actions...
    [Info] 100000 rate actions were initialized.
    [Info] Importing users to PredictionIO...
    [Info] 943 users were imported.
    [Info] Importing items to PredictionIO...
    [Info] 1682 items were imported.
    [Info] Importing rate actions to PredictionIO...
    [Info] 100000 rate actions were imported.

You have successfully imported 943 users, 1682 items and 100000 rate actions to the PredictionIO server!

4. Engine Training
------------------

You need to have an engine to process the data and generate the prediction.

Go to web admin panel. Create an **Item Recommendation Engine** for your app. Name it **movie-rec**. 

Once you create an engine, the PredictionIO server will automatically start the training process with the imported data, as indicated by the **Engine Status** in the web admin panel:

    Engine Status:    Not Running: **Training the first data model**

The engine will also automatically re-train with the latest imported data every hour.
If you want to start the the training process manually, you can click the *running* button of the deployed algo and select *Train Data Model Now*.

5. Retrieve Prediction
----------------------

Take a quick look at the file **movie_rec_app.py**. Pay attention to the following:

.. code-block:: python

    ENGINE_NAME = 'movie-rec'

The engine name should match the name of the engine you created in step 4. This engine name will be used by following PredictionIO API call, which determines which engine you want to retrieve the prediction results from.

.. code-block:: python

    try:
        self._client.identify(u.uid)
        rec = self._client.get_itemrec_topn(n, ENGINE_NAME)
        u.rec = rec['iids']
        self.display_items(u.rec)
    except predictionio.ItemRecNotFoundError:
        print "[Info] Recommendation not found"

The above code tries to retrieve the item recommendations from PredictoinIO and catch the ItemRecNotFoundError exception.

To run this **movic_rec_app.py**, execute the following in terminal:

.. code-block:: console

    $ python movie_rec_app.py

You should see the following console output:

.. code-block:: console

    [Main Menu]
    -----------
    Please input selection:
    0: Quit application.
    1: Get Recommendations from PredictionIO.
    2: Display user's data.

Input '*2*' and enter. The console outputs:

.. code-block:: console

    [Main Menu] / [Display User]
    ----------------------------
    Please enter user id:

Input the user id, say *28*, and enter (with this *ml-100k* data set, valid user ids is from 1 to 943)

.. code-block:: console

    [Main Menu] / [Display User]
    ----------------------------
    Please enter user id:
    28
    [Info] User 28:

    [Info] Top 10 movies rated by this user:
    [Info] Silence of the Lambs, The (1991), rating = 5
    [Info] Twelve Monkeys (1995), rating = 5
    [Info] North by Northwest (1959), rating = 5
    [Info] Fargo (1996), rating = 5
    [Info] Raiders of the Lost Ark (1981), rating = 5
    [Info] Star Trek: The Wrath of Khan (1982), rating = 5
    [Info] Star Trek: First Contact (1996), rating = 5
    [Info] Sling Blade (1996), rating = 5
    [Info] American Werewolf in London, An (1981), rating = 5
    [Info] Contact (1997), rating = 5

    [Info] Movies recommended to this user:
    [Info] Empty.

    Press enter to continue...

Some of the top movies rated by this user are displayed, which are obtained from the ml-100k data set.
Notice that there is no recommended movie for this user yet because you haven't retrieved any recommendation from PredictionIO server.

Let's try to get recommendation for this user.

Go back to main menu. Input *1* and enter:

.. code-block:: console

    [Main Menu] / [Get Recommendations]
    -----------------------------------
    Please enter user id:

Input the user id *28* and enter.

You may see the following output "Recommendation not found".

.. code-block:: console

    [Main Menu] / [Get Recommendations]
    -----------------------------------
    Please enter user id:
    28
    [Info] Getting top 10 item recommendations for user 28...
    [Info] Recommendation not found
    [Info] Go back to previous menu...

This is because the engine is still training, as indicated by the **Engine Status** (*Training the first data model*) displayed in the web admin panel. You can relax and wait for training to complete.

When the prediction results are ready, the **Engine Status** will change to:

    Engine Status:   **Running**

Try to get recommendation for user *28* again. You should see the following console outputs:

.. code-block:: console

    [Main Menu] / [Get Recommendations]
    -----------------------------------
    Please enter user id:
    28
    [Info] Getting top 10 item recommendations for user 28...
    [Info] Apollo 13 (1995)
    [Info] Field of Dreams (1989)
    [Info] Stand by Me (1986)
    [Info] Cool Hand Luke (1967)
    [Info] Lawrence of Arabia (1962)
    [Info] North by Northwest (1959)
    [Info] Annie Hall (1977)
    [Info] Gandhi (1982)
    [Info] Fantasia (1940)
    [Info] Groundhog Day (1993)
    [Info] Go back to previous menu...

You have succesfully recommended movies to this user! :)

