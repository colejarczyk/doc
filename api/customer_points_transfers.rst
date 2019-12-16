Customer Points transfers
=========================

These endpoints will allow you to see Customer Points transfers list.

List of all logged in customer points transfer
----------------------------------------------

To retrieve list of points transfer by a specific customer use ``/api/customer/points/transfer`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET  /api/customer/points/transfer

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| state                | query          | Set 1 if always active, otherwise 0                    |
+----------------------+----------------+--------------------------------------------------------+
| type                 | query          | Current points status: adding or spending              |
+----------------------+----------------+--------------------------------------------------------+
| page                 | query          | *(optional)* Start from page, by default 1             |
+----------------------+----------------+--------------------------------------------------------+
| perPage              | query          | *(optional)* Number of items to display per page,      |
|                      |                | by default = 10                                        |
+----------------------+----------------+--------------------------------------------------------+
| sort                 | query          | *(optional)* Sort by column name,                      |
|                      |                | by default = firstName                                 |
+----------------------+----------------+--------------------------------------------------------+
| direction            | query          | *(optional)* Direction of sorting [ASC, DESC],         |
|                      |                | by default = ASC                                       |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/points/transfer \
        -X "GET" \
        -H "Accept:application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "transfers": [
        {
          "pointsTransferId": "e82c96cf-32a3-43bd-9034-4df343e5f211",
          "accountId": "adbdb586-317b-4bed-8cc0-346199064d45",
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "customerFirstName": "John",
          "customerLastName": "Doe",
          "customerEmail": "user@oloy.com",
          "customerPhone": "11111",
          "createdAt": "2018-01-21T09:45:05+0100",
          "value": 100,
          "state": "active",
          "type": "adding",
          "issuer": "system",
          "expireAt": "2018-02-20T09:45:05+0100"
        },
        {
          "pointsTransferId": "44b4a504-d62e-49c2-8e35-7d8a19d2642e",
          "accountId": "adbdb586-317b-4bed-8cc0-346199064d45",
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "customerFirstName": "John",
          "customerLastName": "Doe",
          "customerEmail": "user@oloy.com",
          "customerPhone": "11111",
          "createdAt": "2018-02-19T09:45:05+0100",
          "value": 6.9,
          "state": "active",
          "type": "adding",
          "transactionId": {
            "transactionId": "00000000-0000-1111-0000-000000000003"
          },
          "issuer": "system",
          "expireAt": "2018-03-21T09:45:05+0100",
          "transactionDocumentNumber": "456"
        }
      ],
      "total": 2
    }
