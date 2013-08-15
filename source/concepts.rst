========
Concepts
========

.. index:: 
   single: concepts

The Basic
---------

To build a predictive feature for your software, first you need to create an Application in PredictionIO. Then you choose 
an engine according to your prediction needs. Finally, you may select a better algorithm for this engine. 

Application
~~~~~~~~~~~

For each web or mobile app, you probably need to create one Application only. All data relating to app will be stored under this Application.

Engine
~~~~~~

In each Application, you can create multiple Engines. Each engine is responsible for one prediction need.
For instance, you may create one engine to recommend news to users and you create another one to help users to discover new friends.

Algorithm
~~~~~~~~~

In each engine, at least one algorithm must be deployed. 


System Components
------------------

PredictionIO consists of a few components:

* Admin Server
* IO Server
* Prediction Stack
 
Admin Server
~~~~~~~~~~~~

PredictionIO's Admin Server component provides a web interface for developers to manage applications, engines and algorithms.

IO Server
~~~~~~~~~

IO Server offers scalable REST API services to communicate with your web or mobile app. 
It is responsible for handling data input and prediction output. 

Prediction Stack
~~~~~~~~~~~~~~~~

Built on top of solid data frameworks and technology, such as Hadoop, Cascading, Scalding and Mahout, 
PredictionIO can handle a huge amount of data efficiently. A variety of machine learning algorithms are available for you to implemenet with just a few clicks.

Data
----

Data Collection
~~~~~~~~~~~~~~~

User Data
~~~~~~~~~

Each user must be represented by a unique user ID.  Optionally, you can provide additional user attributes, such as age, gender, location and income. PredictionIO supports both structured and unstructured data attributes.

Item Data
~~~~~~~~~

Similar to User Data, the minimum requirement for an item record is a unique item ID.  Structured and unstructured item attributes are supported.

Item Type (or category)
+++++++++++++++++++++++
(placeholder)


Behavioral Data
~~~~~~~~~~~~~~~
Behavioral data represents user-to-item and user-to-user actions. 
PredictionIO comes with a number of built-in actions, such as like, dislike, rating, view, view details and conversion.
(You may also add your own action type if they are not enough.)

Built-in Action
+++++++++++++++++++++++

The following list includes all built-in actions in PredictionIO:

``like``
   Use this action when a user explicitly likes an item.

``dislike``
   Use this action when a user explicitly dislikes an item.

``rate``
   Use this action when a user gives rating to an item. It is a 1-5 scale score. 1 is the worst and 5 is the best. (so 3 is neutral) 
   Please convert the score manually if your application follows a different rating scale. 

``view``
    Use this action as a soft implicit preference.
    
``view details``
    Use this action as a stronger implicit preference.

``conversion``
    Use this action when a user performs an action that implies the strongest preference, e.g. when a user purchases a product, when a user download the content or when a user signs up a service.


GEO Information
~~~~~~~~~~~~~~~~

(placeholder)

Algorithm Evaluation
---------------------

Each type of engine comes with scientific evaluation metrics for you to evaluate and compare algorithms.  