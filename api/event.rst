Event API
=========

These endpoints will allow you to retrieve events from Event Store.


Get the list of events
----------------------

To retrieve a paginated list of events, you need to call the ``/api/event`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/event

+----------------------+----------------+------------------------------------------------------------------------------+
| Parameter            | Parameter type |  Description                                                                 |
+======================+================+==============================================================================+
| Authorization        | header         | Token received during authentication                                         |
+----------------------+----------------+------------------------------------------------------------------------------+
| fromId               | query          | *(optional)* Start from event ID, by default from the beginning.             |
+----------------------+----------------+------------------------------------------------------------------------------+
| perPage              | query          | *(optional)* Number of items to display per page,                            |
|                      |                | by default = 10                                                              |
+----------------------+----------------+------------------------------------------------------------------------------+
| sort                 | query          | *(optional)* Sort by column name,                                            |
|                      |                | by default = name                                                            |
+----------------------+----------------+------------------------------------------------------------------------------+
| direction            | query          | *(optional)* Direction of sorting [ASC, DESC],                               |
|                      |                | by default = ASC                                                             |
+----------------------+----------------+------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/event \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    Endpoint will return the first 100 items from the given ``<eventId>``.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "events": [
            {
                "id": 1,
                "uuid": "e5fbe6a2-18f6-4569-8c5c-8f87c7717d87",
                "payload": {
                    "accountId": {
                        "accountId": "e5fbe6a2-18f6-4569-8c5c-8f87c7717d87"
                    },
                    "pointsTransfer": {
                        "id": {
                            "pointsTransferId": "e82c96cf-32a3-43bd-9034-4df343e5f333"
                        },
                        "comment": "Example comment",
                        "createdAt": "2020-10-15T12:06:38+02:00",
                        "value": 100,
                        "canceled": false,
                        "issuer": "system"
                    }
                },
                "type": "OpenLoyalty.Domain.Account.Event.PointsWereSpent",
                "recorderOn": "2020-10-15T10:06:38+00:00"
            }
        ],
        "total": 1
    }

Get event details
-----------------

To retrieve the details of a event, you need to call the ``/api/event/<eventId>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/event/<eventId>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <eventId>     | query          | Event ID                             |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the event with id ``eventId = 212333``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/event/212333 \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "id": 73,
        "uuid": "00000000-0000-474c-b092-b0dd880c07e2",
        "payload": {
            "customerId": {
                "customerId": "00000000-0000-474c-b092-b0dd880c07e2"
            },
            "levelId": {
                "levelId": "e82c96cf-32a3-43bd-9034-4df343e51111"
            },
            "oldLevelId": {
                "levelId": "e82c96cf-32a3-43bd-9034-4df343e50000"
            },
            "updateAt": "2020-10-15T12:06:23+02:00",
            "manually": false,
            "removeLevelManually": false
        },
        "type": "OpenLoyalty.Domain.User.Event.CustomerWasMovedToLevel",
        "recorderOn": "2020-10-15T10:06:23+00:00"
    }
