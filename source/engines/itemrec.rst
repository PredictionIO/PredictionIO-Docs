==========================
Item Recommendation Engine
==========================

*Predicts top N items for a user.*

For the Item Recommendation Engine, the query is a targeted user while the output is a list of N items selected for this user. The goal is to predict items this user likes most.

During the prediction step, for a targeted user, we want to predict a preference score for each available item. Higher score means that the user likes the item more. 
This is where the predictive models of machine learning come into place:

.. image:: /images/itemrec-prediction-step.png

During the ranking step, the system ranks all available items for this user according to the predicted score. Other criteria, such as the preference to the diversity of the item set, can be applied to adjust the ranking. The top N ranked items will be returned as the prediction output.


The Requirement of Training Data 
--------------------------------

In order to build a predictive model to predict a user's preference score towards an item, we need training data like this:

User ID | Item ID | Previous Behavior

For example:

User u1 has viewed 

You should also provide the *time* and *location* that a behavior took place, if they are available.

.. note::
    
    | **Other User and Item Data Attributes**
    | 
    | Your user data may have various attributes, such as age and gender. Your item data may also have some attributes as well, such as price and title. What kind of data attribute you need to provide to PredictionIO depends on the algorithm you choose to build the model.
    | 
    | Currently, all built-in algorithms in PreditionIO are Collaborative Filtering (CF) algorithms. CF algorithms derive the feature vectors of users and items from previous behaviors, i.e. score, only. Therefore, you simply need to identify each user and item with a unique ID. No extra data attribute is needed.
    | 
    | It does not mean that CF algorithms are less accurate though. In fact, researches (such as `this <http://dl.acm.org/citation.cfm?id=1639731>`_) show the exact opposite. Algorithms that require no data attribute can be the winning algorithms.



Built-in Algorithms
-------------------

A standard PredictionIO installation, which includes the Apache Mahout library, comes with the following algorithms:


Scalding kNN Item-based Collaborative Filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behaviors of users on similar items.

Mahout's Threshold Item-based Collaborative Filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behaviors of users on similar items.

Mahout's kNN Item-based Collaborative Filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behaviors of users on similar items.

Mahout's Alternating Least Squares with Weighted Lambda-Regulatization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behaviors of users.

Mahout's kNN User Based Collaborative Filtering (Non-distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behaviors of users who are the k-nearest neighbors (Non-distributed).

Mahout's Threshold User Based Collaborative Filtering (Non-distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behaviors of users whose similarity meets or exceeds a certain threshold (Non-distributed).

Mahout's SlopeOne Rating Based Collaborative Filtering (Non-distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on average difference in preference values between new items and the items for which the user has indicated preferences (Non-distributed).

Mahout's Alternating Least Squares with Weighted Lambda-Regulatization (Non-distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences using matrix factorization (Non-distributed).

Mahout's SVD-RatingSGD Recommender (Non-distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences using matrix factorization (Non-distributed).

Mahout's SVDPlusPlus Recommender (Non-distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Predict user preferences using matrix factorization (Non-distributed).

Random Rank
~~~~~~~~~~~

Predict user preferences randomly.

Latest Rank
~~~~~~~~~~~

Recommend latest items to users.
