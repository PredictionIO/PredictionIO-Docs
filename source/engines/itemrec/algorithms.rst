========================================
Item Recommendation: Built-in Algorithms
========================================

A standard PredictionIO installation, which includes the Apache Mahout library, comes with the following algorithms:


GraphChi's Alternating Least Squares Collaborative Filtering (Single Machine)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users using matrix
factorization.

GraphChi's CCD++ Alternating Least Squares Collaborative Filtering with Parallel Coordinate Descent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users using matrix
factorization.


GraphChi's CLiMF Collaborative Filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users using matrix
factorization with MRR (mean reciprocal rank) optimization.


GraphChi's Stochastic Gradient Descent Collaborative Filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users using matrix
factorization.


Mahout's Alternating Least Squares with Weighted Lambda-Regularization (Distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users using matrix
factorization.


Mahout's Alternating Least Squares with Weighted Lambda-Regularization (Single Machine)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users using matrix
factorization.


Mahout's kNN Item-based Collaborative Filtering (Single Machine)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users on similar items,
and take into account results that are within a configurable neighborhood and
threshold.


Mahout's kNN User-based Collaborative Filtering (Single Machine)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users who are
k-nearest neighbors.


Mahout's SVD++ Recommender (Single Machine)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users using matrix
factorization.


Mahout's SVD-RatingSGD Recommender (Single Machine)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users using matrix
factorization.


Mahout's Threshold Item-based Collaborative Filtering (Distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users on similar items,
and take into account results that are above a configurable threshold.


Mahout's Threshold User-based Collaborative Filtering (Single Machine)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences based on previous behavior of users whose similarity
meets or exceeds a configurable threshold.


Random Rank (Single Machine / Distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predict user preferences randomly. (As a baseline algorithm for evaluation
purposes.)


Latest Rank (Distributed)
~~~~~~~~~~~~~~~~~~~~~~~~~

Recommend latest items to users. (As a non-personal baseline algorithm for
evaluation purposes.)
