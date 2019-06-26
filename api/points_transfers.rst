Points transfers
================

These endpoints will allow you to easily manage Points transfers.


Get a complete list of Points transfers
---------------------------------------

To retrieve a paginated list of Points transfers you will need to call the ``/api/points/transfer`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET  /api/points/transfer

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| customerFirstName                   | query          | *(optional)* First Name                           |
+-------------------------------------+----------------+---------------------------------------------------+
| customerLastName                    | query          | *(optional)* Last Name                            |
+-------------------------------------+----------------+---------------------------------------------------+
| customerPhone                       | query          | *(optional)* Customer Phone                       |
+-------------------------------------+----------------+---------------------------------------------------+
| customerEmail                       | query          | *(optional)* Customer Email                       |
+-------------------------------------+----------------+---------------------------------------------------+
| customerId                          | query          | *(optional)* Customer ID                          |
+-------------------------------------+----------------+---------------------------------------------------+
| state[]                             | query          | *(optional)* Possible values: active, expired     |
+-------------------------------------+----------------+---------------------------------------------------+
| type                                | query          | *(optional)* Possible values: adding, spending,   |
|                                     |                | p2p_adding, p2p_spending                          |
+-------------------------------------+----------------+---------------------------------------------------+
| page                                | query          | *(optional)* Start from page, by default 1        |
+-------------------------------------+----------------+---------------------------------------------------+
| perPage                             | query          | *(optional)* Number of items to display per page, |
|                                     |                | by default = 10                                   |
+-------------------------------------+----------------+---------------------------------------------------+
| sort                                | query          | *(optional)* Sort by column name                  |
+-------------------------------------+----------------+---------------------------------------------------+
| direction                           | query          | *(optional)* Direction of sorting [ASC, DESC],    |
|                                     |                | by default = ASC                                  |
+-------------------------------------+----------------+---------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/points/transfer \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

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
                "pointsTransferId": "ae1c49b1-02ab-4626-982d-71b544b01136",
                "accountId": "49a218ab-71ba-4f7f-8f4e-407df5f84b11",
                "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
                "customerFirstName": "John",
                "customerLastName": "Doe",
                "customerLoyaltyCardNumber": "47834433524",
                "customerEmail": "user@oloy.com",
                "customerPhone": "+48234234000",
                "createdAt": "2018-09-13T16:37:33+0200",
                "expiresAt": "2018-10-13T16:37:33+0200",
                "value": 10,
                "state": "active",
                "type": "adding",
                "comment": "Event - First Purchase - 10",
                "issuer": "system"
            },
            {
                "pointsTransferId": "cd470d77-a08e-4c62-9f47-da180524f683",
                "accountId": "49a218ab-71ba-4f7f-8f4e-407df5f84b11",
                "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
                "customerFirstName": "John",
                "customerLastName": "Doe",
                "customerLoyaltyCardNumber": "47834433524",
                "customerEmail": "user@oloy.com",
                "customerPhone": "+48234234000",
                "createdAt": "2018-09-13T16:37:33+0200",
                "expiresAt": "2018-10-13T16:37:33+0200",
                "value": 6.9,
                "state": "active",
                "type": "adding",
                "transactionId": {
                    "transactionId": "00000000-0000-1111-0000-000000000003"
                },
                "comment": "General spending rule - 2.3",
                "issuer": "system",
                "transactionDocumentNumber": "456",
                "transaction": {
                    "grossValue": 3,
                    "items": [
                        {
                            "sku": {
                                "code": "SKU1"
                            },
                            "name": "item 1",
                            "quantity": 1,
                            "grossValue": 1,
                            "category": "aaa",
                            "labels": [
                                {
                                    "key": "test",
                                    "value": "label"
                                },
                                {
                                    "key": "test",
                                    "value": "label2"
                                }
                            ],
                            "maker": "sss"
                        },
                        {
                            "sku": {
                                "code": "SKU2"
                            },
                            "name": "item 2",
                            "quantity": 2,
                            "grossValue": 2,
                            "category": "bbb",
                            "labels": [],
                            "maker": "ccc"
                        }
                    ]
                }
            }
        ],
        "total": 2
    }
  

Get a complete list of Points transfers (seller)
------------------------------------------------

To retrieve a paginated list of Points transfers you will need to call the ``/api/seller/points/transfer`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET  /api/seller/points/transfer

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| customerFirstName                   | query          | *(optional)* First Name                           |
+-------------------------------------+----------------+---------------------------------------------------+
| customerLastName                    | query          | *(optional)* Last Name                            |
+-------------------------------------+----------------+---------------------------------------------------+
| customerPhone                       | query          | *(optional)* Customer Phone                       |
+-------------------------------------+----------------+---------------------------------------------------+
| customerEmail                       | query          | *(optional)* Customer Email                       |
+-------------------------------------+----------------+---------------------------------------------------+
| customerId                          | query          | *(optional)* Customer ID                          |
+-------------------------------------+----------------+---------------------------------------------------+
| state                               | query          | *(optional)* Possible values: active, expired,    |
|                                     |                | pending                                           |
+-------------------------------------+----------------+---------------------------------------------------+
| type                                | query          | *(optional)* Possible values: adding, spending    |
+-------------------------------------+----------------+---------------------------------------------------+
| page                                | query          | *(optional)* Start from page, by default 1        |
+-------------------------------------+----------------+---------------------------------------------------+
| perPage                             | query          | *(optional)* Number of items to display per page, |
|                                     |                | by default = 10                                   |
+-------------------------------------+----------------+---------------------------------------------------+
| sort                                | query          | *(optional)* Sort by column name                  |
+-------------------------------------+----------------+---------------------------------------------------+
| direction                           | query          | *(optional)* Direction of sorting [ASC, DESC],    |
|                                     |                | by default = ASC                                  |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/points/transfer \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

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
                "pointsTransferId": "cd470d77-a08e-4c62-9f47-da180524f683",
                "accountId": "49a218ab-71ba-4f7f-8f4e-407df5f84b11",
                "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
                "customerFirstName": "John",
                "customerLastName": "Doe",
                "customerLoyaltyCardNumber": "47834433524",
                "customerEmail": "user@oloy.com",
                "customerPhone": "+48234234000",
                "createdAt": "2018-09-13T16:37:33+0200",
                "expiresAt": "2018-10-13T16:37:33+0200",
                "value": 6.9,
                "state": "active",
                "type": "adding",
                "transactionId": {
                    "transactionId": "00000000-0000-1111-0000-000000000003"
                },
                "comment": "General spending rule - 2.3",
                "issuer": "system",
                "transactionDocumentNumber": "456",
                "transaction": {
                    "grossValue": 3,
                    "items": [
                        {
                            "sku": {
                                "code": "SKU1"
                            },
                            "name": "item 1",
                            "quantity": 1,
                            "grossValue": 1,
                            "category": "aaa",
                            "labels": [
                                {
                                    "key": "test",
                                    "value": "label"
                                },
                                {
                                    "key": "test",
                                    "value": "label2"
                                }
                            ],
                            "maker": "sss"
                        },
                        {
                            "sku": {
                                "code": "SKU2"
                            },
                            "name": "item 2",
                            "quantity": 2,
                            "grossValue": 2,
                            "category": "bbb",
                            "labels": [],
                            "maker": "ccc"
                        }
                    ]
                }
            },
            {
                "pointsTransferId": "e82c96cf-32a3-43bd-9034-4df343e5f333",
                "accountId": "cdcc55e9-cfab-4840-991d-0e0f25ba2141",
                "customerId": "00000000-0000-474c-b092-b0dd880c07e2",
                "customerFirstName": "Jane",
                "customerLastName": "Doe",
                "customerLoyaltyCardNumber": "0000",
                "customerEmail": "user-temp@oloy.com",
                "customerPhone": "+48345345000",
                "createdAt": "2018-09-13T16:37:35+0200",
                "expiresAt": "2018-09-13T16:37:35+0200",
                "value": 100,
                "state": "active",
                "type": "spending",
                "comment": "Example comment",
                "issuer": "system"
            }
        ],
        "total": 2
    }

Get a complete list of Points transfers (customer)
------------------------------------------------

To retrieve a paginated list of Points transfers you will need to call the ``/api/customer/points/transfer`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET  /api/customer/points/transfer

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| state                               | query          | *(optional)* Possible values: active, expired,    |
|                                     |                | pending                                           |
+-------------------------------------+----------------+---------------------------------------------------+
| type                                | query          | *(optional)* Possible values: adding, spending    |
+-------------------------------------+----------------+---------------------------------------------------+
| page                                | query          | *(optional)* Start from page, by default 1        |
+-------------------------------------+----------------+---------------------------------------------------+
| perPage                             | query          | *(optional)* Number of items to display per page, |
|                                     |                | by default = 10                                   |
+-------------------------------------+----------------+---------------------------------------------------+
| sort                                | query          | *(optional)* Sort by column name                  |
+-------------------------------------+----------------+---------------------------------------------------+
| direction                           | query          | *(optional)* Direction of sorting [ASC, DESC],    |
|                                     |                | by default = ASC                                  |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/points/transfer \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

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
                "pointsTransferId": "ae1c49b1-02ab-4626-982d-71b544b01136",
                "accountId": "49a218ab-71ba-4f7f-8f4e-407df5f84b11",
                "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
                "customerFirstName": "John",
                "customerLastName": "Doe",
                "customerLoyaltyCardNumber": "47834433524",
                "customerEmail": "user@oloy.com",
                "customerPhone": "+48234234000",
                "createdAt": "2018-09-13T16:37:33+0200",
                "expiresAt": "2018-10-13T16:37:33+0200",
                "value": 10,
                "state": "active",
                "type": "adding",
                "comment": "Event - First Purchase - 10",
                "issuer": "system"
            },
            {
                "pointsTransferId": "cd470d77-a08e-4c62-9f47-da180524f683",
                "accountId": "49a218ab-71ba-4f7f-8f4e-407df5f84b11",
                "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
                "customerFirstName": "John",
                "customerLastName": "Doe",
                "customerLoyaltyCardNumber": "47834433524",
                "customerEmail": "user@oloy.com",
                "customerPhone": "+48234234000",
                "createdAt": "2018-09-13T16:37:33+0200",
                "expiresAt": "2018-10-13T16:37:33+0200",
                "value": 6.9,
                "state": "active",
                "type": "adding",
                "transactionId": {
                    "transactionId": "00000000-0000-1111-0000-000000000003"
                },
                "comment": "General spending rule - 2.3",
                "issuer": "system",
                "transactionDocumentNumber": "456",
                "transaction": {
                    "grossValue": 3,
                    "items": [
                        {
                            "sku": {
                                "code": "SKU1"
                            },
                            "name": "item 1",
                            "quantity": 1,
                            "grossValue": 1,
                            "category": "aaa",
                            "labels": [
                                {
                                    "key": "test",
                                    "value": "label"
                                },
                                {
                                    "key": "test",
                                    "value": "label2"
                                }
                            ],
                            "maker": "sss"
                        },
                        {
                            "sku": {
                                "code": "SKU2"
                            },
                            "name": "item 2",
                            "quantity": 2,
                            "grossValue": 2,
                            "category": "bbb",
                            "labels": [],
                            "maker": "ccc"
                        }
                    ]
                }
            }
        ],
        "total": 2
    }


Add points to customer
----------------------

To add a new points you will need to call the ``/api/points/transfer/add`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/points/transfer/add

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer[customer]                  | query          | Customer ID                                       |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer[points]                    | query          | How many points customer can get                  |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer[comment]                   | query          | *(optional)* Comment                              |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer                            | query          | *(optional)* Points transfer ID                   |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/points/transfer/add \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "transfer=8947546c-c2a4-4ef2-9271-47b3fc28f663" \
        -d "transfer[customer]=b9af6a8c-9cc5-4924-989c-e4af614ab2a3" \
        -d "transfer[points]=9"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "pointsTransferId": "32132863-3d1e-4a94-8bb4-6e42e3c96c0b"
    }


Spend customer points
---------------------

To spend customer points you will need to call the ``/api/points/transfer/spend`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/points/transfer/spend

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer[customer]                  | query          | Customer ID                                       |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer[points]                    | query          | How many points customer can get                  |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer[comment]                   | query          | *(optional)* Comment                              |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer                            | query          | *(optional)* Points transfer ID                   |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/points/transfer/spend \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "transfer=8947546c-c2a4-4ef2-9271-47b3fc28f663" \
        -d "transfer[customer]=b9af6a8c-9cc5-4924-989c-e4af614ab2a3" \
        -d "transfer[points]=1"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "pointsTransferId": "b97a31fe-9bc9-4fff-a467-487f2c316371"
    }


Transfer points between customers (admin)
-----------------------------------------

To transfer points between customers you will need to call the ``/api/admin/p2p-points-tranfer`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/p2p-points-tranfer

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer[sender]                    | query          | email/phone or uuid of customer from whom points  |
|                                     |                | will be transferred                               |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer[receiver]                  | query          | email/phone or uuid of customer who will get      |
|                                     |                | points                                            |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer[points]                    | query          | How many points will be transferred               |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/p2p-points-tranfer \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "transfer[sender]=b9af6a8c-9cc5-4924-989c-e4af614ab2a3" \
        -d "transfer[receiver]=b9af6a8c-9cc5-4924-989c-e4af614ab3c5" \
        -d "transfer[points]=100"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "pointsTransferId": "b97a31fe-9bc9-4fff-a467-487f2c316371"
    }

.. note::

    Returned pointsTransferId is a uuid of created P2P spend points transfer.


Transfer points between customers (customer)
--------------------------------------------

To transfer points between logged in customer and another customer you will need to call the ``/api/customer/points/p2p-transfer`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/points/p2p-transfer

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer[receiver]                  | query          | email/phone or uuid of customer who will get      |
|                                     |                | points                                            |
+-------------------------------------+----------------+---------------------------------------------------+
| transfer[points]                    | query          | How many points will be transferred               |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/p2p-points-tranfer \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "transfer[receiver]=b9af6a8c-9cc5-4924-989c-e4af614ab3c5" \
        -d "transfer[points]=100"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "pointsTransferId": "b97a31fe-9bc9-4fff-a467-487f2c316371"
    }

.. note::

    Returned pointsTransferId is a uuid of created P2P spend points transfer.


Cancel specific points transfer
-------------------------------

To cancel specific points transfer you will need to call the ``/api/points/transfer/<transfer>/cancel`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/points/transfer/<transfer>/cancel

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <transfer>                          | query          | Points transfer ID                                |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/points/transfer/313cf0c1-5376-4f66-9de3-77943760423a/cancel \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    []
