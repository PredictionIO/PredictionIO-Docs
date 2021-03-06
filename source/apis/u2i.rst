==========================
User-to-Item Behavior APIs
==========================

The following API endpoint is provided to collect user-to-item actions:

Record an Action
----------------

To record a user-to-item action, such as a user *views* an item, make an HTTP POST request to this URI:

.. code-block:: rest

    POST /actions/u2i.json


Required Parameters
^^^^^^^^^^^^^^^^^^^

+--------------+--------------------------------------------------------+
| Parameter    | Description                                            |
+==============+========================================================+
| pio_appkey   |  app key of your PredictionIO app.                     |
+--------------+--------------------------------------------------------+
| pio_uid      | | The user ID string of the targeted user.             |
|              | | **Note**: cannot contain any tab (\\t) or comma (,)  |
|              | | characters.                                          |
+--------------+--------------------------------------------------------+
| pio_iid      | | The item ID string of the targeted item.             |
|              | | **Note**: cannot contain any tab (\\t) or comma (,)  |
|              | | characters.                                          |
+--------------+--------------------------------------------------------+
| pio_action   | |  String. Built-in action types are:                  |
|              | |  "rate", "like", "dislike", "view" and "conversion"  |
+--------------+--------------------------------------------------------+
| pio_rate     | | The rating value (integer 1 to 5).                   |
|              | | **Note**: required only if pio_action is "rate".     |
+--------------+--------------------------------------------------------+


.. note::

   |  *Update an Action Record*
   |  Action records will be accumulated. There is no way to update or delete a recorded action.


Optional Parameters
^^^^^^^^^^^^^^^^^^^

+-------------------+-------------------------------------------------------------------+
| Parameter         | Description                                                       |
+===================+===================================================================+
| pio_latlng        | |  Specify a Geo info of the action.                              |
|                   | |  Double separated by commas (<lat>,<long>), e.g. 12.34,5.67     |
+-------------------+-------------------------------------------------------------------+
| pio_t             | |  Specify the time of the action. Default to current time.       |
|                   | |  ISO 8601 format (eg. '2013-09-10T03:06:12Z'),                  |
|                   | |  or milliseconds from 1970-01-01T00:00:00Z (eg. 1234567890000). |
+-------------------+-------------------------------------------------------------------+


Sample Response
^^^^^^^^^^^^^^^

(for the best real-time performance, no response will be returned.)
