=============================
Item Rank: Overview
=============================

*Rank a list of items to a user personally*

With this engine, you can personalize a ranked list of items in your application. The engine rank items in two steps:


**Step 1: Predict User Preferences**

.. image:: /images/engine-itemrec-prediction.png

In this batch-mode process, the engine predicts a preference score for every user-item pair.
The scores are computed by the deployed algorithm in the engine. (See: :doc:`algorithms`)


**Step 2: Rank the Query Items**

With the predicted scores, this engine can rank a list of items for the user according to your REST API/SDK queries.
Ranked items will then be returned.
