=========================
The Basic of PredictionIO
=========================

PredictionIO acts as a server that collects data and serve prediction results through REST APIs/SDKs.
Conceptually, the 3 main building blocks are: App, Engine and Algorithm.

.. image:: /images/concepts-app-engine-algo.png



App
~~~

App in PredictionIO Server is like a database or collection in a database server. 
It is usually corresponds to the application you are building.
Relevant data, such as user behavior, is collected by an app.  
An app contains one or more prediction engines. App data is shared among these engines.

Engine
~~~~~~

An engine must belong to a prediction type (or engine type), such as Item Recommendation or Item Similarity.
Each Engines process data and construct predictive model independently. Therefore, every engine serves its own set of prediction results.
In an app, for example, you may create two engines: one for recommending news to users and another one for suggesting new friends to users.
An algorithm must be deployed in each engine.

Algorithm
~~~~~~~~~

A number of built-in algorithms are available for use in each type of engine.
An algorithm, and the setting of its parameters, determines how predictive model is constructed. In another word, prediction accuracy or performance can be improved by tuning a suitable algorithm.
PredictionIO comes with tools and metrics for algorithm evaluation.