===============================
Troubleshooting an Installation
===============================

We are sorry to hear that you run into troubles during PredictionIO setup. This
troubleshooting guide aims to help you to solve most problems.

If you continue to face difficulties, please do not hesitate to seek support at
`PredictionIO Google Group
<http://groups.google.com/group/predictionio-user/>`_.

The following steps assume that you have placed PredictionIO at your home
directory.

Before you continue, note that:

*   It is normal that you do not get prediction results 1 hour after you deploy
    an algorithm and import data. The system updates prediction results
    periodically.

*   Check these log files to see if you can identify some obvious problems:

    *   ``{PredictionIO Installation Path}/logs/{all logs}``
    *   ``{PredictionIO Installation Path}/vendors/hadoop-{current version}/
        logs/{jobtracker/namenode/datanode log files}``


Step 1: Stop Everything
-----------------------

First, you should stop all PredictionIO services. To do so:

.. code-block:: console

    $ cd {PredictionIO Installation Path}
    $ bin/stop-all.sh

If you are running the local Hadoop that comes with PredictionIO, you should
also stop Hadoop with (if you did not let ``bin/stop-all.sh`` stop it for you):

.. code-block:: console

    $ vendors/hadoop-{current version}/bin/stop-all.sh


Step 2: Check MongoDB and JAVA_HOME
-----------------------------------

Please make sure that MongoDB is running.

If you are using the local Hadoop installed by PredictionIO, please check that
you have a correct JAVA_HOME path in your hadoop config. This JAVA_HOME should
match with your preferred Java (1.6+) installation in your system.

.. code-block:: console

    $ java -version
    $ cd {PredictionIO Installation Path}

Open ``vendors/hadoop-{current version}/conf/hadoop-env.sh`` and look for the
line where it specifies the ``JAVA_HOME`` environmental variable. Replace the
value with an appropriate one. If you cannot find such line, add one, e.g.

.. code-block:: sh

    export JAVA_HOME=your_java_installation_path

You may now start PredictionIO and try again.

.. code-block:: console

    $ bin/start-all.sh

If you still cannot access the web admin panel, please *stop everything* again
and proceed to the next step.


Step 3:  Erase Everything
-------------------------

If you cannot fix the problems with the steps above, it is possible that your
PredictionIO meta data is corrupted. You may need to erase all PredictionIO
files and data with the steps below.

.. note::
    Please make sure that PredictionIO services and its Hadoop are stopped.


Delete PredictionIO MongoDB Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove everything related to PredictionIO in your MongoDB. Default database
names are assumed. If you have changed these names in your configuration,
please modify the following example accordingly.

.. code-block:: console

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
    > db.dropDatabase();
    > use predictionio_validation_appdata;
    > db.dropDatabase();
    > use predictionio_training_modeldata;
    > db.dropDatabase();


Format Hadoop Namenode and DataNode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    Please make sure you understand what you are doing here, as you may erase
    your other Hadoop data unintentionally.

If you are using the Hadoop installed by PredictionIO, you should format its
NameNode and DataNode to erase its data. If you have specified a non-default
storage for NameNode and DataNode (described in
:doc:`install-predictionio-on-linux`), please make sure you manually remove
all its content before formatting the NameNode.

.. code-block:: console

    $ cd {PredictionIO Installation Path}/vendors/hadoop-{current version}
    $ bin/hadoop namenode -format

Now you can setup PredictionIO again by doing:

.. code-block:: console

    $ bin/setup.sh
    $ bin/users
    $ bin/start-all.sh

Thanks for your patience! If you still encounter any problem, please contact us
at `PredictionIO Google Group
<http://groups.google.com/group/predictionio-user/>`_.
