=========
User APIs
=========

The following API endpoints are provided to manage user data in an app:

Add a User
----------

To add a user record, make an HTTP POST request to this URI:

.. code-block:: rest

    POST /users.json
    

Required Parameters
^^^^^^^^^^^^^^^^^^^

+--------------+--------------------------------------------------------+
| Parameter    | Description                                            |
+==============+========================================================+
| pio_appkey   |  app key of your PredictionIO app.                     |
+--------------+--------------------------------------------------------+
| pio_uid      | The user ID string of the targeted user.               |
+--------------+--------------------------------------------------------+


.. note::

   |  *Update a User Record*
   |  If the pio_uid value is the same as the one of a previous record, all attributes of the previous user record will be discarded. Attributes of the new request will be stored.  


Optional Parameters
^^^^^^^^^^^^^^^^^^^

+-------------------+-------------------------------------------------------------------+
| Parameter         | Description                                                       |
+===================+===================================================================+
| pio_latlng        | |  Specify a Geo info of the targeted user.                       |
|                   | |  Double separated by commas (<lat>,<long>), e.g. 12.34,5.67     |
+-------------------+-------------------------------------------------------------------+
| pio_inactive      | Specify the user status. (true/false)                             |
+-------------------+-------------------------------------------------------------------+
| (any string)      | The values of any param without the prefix 'pio\_' will be stored.|
+-------------------+-------------------------------------------------------------------+

Note: pio_ct is a reserved parameter, please do not use it.


Sample Response
^^^^^^^^^^^^^^^

.. code-block:: json

    {"message":"User created."}
   
   
   
Get a User Record
-----------------

To retrieve a user record, make an HTTP GET request to this URI:

.. code-block:: rest

    GET /users/<the targeted uid>.json
    
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

    {"pio_uid":"313", "custom1": "value1"}


Delete a User Record
--------------------

To delete a user record, make an HTTP DELETE request to this URI:

.. code-block:: rest

    DELETE /users/<the targeted uid>.json
    
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

    {"message":"User deleted."}
