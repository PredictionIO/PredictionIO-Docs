===============
Data Collection
===============

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

