Analytics API
=============

These endpoints will allow you to easily analyze your data in the Open Loyalty.

Getting number of registered customers
--------------------------------------

To retrieve number of registered customers in the loyalty program you will need to call the ``/api/admin/analytics/customer`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/analytics/customers

+----------------------+----------------+------------------------------------------+
| Parameter            | Parameter type |  Description                             |
+======================+================+==========================================+
| Authorization        | header         | Token received during authentication     |
+----------------------+----------------+------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/analytics/customers \
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
      "total": 2
    }

Getting number of spent and transferred points
----------------------------------------------

To retrieve a number of spent and transferred points you will need to call the ``/api/admin/analytics/points`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/analytics/points

+----------------------+----------------+------------------------------------------+
| Parameter            | Parameter type |  Description                             |
+======================+================+==========================================+
| Authorization        | header         | Token received during authentication     |
+----------------------+----------------+------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/analytics/points \
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
      "totalSpendingTransfers": 1,
      "totalPointsSpent": 100
    }

Getting an information about referrals
--------------------------------------

To retrieve the details of referrals you will need to call the ``/api/admin/analytics/referrals`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/analytics/referrals

+----------------------+----------------+------------------------------------------+
| Parameter            | Parameter type |  Description                             |
+======================+================+==========================================+
| Authorization        | header         | Token received during authentication     |
+----------------------+----------------+------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/analytics/referrals \
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
      "total": 4,
      "totalCompleted": 0,
      "totalRegistered": 0
    }

Getting an information about transactions
-----------------------------------------

To retrieve an information about transactions you will need to call the ``/api/admin/analytics/transactions`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/analytics/transactions

+----------------------+----------------+------------------------------------------+
| Parameter            | Parameter type |  Description                             |
+======================+================+==========================================+
| Authorization        | header         | Token received during authentication     |
+----------------------+----------------+------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/analytics/transactions \
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
      "total": 2,
      "amount": 6,
      "amountWithoutDeliveryCosts": 6,
      "currency": "eur"
    }
