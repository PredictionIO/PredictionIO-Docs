=============================
Item Recommendation: Overview
=============================

*Recommend N items to a user personally*

With this engine, you can add discovery or recommendation features to your application. The engine makes recommendation in two steps:  


**Step 1: Predict User Preferences**  

.. image:: /images/engine-itemrec-prediction.png
    
In this batch-mode process, the engine predicts a preference score for every user-item pair. 
The scores are computed by the deployed algorithm in the engine. (See: :doc:`algorithms`)


**Step 2: Rank Top N Items**

With the predicted scores, this engine can rank all available items for any user according to your REST API/SDK queries.
Advanced queries, such as Geo-based search, is supported.
Top N items will then be returned as prediction results.
