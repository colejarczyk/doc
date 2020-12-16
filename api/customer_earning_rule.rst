Customer Earning API
====================

These endpoints will allow you to easily viewing active earning rules.

.. note::

    Each role in the Open Loyalty has individual endpoints to viewing active earning rules.



Return all active earning rules
-------------------------------

To view active earning rules, you need to call the ``/api/<storeCode>/customer/earningRule`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET  /api/<storeCode>/customer/earningRule

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store to get the earning rules from.               |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/earningRule \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "earningRules": [
        {
          "levels": [
            "000096cf-32a3-43bd-9034-4df343e5fd93"
          ],
          "segments": [],
          "earningRuleId": "00000000-0000-474c-b092-b0dd880c0121",
          "name": "Facebook like test rule",
          "description": "sth",
          "active": true,
          "startAt": "2018-01-19T09:45:00+0100",
          "endAt": "2018-03-19T09:45:00+0100",
          "allTimeActive": false,
          "usages": [],
          "eventName": "facebook_like",
          "pointsAmount": 100,
          "limit": {},
          "type": "custom_event",
          "usageUrl": "http://backend.openloyalty.test.openloyalty.io/api/v1/earnRule/facebook_like/customer/:customerId",
          "segmentNames": [],
          "levelNames": {
            "000096cf-32a3-43bd-9034-4df343e5fd93": "level0"
          }
        },
        {
          "levels": [
            "000096cf-32a3-43bd-9034-4df343e5fd93"
          ],
          "segments": [],
          "earningRuleId": "7664138c-b5a4-4dcd-80ba-0049a92166db",
          "name": "name",
          "description": "description",
          "active": true,
          "allTimeActive": true,
          "usages": [],
          "eventName": "custom_event_name",
          "pointsAmount": 1,
          "limit": {
            "active": false
          },
          "type": "custom_event",
          "usageUrl": "http://backend.openloyalty.test.openloyalty.io/api/v1/earnRule/custom_event_name/customer/:customerId",
          "segmentNames": [],
          "levelNames": {
            "000096cf-32a3-43bd-9034-4df343e5fd93": "level0"
          }
        },
        {
          "levels": [
            "000096cf-32a3-43bd-9034-4df343e5fd93"
          ],
          "segments": [],
          "earningRuleId": "7d482776-318a-48dd-90cd-6b3f06a3f4e8",
          "name": "sdgsdgsdg",
          "description": "description",
          "active": true,
          "allTimeActive": true,
          "usages": [],
          "eventName": "custom_event_name_1",
          "pointsAmount": 1,
          "limit": {
            "active": false
          },
          "type": "custom_event",
          "usageUrl": "http://backend.openloyalty.test.openloyalty.io/api/v1/earnRule/custom_event_name_1/customer/:customerId",
          "segmentNames": [],
          "levelNames": {
            "000096cf-32a3-43bd-9034-4df343e5fd93": "level0"
          }
        }
      ],
      "currency": "eur"
    }



Use a custom event earning rule
-------------------------------

To trigger custom event earning rules, you need to call the ``/api/<storeCode>/customer/earningRule/<eventName>`` endpoint with the ``POST`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    POST  /api/<storeCode>/customer/earningRule/<eventName>

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the earning rule belongs to.                 |
+------------------------------------+----------------+----------------------------------------------------------------+
| eventName                          | string         |  Name of custom event                                          |
+------------------------------------+----------------+----------------------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/earningRule/customerAttendedEvent \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
     "points": 12
    }
