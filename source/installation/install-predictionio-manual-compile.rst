========================================
Compile PredictionIO Components Manually
========================================

Manual Build
------------

Download Apache Mahout
~~~~~~~~~~~~~~~~~~~~~~

If you plan to deploy Apache Mahout algorithms, you need to obtain a binary distribution from its official web site.
Currently, only 0.7 has been tested.
Once you have downloaded and unpacked the content, copy `mahout-core-0.7-job.jar` to the `lib`.

    cp mahout-core-0.7-job.jar ~/PredictionIO/lib

Compile Components
~~~~~~~~~~~~~~~~~~

**Common Dependencies**

Compile dependencies first using sbt.

    cd ~/PredictionIO/commons

    sbt clean update +publish

    cd ~/PredictionIO/output

    sbt clean update +publish

    cd ~/PredictionIO/process/commons/hadoop/scalding

    sbt clean update +publish

If you run into any memory space problem, you may want to try adding `-Xmx512m` to your `sbt` commands, e.g.

    sbt clean update +publish -Xmx512m

**Process Assembly for ItemRec Engine**

Compile and build the process assembly using sbt.

    cd ~/PredictionIO/process/engines/itemrec/algorithms/hadoop/scalding

    sbt clean update assembly

    cd ~/PredictionIO/process/engines/itemrec/evaluations/hadoop/scalding

    sbt clean update assembly

    cd ~/PredictionIO/process/engines/itemrec/evaluations/scala/topkitems

    sbt clean update assembly

**Process Assembly for ItemSim Engine**

    cd ~/PredictionIO/process/engines/itemsim/evaluations/hadoop/scalding

    sbt clean update assembly

**Compile User Tool**

Compile and pack the command line user administration tool.

    cd ~/PredictionIO/tools/users

    sbt clean update pack


Starting the Admin Panel
------------------------

Similar to the CLI tool, you may want to change your configuration, which is located at
`~/PredictionIO/servers/admin/conf/application.conf`

The commons settings database, specified by `io.prediction.commons.settings.db.*` keys,
should be the same as the one specified in the CLI tool.

Assuming you have installed the Play framework at /opt/play,
where `>` indicates commands that will be run in the Play console.

    cd ~/PredictionIO/servers/admin

    /opt/play/play

    > clean

    > update

    > compile

    > run

To access the admin panel, point your browser to http://localhost:9000/.
After the first run, you may skip `update` and `compile`.

Starting the API Server
------------------------

Again, change the configuration in `~/PredictionIO/servers/api/conf/application.conf`
where you see fit. With the same assumption from the step before,

    cd ~/PredictionIO/servers/api

    /opt/play/play

    > clean

    > update

    > compile

    > run 8000

This will start the API server on the default port 8000.

Starting the Scheduler
----------------------

Change the configuration in `~PredictionIO/servers/scheduler/conf/application.conf`
where you see fit.

In this configuration, however, you may want to change all database host names to one
that can be resolved by all nodes in your Hadoop farm.

With the same assumption from the step before,

    cd ~/PredictionIO/servers/scheduler

    /opt/play/play

    > clean

    > update

    > compile

    > run 7000

This will start the scheduler on the default port 7000.