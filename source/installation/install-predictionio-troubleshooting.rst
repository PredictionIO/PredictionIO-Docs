============================
Installation Troubleshooting
============================

We are sorry to hear that you run into troubles during PredictionIO setup. This troubleshooting guide aims to help you to solve most problems.

If you continue to face difficulties, please don't hesitate to seek support at `PredictionIO Google Group <http://groups.google.com/group/predictionio-user/>`_. 

The following steps assume that you have placed PredictionIO at your home directory.

Before you continue, note that:

*   It is normal that you do not get prediction results 1 hour after you deploy an algorithm and import data. The system updates prediction results periodically.

*   Check these log files to see if you can identify some obvious problems:
    
    *   dist/target/PredictionIO-{current version}/logs/{all logs}
    *   ~/PredictionIO/dist/target/PredictionIO-{current version}/vendors/hadoop-{current version}/logs/{jobtracker log file}


Step 1: Stop Everything
-----------------------

First, you should stop all PredictionIO services. To do so:

    cd ~/PredictionIO/dist/target/PredictionIO-{current version}

    bin/stop-all.sh

If you are running the local Hadoop that comes with PredictionIO, you should also stop Hadoop with:

    vendors/hadoop-{current version}/bin/stop-all.sh


Step 2: Check MongoDB and JAVA_HOME
-----------------------------------

Please make sure that MongoDB is running.

If you are using the local Hadoop installed by PredictionIO,  please check that you have a correct JAVA_HOME path in your hadoop config.
This JAVA_HOME should match with your system default java version.

    java -version 

    cd ~/PredictionIO/dist/target/PredictionIO-{current version}
    
    *OPEN* vendors/hadoop-{current version}/conf/hadoop-env.sh 

You may now start PredictionIO and try again.

    cd ~/PredictionIO/dist/target/PredictionIO-{current version}

    bin/start-all.sh
    
If you still cannot access the web admin panel, please *stop everything* again and proceed to the next step.

Step 3:  Erase Everything
-------------------------

If you cannot fix the problems with the steps above, it is possible that your PredictionIO built is corrupted.
You may need to erase all PredictionIO files and data with the steps below. 

.. note::
    Please make sure that PredictionIO services and its Hadoop are stopped.


Delete PredictionIO MongoDB Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove everything related to PredictionIO in your MongoDB.

    $ mongo
    
    > use predictionio;
    
    > db.dropDatabase();
    
    > use predictionio_appdata;
    
    > db.dropDatabase();
    
    > use predictionio_modeldata;
    
    > db.dropDatabase();
    
    > use predictionio_test_appdata;
    
    > db.dropDatabase();
    
    > use predictionio_training_appdata;

Format Hadoop Namenode and Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    Please make sure you understand what you are doing here, as you may erase your other Hadoop data unintentionally.
    
If you are using the Hadoop installed by PredictionIO, you should format its namenode and erase its data:

    cd ~/PredictionIO/dist/target/PredictionIO-{current version}/vendors/hadoop-{current version}
    
    bin/hadoop namenode -format

    rm -rf /tmp/hadoop-{your user name}

Delete PredictionIO
~~~~~~~~~~~~~~~~~~~

Finally, delete all PredictionIO files

    cd ~/
    
    rm -rf PredictionIO


Step 4:  Build Again with SBT Config
------------------------------------

Now you are ready for a clean build of PredictionIO, but before you do so, you should increase the memory allowance of your SBT to avoid build failure.

Please create or edit ~/.sbtconfig with these lines:

    | SBT_OPTS="-Xms512M -Xmx512M -Xss1M
    |  -XX:+CMSClassUnloadingEnabled
    |  -XX:+UseConcMarkSweepGC -XX:MaxPermSize=724M"
     
Now you can follow :doc:`../installation` again for a clean installation.

Thanks for your patience! If you still encounter any problem, please contact us at `PredictionIO Google Group <http://groups.google.com/group/predictionio-user/>`_.