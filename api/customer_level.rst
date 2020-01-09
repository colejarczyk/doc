Customer Level API
=========

These endpoints will allow you to see Levels for a customer.


Get complete list of levels
---------------------------

To retrieve the complete list of levels you will need to call the ``/api/customer/level`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/level

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| page                 | query          | *(optional)* Start from page, by default 1             |
+----------------------+----------------+--------------------------------------------------------+
| perPage              | query          | *(optional)* Number of items to display per page,      |
|                      |                | by default = 10                                        |
+----------------------+----------------+--------------------------------------------------------+
| sort                 | query          | *(optional)* Sort by column name,                      |
|                      |                | by default = name                                      |
+----------------------+----------------+--------------------------------------------------------+
| direction            | query          | *(optional)* Direction of sorting [ASC, DESC],         |
|                      |                | by default = ASC                                       |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/level \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "levels": [
        {
          "name": "level1",
          "description": "example level",
          "conditionValue": 20,
          "hasPhoto": true
        },
        {
          "name": "level2",
          "description": "example level",
          "conditionValue": 200,
          "hasPhoto": false
        },
      ],
      "total": 2
    }
