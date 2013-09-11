=============
API Endpoints
=============

.. index::
   single: apis

This section describes the RESTful APIs of PredictionIO. 
By default, PredictionIO Server uses port 8000 for API services. So the base URI is: 
    
    http://<yourhost>:8000/

The following APIs enable you to collect and manage app data.

.. toctree::
   :maxdepth: 1

   user
   item

The followings are engine-specific APIs for querying prediction results.

.. toctree::
   :maxdepth: 1
   
   Item Recommendation APIs <../engines/itemrec/api>   
   Item Similarity APIs <../engines/itemsim/api>
   