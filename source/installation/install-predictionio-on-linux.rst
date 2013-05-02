================================
Installing PredictionIO on Linux
================================

Prerequisites
-------------

The default PredictionIO setup assumes that you have the following environment:

* A recent version of Linux (other OS's have not been tested yet)
* Java 7.0+

In addition, the following software are required:

* Apache Hadoop 1.0+ (or any compatible distribution that supports the "hadoop jar" command)
* MongoDB 2.0+ (http://www.mongodb.org/)

.. note::

   You may continue the installation process without Hadoop and MongoDB.
   The setup script will install them for you quickly.

* curl
* gzip
* tar
* unzip
* zip


Installation
------------

To start using PredictionIO, please follow the steps below.


Downloading and Setting Up PredictionIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start by downloading a `binary release <http://prediction.io/download>`_ of PredictionIO.

Please be aware that:

*   Hadoop

    If you do not have Hadoop installed, setup-vendors.sh script will set up one for you. In order to do so, please check that you can ssh to the localhost without a passphrase:

    .. code-block:: console

        $ ssh localhost

    If you see "connection refused", it means that the SSH service has not been enabled in the machine yet. Please enable it before you continue.

    If you cannot ssh to localhost without a passphrase, execute the following commands:

    .. code-block:: console

        $ ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa
        $ cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys

    By default, Hadoop uses `/tmp` as NameNode and DataNode storage. In some
    cases, this will be insufficient and cause DataNode to go offline during
    Hadoop job execution. To specify a different location for NameNode and
    DataNode storage, edit ``vendors/hadoop-<version>/conf/hdfs-site.xml`` and
    add:

    .. code-block:: xml

        <property>
            <name>dfs.name.dir</name>
            <value>/path_to_big_storage_for_namenode</value>
        </property>
        <property>
            <name>dfs.data.dir</name>
            <value>/path_to_big_storage_for_datanode</value>
        </property>

    Make sure NameNode and DataNode directories are different to avoid any locking error.

*   Java 7

    If you are asked to provide your Java installation path, please type in the *JAVA_HOME* path of a Java 7 installation in your system.
    PredictionIO contains Hadoop job JARs that are compiled against Java 7, and your Hadoop must also be running Java 7 to guarantee compatibility.

Now you can run these commands:

.. code-block:: console

    $ unzip PredictionIO-{current version}.zip
    $ cd PredictionIO-{current version}
    $ bin/setup-vendors.sh



Start PredictionIO
~~~~~~~~~~~~~~~~~~~

.. note::

    Please make sure that **MongoDB** is running before you run this start script.

To start all PredictionIO services:

.. code-block:: console

    $ bin/start-all.sh


Now, you should be able to access PredictionIO at http://localhost:9000/!

Create an Administrator Account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    Please make sure that **MongoDB** is running before you run this tool.

You must add at least one administrator to be able to log in the web panel:

.. code-block:: console

    $ bin/users


Stop PredictionIO
~~~~~~~~~~~~~~~~~

To stop all PredictionIO services:

.. code-block:: console

    $ bin/stop-all.sh

If you are running the local Hadoop that comes with PredictionIO, you can stop Hadoop with:

.. code-block:: console

    $ vendors/hadoop-{current version}/bin/stop-all.sh


Troubleshooting
---------------

If you cannot run PredictionIO properly, please refer to our :doc:`Installation Troubleshooting Guide <install-predictionio-troubleshooting>`.


Advanced Notes
--------------

MongoDB at a non-local hosts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default configuration assumes that you are running MongoDB at localhost:27017.
If this is not the case, update the configuration in ``conf/predictionio.conf``.

    io.prediction.commons.settings.db.type=mongodb

    io.prediction.commons.settings.db.host=your.host.com

    io.prediction.commons.settings.db.port=12345

Compile Components Manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are a PredictionIO contributor/developer, you may want to :doc:`compile each component manually <install-predictionio-manual-compile>`.