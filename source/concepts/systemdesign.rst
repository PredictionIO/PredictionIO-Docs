=============================
System Design of PredictionIO
=============================

PredictionIO is mainly built with Scala. Scala runs on the JVM, so Java and Scala stacks can be freely mixed for totally seamless integration. 
PredictionIO Server consists of a few components:

* Admin Server
* IO Server
* Scheduler
* Data Store
* Data Processing Stack

.. image:: /images/concepts-systemdesign.png
 
Admin Server
------------

PredictionIO's Admin Server component provides a web interface for developers to manage applications, engines and algorithms.
It is built on top of Play Framework.

IO Server
---------

IO Server offers scalable REST API services to communicate with your web or mobile app.  It is responsible for handling data input and prediction output. 
It is built on top of Play Framework.

Scheduler
---------

A scalable scheduler that can be used to manage schedules for executing tens, hundreds, or even tens-of-thousands of jobs.
Quartz is the default scheduler.
 
Data Store
----------

Data store manages the collected data, the predictive model and the cached prediction results. MongoDB is the default data store.

Data Processing Stack
---------------------

Built on top of solid data frameworks and technology, such as Hadoop, Cascading, Scalding and Mahout, 
PredictionIO can handle a huge amount of data efficiently. A variety of machine learning algorithms are available for you to implemenet with just a few clicks.

