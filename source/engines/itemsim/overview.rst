=========================
Item Similarity: Overview
=========================

*People who like this may also like....*

This engine tries to suggest *N* items that are similar to a targeted item.
By being 'similar', it does not necessarily mean that the two items look alike, nor they share similar attributes.  
The definition of similarity is independently defined by each algorithm and is usually calculated by a *distance function*.
The built-in algorithms assume that similarity between two items means the likelihood any user would like (or buy, view etc) both of them.

The engine suggests similar items through a two-step process:  

**Step 1: Estimate Item Similarity**  

.. image:: /images/engine-itemsim-score.png
    
In this batch-mode process, the engine estimates a similarity score for every item-item pair. 
The scores are computed by the deployed algorithm in the engine. (See: :doc:`algorithms`)


**Step 2: Rank Top N Items**

With the similarity scores, this engine can rank all available items according to their similarity to a targeted item.
Advanced queries, such as Geo-based search, is supported. Top N most similar items will then be returned.
