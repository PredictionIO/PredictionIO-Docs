==========================
Item Recommendation Engine
==========================

This engine predicts top N user preferences to items.

Algorithms
----------

Scala-based kNN Item-based Collaborative Filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This item-based k-NearestNeighbor algorithm predicts user preferences based on previous behaviors of users on similar items.

Mahout kNN Item-based Collaborative Filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predicts user preferences based on previous behaviors of users on similar items.

Mahout Alternating Least Squares with Weighted Lambda-Regulatization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predicts user preferences based on previous behaviors of users.

Mahout's kNN User Based Collaborative Filtering (Non-distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predicts user preferences based on previous behaviors of users who are the k-nearest neighbors (Non-distributed).

Mahout's Threshold User Based Collaborative Filtering (Non-distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predicts user preferences based on previous behaviors of users whose similarity meets or exceeds a certain threshold (Non-distributed).

Mahout's SlopeOne Rating Based Collaborative Filtering (Non-distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predicts user preferences based on average difference in preference values between new items and the items for which the user has indicated preferences (Non-distributed).

Random Rank
~~~~~~~~~~~

Predict user preferences randomly.

Latest Rank
~~~~~~~~~~~

Recommend latest items to users.
