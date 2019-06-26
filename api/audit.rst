Audit API
=========

These endpoints will allow you to see the list of actions taken in the Open Loyalty.

Getting log
-----------

To retrieve action log you will need to call the ``/api/audit/log`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/audit/log

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| entityType           | query          | *(optional)* Narrow results to given entity type       |
|                      |                | for example: ``customer``                              |
+----------------------+----------------+--------------------------------------------------------+
| eventType            | query          | *(optional)* Narrow results to given event type        |
|                      |                | for example: ``RegisterCustomer``                      |
+----------------------+----------------+--------------------------------------------------------+
| entityId             | query          | *(optional)* Narrow results to given entity ID         |
+----------------------+----------------+--------------------------------------------------------+
| username             | query          | *(optional)* Narrow results to given username          |
+----------------------+----------------+--------------------------------------------------------+
| auditLogId           | query          | *(optional)* Narrow results to given audit log ID      |
+----------------------+----------------+--------------------------------------------------------+
| createdAtFrom        | query          | *(optional)* For example ``2017-09-27``                |
+----------------------+----------------+--------------------------------------------------------+
| createdAtTo          | query          | *(optional)* For example ``2017-09-27``                |
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

    curl http://localhost:8181/api/audit/log \
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
      "logs": [
        {
          "auditLogId": {
            "auditLogId": "916e963e-dd14-4ef8-849a-e5b54779657d"
          },
          "createdAt": "2017-09-21T13:54:05+0200",
          "eventType": "MoveCustomerToLevel",
          "entityType": "customer",
          "entityId": "00000000-0000-474c-b092-b0dd880c07e1",
          "username": "<notlogged>",
          "data": [
            "000096cf-32a3-43bd-9034-4df343e5fd93"
          ]
        },
        {
          "auditLogId": {
            "auditLogId": "1efe9c57-c42f-41a1-988c-c4f5b65382d8"
          },
          "createdAt": "2017-09-21T13:54:05+0200",
          "eventType": "RegisterCustomer",
          "entityType": "customer",
          "entityId": "00000000-0000-474c-b092-b0dd880c07e1",
          "username": "<notlogged>",
          "data": {
            "firstName": "John",
            "lastName": "Doe",
            "gender": "male",
            "phone": "11111",
            "email": "user@oloy.com",
            "birthDate": 653011200,
            "createdAt": 1470646394,
            "company": {
              "name": "test",
              "nip": "nip"
            },
            "loyaltyCardNumber": "000000",
            "address": {
              "street": "Dmowskiego",
              "address1": "21",
              "city": "Wrocław",
              "country": "pl",
              "postal": "50-300",
              "province": "Dolnośląskie"
            }
          }
        }
      ],
      "total": 92
    }

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/audit/log \
        -G \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "entityType=customer" \
        -d "page=2" \
        -d "perPage=2" \
        -d "sort=username" \
        -d "direction=DESC"

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "logs": [
        {
          "auditLogId": {
            "auditLogId": "b6781066-a292-4043-bd14-52998ee10691"
          },
          "createdAt": "2017-09-21T13:54:05+0200",
          "eventType": "ActivateCustomer",
          "entityType": "customer",
          "entityId": "00000000-0000-474c-b092-b0dd880c07e1",
          "username": "<notlogged>",
          "data": []
        },
        {
          "auditLogId": {
            "auditLogId": "4574e09b-280c-4e5d-bdd2-327589c714da"
          },
          "createdAt": "2017-09-21T13:54:05+0200",
          "eventType": "MoveCustomerToLevel",
          "entityType": "customer",
          "entityId": "00000000-0000-474c-b092-b0dd880c07e2",
          "username": "<notlogged>",
          "data": [
            "000096cf-32a3-43bd-9034-4df343e5fd93"
          ]
        }
      ],
      "total": 92
    }
