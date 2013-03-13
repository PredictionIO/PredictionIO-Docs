================================
Installing PredictionIO on Linux
================================

Prerequisites
-------------


The default PredictionIO setup assumes that you have the following environment:

* A recent version of Linux (other OS's have not been tested yet)
* Java 7.0+

To run PredictionIO, the following software are also required:

* Apache Hadoop 1.0+ (or any compatible distribution that supports the "hadoop jar" command)
* MongoDB 2.0+ (http://www.mongodb.org/)

.. note::

   You may still continue the installation process without any of the above software.
   The setup script can install a local version for you quickly.

In addition, the following commands are required in your search path:

* curl
* gzip
* tar
* unzip
* zip


Installation
------------

To start using PredictionIO, please follow the steps below.


Downloading and Deploying PredictionIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PredictionIO ships with setup scripts that help you download and install prerequisites automatically.
Start by downloading a `binary release <http://prediction.io/download>`_ of PredictionIO, then

    unzip PredictionIO-{current version}.zip

    cd PredictionIO-{current version}

    bin/setup-vendors.sh


*   Hadoop

    If you do not have Hadoop installed, setup-vendors.sh script will set up one for you. In order to do so, please check that you can ssh to the localhost without a passphrase:

        $ ssh localhost

    If you cannot ssh to localhost without a passphrase, execute the following commands:

        $ ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa

        $ cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys

*   Java

    If you are asked to provide your Java installation path, please type in the *JAVA_HOME* path of a Java 7 installation in your system.
    PredictionIO contains Hadoop job JARs that are compiled against Java 7, and your Hadoop must also be running Java 7 to guarantee compatibility.


Start PredictionIO
~~~~~~~~~~~~~~~~~~~

.. note::

    Please make sure that MongoDB is running before you run this start script.

To start all PredictionIO services:

    bin/start-all.sh


Now, you should be able to access PredictionIO at http://localhost:9000/!

Create an Administrator Account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    Please make sure that MongoDB is running before you run this tool.

You must add at least one administrator to be able to log in the web panel:

    bin/users


Stop PredictionIO
~~~~~~~~~~~~~~~~~

To stop all PredictionIO services:

    bin/stop-all.sh

If you are running the local Hadoop that comes with PredictionIO, you can stop Hadoop with:

    vendors/hadoop-{current version}/bin/stop-all.sh


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