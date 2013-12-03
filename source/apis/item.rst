=========
Item APIs
=========

The following API endpoints are provided to manage item data in an app:

Add an Item
-----------

To add an item record, make an HTTP POST request to this URI:

.. code-block:: rest

    POST /items.json


Required Parameters
^^^^^^^^^^^^^^^^^^^

+--------------+--------------------------------------------------------+
| Parameter    | Description                                            |
+==============+========================================================+
| pio_appkey   |  app key of your PredictionIO app.                     |
+--------------+--------------------------------------------------------+
| pio_iid      | | The item ID string of the targeted item.             |
|              | | **Note**: cannot contain the tab (\\t) or comma (,)  |
|              | characters.                                            |
+--------------+--------------------------------------------------------+
| pio_itypes   | |  An array of item types that the item belongs to.    |
|              | |  Item type cannot contain the tab (\\t) character.   |
|              | |  Comma-separated string, e.g. "type1, type2"         |
+--------------+--------------------------------------------------------+


.. note::

   |  *Update a Item Record*
   |  If the pio_iid value is the same as the one of a previous record, all attributes of the previous item record will be discarded. Attributes of the new request will be stored.


Optional Parameters
^^^^^^^^^^^^^^^^^^^

+-------------------+-------------------------------------------------------------------+
| Parameter         | Description                                                       |
+===================+===================================================================+
| pio_latlng        | |  Specify a Geo info of the targeted item.                       |
|                   | |  Double separated by commas (<lat>,<long>), e.g. 12.34,5.67     |
+-------------------+-------------------------------------------------------------------+
| pio_inactive      | Specify the item status. (true/false)                             |
+-------------------+-------------------------------------------------------------------+
| pio_startT        | |  Start time that the item becomes available.                    |
|                   | |  ISO 8601 format (eg. '2013-09-10T03:06:12Z'),                  |
|                   | |  or milliseconds from 1970-01-01T00:00:00Z (eg. 1234567890000). |
+-------------------+-------------------------------------------------------------------+
| pio_endT          | |  Expiration time that the item becomes unavailable.             |
|                   | |  ISO 8601 format (eg. '2013-09-10T03:06:12Z'),                  |
|                   | |  or milliseconds from 1970-01-01T00:00:00Z (eg. 1234567890000). |
+-------------------+-------------------------------------------------------------------+
| pio_price         | Selling price of the item, if it is a product.                    |
+-------------------+-------------------------------------------------------------------+
| pio_profit        | Profit when the item is sold, if it is a product.                 |
+-------------------+-------------------------------------------------------------------+
| (any string)      | The values of any param without the prefix 'pio\_' will be stored.|
+-------------------+-------------------------------------------------------------------+

Note: pio_ct is a reserved parameter, please do not use it.


Sample Response
^^^^^^^^^^^^^^^

.. code-block:: json

    {"message":"Item created."}



Get an Item Record
------------------

To retrieve an item record, make an HTTP GET request to this URI:

.. code-block:: rest

    GET /items/<the targeted iid>.json

Required Parameters
^^^^^^^^^^^^^^^^^^^

+--------------+--------------------------------------------------------+
| Parameter    | Description                                            |
+==============+========================================================+
| pio_appkey   |  app key of your PredictionIO app.                     |
+--------------+--------------------------------------------------------+

Sample Response
^^^^^^^^^^^^^^^

.. code-block:: json

    {
        "pio_iid":"testiid2",
        "pio_itypes":["type1","type2"],
        "pio_startT":123456789,
        "pio_endT":1360647801400,
        "pio_price":1.23,
        "pio_profit":9.87,
        "pio_latlng":[12.34,5.678],
        "pio_inactive":true,
        "custom2":"2.34",
        "custom1":"value1"
    }


Delete an Item Record
---------------------

To delete an item record, make an HTTP DELETE request to this URI:

.. code-block:: rest

    DELETE /items/<the targeted iid>.json

Required Parameters
^^^^^^^^^^^^^^^^^^^

+--------------+--------------------------------------------------------+
| Parameter    | Description                                            |
+==============+========================================================+
| pio_appkey   |  app key of your PredictionIO app.                     |
+--------------+--------------------------------------------------------+

Sample Response
^^^^^^^^^^^^^^^

.. code-block:: json

    {"message":"Item deleted."}
