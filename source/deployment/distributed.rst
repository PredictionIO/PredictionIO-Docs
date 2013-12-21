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
  storage. As an example, for each 1 million users, you will need 120 MB of
  space.

* Behavior Data

  In most cases, your application's users will generate many actions, and it is
  usually due to storage growth that you need to scale the data storage.
  Assuming User ID's and Item ID's are UUID's that are 36-character long, each
  user-to-item action would require around 150 bytes of disk storage. If you
  run an online store with 100000 active users and each of them generates 20
  actions daily, your data store will grow by around 300 MB each day, which is
  about 9 GB per month.

* Prediction Model

  With similar assumption on User/Item ID's length, each user/item-prediction
  pair would require around 150 bytes of disk storage. The total required
  space is more elaborated:

  ``# users or items * # predictions per user or item * # algorithms trained * 2``

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




Scheduler Server
~~~~~~~~~~~~~~~~

If you only train with non-distributed algorithms, you may need to scale the
scheduler because non-distributed algorithms run on the same machine as the
scheduler. Due to different nature of different algorithms, there is no
standard rules to determine when you need to scale the scheduler.


Scaling
-------



For details about horizontally scaling MongoDB, please refer to MongoDB's
manual about `sharding
<http://docs.mongodb.org/manual/core/sharding-introduction/>`_.
