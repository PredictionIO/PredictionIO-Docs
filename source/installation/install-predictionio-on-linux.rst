================================
Installing PredictionIO on Linux
================================

Prerequisites
-------------

The current default PredictionIO setup assumes that you have the following installed and configured in a trusted environment:

* At least 512MB of free memory for building the source
* A recent version of Linux (other OS's have not been tested yet)
* JDK 7.0+ (may work with JDK 6 but untested at the moment)
* Apache Hadoop 1.0+ (or any compatible distribution that supports the "hadoop jar" command)
* MongoDB 2.0+ (http://www.mongodb.org/)
* Scala 2.9.2 and 2.10.0+ (sbt will download correct compilers automatically) (http://www.scala-lang.org/)
* sbt 0.12.1+ (http://www.scala-sbt.org/)
* Play 2.1+ (http://www.playframework.org/)

Installation
------------
Cloning
~~~~~~~

Simply clone PredictionIO to your local machine.
The following steps assume that you have cloned the repo at your home directory.

    cd ~

    git clone git://github.com/PredictionIO/PredictionIO.git

Downloading Apache Mahout
~~~~~~~~~~~~~~~~~~~~~~~~~

If you plan to deploy Apache Mahout algorithms, you need to obtain a binary distribution from its official web site.
Currently, only 0.7 has been tested.
Once you have downloaded and unpacked the content, copy `mahout-core-0.7-job.jar` to the `lib`.

    cp mahout-core-0.7-job.jar ~/PredictionIO/lib


Compiling PredictionIO
~~~~~~~~~~~~~~~~~~~~~~

**Common Dependencies**

Compile dependencies first using sbt.

    cd ~/PredictionIO/commons

    sbt clean update +publish

    cd ~/PredictionIO/output

    sbt clean update +publish

If you run into any memory space problem, you may want to try adding `-Xmx512m` to your `sbt` commands, e.g.

    sbt clean update +publish -Xmx512m

**Process Assembly**

Compile and build the process assembly using sbt,
where `>` indicates commands that will be run in the sbt console.

    cd ~/PredictionIO/process/hadoop/scala

    sbt clean update assembly

**MAP@k Top-K Items Collector**

Compile and build the collector using sbt.

    cd ~/PredictionIO/process/hadoop/scala/engines/itemrec/evaluations/topkitems

    sbt clean update assembly

**Command-line User Administration Tool**

.. note::
   It is not necessary to have MongoDB running to compile the command line user administration tool.

Compile and pack the command line user administration tool.
The default configuration assumes that you are running MongoDB at localhost:27017.
If this is not the case, update the configuration in
`~/PredictionIO/tools/users/src/main/resources/application.conf` before compiling.

    io.prediction.commons.settings.db.type=mongodb

    io.prediction.commons.settings.db.host=your.host.com

    io.prediction.commons.settings.db.port=12345

After that, compile the tool.

    cd ~/PredictionIO/tools/users

    sbt clean update pack

Adding a User
~~~~~~~~~~~~~

.. note::
    MongoDB must be running for this step and beyond.

You must add at least one user to be able to log in.
Run

    ~/PredictionIO/tools/users/target/pack/bin/users

and follow the on-screen instructions to create a user.

Starting the Admin Panel
~~~~~~~~~~~~~~~~~~~~~~~~

Similar to the CLI tool, you may want to change your configuration, which is located at
`~/PredictionIO/adminServer/conf/application.conf`

The commons settings database, specified by `io.prediction.commons.settings.db.*` keys,
should be the same as the one specified in the CLI tool.

Assuming you have installed the Play framework at /opt/play,
where `>` indicates commands that will be run in the Play console.

    cd ~/PredictionIO/adminServer

    /opt/play/play

    > clean

    > update

    > compile

    > run

To access the admin panel, point your browser to http://localhost:9000/.
After the first run, you may skip `update` and `compile`.

Starting the API Server
~~~~~~~~~~~~~~~~~~~~~~~

Again, change the configuration in `~/PredictionIO/output/api/conf/application.conf`
where you see fit. With the same assumption from the step before,

    cd ~/PredictionIO/output/api

    /opt/play/play

    > clean

    > update

    > compile

    > run 8000

This will start the API server on the default port 8000.

Starting the Scheduler
~~~~~~~~~~~~~~~~~~~~~~

Change the configuration in `~PredictionIO/scheduler/conf/application.conf`
where you see fit.

In this configuration, however, you may want to change all database host names to one
that can be resolved by all nodes in your Hadoop farm.

With the same assumption from the step before,

    cd ~/PredictionIO/scheduler

    /opt/play/play

    > clean

    > update

    > compile

    > run 7000

This will start the scheduler on the default port 7000.


UPGRADING
---------

From 0.1 to 0.2
~~~~~~~~~~~~~~~

In 0.2, PredictionIO stores its algorithm settings in a more modular way.
This breaks backward compatibility with 0.1 and requires a tool to migrate this data.

    cd ~/PredictionIO/tools/migration/0.2/algoinfos

    sbt clean update run

Follow the on-screen instructions to complete the migration.
After the upgrade, the suite should return to normal operation.