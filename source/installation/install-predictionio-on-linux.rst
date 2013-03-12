================================
Installing PredictionIO on Linux
================================

Prerequisites
-------------


The current default PredictionIO setup assumes that you have the following environment:

* At least 512MB of free memory for building the source
* A recent version of Linux (other OS's have not been tested yet)
* JDK 7.0+ (may work with JDK 6 but untested at the moment)

To run PredictionIO, the following software are required:

* Apache Hadoop 1.0+ (or any compatible distribution that supports the "hadoop jar" command)
* MongoDB 2.0+ (http://www.mongodb.org/)
* Scala 2.9.2 and 2.10.0+ (sbt will download correct compilers automatically) (http://www.scala-lang.org/)
* sbt 0.12.1+ (http://www.scala-sbt.org/)
* Play 2.1+ (http://www.playframework.org/)

.. note::

   You may still continue the installation process without any of these softwares.
   The build script can install a local version for you quickly.

To clone the software repository, and to enable automatic installation of 3rd party software,
the following commands are required in your search path:

* curl
* git
* gzip
* tar
* unzip
* zip

Installation
------------

To start using PredictionIO, please follow the steps below.

Cloning
~~~~~~~

Simply clone PredictionIO to your local machine.
The following steps assume that you have cloned the repo at your home directory.

    cd ~

    git clone git://github.com/PredictionIO/PredictionIO.git



Compiling and Deploying PredictionIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PredictionIO ships with build scripts that help you download and install build prerequisites automatically.

    cd ~/PredictionIO

    bin/build.sh

    bin/package.sh

    cd ~/PredictionIO/dist/target/PredictionIO-{current version}

    bin/setup-vendors.sh


*   Hadoop

    If you do not have Hadoop installed, setup-vendors.sh script will set up one for you. In order to do so, please check that you can ssh to the localhost without a passphrase:

        $ ssh localhost

    If you cannot ssh to localhost without a passphrase, execute the following commands:

        $ ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa

        $ cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys

    To prevent any compatibility issue, when asked for a Java installation, please provide one that was used to build PredictionIO.


Start PredictionIO
~~~~~~~~~~~~~~~~~~~

.. note::

    Please make sure that MongoDB is running before you run this start script.

To start all PredictionIO services:

    cd ~/PredictionIO/dist/target/PredictionIO-{current version}

    bin/start-all.sh


Now, you should be able to access PredictionIO at http://localhost:9000/!

Create an Administrator Account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    Please make sure that MongoDB is running before you run this tool.

You must add at least one administrator to be able to log in the web panel:

    ~/PredictionIO/tools/users/target/pack/bin/users


Stop PredictionIO
~~~~~~~~~~~~~~~~~

To stop all PredictionIO services:

    cd ~/PredictionIO/dist/target/PredictionIO-{current version}

    bin/stop-all.sh

If you are running the local Hadoop that comes with PredictionIO, you can stop Hadoop with:

    vendors/hadoop-{current version}/bin/stop-all.sh



Upgrading
---------

From 0.1 to 0.2
~~~~~~~~~~~~~~~

In 0.2, PredictionIO stores its algorithm settings in a more modular way.
This breaks backward compatibility with 0.1 and requires a tool to migrate this data.

    cd ~/PredictionIO/tools/migration/0.2/algoinfos

    sbt clean update run

Follow the on-screen instructions to complete the migration.
After the upgrade, the suite should return to normal operation.


Advanced Notes
--------------

MongoDB at a non-local hosts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default configuration assumes that you are running MongoDB at localhost:27017.
If this is not the case, update the configuration in
`~/PredictionIO/tools/users/src/main/resources/application.conf` before compiling.

    io.prediction.commons.settings.db.type=mongodb

    io.prediction.commons.settings.db.host=your.host.com

    io.prediction.commons.settings.db.port=12345


(TODO)

Compile Components Manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are a PredictionIO contributor/developer, you may want to :doc:`compile each component manually <install-predictionio-manual-compile>`.