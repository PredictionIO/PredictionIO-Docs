=============================
First Ruby PredictionIO App
=============================

This is a quickstart guide of using PredictionIO Ruby SDK to write a very simple app.  It assumes that you have installed PredictionIO server.

Add your App to PredictionIO
----------------------------

Go to the web admin panel of PredictionIO Server at ``http://<yourhost>:9000/``.
Follow on-screen instruction to add the first app.
Now an **app key** can be obtained from the control panel. You need this key for all PredictionIO API/SDK calls.

Create a Prediction Engine
--------------------------

Next, you need to create a **Prediction Engine** under the new app. Each engine deals with one specific prediction problem.
Let's start by creating an **Item Recommendation Engine** (itemrec) and name it **engine1**.

Create a Ruby Project
-----------------------

Let's create a new project directory:

.. code-block:: console

    mkdir rbdemo
    cd rbdemo

Install Ruby SDK
------------------

To install the Ruby SDK, run

.. code-block:: console

    gem install predictionio


This will install the ``predictionio`` module to your Ruby distribution.

Generate and Import Data
------------------------

In the same directory, create import.rb as below.

Replace **<your app key>** with your app key string.

.. code-block:: ruby

    require "predictionio"

    client = PredictionIO::Client.new("<your app key>")

    # generate 10 users, with user ids "1","2",....,"10"
    user_ids = ("1".."10").to_a
    user_ids.each do |uid|
      puts "Add user #{uid}"
      client.create_user(uid)
    end

    # generate 50 items, with item ids "1","2",....,"50"
    # assign type id 1 to all of them
    item_ids = ("1".."50").to_a
    item_ids.each do |iid|
      puts "Add item #{iid}"
      client.create_item(iid, ["1"])
    end

    # each user randomly views 10 items
    user_ids.each do |uid|
      item_ids.sample(10).each do |iid|
        puts "User #{uid} views item #{iid}"
        client.identify(uid)
        client.record_action_on_item("view", iid)
      end
    end

And execute it to generate users, items and random view actions.

.. code-block:: console

    ruby import.rb

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

If you can see some jobs are running, your setup is probably okay. Press Ctrl+C to exit log viewing.


Retrieve Prediction
-------------------

Create a file 'show.rb' with this code:

Replace **<engine name>** with your engine name. It should be named '**engine1**' in this example.

.. code-block:: ruby

    require "predictionio"

    client = PredictionIO::Client.new("<your app key>")

    # Recommend 5 items to each user
    ("1".."10").each do |uid|
      puts "Retrieve top 5 recommendations for user #{uid}"
      client.identify(uid)
      begin
        rec = client.get_itemrec_top_n("<engine name>", 5)
        puts "#{rec}"
      rescue PredictionIO::Client::ItemRecNotFoundError => e
        puts "Recommendation not found"
      end
    end

Execute it AFTER your engine status becomes **Running** or you may not see any recommendation.

.. code-block:: console

    ruby show.rb


Congratulations! You have just create a "hello world" of PredictionIO in Ruby.


.. note::

   - You can create multiple prediction engines for an app to serve different prediction purposes.
   - You can import all kind of data into this app. Data will be shared among all engines.
   - For each engine, an algorithm is selected by default. You may manually select another one.
   - Pay attention to the engine status on the web admin panel. You can retrieve prediction only if its status is *running*.
   
