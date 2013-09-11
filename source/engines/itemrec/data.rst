=====================================
Item Recommendation: Data Requirement
=====================================

To build a predictive model, all built-in algorithms of this engine require the following data:

* User data
* Item data
* User-to-item behavioral data, such as like, rate and view.

Please refer to :doc:`../../concepts/data`.

.. note::
    
    | **Extra User and Item Data Attributes**
    | 
    | Your user data may contain additional attributes, such as age and gender. Your item data may also contain other attributes, such as price and title. What kind of data attribute you need to provide to PredictionIO depends on the algorithm you choose to build the model.
    | 
    | Currently, all built-in algorithms in PreditionIO are Collaborative Filtering (CF) algorithms. CF algorithms derive the feature vectors of users and items from previous behaviors, i.e. score, only. Therefore, you simply need to identify each user and item with a unique ID. No extra data attribute is needed.
    | 
    | It does not mean that CF algorithms are less accurate though. In fact, researches (such as `this <http://dl.acm.org/citation.cfm?id=1639731>`_) show the exact opposite. An algorithm that requires no data attribute can be the winning algorithm.

