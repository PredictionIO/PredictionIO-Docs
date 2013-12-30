======================
Distributed Deployment
======================

PredictionIO is built on top of horizontally scalable components. Each of them
can be scaled to suit your environment and needs.

Components that can be scaled:

* persistent data store (MongoDB);
* distributed computation engine and storage (Hadoop MapReduce and HDFS);
* job scheduling and execution service (PredictionIO scheduler server).

Scaling is not a trivial process. If your data size is not very large, your
best bet is to run PredictionIO on a single machine. In following sections,
guidelines will be provided to assist you in deciding whether you should scale
or not.


Scale or Not?
-------------

In this section, we will establish some rule of thumbs on whether you should
scale or not for each component.


Persistent Data Store
~~~~~~~~~~~~~~~~~~~~~

.. note::

    As of writing, only MongoDB is supported. Other data stores will be
    supported in the future eventually.

The persistent data store serves a few purposes:

* stores PredictionIO settings such as app, engine, and algorithm settings, etc.;
* captures user behavior, such as user-to-item actions;
* stores user prediction model.

Unless you are hosting PredictionIO at web-scale, it is very unlikely you need
to scale for PredictionIO settings.

If your application captures user behavior rapidly and your machine that is
hosting the data store is running out of space, or is not responding to writes
fast enough, you may consider scaling the data store.

PredictionIO regularly trains a prediction model and writes it out to the
persistent data store for fast and easy access (trading off with disk space).
This store is accessed by PredictionIO REST API server to provide predictions
to its end clients. If you have a read-intensive application and your machine
that is hosting the data store is not responding quick enough, you may consider
scaling the data store.

* User and Item Data

  If your application regularly generates new users and/or items, you need to
  take this growth into consideration. If your User/Item ID's are UUID's that
  are 36-character long, each user/item would require around 120 bytes of disk
  storage.

  ``120B * # users or items``

  As an example, for each 1 million users, you will need 120 MB of space.

* Behavior Data

  In most cases, your application's users will generate many actions, and it is
  usually due to storage growth that you need to scale the data storage.
  Assuming User ID's and Item ID's are UUID's that are 36-character long, each
  user-to-item action would require around 150 bytes of disk storage.

  ``150B * # actions``

  If you run an online store with 100000 active users and each of them
  generates 20 actions daily, your data store will grow by around 300 MB each
  day, which is about 9 GB per month.

* Prediction Model

  With similar assumption on User/Item ID's length, each user/item-prediction
  pair would require around 150 bytes of disk storage. The total required
  space is more elaborated:

  ``150B * # users or items * # predictions per user or item * # algorithms trained * 2``

  As an example, if you have 1 million users, 50 predictions per users and 5
  engines each with one deployed algorithm, the total storage requirement will
  be 75 GB. The double factor at the end of the equation applies only to
  deployed algorithm. This is because PredictionIO will not delete the old
  prediction model until a new one has finished writing. This mechanism allows
  non-interrupted prediction retrieval via the API server.

  Notice that this requirement also applies to evaluation and tuning. When
  evaluation or tuning runs, it is quite common that the system will train
  around 3 to 15 algorithms. In this case, the double factor should be removed
  from the calculation because there will only be one prediction model for each
  algorithm.


Hadoop
~~~~~~

The Hadoop distribution is a large collection of components for building
clusters that is capable of highly parallelized computation and distributed
storage. Scaling Hadoop is a very board topic itself. In this section, we are
going to touch a couple aspects briefly that are specific to PredictionIO. For
full details of scaling Hadoop, please refer to http://hadoop.apache.org/.

When training jobs are not finishing quick enough, you may consider scaling the
computation aspect of the Hadoop cluster--its MapReduce capacity, which could
be roughly measured by the number of mapper and reducer job slots. There are
two factors that will increase the computation demand:

* data size;
* number of training algorithms.

They will be explained respectively below.

Before an algorithm trains, data will be preprocessed and copied to Hadoop
Distributed Filesystem (HDFS). When the total data size exceed a certain size
(data store dependent), it will be splitted into chunks, and multiple copy jobs
will be spawned. Each of these jobs will occupy a mapper job slot. When your
data size is large enough to cause many of these jobs to spawn and exceeds the
number of available mapper job slots of your Hadoop cluster, you may consider
adding additional TaskTracker nodes to handle the load.

Large data size may also cause many mapper jobs to be spawned for computation.
If that is the case, you may consider adding additional TaskTracker nodes.

If you have many deployed algorithms, they may compete for job slots. If that
is the case, you may consider adding additional TaskTracker nodes.


Scheduler Server
~~~~~~~~~~~~~~~~

If you only train with non-distributed algorithms, you may need to scale the
scheduler because non-distributed algorithms run on the same machine as the
scheduler. Due to different nature of different algorithms, there is no
standard rules to determine when you need to scale the scheduler. If your
scheduler server is:

* heavily loaded by one non-distributed algorithm, you may need to scale up
  your machine;

* moderately loaded by one non-distributed algorithm, but heavily loaded when
  there is more than one non-distributed algorithm training simultaneously,
  you may consider adding more scheduler servers.


Scaling
-------

In this section, we will cover some basics of scaling individual components of
PredictionIO.


Persistent Data Store
~~~~~~~~~~~~~~~~~~~~~

.. note::

    As of writing, only MongoDB is supported. Other data stores will be
    supported in the future eventually.

If you decide to scale the persistent data store (MongoDB as of writing), it is
most likely that your app and/or model data size exceeds the capacity of a
single server. Assuming default settings, you should inspect these collections
and decide what to scale:

* predictionio_appdata

  * users
  * items
  * u2iActions

* predictionio_modeldata

  * itemRecScores
  * itemSimScores

For details about horizontally scaling MongoDB, please refer to MongoDB's
manual about `sharding
<http://docs.mongodb.org/manual/core/sharding-introduction/>`_.


Hadoop
~~~~~~

Scaling Hadoop can be a very complicated process. To go beyond the default
single node setup, please refer to `Hadoop cluster setup
<http://hadoop.apache.org/docs/r1.2.1/cluster_setup.html>`_.

If you are running on a pretty powerful machine, you may try to increase the
number of map and reduce task slots first by adding something similar to the
following to ``vendors/hadoop-1.2.1/conf/mapred-site.xml``:

.. code-block:: xml

    <property>
        <name>mapred.tasktracker.map.tasks.maximum</name>
        <value>8</value>
    </property>
    <property>
        <name>mapred.tasktracker.reduce.tasks.maximum</name>
        <value>4</value>
    </property>

The above example assumed a 8-core machine with reasonable amount of memory
and disk I/O performance (so that these are not limiting bottlenecks). For map
tasks, varing between ``0.5*(# cpu cores)`` to ``2*(# cpu cores)`` is a good
start. Reduce tasks usually require more resources, so it is a resonable start
to set it at half the number of map task slots.


Scheduler Server
~~~~~~~~~~~~~~~~

TBD
