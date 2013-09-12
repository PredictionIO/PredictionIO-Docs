==================================
Item Recommendation: API Endpoints
==================================

Item Recommendation Engine supports the following API endpoints:

Get Top N Recommendation
------------------------

To recommend top N items to a user, make an HTTP GET request to itemrec engine URI:

.. code-block:: rest

    GET /engines/itemrec/<your engine name>/topn.json
    
The query is a targeted user while the output is a list of N items.


Required Parameters
^^^^^^^^^^^^^^^^^^^

+--------------+--------------------------------------------------------+
| Parameter    | Description                                            |
+==============+========================================================+
| pio_appkey   |  app key of your PredictionIO app.                     |
+--------------+--------------------------------------------------------+
| pio_uid      | The user ID string of the targeted user.               |
+--------------+--------------------------------------------------------+
| pio_n        | The max. number of recommended items returned.         |
+--------------+--------------------------------------------------------+


Optional Parameters
^^^^^^^^^^^^^^^^^^^

+-------------------+---------------------------------------------------------+
| Parameter         | Description                                             |
+===================+=========================================================+
| pio_itypes        | |  Specify the type(s) of items to be recommended.      |
|                   | |  (comma-separated string, eg "type1,type2")           |
+-------------------+---------------------------------------------------------+
| pio_latlng        | Specify a Geo search point with latitude and longitude. |
+-------------------+---------------------------------------------------------+
| pio_within        | Selects geometries within a bounding distance.          |
+-------------------+---------------------------------------------------------+
| pio_unit          | Specify the unit of pio_within. "km" or "mi".           |
+-------------------+---------------------------------------------------------+
| pio_attributes    | Specify which custom attributes to be returned.         |
+-------------------+---------------------------------------------------------+

Sample Response
^^^^^^^^^^^^^^^

.. code-block:: json

    {
        "pio_iids":["item2", "item3", "item8"]
    }