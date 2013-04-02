==========================
First PHP PredictionIO App
==========================

It's a quickstart guide of using PredictionIO PHP SDK to write a very simple app. It assumes that you have installed PredictionIO server.

Let's create a new project directory:

.. code-block:: console

    mkdir phpdemo
    cd phpdemo
        
Install PHP SDK
----------------

To communicate with PredictionIO server in PHP code, we can use the PredictionIO PHP client.
We are going to install it with Composer: 

1.  Create a file called **``composer.json``** in your project directory, which adds `predictionio/predictionio` as a dependency.
    It should look like this: 

.. code-block:: javascript

    {
        "require": {
            "predictionio/predictionio": "*"
        }
    }

2.  Install Composer:

.. code-block:: console

    curl -sS https://getcomposer.org/installer | php -d detect_unicode=Off


3.  Use Composer to install your dependencies:

.. code-block:: console

    php composer.phar install

Now you are ready to write the actual PHP code.

Generate and Import Data
------------------------

In the same directory, create import.php as below.

Replace **<your app key>** with your app key string.

.. code-block:: php

    <?php 
        // use composer's autoloader to load PredictionIO PHP SDK
        require_once("vendor/autoload.php");  
        use PredictionIO\PredictionIOClient;
        $client = PredictionIOClient::factory(array("appkey" => "<your app key>"));
        
        // generate 10 users, with user ids 1,2,....,10
        for ($i=1; $i<=10; $i++) {
            echo "Add user ". $i . "\n";
            $command = $client->getCommand('create_user', array('uid' => $i));
            $response = $client->execute($command);
        }
    
        // generate 50 items, with item ids 1,2,....,50
        // assign type id 1 to all of them
        for ($i=1; $i<=50; $i++) {
            echo "Add item ". $i . "\n";
            $command = $client->getCommand('create_item', array('iid' => $i, 'itypes' => 1));
            $response = $client->execute($command);
        }
    
        // each user randomly views 10 items
        for ($u=1; $u<=10; $u++) {
            for ($count=0; $count<3; $count++) {
                $i = rand(1, 50); // randomly pick an item
                echo "User ". $u . " views item ". $i ."\n";
                $client->execute($client->getCommand('user_view_item', array('uid' => $u, 'iid' => $i)));
            }
        }
    ?>

And execute it to generate user, item and random view actions.

.. code-block:: console

    php import.php


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

Create a file 'show.php' with this code:

Replace **<engine name>** with your engine name. It should be named '**engine1**' in this example.

.. code-block:: php

    <?php 
        // use composer's autoloader to load PredictionIO PHP SDK
        require_once("vendor/autoload.php");  
        use PredictionIO\PredictionIOClient;
        $client = PredictionIOClient::factory(array("appkey" => "<your app key>"));

        // Recommend 5 items to each user
        for ($u=1; $u<=10; $u++) {
            echo "Retrieve top 5 recommendations for user ". $u . "\n";
            try {
                $rec = $client->execute($client->getCommand('itemrec_get_top_n', array('engine' => '<engine name>', 'uid' => $u, 'n' => 5)));
                print_r($rec);
            } catch (Exception $e) {
               echo 'Caught exception: ',  $e->getMessage(), "\n";
            }
        }
    ?>
    
Execute it AFTER your engine status becomes **Running** or you may not see any recommendation.

.. code-block:: console

    php show.php
    
    
Congratulations! You have just create a "hello world" of PredictionIO in PHP.
