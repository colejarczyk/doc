Customer Earning API
====================

These endpoints will allow you to easily viewing active earning rules.

.. note::

    Each role in the Open Loyalty has individual endpoints to viewing active earning rules.


Method will return all active earning rules.
--------------------------------------------

To viewing active earning rules you will need to call the ``/api/customer/earningRule`` endpoint with the ``GET`` method.



Definition
^^^^^^^^^^

.. code-block:: text

    GET  /api/customer/earningRule

+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                                                  |
+====================================+================+===============================================================================================+
| Authorization                      | header         |  Token received during authentication                                                         |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+



Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/earningRule \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9..."        

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

Exemplary Response
^^^^^^^^^^^^^^^^^^

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
