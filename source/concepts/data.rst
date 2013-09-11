===============
Data Collection
===============

To make prediction, PredictionIO app collects mainly 3 types of data: *User Data*, *Item Data* and *Behavioral Data*.

User Data
---------

Each user record corresponds to a unique user or customer of your application. 
The only required data attribute is a user ID string, which normally matches with the one in your database.  
You may also provide any extra data attributes, such as age, gender, location and income.

Item Data
---------

An item record corresponds to an object of your application. An object can be anything, e.g., a book, a restaurant, a document, a product, a video or any other content.
Each item record requires 2 data attributes: an Item ID string and an array of item types. You may also provide any extra data attributes to each item record. 
Similar to an user ID, an item ID normally matches with the ID of the corresponding object in your database. An item type is a string that categorizes an item.

Item Type
~~~~~~~~~

There may be one or more type of items in your application. They can be categorized with item type strings. Each item can also belong to more than one item type.
Let say you are building a software marketplace service that categorizes software as Freeware or Shareware. Each software is further categorized as Developer Tool, Database Server and System Utility etc.
In this case, the item type array of an item record may look like this: ['Software', Freeware', 'Developer Tool'].


Behavioral Data
---------------

User-to-item actions and user-to-user actions are collected as behavioral data. They are used for constructing predictive models. 
A behavior record looks like this: User *A* **likes** Item *X*, where **like** is a user-to-item action type.

Built-in Action Type
~~~~~~~~~~~~~~~~~~~~

PredictionIO comes with some user-to-item action types:

``like``
   A user explicitly likes an item.

``dislike``
   A user explicitly dislikes an item.

``rate``
   A user gives rating to an item. It is a 1-5 scale score. 1 is the worst and 5 is the best. (so 3 is neutral) 
   Please convert the score manually if your application follows a different rating scale. 

``view``
    A user browses an item. It may be regarded as a soft implicit preference.    
``conversion``
    A user performs an action that implies the strongest preference, e.g. when a user purchases a product, when a user download the content or when a user signs up a service.

You may also add your own custom action type.

.. 
    ``view details``
    A user requests to read more about an item. It may be regarded as a stronger implicit preference.