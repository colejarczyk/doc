Transactions
============

These endpoints will allow you to easily manage transactions.


Assign customer to specific transaction
---------------------------------------

To assign customer to specific transaction you will need to call the ``/api/admin/transaction/customer/assign`` endpoint with the ``POST`` method.

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

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "transactionId": "00000000-0000-1111-0000-000000000002"
    }

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "form": {
        "children": {
          "transactionDocumentNumber": {
            "errors": [
              "Customer is already assign to this transaction"
            ]
          },
          "customerId": {},
          "customerLoyaltyCardNumber": {},
          "customerPhoneNumber": {}
        }
      },
      "errors": []
    }


Assign customer to specific transaction (seller)
------------------------------------------------

To assign customer to specific transaction you will need to call the ``/api/seller/transaction/customer/assign`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/seller/transaction/customer/assign

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

    curl http://localhost:8181/api/seller/transaction/customer/assign \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."
        -d "assign[transactionDocumentNumber]=123" \
        -d "assign[customerId]=57524216-c059-405a-b951-3ab5c49bae14" \
        -d "assign[customerLoyaltyCardNumber]=333" \
        -d "assign[customerPhoneNumber]=333333"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "transactionId": "00000000-0000-1111-0000-000000000005"
    }


Get complete list of all transactions (customer)
------------------------------------------------

To return complete list of all transactions you will need to call the ``/api/customer/transaction`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/transaction

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_loyaltyCardNumber      | query          | *(optional)* Loyalty Card Number                  |
+-------------------------------------+----------------+---------------------------------------------------+
| documentType                        | query          | *(optional)* Document Type                        |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_name                   | query          | *(optional)* Customer Name                        |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_email                  | query          | *(optional)* Customer Email                       |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_phone                  | query          | *(optional)* Customer Phone                       |
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

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/transaction \
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
      "transactions": [
        {
          "grossValue": 3,
          "transactionId": "00000000-0000-1111-0000-000000000003",
          "documentNumber": "456",
          "purchaseDate": "2018-02-20T09:45:04+0100",
          "purchasePlace": "wroclaw",
          "documentType": "sell",
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "customerData": {
            "email": "user@oloy.com",
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

Get transaction details
-----------------------

To return transaction details you will need to call the ``/api/customer/transaction/<transaction>`` endpoint with the ``GET`` method.

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

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

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
      "customerData": {
        "email": "user@oloy.com",
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


Get complete list of all transactions (seller)
----------------------------------------------

To get complete list of all transactions you will need to call the ``/api/seller/transaction`` endpoint with the ``GET`` method.

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
| documentType                        | query          | *(optional)* Document Type                        |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_name                   | query          | *(optional)* Customer Name                        |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_email                  | query          | *(optional)* Customer Email                       |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_phone                  | query          | *(optional)* Customer Phone                       |
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

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/transaction\
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
      "transactions": [
         {
      "grossValue": 3,
      "transactionId": "00000000-0000-1111-0000-000000000004",
      "documentNumber": "789",
      "purchaseDate": "2018-02-20T09:45:04+0100",
      "purchasePlace": "wroclaw",
      "documentType": "sell",
      "customerId": "00000000-0000-474c-b092-b0dd880c07e2",
      "customerData": {
        "email": "user-temp@oloy.com",
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
        "email": "open@oloy.com",
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

Get logged in customer transactions (seller)
--------------------------------------------

To return logged in customer transactions you will need to call the ``/api/seller/transaction/customer/<customer>`` endpoint with the ``GET`` method.

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
| documentNumber                      | query          | *(optional)* Document Number                      |
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

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

Exemplary Response
^^^^^^^^^^^^^^^^^^

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

To return transactions with provided document number you will need to call the ``/api/seller/transaction/<documentNumber>`` endpoint with the ``GET`` method.

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

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

Exemplary Response
^^^^^^^^^^^^^^^^^^

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





Get complete list of all transactions
-------------------------------------

To return complete list of all transactions you will need to call the ``/api/transaction`` endpoint with the ``GET`` method.

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
| documentType                        | query          | *(optional)* Document Type                        |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_name                   | query          | *(optional)* Customer Name                        |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_email                  | query          | *(optional)* Customer Email                       |
+-------------------------------------+----------------+---------------------------------------------------+
| customerData_phone                  | query          | *(optional)* Customer Phone                       |
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

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

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
          "customerData": {
            "email": "user@oloy.com",
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


Register new transaction
------------------------

To register new transaction you will need to call the ``/api/transaction`` endpoint with the ``POST`` method.

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
| transaction[transactionData][purchaseDate]   | query          | *(optional)* Purchase date                        |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][sku][code]              | query          | SKU Code                                          |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][name]                   | query          | Product name                                      |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][quantity]               | query          | Quantity                                          |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][grossValue]               | query          | Gross value                                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][category]               | query          | Category Name                                     |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][maker]                   | query          | Brand name                                        |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][labels][][key]          | query          | Label key                                         |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][labels][][value]        | query          | Label value                                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][name]               | query          | Customer name                                     |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][email]               | query          | *(optional)* Customer email                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[customerData][phone]               | query          | *(optional)* Customer phone                       |
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
| transaction[customerData][address][city]       | query          | *(optional)* City                                 |
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
        -d "transaction[transactionData][purchaseDate]=2017-08-22" \
        -d "transaction[transactionData][documentType]=return"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json
    {
      "transactionId": "d5b1119a-698b-40b4-9ac4-8ef704fa4433"
    }

Update transaction labels
-------------------------

To update transaction labels you will need to log in as admin and call the ``/api/admin/transaction/labels`` endpoint with the ``POST`` method.

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

    curl http://localhost:8181/api/transaction \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "transaction_labels[transactionId]=00000000-0000-1111-0000-000000000000" \
        -d "transaction_labels[label][0][key]=some label" \
        -d "transaction_labels[label][0][value]=some value"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json
    {
      "transactionId": "d5b1119a-698b-40b4-9ac4-8ef704fa4433"
    }

Add new transaction labels as customer
--------------------------------------

To update transaction labels you will need to log in as customer and call the ``/api/customer/transaction/labels/append`` endpoint with the ``PUT`` method.
Customer can only add new labels to transaction which is assigned to him.

Definition
^^^^^^^^^^

.. code-block:: text

    POST  /api/customer/transaction/labels/append

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| append[transactionDocumentNumber]            | query          | Transaction ID                                    |
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

    curl http://localhost:8181/api/transaction \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "append[transactionDocumentNumebr]=123" \
        -d "append[label][0][key]=some label" \
        -d "append[label][0][value]=some value"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json
    {
      "transactionId": "d5b1119a-698b-40b4-9ac4-8ef704fa4433"
    }

Get available item labels
-------------------------

To return available labels you will need to call the ``/api/transaction/item/labels`` endpoint with the ``GET`` method.

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

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *label* or *label2* are an exemplary values. You can name labels as you like.

Exemplary Response
^^^^^^^^^^^^^^^^^^

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


Number of points which can be obtained after registering such transaction
-------------------------------------------------------------------------

To return number of points which can be obtained after registering such transaction you will need to call the ``/api/transaction/simulate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/transaction/simulate

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction                                  | query          | Transaction ID                                    |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][sku][code]              | query          | SKU code                                          |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][name]                     | query          | Product name                                      |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][quantity]                  | query          | Quantity                                          |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][grossValue]              | query          | Gross value                                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][category]               | query          | Category name                                     |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][maker]                   | query          | Brand name                                        |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][labels][][key]          | query          | Label key                                         |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[items][][labels][][value]        | query          | Label value                                       |
+----------------------------------------------+----------------+---------------------------------------------------+
| transaction[purchaseDate]                      | query          | Purchase date                                     |
+----------------------------------------------+----------------+---------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/transaction/simulate \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "transaction=00000000-0000-1111-0000-000000000099" \
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

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "points": 2.3
    }


Get transaction details
-----------------------

To get transaction details you will need to call the ``/api/transaction/<transaction>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET  /api/transaction/<transaction>

+----------------------------------------------+----------------+---------------------------------------------------+
| Parameter                                    | Parameter type | Description                                       |
+==============================================+================+===================================================+
| Authorization                                | header         | Token received during authentication              |
+----------------------------------------------+----------------+---------------------------------------------------+
| <transaction>                                 | query          | Transaction ID                                    |
+----------------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

 To see details of ``transaction = 00000000-0000-1111-0000-000000000005``email use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/transaction/00000000-0000-1111-0000-000000000005 \
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
