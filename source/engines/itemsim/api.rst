==============================
Item Similarity: API Endpoints
==============================

Item Similarity Engine supports the following API endpoints:

Get Similar Items
-----------------

To suggest top N items that are most similar to a targeted item, make an HTTP GET request to itemsim engine URI:

.. code-block:: rest

    GET /engines/itemsim/<your engine name>/topn.json

The query is a targeted item while the output is a list of N items.


Required Parameters
^^^^^^^^^^^^^^^^^^^

+--------------+--------------------------------------------------------+
| Parameter    | Description                                            |
+==============+========================================================+
| pio_appkey   |  app key of your PredictionIO app.                     |
+--------------+--------------------------------------------------------+
| pio_iid      | | The item ID string of the targeted item, or          |
|              | | comma-separated multiple items IDs string (See note).|
+--------------+--------------------------------------------------------+
| pio_n        | The max. number of items returned.                     |
+--------------+--------------------------------------------------------+


.. note::

   If multiple item IDs are specified (For example: pio_iid=item0,item1,item2), all the specified items will be taken into account when return the top N similar items. One typical usage is that you could keep track a list of recent viewed items of the user and then use this list of recently viewed items to recommend items to the user. This could also be used to provide recommendation to anonymous users as soon as they have viewed a few items.


Optional Parameters
^^^^^^^^^^^^^^^^^^^

+-------------------+---------------------------------------------------------+
| Parameter         | Description                                             |
+===================+=========================================================+
| pio_itypes        | |  Specify the type(s) of items to be retrieved.        |
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
