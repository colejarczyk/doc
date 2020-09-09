Transactions
============

These endpoints will allow you to easily manage transactions.



Import transactions
-------------------

To import an XML file with transactions, you need to call the ``/api/admin/transaction/import`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/transaction/import

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| file[file]                          | query          | XML file with transactions                        |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/transaction/import \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "file[file]=C:\\fakepath\\transaction.xml"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "items": [
        {
          "status": "error",
          "message": "Convert exception: Value \"00000000-0000-474c-1111-b0dd880c07e\" is not a valid UUID.",
          "identifier": "0001_pos2_zzleID"
        },
        {
          "status": "success",
          "processImportResult": {
            "object": {
              "transactionId": "98b15ef5-94ad-43ef-9984-0d41197d14e6"
            }
          },
          "identifier": "id_bez_tymrazem"
        }
      ],
      "totalProcessed": 2,
      "totalSuccess": 1,
      "totalFailed": 1
    }

Match transactions with the customers by importing a XML file
-------------------------------------------------------------

In order to match many transactions to many customers using an XML file, you need to call the ``/admin/transaction/customer/assign/import`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /admin/transaction/customer/assign/import

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| file[file]                          | query          | XML file with transactions                        |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/transaction/customer/assign/import \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "file[file]=C:\\fakepath\\match-customer.xml"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example XML
^^^^^^^^^^^

.. code-block:: xml
    <?xml version="1.0" encoding="UTF-8"?>
    <matchCustomers>
        <matchCustomer>
           <customerId>00000000-0000-474c-b092-b0dd880c07e2</customerId>
           <customerEmail>john.doe@example.com</customerEmail>
           <customerPhoneNumber>+48888888888</customerPhoneNumber>
           <customerLoyaltyCardNumber>936592735</customerLoyaltyCardNumber>
           <transactionDocumentNumber>123</transactionDocumentNumber>
        </matchCustomer>
    </matchCustomers>

.. note::

    Only one customer* field is required (customerId, customerEmail, customerPhoneNumber, customerLoyaltyCardNumber).

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "items": [
            {
                "status": "error",
                "message": "(match_customer-2019-11-08_1005-5dc52fe92bc59.xml) Processing exception: Customer is already assigned to this transaction",
                "identifier": "123"
            }
        ],
        "totalProcessed": 1,
        "totalSuccess": 0,
        "totalFailed": 1
    }



Assign a customer to a specific transaction (admin)
---------------------------------------------------

To assign a customer to a specific transaction, you need to call the ``/api/admin/transaction/customer/assign`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/transaction/customer/assign

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[transactionDocumentNumber]   | query          | Transaction Document Number                       |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[customerId]                  | query          | Customer ID                                       |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[customerLoyaltyCardNumber]   | query          | Customer Loyalty Number                           |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[customerPhoneNumber]         | query          | Customer Phone Number                             |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/transaction/customer/assign \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "assign[transactionDocumentNumber]=888" \
        -d "assign[customerId]=57524216-c059-405a-b951-3ab5c49bae14" \
        -d "assign[customerLoyaltyCardNumber]=333" \
        -d "assign[customerPhoneNumber]=333333"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "transactionId": "00000000-0000-1111-0000-000000000002"
    }

Example Error Response
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "form": {
        "children": {
          "transactionDocumentNumber": {
            "errors": [
              "Customer is already assigned to this transaction"
            ]
          },
          "customerId": {},
          "customerLoyaltyCardNumber": {},
          "customerPhoneNumber": {}
        }
      },
      "errors": []
    }



Assign a customer to a specific transaction (customer)
------------------------------------------------------

To assign a logged-in customer to a specific transaction, you need to call the ``/api/customer/transaction/customer/assign`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/transaction/customer/assign

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[transactionDocumentNumber]   | query          | Transaction Document Number                       |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[customerId]                  | query          | Customer ID                                       |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[customerLoyaltyCardNumber]   | query          | Customer Loyalty Number                           |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[customerPhoneNumber]         | query          | Customer Phone Number                             |
+-------------------------------------+----------------+---------------------------------------------------+

.. note::

    If you are using the auto-generated docs, you may see there are other fields in the assign[] object.
    They are ignored in this endpoint. Do not use them in your application as they will be removed in a future version.

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/transaction/customer/assign \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."
        -d "assign[transactionDocumentNumber]=888"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "transactionId": "9f805211-9326-4b47-b5a6-8155d6ae9d2c"
    }



Assign a customer to specific transaction (seller)
--------------------------------------------------

To assign a customer to a specific transaction, you need to call the ``/api/pos/transaction/customer/assign`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/pos/transaction/customer/assign

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[transactionDocumentNumber]   | query          | Transaction Document Number                       |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[customerId]                  | query          | Customer ID                                       |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[customerLoyaltyCardNumber]   | query          | Customer Loyalty Number                           |
+-------------------------------------+----------------+---------------------------------------------------+
| assign[customerPhoneNumber]         | query          | Customer Phone Number                             |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/pos/transaction/customer/assign \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."
        -d "assign[transactionDocumentNumber]=123" \
        -d "assign[customerId]=57524216-c059-405a-b951-3ab5c49bae14" \
        -d "assign[customerLoyaltyCardNumber]=333" \
        -d "assign[customerPhoneNumber]=333333"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "transactionId": "00000000-0000-1111-0000-000000000005"
    }



Get a list of transactions (customer)
-------------------------------------

To retrieve a complete or filtered list of all transactions a customer has access to, you need to call the ``/api/customer/transaction`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/transaction

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| documentType                        | query          | *(optional)* Document Type                        |
+-------------------------------------+----------------+---------------------------------------------------+
| customerId                          | query          | *(optional)* Customer ID                          |
+-------------------------------------+----------------+---------------------------------------------------+
| documentNumber                      | query          | *(optional)* Document Number                      |
+-------------------------------------+----------------+---------------------------------------------------+
| posId                               | query          | *(optional)* POS ID                               |
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

.. note::

    If you are using the auto-generated docs, you may see there are other params, named ``customerData_*``.
    They are not used in this endpoint. Do not use them in your application as they will be removed in a future version.

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/transaction \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
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
      "transactions": [
        {
          "grossValue": 3,
          "transactionId": "00000000-0000-1111-0000-000000000003",
          "documentNumber": "456",
          "purchaseDate": "2018-02-20T09:45:04+0100",
          "purchasePlace": "wroclaw",
          "documentType": "sell",
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "assignedToCustomerDate": "1970-01-01T01:00:00+01:00",
          "customerData": {
            "email": "user@example.com",
            "name": "Jan Nowak",
            "nip": "aaa",
            "phone": "123",
            "loyaltyCardNumber": "sa2222",
            "address": {
              "street": "Bagno",
              "address1": "12",
              "province": "Mazowieckie",
              "city": "Warszawa",
              "postal": "00-800",
              "country": "PL"
            }
          },
          "labels": [
            {
              "key": "scan_id",
              "value": "123"
            }
          ],
          "items": [
            {
              "sku": {
                "code": "SKU1"
              },
              "name": "item 1",
              "quantity": 1,
              "grossValue": 1,
              "category": "aaa",
              "maker": "sss",
              "labels": [
                {
                  "key": "test",
                  "value": "label"
                },
                {
                  "key": "test",
                  "value": "label2"
                }
              ]
            },
            {
              "sku": {
                "code": "SKU2"
              },
              "name": "item 2",
              "quantity": 2,
              "grossValue": 2,
              "category": "bbb",
              "maker": "ccc",
              "labels": []
            }
          ],
          "currency": "eur",
          "pointsEarned": 6.9
        },
        {
          "grossValue": 3,
          "transactionId": "00000000-0000-1111-0000-000000000005",
          "documentNumber": "888",
          "purchaseDate": "2018-02-20T09:45:04+0100",
          "purchasePlace": "wroclaw",
          "documentType": "sell",
          "customerId": "57524216-c059-405a-b951-3ab5c49bae14",
          "assignedToCustomerDate": "1970-01-01T01:00:00+01:00",
          "customerData": {
            "email": "o@lo.com",
            "name": "Jan Nowak",
            "nip": "aaa",
            "phone": "123",
            "loyaltyCardNumber": "sa21as222",
            "address": {
              "street": "Bagno",
              "address1": "12",
              "province": "Mazowieckie",
              "city": "Warszawa",
              "postal": "00-800",
              "country": "PL"
            }
          },
          "labels": [
            {
              "key": "scan_id",
              "value": "343"
            }
          ],
          "items": [
            {
              "sku": {
                "code": "SKU1"
              },
              "name": "item 1",
              "quantity": 1,
              "grossValue": 1,
              "category": "aaa",
              "maker": "sss",
              "labels": [
                {
                  "key": "test",
                  "value": "label"
                },
                {
                  "key": "test",
                  "value": "label2"
                }
              ]
            },
            {
              "sku": {
                "code": "SKU2"
              },
              "name": "item 2",
              "quantity": 2,
              "grossValue": 2,
              "category": "bbb",
              "maker": "ccc",
              "labels": []
            }
          ],
          "currency": "eur",
          "pointsEarned": 6
        }
      ],
      "total": 2
    }



Get transaction details (customer)
----------------------------------

To retrieve transaction details, you need to call the ``/api/customer/transaction/<transaction>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/transaction/<transaction>

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <transaction>                       | query          | Transaction ID                                    |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/transaction/00000000-0000-1111-0000-000000000003 \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
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
      "grossValue": 3,
      "transactionId": "00000000-0000-1111-0000-000000000003",
      "documentNumber": "456",
      "purchaseDate": "2018-02-20T09:45:04+0100",
      "purchasePlace": "wroclaw",
      "documentType": "sell",
      "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
      "assignedToCustomerDate": "1970-01-01T01:00:00+01:00",
      "customerData": {
        "email": "user@example.com",
        "name": "Jan Nowak",
        "nip": "aaa",
        "phone": "123",
        "loyaltyCardNumber": "sa2222",
        "address": {
          "street": "Bagno",
          "address1": "12",
          "province": "Mazowieckie",
          "city": "Warszawa",
          "postal": "00-800",
          "country": "PL"
        }
      },
      "labels": [
        {
          "key": "scan_id",
          "value": "123"
        }
      ],
      "items": [
        {
          "sku": {
            "code": "SKU1"
          },
          "name": "item 1",
          "quantity": 1,
          "grossValue": 1,
          "category": "aaa",
          "maker": "sss",
          "labels": [
            {
              "key": "test",
              "value": "label"
            },
            {
              "key": "test",
              "value": "label2"
            }
          ]
        },
        {
          "sku": {
            "code": "SKU2"
          },
          "name": "item 2",
          "quantity": 2,
          "grossValue": 2,
          "category": "bbb",
          "maker": "ccc",
          "labels": []
        }
      ],
      "currency": "eur",
      "pointsEarned": 6.9
    }



Get a list of transactions (seller)
-----------------------------------

To get a complete or filtered list of transactions
you need to call the ``/api/seller/transaction`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/transaction

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_loyaltyCardNumber      | query          | *(optional)* Loyalty Card Number                  |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_name                   | query          | *(optional)* Customer Name                        |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_email                  | query          | *(optional)* Customer Email                       |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_phone                  | query          | *(optional)* Customer Phone                       |
+-------------------------------------+----------------+---------------------------------------------------+
| customerId                          | query          | *(optional)* Customer ID                          |
+-------------------------------------+----------------+---------------------------------------------------+
| documentType                        | query          | *(optional)* Document Type                        |
+-------------------------------------+----------------+---------------------------------------------------+
| documentNumber                      | query          | *(optional)* Document Number                      |
+-------------------------------------+----------------+---------------------------------------------------+
| posId                               | query          | *(optional)* POS ID                               |
+-------------------------------------+----------------+---------------------------------------------------+
| purchaseDateFrom                    | query          | *(optional)* purchase date's lower limit          |
+-------------------------------------+----------------+---------------------------------------------------+
| purchaseDateTo                      | query          | *(optional)* purchase date's upper limit          |
+-------------------------------------+----------------+---------------------------------------------------+
| grossValueFrom                      | query          | *(optional)* transaction gross value lower limit  |
+-------------------------------------+----------------+---------------------------------------------------+
| grossValueTo                        | query          | *(optional)* transaction gross value upper limit  |
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

    curl http://localhost:8181/api/seller/transaction\
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
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
      "transactions": [
         {
      "grossValue": 3,
      "transactionId": "00000000-0000-1111-0000-000000000004",
      "documentNumber": "789",
      "purchaseDate": "2018-02-20T09:45:04+0100",
      "purchasePlace": "wroclaw",
      "documentType": "sell",
      "customerId": "00000000-0000-474c-b092-b0dd880c07e2",
      "assignedToCustomerDate": "1970-01-01T01:00:00+01:00",
      "customerData": {
        "email": "user-temp@example.com",
        "name": "Jan Nowak",
        "nip": "aaa",
        "phone": "123",
        "loyaltyCardNumber": "sa2222",
        "address": {
          "street": "Bagno",
          "address1": "12",
          "province": "Mazowieckie",
          "city": "Warszawa",
          "postal": "00-800",
          "country": "PL"
        }
      },
      "labels": [
        {
          "key": "scan_id",
          "value": "123"
        }
      ],
      "items": [
        {
          "sku": {
            "code": "SKU1"
          },
          "name": "item 1",
          "quantity": 1,
          "grossValue": 1,
          "category": "aaa",
          "maker": "sss",
          "labels": [
            {
              "key": "test",
              "value": "label"
            },
            {
              "key": "test",
              "value": "label2"
            }
          ]
        },
        {
          "sku": {
            "code": "SKU2"
          },
          "name": "item 2",
          "quantity": 2,
          "grossValue": 2,
          "category": "bbb",
          "maker": "ccc",
          "labels": []
        }
      ],
      "currency": "eur"
    },
    {
      "grossValue": 3,
      "transactionId": "00000000-0000-1111-0000-000000000002",
      "documentNumber": "345",
      "purchaseDate": "2018-02-20T09:45:04+0100",
      "purchasePlace": "wroclaw",
      "documentType": "sell",
      "customerId": "57524216-c059-405a-b951-3ab5c49bae14",
      "customerData": {
        "email": "open@example.com",
        "name": "Jan Nowak",
        "nip": "aaa",
        "phone": "123",
        "loyaltyCardNumber": "sa2222",
        "address": {
          "street": "Bagno",
          "address1": "12",
          "province": "Mazowieckie",
          "city": "Warszawa",
          "postal": "00-800",
          "country": "PL"
        }
      },
      "labels": [
        {
          "key": "scan_id",
          "value": "222"
        }
      ],
      "items": [
        {
          "sku": {
            "code": "SKU1"
          },
          "name": "item 1",
          "quantity": 1,
          "grossValue": 1,
          "category": "aaa",
          "maker": "sss",
          "labels": [
            {
              "key": "test",
              "value": "label"
            },
            {
              "key": "test",
              "value": "label2"
            }
          ]
        },
        {
          "sku": {
            "code": "SKU2"
          },
          "name": "item 2",
          "quantity": 2,
          "grossValue": 2,
          "category": "bbb",
          "maker": "ccc",
          "labels": []
        }
      ],
      "currency": "eur",
      "pointsEarned": 6
        }
      ],
      "total": 2
    }



Get customer's transactions (seller)
------------------------------------

To retrieve a list of customer transactions, you need to call the ``/api/seller/transaction/customer/<customer>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

     GET  /api/seller/transaction/customer/<customer>

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <customer>                          | query          | Customer ID                                       |
+-------------------------------------+----------------+---------------------------------------------------+
| documentNumber                      | query          | *(optional)* Filter by Document Number            |
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

    curl http://localhost:8181/api/seller/transaction/customer/4b32a723-9923-46fc-a2bc-d09767e5e59b \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
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
      "transactions": [
        {
          "grossValue": 2200,
          "transactionId": "c13e4e89-2e9a-482d-8ab0-41a8eb9927ed",
          "documentNumber": "214124124130",
          "purchaseDate": "2017-08-23T00:00:00+0200",
          "documentType": "return",
          "customerId": "4b32a723-9923-46fc-a2bc-d09767e5e59b",
          "assignedToCustomerDate": "1970-01-01T01:00:00+01:00",
          "customerData": {
            "email": "tomasztest8@wp.pl",
            "name": "Firstname+Lastname",
            "nip": "00000000000000",
            "phone": "00000000000000",
            "loyaltyCardNumber": "11111111111",
            "address": {
              "street": "Street+name",
              "address1": "123",
              "province": "Dolnoslaskie",
              "city": "Wroclaw",
              "postal": "00-000",
              "country": "PL"
            }
          },
          "labels": [
            {
              "key": "scan_id",
              "value": "333"
            }
          ],
          "items": [
            {
              "sku": {
                "code": "test0101"
              },
              "name": "Product+name",
              "quantity": 1,
              "grossValue": 2200,
              "category": "Category+Name",
              "maker": "Marker+name",
              "labels": [
                {
                  "key": "Label+key",
                  "value": "Label+value"
                }
              ]
            }
          ],
          "excludedLevelCategories": [
            "category_excluded_from_level"
          ],
          "currency": "eur"
        }
      ],
      "total": 1
    }



Get transactions with provided document number (seller)
-------------------------------------------------------

To retrieve a list of transactions with provided document number, you need to call the ``/api/seller/transaction/<documentNumber>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/transaction/<documentNumber>

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <documentNumber>                    | query          | Document Number ID                                |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/transaction/214124124125 \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    This endpoint uses *documentNumber*, your *internal* identifier of a transaction.
    This is not the same as *transactionId* and should be easier to find for the merchant.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "transactions": [
        {
          "grossValue": 1500,
          "transactionId": "d5b1119a-698b-40b4-9ac4-8ef704fa4433",
          "documentNumber": "214124124125",
          "purchaseDate": "2017-08-22T00:00:00+0200",
          "documentType": "sell",
          "customerId": "4b32a723-9923-46fc-a2bc-d09767e5e59b",
          "assignedToCustomerDate": "1970-01-01T01:00:00+01:00",
          "customerData": {
            "email": "tomasztest8@wp.pl",
            "name": "Firstname+Lastname",
            "nip": "00000000000000",
            "phone": "00000000000000",
            "loyaltyCardNumber": "11111111111",
            "address": {
              "street": "Street+name",
              "address1": "123",
              "province": "Dolnoslaskie",
              "city": "Wroclaw",
              "postal": "00-000",
              "country": "PL"
            }
          },
          "labels": [
            {
              "key": "scan_id",
              "value": "123"
            }
          ],
          "items": [
            {
              "sku": {
                "code": "test0101"
              },
              "name": "Product+name",
              "quantity": 1,
              "grossValue": 1500,
              "category": "Category+Name",
              "maker": "Marker+name",
              "labels": [
                {
                  "key": "Label+key",
                  "value": "Label+value"
                }
              ]
            }
          ],
          "excludedLevelCategories": [
            "category_excluded_from_level"
          ],
          "currency": "eur"
        }
      ],
      "total": 1
    }



Get a list of transactions
--------------------------

To retrieve a complete or filtered list of transactions, you need to call the ``/api/transaction`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET  /api/transaction

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_loyaltyCardNumber      | query          | *(optional)* Loyalty Card Number                  |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_name                   | query          | *(optional)* Customer Name                        |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_email                  | query          | *(optional)* Customer Email                       |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_phone                  | query          | *(optional)* Customer Phone                       |
+-------------------------------------+----------------+---------------------------------------------------+
| customerId                          | query          | *(optional)* Customer ID                          |
+-------------------------------------+----------------+---------------------------------------------------+
| documentType                        | query          | *(optional)* Document Type                        |
+-------------------------------------+----------------+---------------------------------------------------+
| documentNumber                      | query          | *(optional)* Document Number                      |
+-------------------------------------+----------------+---------------------------------------------------+
| posId                               | query          | *(optional)* POS ID                               |
+-------------------------------------+----------------+---------------------------------------------------+
| purchaseDateFrom                    | query          | *(optional)* purchase date's lower limit          |
+-------------------------------------+----------------+---------------------------------------------------+
| purchaseDateTo                      | query          | *(optional)* purchase date's upper limit          |
+-------------------------------------+----------------+---------------------------------------------------+
| grossValueFrom                      | query          | *(optional)* transaction gross value lower limit  |
+-------------------------------------+----------------+---------------------------------------------------+
| grossValueTo                        | query          | *(optional)* transaction gross value upper limit  |
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
| labels                              | query          | *(optional)* Filter transactions by labels.       |
|                                     |                | Format "labels[0][key]=label_key                  |
|                                     |                | & labels[0][value]=first_value                    |
|                                     |                | & labels[1][key]=another_key"                     |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/transaction \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
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
      "transactions": [
        {
          "grossValue": 3,
          "transactionId": "00000000-0000-1111-0000-000000000003",
          "documentNumber": "456",
          "purchaseDate": "2018-02-20T09:45:04+0100",
          "purchasePlace": "wroclaw",
          "documentType": "sell",
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "assignedToCustomerDate": "1970-01-01T01:00:00+01:00",
          "customerData": {
            "email": "user@example.com",
            "name": "Jan Nowak",
            "nip": "aaa",
            "phone": "123",
            "loyaltyCardNumber": "sa2222",
            "address": {
              "street": "Bagno",
              "address1": "12",
              "province": "Mazowieckie",
              "city": "Warszawa",
              "postal": "00-800",
              "country": "PL"
            }
          },
          "labels": [
            {
              "key": "scan_id",
              "value": "123"
            }
          ],
          "items": [
            {
              "sku": {
                "code": "SKU1"
              },
              "name": "item 1",
              "quantity": 1,
              "grossValue": 1,
              "category": "aaa",
              "maker": "sss",
              "labels": [
                {
                  "key": "test",
                  "value": "label"
                },
                {
                  "key": "test",
                  "value": "label2"
                }
              ]
            },
            {
              "sku": {
                "code": "SKU2"
              },
              "name": "item 2",
              "quantity": 2,
              "grossValue": 2,
              "category": "bbb",
              "maker": "ccc",
              "labels": []
            }
          ],
          "currency": "eur",
          "pointsEarned": 6.9
        },
        {
          "grossValue": 3,
          "transactionId": "00000000-0000-1111-0000-000000000005",
          "documentNumber": "888",
          "purchaseDate": "2018-02-20T09:45:04+0100",
          "purchasePlace": "wroclaw",
          "documentType": "sell",
          "customerId": "57524216-c059-405a-b951-3ab5c49bae14",
          "customerData": {
            "email": "o@lo.com",
            "name": "Jan Nowak",
            "nip": "aaa",
            "phone": "123",
            "loyaltyCardNumber": "sa21as222",
            "address": {
              "street": "Bagno",
              "address1": "12",
              "province": "Mazowieckie",
              "city": "Warszawa",
              "postal": "00-800",
              "country": "PL"
            }
          },
          "labels": [
            {
              "key": "scan_id",
              "value": "234"
            }
          ],
          "items": [
            {
              "sku": {
                "code": "SKU1"
              },
              "name": "item 1",
              "quantity": 1,
              "grossValue": 1,
              "category": "aaa",
              "maker": "sss",
              "labels": [
                {
                  "key": "test",
                  "value": "label"
                },
                {
                  "key": "test",
                  "value": "label2"
                }
              ]
            },
            {
              "sku": {
                "code": "SKU2"
              },
              "name": "item 2",
              "quantity": 2,
              "grossValue": 2,
              "category": "bbb",
              "maker": "ccc",
              "labels": []
            }
          ],
          "currency": "eur",
          "pointsEarned": 6
        }
      ],
      "total": 2
    }



Register a new transaction
--------------------------

To register a new transaction, you need to call the ``/api/transaction`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST  /api/transaction

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[transactionData][documentType]   | query          | Document type for Transaction Data, 2 possible    | 
|                                              |                | values: return, sell                              |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[transactionData][documentNumber] | query          | Document number                                   |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[revisedDocument]                 | query          | Sales document number                             |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[transactionData][purchaseDate]   | query          | *(optional)* Purchase date                        |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][sku][code]              | query          | SKU Code                                          |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][name]                   | query          | Product name                                      |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][quantity]               | query          | Quantity                                          |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][grossValue]             | query          | Gross value                                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][category]               | query          | Category Name                                     |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][maker]                  | query          | Brand name                                        |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][labels][][key]          | query          | Label key                                         |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][labels][][value]        | query          | Label value                                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][name]              | query          | Customer name                                     |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][email]             | query          | *(optional)* Customer email                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][phone]             | query          | *(optional)* Customer phone                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][loyaltyCardNumber] | query          | *(optional)* Customer Loyalty card number         |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][nip]               | query          | *(optional)* Customer NIP                         |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][street]   | query          | *(optional)* Street                               |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][address1] | query          | *(optional)* Customer address1                    |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][postal]   | query          | *(optional)* Postal code                          |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][city]     | query          | *(optional)* City                                 |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][province] | query          | *(optional)* Province                             |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][country]  | query          | *(optional)* Country                              |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[labels][0][key]                  | query          | *(optional)* First label key                      |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[labels][0][value]                | query          | *(optional)* First label value                    |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[labels][1][key]                  | query          | *(optional)* Second label key                     |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[labels][1][value]                | query          | *(optional)* Second label value                   |
+----------------------------------------------+----------------+---------------------------------------------------+

.. note::

    You need to provide one of the following:
    transaction[customerData][email],
    transaction[customerData][phone],
    transaction[customerData][loyaltyCardNumber],
    to match a customer with a transaction.

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/transaction \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "transaction[items][0][sku][code]=test0101" \
        -d "transaction[items][0][name]=Product+name" \
        -d "transaction[items][0][quantity]=1" \
        -d "transaction[items][0][grossValue]=1500.00" \
        -d "transaction[items][0][category]=Category+Name" \
        -d "transaction[items][0][maker]=Marker+name" \
        -d "transaction[items][0][labels][0][key]=Label+key" \
        -d "transaction[items][0][labels][0][value]=Label+value" \
        -d "transaction[customerData][name]=Firstname+Lastname" \
        -d "transaction[customerData][email]=tomasztest8@wp.pl" \
        -d "transaction[customerData][phone]=00000000000000" \
        -d "transaction[customerData][loyaltyCardNumber]=11111111111" \
        -d "transaction[customerData][nip]=00000000000000" \
        -d "transaction[customerData][address][street]=Street+name" \
        -d "transaction[customerData][address][address1]=123" \
        -d "transaction[customerData][address][postal]=00-000" \
        -d "transaction[customerData][address][city]=Wroclaw" \
        -d "transaction[customerData][address][province]=Dolnoslaskie" \
        -d "transaction[customerData][address][country]=PL" \
        -d "transaction[transactionData][documentNumber]=214124124125" \
        -d "transaction[transactionData][purchaseDate]=2019-02-20 09:28" \
        -d "transaction[transactionData][documentType]=sell"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "transactionId": "d5b1119a-698b-40b4-9ac4-8ef704fa4433"
    }



Update transaction labels
-------------------------

To update transaction labels, you need to log in as admin and call the ``/api/admin/transaction/labels`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST  /api/admin/transaction/labels

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction_labels[transactionId]            | query          | Transaction ID                                    |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction_labels[labels][0][key]           | query          | *(optional)* First label key                      |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction_labels[labels][0][value]         | query          | *(optional)* First label value                    |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction_labels[labels][1][key]           | query          | *(optional)* Second label key                     |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction_labels[labels][1][value]         | query          | *(optional)* Second label value                   |
+----------------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/transaction/labels \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "transaction_labels[transactionId]=00000000-0000-1111-0000-000000000000" \
        -d "transaction_labels[label][0][key]=some label" \
        -d "transaction_labels[label][0][value]=some value"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "transactionId": "d5b1119a-698b-40b4-9ac4-8ef704fa4433"
    }



Add new transaction labels as customer
--------------------------------------

To update transaction labels, you need to log in as a customer and call the ``/api/customer/transaction/labels/append`` endpoint with the ``PUT`` method.
A customer can only add new labels to transactions which are assigned to them.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT  /api/customer/transaction/labels/append

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| append[transactionDocumentNumber]            | query          | Transaction document number                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| append[labels][0][key]                       | query          | *(optional)* First label key                      |
+----------------------------------------------+----------------+---------------------------------------------------+
| append[labels][0][value]                     | query          | *(optional)* First label value                    |
+----------------------------------------------+----------------+---------------------------------------------------+
| append[labels][1][key]                       | query          | *(optional)* Second label key                     |
+----------------------------------------------+----------------+---------------------------------------------------+
| append[labels][1][value]                     | query          | *(optional)* Second label value                   |
+----------------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/transaction/labels/append \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "append[transactionDocumentNumebr]=123" \
        -d "append[labels][0][key]=some label" \
        -d "append[labels][0][value]=some value"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "transactionId": "d5b1119a-698b-40b4-9ac4-8ef704fa4433"
    }



Get available item labels
-------------------------

To retrieve available labels, you need to call the ``/api/transaction/item/labels`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/transaction/item/labels

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/transaction/item/labels \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *label* and *label2* are example values. You can name labels as you wish.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "labels": {
        "test": [
          "label",
          "label2"
        ]
      }
    }



Number of points which can be obtained after registering given transaction
--------------------------------------------------------------------------

To retrieve the number of points which can be obtained after registering a given transaction, you need to call the ``/api/transaction/simulate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/transaction/simulate

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][sku][code]              | query          | SKU code                                          |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][name]                   | query          | Product name                                      |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][quantity]               | query          | Quantity                                          |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][grossValue]             | query          | Gross value                                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][category]               | query          | Category name                                     |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][maker]                  | query          | Brand name                                        |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][labels][][key]          | query          | Label key                                         |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][labels][][value]        | query          | Label value                                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[purchaseDate]                    | query          | Purchase date                                     |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][name]              | query          | Customer name                                     |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][email]             | query          | *(optional, see below)* Customer email            |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][phone]             | query          | *(optional, see below)* Customer phone            |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][loyaltyCardNumber] | query          | *(optional, see below)* Loyalty card number       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][nip]               | query          | *(optional)* Customer NIP                         |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][street]   | query          | *(optional)* Street                               |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][address1] | query          | *(optional)* Customer address1                    |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][postal]   | query          | *(optional)* Postal code                          |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][city]     | query          | *(optional)* City                                 |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][province] | query          | *(optional)* Province                             |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][address][country]  | query          | *(optional)* Country                              |
+----------------------------------------------+----------------+---------------------------------------------------+

**Heads up!** One of the following: email, phone, loyaltyCardNumber is required, along with the name, in order to find the user for the simulation to be performed.

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/transaction/simulate \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "transaction[items][0][sku][code]=SKU1" \
        -d "transaction[items][0][name]=item+8" \
        -d "transaction[items][0][quantity]=1" \
        -d "transaction[items][0][grossValue]=1" \
        -d "transaction[items][0][category]=aaa" \
        -d "transaction[items][0][maker]=sss" \
        -d "transaction[items][0][labels][0]=labels" \
        -d "transaction[items][0][labels][0][key]=test" \
        -d "transaction[items][0][labels][0][value]=label" \
        -d "transaction[purchaseDate]=2022-02-20T09:45:04+0100"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "points": 2.3
    }



Get transaction details (admin)
-------------------------------

To get transaction details, you need to call the ``/api/transaction/<transaction>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET  /api/transaction/<transaction>

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| <transaction>                                | query          | Transaction ID                                    |
+----------------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

 To see details of a transaction with ID ``00000000-0000-1111-0000-000000000005``, use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/transaction/00000000-0000-1111-0000-000000000005 \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
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
      "grossValue": 3,
      "transactionId": "00000000-0000-1111-0000-000000000005",
      "documentNumber": "888",
      "purchaseDate": "2018-02-20T09:45:04+0100",
      "purchasePlace": "wroclaw",
      "documentType": "sell",
      "customerId": "57524216-c059-405a-b951-3ab5c49bae14",
      "assignedToCustomerDate": "1970-01-01T01:00:00+01:00",
      "customerData": {
        "email": "o@lo.com",
        "name": "Jan Nowak",
        "nip": "aaa",
        "phone": "123",
        "loyaltyCardNumber": "sa21as222",
        "address": {
          "street": "Bagno",
          "address1": "12",
          "province": "Mazowieckie",
          "city": "Warszawa",
          "postal": "00-800",
          "country": "PL"
        }
      },
      "labels": [
        {
          "key": "scan_id",
          "value": "123"
        }
      ],
      "items": [
        {
          "sku": {
            "code": "SKU1"
          },
          "name": "item 1",
          "quantity": 1,
          "grossValue": 1,
          "category": "aaa",
          "maker": "sss",
          "labels": [
            {
              "key": "test",
              "value": "label"
            },
            {
              "key": "test",
              "value": "label2"
            }
          ]
        },
        {
          "sku": {
            "code": "SKU2"
          },
          "name": "item 2",
          "quantity": 2,
          "grossValue": 2,
          "category": "bbb",
          "maker": "ccc",
          "labels": []
        }
      ],
      "currency": "eur",
      "pointsEarned": 6
    }
