Transactions
============

These endpoints will allow you to easily manage transactions.



Import transactions
-------------------

To import an XML file with transactions, you need to call the ``/api/<storeCode>/admin/transaction/import`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/admin/transaction/import

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                         | query          | Code of the store to import transactions into.    |
+-------------------------------------+----------------+---------------------------------------------------+
| file[file]                          | query          | XML file with transactions                        |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/transaction/import \
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

In order to match many transactions to many customers using an XML file, you need to call the ``api/<storeCode>/admin/transaction/customer/assign/import`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST api/<storeCode>/admin/transaction/customer/assign/import

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                         | query          | Code of the store to match transactions in.       |
+-------------------------------------+----------------+---------------------------------------------------+
| file[file]                          | query          | XML file with transactions                        |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/transaction/customer/assign/import \
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

To assign a customer to a specific transaction, you need to call the ``/api/<storeCode>/admin/transaction/customer/assign`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/admin/transaction/customer/assign

+-------------------------------------+----------------+---------------------------------------------------------------+
| Parameter                           | Parameter type | Description                                                   |
+=====================================+================+===============================================================+
| Authorization                       | header         | Token received during authentication                          |
+-------------------------------------+----------------+---------------------------------------------------------------+
| <storeCode>                         | query          | Code of the store the customer and the transaction belong to. |
+-------------------------------------+----------------+---------------------------------------------------------------+
| assign[transactionDocumentNumber]   | query          | Transaction Document Number                                   |
+-------------------------------------+----------------+---------------------------------------------------------------+
| assign[customerId]                  | query          | Customer ID                                                   |
+-------------------------------------+----------------+---------------------------------------------------------------+
| assign[customerLoyaltyCardNumber]   | query          | Customer Loyalty Number                                       |
+-------------------------------------+----------------+---------------------------------------------------------------+
| assign[customerPhoneNumber]         | query          | Customer Phone Number                                         |
+-------------------------------------+----------------+---------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/transaction/customer/assign \
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

To assign a logged-in customer to a specific transaction, you need to call the ``/api/<storeCode>/customer/transaction/customer/assign`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/transaction/customer/assign

+-------------------------------------+----------------+---------------------------------------------------------------+
| Parameter                           | Parameter type | Description                                                   |
+=====================================+================+===============================================================+
| Authorization                       | header         | Token received during authentication                          |
+-------------------------------------+----------------+---------------------------------------------------------------+
| <storeCode>                         | query          | Code of the store the customer and the transaction belong to. |
+-------------------------------------+----------------+---------------------------------------------------------------+
| assign[transactionDocumentNumber]   | query          | Transaction Document Number                                   |
+-------------------------------------+----------------+---------------------------------------------------------------+
| assign[customerId]                  | query          | Customer ID                                                   |
+-------------------------------------+----------------+---------------------------------------------------------------+
| assign[customerLoyaltyCardNumber]   | query          | Customer Loyalty Number                                       |
+-------------------------------------+----------------+---------------------------------------------------------------+
| assign[customerPhoneNumber]         | query          | Customer Phone Number                                         |
+-------------------------------------+----------------+---------------------------------------------------------------+

.. note::

    If you are using the auto-generated docs, you may see there are other fields in the assign[] object.
    They are ignored in this endpoint. Do not use them in your application as they will be removed in a future version.

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/transaction/customer/assign \
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

Get a list of transactions (customer)
-------------------------------------

To retrieve a complete or filtered list of all transactions a customer has access to, you need to call the ``/api/<storeCode>/customer/transaction`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/customer/transaction

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                         | query          | Code of the store the customer belongs to.        |
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

    curl http://localhost:8181/api/DEFAULT/customer/transaction \
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

To retrieve transaction details, you need to call the ``/api/<storeCode>/customer/transaction/<transaction>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/customer/transaction/<transaction>

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                         | query          | Code of the store the transaction belongs to.     |
+-------------------------------------+----------------+---------------------------------------------------+
| <transaction>                       | query          | Transaction ID                                    |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/transaction/00000000-0000-1111-0000-000000000003 \
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

Get a list of transactions
--------------------------

To retrieve a complete or filtered list of transactions, you need to call the ``/api/<storeCode>/transaction`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET  /api/<storeCode>/transaction

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                         | query          | Code of the store to get transactions from.       |
+-------------------------------------+----------------+---------------------------------------------------+
| _page                               | query          | *(optional)* Start from page, by default 1        |
+-------------------------------------+----------------+---------------------------------------------------+
| _itemsOnPage                        | query          | *(optional)* Number of items to display per page, |
|                                     |                | by default = 10                                   |
+-------------------------------------+----------------+---------------------------------------------------+
| _orderBy                            | query          | *(optional)* Sort by column name                  |
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
| purchaseDate                        | query          | *(optional)* purchase date's limit                |
+-------------------------------------+----------------+---------------------------------------------------+
| grossValue                          | query          | *(optional)* transaction gross value limit        |
+-------------------------------------+----------------+---------------------------------------------------+
| labels                              | query          | *(optional)* Filter transactions by labels.       |
|                                     |                | Format "labels[eq]=(key1;value1),(key2;value2),"  |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/transaction \
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

To register a new transaction, you need to call the ``/api/<storeCode>/transaction`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST  /api/<storeCode>/transaction

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                                  | query          | Code of the store to add transaction to.          |
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

    curl http://localhost:8181/api/DEFAULT/transaction \
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

To update transaction labels, you need to log in as admin and call the ``/api/<storeCode>/admin/transaction/labels`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST  /api/<storeCode>/admin/transaction/labels

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                                  | query          | Code of the store the transaction belongs to.     |
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

    curl http://localhost:8181/api/DEFAULT/admin/transaction/labels \
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

To update transaction labels, you need to log in as a customer and call the ``/api/<storeCode>/customer/transaction/labels/append`` endpoint with the ``PUT`` method.
A customer can only add new labels to transactions which are assigned to them.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT  /api/<storeCode>/customer/transaction/labels/append

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                                  | query          | Code of the store the customer belongs to.        |
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

    curl http://localhost:8181/api/DEFAULT/customer/transaction/labels/append \
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

Number of points which can be obtained after registering given transaction
--------------------------------------------------------------------------

To retrieve the number of points which can be obtained after registering a given transaction, you need to call the ``/api/<storeCode>/transaction/simulate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/transaction/simulate

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                                  | query          | Code of the store to simulate transaction in.     |
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

    curl http://localhost:8181/api/DEFAULT/transaction/simulate \
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

To get transaction details, you need to call the ``/api/<storeCode>/transaction/<transaction>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET  /api/<storeCode>/transaction/<transaction>

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                                  | query          | Code of the store the transaction belongs to.     |
+----------------------------------------------+----------------+---------------------------------------------------+
| <transaction>                                | query          | Transaction ID                                    |
+----------------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

 To see details of a transaction with ID ``00000000-0000-1111-0000-000000000005``, use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/transaction/00000000-0000-1111-0000-000000000005 \
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
