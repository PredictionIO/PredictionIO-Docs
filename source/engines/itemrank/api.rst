==================================
Item Rank: API Endpoints
==================================

Item Rank Engine supports the following API endpoints:

Get Ranked Item
---------------

To rank a list items for a user, make an HTTP GET request to itemrank engine URI:

.. code-block:: rest

    GET /engines/itemrank/<your engine name>/ranked.json

The query is a targeted user and a list of item ids while the output is a list of ranked item ids.


Required Parameters
^^^^^^^^^^^^^^^^^^^

+--------------+--------------------------------------------------------+
| Parameter    | Description                                            |
+==============+========================================================+
| pio_appkey   |  app key of your PredictionIO app.                     |
+--------------+--------------------------------------------------------+
| pio_uid      | The user ID string of the targeted user.               |
+--------------+--------------------------------------------------------+
| pio_iids     | Comma separated item ids string to be ranked.          |
+--------------+--------------------------------------------------------+


Optional Parameters
^^^^^^^^^^^^^^^^^^^

+-------------------+---------------------------------------------------------+
| Parameter         | Description                                             |
+===================+=========================================================+
| pio_attributes    | Specify which custom attributes to be returned.         |
+-------------------+---------------------------------------------------------+

Sample Response
^^^^^^^^^^^^^^^

.. code-block:: json

    {
        "pio_iids":["item2", "item3", "item8"]
    }
