Analytics API
=============

These endpoints will allow you to easily analyze your data in Open Loyalty.

Getting the number of registered customers
--------------------------------------

To get the number of registered customers in a loyalty program, you need to call the ``/api/<storeCode>/admin/analytics/customers``
endpoint with the ``GET`` method. Additionally, the method returns the number of registered customers for each of the following past intervals (day, week, month, year).

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/admin/analytics/customers

+----------------------+----------------+--------------------------------------------+
| Parameter            | Parameter type |  Description                               |
+======================+================+============================================+
| Authorization        | header         | Token received during authentication       |
+----------------------+----------------+--------------------------------------------+
| <storeCode>          | query          | Code of the store to get the analytics of. |
+----------------------+----------------+--------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/analytics/customers \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.
    
Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "total": 10,
        "intervals": {
            "in_1_days": 0,
            "in_7_days": 0,
            "in_30_days": 0,
            "in_365_days": 0
        }
    }

Getting the number of spent and transferred points
--------------------------------------------------

To retrieve the number of spent and transferred points, you need to call the ``/api/<storeCode>/admin/analytics/points`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/admin/analytics/points

+----------------------+----------------+--------------------------------------------+
| Parameter            | Parameter type |  Description                               |
+======================+================+============================================+
| Authorization        | header         | Token received during authentication       |
+----------------------+----------------+--------------------------------------------+
| <storeCode>          | query          | Code of the store to get the analytics of. |
+----------------------+----------------+--------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/analytics/points \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."
        
.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "totalSpendingTransfers": 1,
      "totalPointsSpent": 100
    }

Getting information about referrals
-----------------------------------

To retrieve the details of referrals, you need to call the ``/api/<storeCode>/admin/analytics/referrals`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/admin/analytics/referrals

+----------------------+----------------+--------------------------------------------+
| Parameter            | Parameter type |  Description                               |
+======================+================+============================================+
| Authorization        | header         | Token received during authentication       |
+----------------------+----------------+--------------------------------------------+
| <storeCode>          | query          | Code of the store to get the analytics of. |
+----------------------+----------------+--------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/analytics/referrals \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.
    
Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "total": 4,
      "totalCompleted": 0,
      "totalRegistered": 0
    }

Getting information about transactions
--------------------------------------

To retrieve information about transactions, you need to call the ``/api/<storeCode>/admin/analytics/transactions`` endpoint with the ``GET`` method.
Additionally, the method returns the number of orders for each of the following past intervals (day, week, month, year).

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/admin/analytics/transactions

+---------------------------------------+----------------+--------------------------------------------+
| Parameter                             | Parameter type |  Description                               |
+=======================================+================+============================================+
| Authorization                         | header         | Token received during authentication       |
+---------------------------------------+----------------+--------------------------------------------+
| <storeCode>                           | query          | Code of the store to get the analytics of. |
+---------------------------------------+----------------+--------------------------------------------+
| excludeCustomersWithoutTransaction    | query          | exclude customers without transaction      |
+---------------------------------------+----------------+--------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/analytics/transactions \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.
    
Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "total": 5,
        "countIntervals": {
            "in_1_days": 0,
            "in_7_days": 0,
            "in_30_days": 0,
            "in_365_days": 0
        },
        "amount": 1126,
        "amountWithoutDeliveryCosts": 1126,
        "currency": "EUR"
    }

Get level statistics
--------------------

To get level statistics, you need to call the ``/api/<storeCode>/admin/analytics/levels`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/admin/analytics/levels

+----------------------+----------------+--------------------------------------------+
| Parameter            | Parameter type |  Description                               |
+======================+================+============================================+
| Authorization        | header         | Token received during authentication       |
+----------------------+----------------+--------------------------------------------+
| <storeCode>          | query          | Code of the store to get the analytics of. |
+----------------------+----------------+--------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/analytics/levels \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "total": 4,
        "levels": [
            {
                "levelId": "e82c96cf-32a3-43bd-9034-4df343e50000",
                "name": "level0",
                "conditionValue": "0.00",
                "store": "",
                "customers": 9
            },
            {
                "levelId": "e82c96cf-32a3-43bd-9034-4df343e51111",
                "name": "level1",
                "conditionValue": "20.00",
                "store": "",
                "customers": 0
            },
            {
                "levelId": "e82c96cf-32a3-43bd-9034-4df343e52222",
                "name": "level2",
                "conditionValue": "200.00",
                "store": "",
                "customers": 0
            },
            {
                "levelId": "e82c96cf-32a3-43bd-9034-4df343e53333",
                "name": "level3",
                "conditionValue": "999.00",
                "store": "",
                "customers": 1
            }
        ]
    }
