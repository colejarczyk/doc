Customer API
============

These endpoints allow you to easily manage customers.

.. note::

    Each role in the Open Loyalty has individual endpoints to manage customers.



Activate a customer
-------------------

To activate a customer, you need to call the ``/api/<storeCode>/admin/customer/<customer>/activate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/admin/customer/<customer>/activate

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type | Description                                                    |
+====================================+================+================================================================+
| Authorization                      | header         | Token received during authentication                           |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the activated customer belongs to.           |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | request        | Customer's UUID                                                |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/customer/1bbafb37-b51b-47c5-b3e4-e0a2d028e655/activate \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customer = 1bbafb37-b51b-47c5-b3e4-e0a2d028e655* id is an example value. Your value may be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Deactivate a customer
---------------------

To deactivate a customer, you need to call the ``/api/<storeCode>/admin/customer/<customer>/deactivate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/admin/customer/<customer>/deactivate

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type | Description                                                    |
+====================================+================+================================================================+
| Authorization                      | header         | Token received during authentication                           |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the deactivated customer belongs to.         |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | request        | Customer's UUID                                                |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/customer/1bbafb37-b51b-47c5-b3e4-e0a2d028e655/deactivate \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customer = 1bbafb37-b51b-47c5-b3e4-e0a2d028e655* id is an example value. Your value may be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Get customer status
-------------------

To get a customer status, you need to call the ``/api/<storeCode>/admin/customer/<customer>/status`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/admin/customer/<customer>/status

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type | Description                                                    |
+====================================+================+================================================================+
| Authorization                      | header         | Token received during authentication                           |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store to get the customer from.                    |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | request        | Customer's UUID                                                |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/customer/1bbafb37-b51b-47c5-b3e4-e0a2d028e655/status \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customer = 1bbafb37-b51b-47c5-b3e4-e0a2d028e655* id is an example value. Your value may be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "firstName": "Test",
      "lastName": "test",
      "customerId": "a284f230-c1c0-4a1c-af9a-159b81de1f2b",
      "points": 0,
      "totalEarnedPoints": 0,
      "usedPoints": 0,
      "expiredPoints": 0,
      "lockedPoints": 0,
      "level": "15.00%",
      "levelName": "level1",
      "levelConditionValue": 20,
      "nextLevel": "20.00%",
      "nextLevelName": "level2",
      "nextLevelConditionValue": 200,
      "transactionsAmountToNextLevelWithoutDeliveryCosts": 100,
      "transactionsAmountWithoutDeliveryCosts": 100,
      "averageTransactionsAmount": "50.00",
      "transactionsCount": 2,
      "transactionsAmount": 100,
      "pointsToNextLevel": 200,
      "currency": "eur",
      "levelWillExpireInDays": 100,
      "pointsSinceLastLevelRecalculation": 0,
      "pointsRequiredToRetainLevel": 20
      "pointsExpiringNextMonth": 150
    }

.. note::

    The information in response may vary depends on the loyalty program configuration. Here is an example
    of all possible information combine.



Get customers
-------------

To get a list of customers, you need to call the ``/api/<storeCode>/customer/`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/customer

+------------------------------+----------------+----------------------------------------------------------------------+
| Parameter                    | Parameter type | Description                                                          |
+==============================+================+======================================================================+
| Authorization                | header         | Token received during authentication                                 |
+------------------------------+----------------+----------------------------------------------------------------------+
| <storeCode>                  | query          | Code of the store to get the customers from.                         |
+------------------------------+----------------+----------------------------------------------------------------------+
| firstName                    | request        | *(optional)* Customer's first name                                   |
+------------------------------+----------------+----------------------------------------------------------------------+
| lastName                     | request        | *(optional)* Customer's last name                                    |
+------------------------------+----------------+----------------------------------------------------------------------+
| phone                        | request        | *(optional)* Customer's phone                                        |
+------------------------------+----------------+----------------------------------------------------------------------+
| email                        | request        | *(optional)* Customer's email address                                |
+------------------------------+----------------+----------------------------------------------------------------------+
| loyaltyCardNumber            | request        | *(optional)* Customer's loyalty card number                          |
+------------------------------+----------------+----------------------------------------------------------------------+
| transactionsAmountFrom       | request        | *(optional)* Customer's transactions amount lower limit              |
+------------------------------+----------------+----------------------------------------------------------------------+
| transactionsAmountTo         | request        | *(optional)* Customer's transactions amount upper limit              |
+------------------------------+----------------+----------------------------------------------------------------------+
| averageTransactionAmountFrom | request        | *(optional)* Customer's average transaction amount lower limit       |
+------------------------------+----------------+----------------------------------------------------------------------+
| averageTransactionAmountTo   | request        | *(optional)* Customer's average transaction amount upper limit       |
+------------------------------+----------------+----------------------------------------------------------------------+
| transactionsCountFrom        | request        | *(optional)* Customer's transactions count lower limit               |
+------------------------------+----------------+----------------------------------------------------------------------+
| transactionsCountTo          | request        | *(optional)* Customer's transactions count upper limit               |
+------------------------------+----------------+----------------------------------------------------------------------+
| daysFromLastTransactionTo    | request        | *(optional)* Customers days from last transaction upper limit        |
+------------------------------+----------------+----------------------------------------------------------------------+
| hoursFromLastUpdateTo        | request        | *(optional)* Customer's hours from last update upper limit           |
+------------------------------+----------------+----------------------------------------------------------------------+
| strict                       | query          | *(optional)* If true, search for exact value, otherwise like value   |
|                              |                | For example ``1``, by default = 0                                    |
+------------------------------+----------------+----------------------------------------------------------------------+
| page                         | query          | *(optional)* Start from page, by default 1                           |
+------------------------------+----------------+----------------------------------------------------------------------+
| perPage                      | query          | *(optional)* Number of items to display per page,                    |
|                              |                | by default = 10                                                      |
+------------------------------+----------------+----------------------------------------------------------------------+
| sort                         | query          | *(optional)* Sort by column name.                                    |
|                              |                | Note: column names corresponding to parameters ending in ``From`` or |
|                              |                | ``To`` do not have this suffix, eg. ``transactionCount``,            |
|                              |                | ``averageTransactionAmount``.                                        |
+------------------------------+----------------+----------------------------------------------------------------------+
| direction                    | query          | *(optional)* Direction of sorting [ASC, DESC]                        |
+------------------------------+----------------+----------------------------------------------------------------------+
| _locale                      | query          | *(optional)* Retrieves data in given locale                          |
+------------------------------+----------------+----------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer \
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
      "customers": [
        {
          "customerId": "41fd3247-2069-4677-8904-584f0ed9f6be",
          "active": true,
          "firstName": "test",
          "lastName": "test",
          "email": "test4@example.com",
          "address": {},
          "createdAt": "2018-02-02T11:39:17+0100",
          "levelId": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "agreement1": true,
          "agreement2": false,
          "agreement3": false,
          "updatedAt": "2018-02-02T11:39:28+0100",
          "campaignPurchases": [],
          "transactionsCount": 0,
          "transactionsAmount": 0,
          "transactionsAmountWithoutDeliveryCosts": 0,
          "amountExcludedForLevel": 0,
          "averageTransactionAmount": 0,
          "currency": "eur",
          "levelPercent": "14.00%"
        },
        {
          "customerId": "142cbe32-da28-42d0-87aa-f93f3e1ebb91",
          "active": true,
          "firstName": "test",
          "lastName": "test",
          "email": "test3@example.com",
          "address": {},
          "createdAt": "2018-02-02T11:38:19+0100",
          "levelId": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "agreement1": true,
          "agreement2": false,
          "agreement3": false,
          "updatedAt": "2018-02-02T11:38:20+0100",
          "campaignPurchases": [],
          "transactionsCount": 0,
          "transactionsAmount": 0,
          "transactionsAmountWithoutDeliveryCosts": 0,
          "amountExcludedForLevel": 0,
          "averageTransactionAmount": 0,
          "currency": "eur",
          "levelPercent": "14.00%"
        }
      ],
      "total": 2
    }

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."
        -d "email=example.com" \
        -d "strict=0" \
        -d "page=1" \
        -d "perPage=2" \
        -d "sort=customerId" \
        -d "direction=asc"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customers": [
        {
          "customerId": "00000000-0000-474c-b092-b0dd880c07e2",
          "active": true,
          "firstName": "Jane",
          "lastName": "Doe",
          "gender": "male",
          "email": "user-temp@example.com",
          "phone": "111112222",
          "birthDate": "1990-09-11T02:00:00+0200",
          "address": {
            "street": "Bagno",
            "address1": "1",
            "province": "Mazowieckie",
            "city": "Warszawa",
            "postal": "00-000",
            "country": "PL"
          },
          "loyaltyCardNumber": "0000",
          "createdAt": "2016-08-08T10:53:14+0200",
          "levelId": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "agreement1": false,
          "agreement2": false,
          "agreement3": false,
          "updatedAt": "2018-02-02T11:23:18+0100",
          "campaignPurchases": [],
          "transactionsCount": 1,
          "transactionsAmount": 3,
          "transactionsAmountWithoutDeliveryCosts": 3,
          "amountExcludedForLevel": 0,
          "averageTransactionAmount": 3,
          "lastTransactionDate": "2018-02-03T11:23:21+0100",
          "currency": "eur",
          "levelPercent": "14.00%"
        },
        {
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "active": false,
          "firstName": "John",
          "lastName": "Doe",
          "gender": "male",
          "email": "user@example.com",
          "phone": "11111",
          "birthDate": "1990-09-11T02:00:00+0200",
          "createdAt": "2016-08-08T10:53:14+0200",
          "levelId": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "agreement1": false,
          "agreement2": false,
          "agreement3": false,
          "updatedAt": "2018-02-02T11:23:17+0100",
          "campaignPurchases": [],
          "transactionsCount": 1,
          "transactionsAmount": 3,
          "transactionsAmountWithoutDeliveryCosts": 3,
          "amountExcludedForLevel": 0,
          "averageTransactionAmount": 3,
          "lastTransactionDate": "2018-02-03T11:23:21+0100",
          "currency": "eur",
          "levelPercent": "14.00%"
        }
      ],
      "total": 2
    }

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."
        -d "email=example.com" \
        -d "strict=1" \
        -d "page=1" \
        -d "perPage=2" \
        -d "sort=customerId" \
        -d "direction=asc"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customers": [],
      "total": 0
    }



Get a customer list as an admin
-------------------------------

To get a list of all customers, you need to call the ``/api/<storeCode>/admin/customer`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/admin/customer

+------------------------------+----------------+----------------------------------------------------------------------+
| Parameter                    | Parameter type |  Description                                                         |
+====================================+================+================================================================+
| Authorization                | header         |  Token received during authentication                                |
+------------------------------+----------------+----------------------------------------------------------------------+
| <storeCode>                  | query          | Code of the store to get the customers from.                         |
+------------------------------+----------------+----------------------------------------------------------------------+
| firstName                    | request        | *(optional)* Customer's first name                                   |
+------------------------------+----------------+----------------------------------------------------------------------+
| lastName                     | request        | *(optional)* Customer's last name                                    |
+------------------------------+----------------+----------------------------------------------------------------------+
| phone                        | request        | *(optional)* Customer's phone                                        |
+------------------------------+----------------+----------------------------------------------------------------------+
| email                        | request        | *(optional)* Customer's email address                                |
+------------------------------+----------------+----------------------------------------------------------------------+
| loyaltyCardNumber            | request        | *(optional)* Customer's loyalty card number                          |
+------------------------------+----------------+----------------------------------------------------------------------+
| transactionsAmountFrom       | request        | *(optional)* Customer's transactions amount lower limit              |
+------------------------------+----------------+----------------------------------------------------------------------+
| transactionsAmountTo         | request        | *(optional)* Customer's transactions amount upper limit              |
+------------------------------+----------------+----------------------------------------------------------------------+
| averageTransactionAmountFrom | request        | *(optional)* Customer's average transaction amount lower limit       |
+------------------------------+----------------+----------------------------------------------------------------------+
| averageTransactionAmountTo   | request        | *(optional)* Customer's average transaction amount upper limit       |
+------------------------------+----------------+----------------------------------------------------------------------+
| transactionsCountFrom        | request        | *(optional)* Customer's transactions count lower limit               |
+------------------------------+----------------+----------------------------------------------------------------------+
| transactionsCountTo          | request        | *(optional)* Customer's transactions count upper limit               |
+------------------------------+----------------+----------------------------------------------------------------------+
| daysFromLastTransactionTo    | request        | *(optional)* Customers days from last transaction upper limit        |
+------------------------------+----------------+----------------------------------------------------------------------+
| hoursFromLastUpdateTo        | request        | *(optional)* Customer's hours from last update upper limit           |
+------------------------------+----------------+----------------------------------------------------------------------+
| strict                       | query          | *(optional)* If true, search for exact value, otherwise like value   |
|                              |                | For example ``1``, by default = 0                                    |
+------------------------------+----------------+----------------------------------------------------------------------+
| page                         | query          | *(optional)* Start from page, by default 1                           |
+------------------------------+----------------+----------------------------------------------------------------------+
| perPage                      | query          | *(optional)* Number of items to display per page,                    |
|                              |                | by default = 10                                                      |
+------------------------------+----------------+----------------------------------------------------------------------+
| sort                         | query          | *(optional)* Sort by column name.                                    |
|                              |                | Note: column names corresponding to parameters ending in ``From`` or |
|                              |                | ``To`` do not have this suffix, eg. ``transactionCount``,            |
|                              |                | ``averageTransactionAmount``.                                        |
+------------------------------+----------------+----------------------------------------------------------------------+
| direction                    | query          | *(optional)* Direction of sorting [ASC, DESC]                        |
+------------------------------+----------------+----------------------------------------------------------------------+
| _locale                      | query          | *(optional)* Retrieves data in given locale                          |
+------------------------------+----------------+----------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/customer \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "email=example.com" \
        -d "strict=0" \
        -d "page=1" \
        -d "perPage=2" \
        -d "sort=customerId" \
        -d "direction=asc"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customers": [
        {
          "customerId": "41fd3247-2069-4677-8904-584f0ed9f6be",
          "active": true,
          "firstName": "test",
          "lastName": "test",
          "email": "test4@example.com",
          "address": {},
          "createdAt": "2018-02-02T11:39:17+0100",
          "levelId": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "agreement1": true,
          "agreement2": false,
          "agreement3": false,
          "updatedAt": "2018-02-02T11:39:28+0100",
          "campaignPurchases": [],
          "transactionsCount": 0,
          "transactionsAmount": 0,
          "transactionsAmountWithoutDeliveryCosts": 0,
          "amountExcludedForLevel": 0,
          "averageTransactionAmount": 0,
          "currency": "eur",
          "levelPercent": "14.00%"
        },
        {
          "customerId": "142cbe32-da28-42d0-87aa-f93f3e1ebb91",
          "active": true,
          "firstName": "test",
          "lastName": "test",
          "email": "test3@example.com",
          "address": {},
          "createdAt": "2018-02-02T11:38:19+0100",
          "levelId": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "agreement1": true,
          "agreement2": false,
          "agreement3": false,
          "updatedAt": "2018-02-02T11:38:20+0100",
          "campaignPurchases": [],
          "transactionsCount": 0,
          "transactionsAmount": 0,
          "transactionsAmountWithoutDeliveryCosts": 0,
          "amountExcludedForLevel": 0,
          "averageTransactionAmount": 0,
          "currency": "eur",
          "levelPercent": "14.00%"
        }
      ],
      "total": 2
    }



Activate a customer using SMS activation token
----------------------------------------------

To activate a customer using a token (sms code), you need to call the ``/api/<storeCode>/customer/activate-sms/<token>`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/activate-sms/<token>

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type | Description                                                    |
+====================================+================+================================================================+
| <storeCode>                        | query          | Code of the store the customer to be activated belongs to.     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <token>                            | request        | Customer's token, SMS activation code                          |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/activate-sms/954604\
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded"

.. note::

    The *token = 954604* is an example value. Your value may be different.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content

.. code-block:: json

    (no content)



Activate a customer using activation token
------------------------------------------

To activate a customer using a token, you need to call the ``/api/<storeCode>/customer/activate/<token>`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/activate/<token>

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type | Description                                                    |
+====================================+================+================================================================+
| <storeCode>                        | query          | Code of the store the customer to be activated belongs to.     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <token>                            | request        | Customer's token                                               |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/activate/abcde \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *token = abcde* is an example value. Your value may be different.
    For testing, the value can be checked in the database, table ``ol_user``, field ``action_token``.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Anonymize customer
------------------

To anonymize the customer, you need to call the ``/api/<storeCode>/admin/customer/<customer>/anonymize`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/admin/customer/<customer>/anonymize

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <storeCode>          | query          | Code of the store the customer belongs to.             |
+----------------------+----------------+--------------------------------------------------------+
| <customer>           | query          | Customer UUID                                          |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/customer/c9be6a4e-9a21-414a-bbbd-f506d9ffad85/anonymize \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204

.. code-block:: json

    (no content)


Check if customer with given phone number or email exists
---------------------------------------------------------

To check if a customer with a given phone number or email exists, you need to call the ``/api/<storeCode>/customer/check`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/customer/check

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type | Description                                                    |
+====================================+================+================================================================+
| Authorization                      | header         | Token received during authentication                           |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store to check for customers.                      |
+------------------------------------+----------------+----------------------------------------------------------------+
| emailOrPhone                       | request        | Customer's email or phone                                      |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/check?emailOrPhone=899000333 \
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
        "total": 1
    }



Create a new customer
---------------------

To create a new customer, you need to call the ``/api/<storeCode>/customer/register`` endpoint with the ``POST`` method.

.. note::

    This endpoint allows you to set more customer parameters than ``/api/<storeCode>/customer/self-register`` and is used when creating
    a new customer in the admin cockpit or POS cockpit. The The self register endpoint is used in the client cockpit for registration
    and has some limitations.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/register

+-----------------------------------+----------------+-----------------------------------------------------------------+
| Parameter                         | Parameter type | Description                                                     |
+===================================+================+=================================================================+
| Authorization                     | header         | Token received during authentication                            |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| <storeCode>                       | query          | Code of the store to register the customer in.                  |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[firstName]               | request        | First name                                                      |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[lastName]                | request        | Last name                                                       |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[gender]                  | request        | *(optional)* Gender. Possible values ``male``, ``female``,      |
|                                   |                | ``not_disclosed``                                               |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[email]                   | request        | E-mail address *(unique)*                                       |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[phone]                   | request        | *(optional)* A phone number *(unique)*                          |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[birthDate]               | request        | *(optional)* Birth date in format YYYY-MM-DD HH:mm,             |
|                                   |                | for example ``2017-10-05``.                                     |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[createdAt]               | request        | *(optional)* Created at in format YYYY-MM-DD HH:mm:ss,          |
|                                   |                | for example ``2017-01-01 14:15:16``.                            |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[address][street]         | request        | *(optional)* Street name                                        |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[address][address1]       | request        | *(optional)* Building number                                    |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[address][address2]       | request        | *(optional)* Flat/Unit name                                     |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[address][postal]         | request        | *(optional)* Post code                                          |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[address][city]           | request        | *(optional)* City name                                          |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[address][province]       | request        | *(optional)* Province name                                      |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[address][country]        | request        | *(optional)* Country name                                       |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[company][name]           | request        | *(optional)* Company name                                       |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[company][nip]            | request        | *(optional)* Tax ID                                             |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[loyaltyCardNumber]       | request        | *(optional)* Loyalty card number *(unique)*                     |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[labels]                  | request        | *(optional)* String of labels in form of ``key1:val1;key2:val2``|
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[agreement1]              | request        | First agreement. Set 1 if true, otherwise 0                     |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[agreement2]              | request        | *(optional)* Second agreement. Set 1 if true, otherwise 0       |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[agreement3]              | request        | *(optional)* Third agreement. Set 1 if true, otherwise 0        |
+-----------------------------------+----------------+-----------------------------------------------------------------+
| customer[referral_customer_email] | request        | *(optional)* Referral customer e-mail address.                  |
+-----------------------------------+----------------+-----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/register \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customer[firstName]=John" \
        -d "customer[lastName]=Kowalski" \
        -d "customer[email]=john4@example.com" \
        -d "customer[phone]=000000005000" \
        -d "customer[agreement1]=1"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customerId": "e0eb0355-8aaa-4fb1-8159-f58e81b7a25c",
      "email": "john4@example.com"
    }

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/register \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customer[firstName]=John" \
        -d "customer[lastName]=Kowalski" \
        -d "customer[email]=john3@example.com" \
        -d "customer[phone]=000000004000" \
        -d "customer[birthDate]=1990-01-01" \
        -d "customer[address][street]=Street" \
        -d "customer[address][postal]=00-000" \
        -d "customer[address][city]=Wroclaw" \
        -d "customer[address][province]=Dolnoslaskie" \
        -d "customer[address][country]=Poland" \
        -d "customer[company][nip]=111-222-33-44" \
        -d "customer[company][name]=Company+name" \
        -d "customer[loyaltyCardNumber]=00000000000000002" \
        -d "customer[agreement1]=1" \
        -d "customer[agreement2]=1" \
        -d "customer[agreement3]=1"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customerId": "e0eb0355-8aaa-4fb1-8159-f58e81b7a25c",
      "email": "john3@example.com"
    }

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/register \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "form": {
        "children": {
          "firstName": {},
          "lastName": {},
          "gender": {},
          "email": {},
          "phone": {},
          "birthDate": {},
          "createdAt": {},
          "address": {
            "children": {
              "street": {},
              "address1": {},
              "address2": {},
              "postal": {},
              "city": {},
              "province": {},
              "country": {}
            }
          },
          "company": {
            "children": {
              "name": {},
              "nip": {}
            }
          },
          "loyaltyCardNumber": {},
          "agreement1": {},
          "agreement2": {},
          "agreement3": {},
          "referral_customer_email": {},
          "levelId": {},
          "posId": {}
        }
      },
      "errors": []
    }



Get customer details
---------------------

To get details about a customer, you need to call the ``/api/<storeCode>/customer/<customer>`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/customer/<customer>

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type | Description                                                    |
+====================================+================+================================================================+
| Authorization                      | header         | Token received during authentication                           |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store to get the customer from.                    |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          | Customer ID                                                    |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/00000000-0000-474c-b092-b0dd880c07e1 \
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
      "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
      "active": true,
      "firstName": "John",
      "lastName": "Doe",
      "gender": "male",
      "email": "user@example.com",
      "phone": "+48234234000",
      "birthDate": "1990-09-11T02:00:00+0200",
      "lastLevelRecalculation": "2019-03-19T12:00:09+0100",
      "loyaltyCardNumber": "47834433524",
      "createdAt": "2016-08-08T10:53:14+0200",
      "id": "e82c96cf-32a3-43bd-9034-4df343e50000",
      "levelId": "e82c96cf-32a3-43bd-9034-4df343e50000",
      "agreement1": false,
      "agreement2": false,
      "agreement3": false,
      "status": {
        "availableTypes": [
          "new",
          "active",
          "blocked",
          "deleted"
        ],
        "availableStates": [
          "no-card",
          "card-sent",
          "with-card"
        ],
        "type": "active",
        "state": "no-card"
      },
      "updatedAt": "2019-03-19T11:52:49+0100",
      "campaignPurchases": [],
      "transactionsCount": 2,
      "transactionsAmount": 3,
      "transactionsAmountWithoutDeliveryCosts": 3,
      "amountExcludedForLevel": 0,
      "averageTransactionAmount": 1.5,
      "lastTransactionDate": "2019-03-20T11:52:56+0100",
      "labels": [],
      "level": {
        "levelId": {
          "id": "e82c96cf-32a3-43bd-9034-4df343e50000",
          "levelId": "e82c96cf-32a3-43bd-9034-4df343e50000"
        },
        "name": "level0",
        "translations": {
          "en": {
            "name": "level0"
          },
          "pl": {
            "name": "poziom0"
          }
        }
      },
      "version": 7,
      "currency": "eur",
      "segments": [],
      "levelPercent": "0.00%"
    }



Update a customer
-----------------

To update an existing customer, you need to call the ``/api/<storeCode>/customer/<customer>`` endpoint with the ``PUT`` method.

.. note::

    The fields you omit will not be affected. The fields you include and leave empty will have their current values removed.
    Eg. ``customer[email]=&customer[loyaltyCardNumber]=000012`` will set loyaltyCardNumber, erase email and leave all other fields unaffected.

.. note::

    All simple fields can be updated separately, but compound fields (address, company) must be updated as a whole.
    Any attempt to update only one of the address fields will result in deleting other parts of the address.
    Any attempt to update only the name or NIP will result in error code 500.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/<storeCode>/customer/<customer>

+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                                                |
+====================================+================+=============================================================================================+
| Authorization                      | header         | Token received during authentication                                                        |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the updated customer belongs to.                                          |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| <customer>                         | query          | Customer ID                                                                                 |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[firstName]                | request        | *(optional)* First name                                                                     |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[lastName]                 | request        | *(optional)* Last name                                                                      |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[gender]                   | request        | *(optional)* Gender. Possible values ``male``, ``female``                                   |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[email]                    | request        | *(optional)* *(unique)* E-mail address                                                      |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[phone]                    | request        | *(optional)* A phone number *(unique)*                                                      |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[birthDate]                | request        | *(optional)* Birth date in format YYYY-MM-DD HH:mm, for example ``2017-10-05``              |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[createdAt]                | request        | *(optional)* Created at in format YYYY-MM-DD HH:mm:ss, for example ``2017-01-01 14:15:16``. |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][street]          | request        | *(optional)* Street name                                                                    |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][address1]        | request        | *(optional)* Building number                                                                |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][address2]        | request        | *(optional)* Flat/Unit name                                                                 |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][postal]          | request        | *(optional)* Post code                                                                      |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][city]            | request        | *(optional)* City name                                                                      |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][province]        | request        | *(optional)* Province name                                                                  |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][country]         | request        | *(optional)* Country name                                                                   |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[company][name]            | request        | *(optional)* Company name                                                                   |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[company][nip]             | request        | *(optional)* Tax ID                                                                         |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[loyaltyCardNumber]        | request        | *(optional)* Loyalty card number *(unique)*                                                 |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[labels]                   | request        | *(optional)* String of labels in form of ``key1:val1;key2:val2``.                           |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[agreement1]               | request        | *(optional)* First agreement. Set 1 if true, otherwise 0                                    |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[agreement2]               | request        | *(optional)* Second agreement. Set 1 if true, otherwise 0                                   |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[agreement3]               | request        | *(optional)* Third agreement. Set 1 if true, otherwise 0                                    |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[referral_customer_email]  | request        | *(optional)* Referral customer e-mail address.                                              |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/e0eb0355-8aaa-4fb1-8159-f58e81b7a25c \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customer[email]=john4@example.com" \
        -d "customer[phone]=" \
        -d "customer[agreement2]=1"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json


    {
        "customerId": "e0eb0355-8aaa-4fb1-8159-f58e81b7a25c"
    }

.. note::

    In earlier versions, this endpoint returned user data after performing an update.
    This feature was removed because in certain circumstances old data from before the update could be returned.
    Use GET /api/customer/<customer> after the update to always get the up-to-date values instead.

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/e0eb0355-8aaa-4fb1-8159-f58e81b7a25c \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customer[phone]=+440000000"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
        "form": {
            "children": {
                "firstName": {},
                "lastName": {},
                "gender": {},
                "email": {},
                "phone": {
                    "errors": [
                        "This value is not a valid phone number."
                    ]
                },
                "birthDate": {},
                "createdAt": {},
                "address": {
                    "children": {
                        "street": {},
                        "address1": {},
                        "address2": {},
                        "postal": {},
                        "city": {},
                        "province": {},
                        "country": {}
                    }
                },
                "company": {
                    "children": {
                        "name": {},
                        "nip": {}
                    }
                },
                "loyaltyCardNumber": {},
                "labels": {},
                "agreement1": {},
                "agreement2": {},
                "agreement3": {},
                "referral_customer_email": {},
                "levelId": {},
                "posId": {}
            }
        },
        "errors": []
    }



Confirm a change of authentication credential
---------------------------------------------

To activate a change of phone number when it is used as a log in credential, you need to call ``/api/<storeCode>/customer/confirm-change/<token>`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/confirm-change/<token>

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer belongs to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <token>                            | request        |  Customer's token, SMS activation code                         |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/confirm-change/153105\
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *token = 153105* is an example value. Your value can be different.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content

.. code-block:: json

    (no content)



Customer registrations
----------------------

To get information about customer registrations, you need to call the ``/api/<storeCode>/customer/registrations`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/customer/registrations

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         | Token received during authentication                           |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customers belong to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <interval>                         | request        | Group result by (day|month|year)                               |
+------------------------------------+----------------+----------------------------------------------------------------+
| <lastDays>                         | request        | Display data in last days                                      |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/registrations \
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
      "2018-01-06": 0,
      "2018-01-07": 0,
      "2018-01-08": 0,
      "2018-01-09": 0,
      "2018-01-10": 0,
      "2018-01-11": 0,
      "2018-01-12": 0,
      "2018-01-13": 0,
      "2018-01-14": 0,
      "2018-01-15": 0,
      "2018-01-16": 0,
      "2018-01-17": 0,
      "2018-01-18": 0,
      "2018-01-19": 0,
      "2018-01-20": 0,
      "2018-01-21": 0,
      "2018-01-22": 0,
      "2018-01-23": 0,
      "2018-01-24": 0,
      "2018-01-25": 0,
      "2018-01-26": 0,
      "2018-01-27": 0,
      "2018-01-28": 0,
      "2018-01-29": 0,
      "2018-01-30": 0,
      "2018-01-31": 0,
      "2018-02-01": 0,
      "2018-02-02": 5,
      "2018-02-03": 0,
      "2018-02-04": 0
    }



Remove customer's avatar
------------------------

To remove the avatar of a customer using an admin token, you need to call the ``/api/<storeCode>/customer/<customer>/avatar`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/<storeCode>/customer/<customer>/avatar

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer belongs to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/avatar \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Get a customer's avatar
-----------------------

To get a customer's avatar using an admin token, you need to call the ``/api/<storeCode>/customer/<customer>/avatar`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/customer/<customer>/avatar

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer belongs to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/avatar \
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

    STATUS: 204 No Content



Set customer's avatar
---------------------

To set a customer's avatar using an admin token, you need to call the ``/api/<storeCode>/customer/<customer>/avatar`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/<customer>/avatar

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer belongs to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+
| avatar[file]                       | request        |  Avatar file                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/avatar \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "avatar[file]=C:\\fakepath\\avatar.jpg"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *photo[file]=C:\fakepath\avatar.png* is an example value. Your value may be different.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Assign a customer to a level
----------------------------

To assign a customer to a level using an admin token, you need to call the ``/api/<storeCode>/customer/<customer>/level`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/<customer>/level

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer belongs to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+
| levelId                            | request        |  Level ID                                                      |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/level \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "levelId=e82c96cf-32a3-43bd-9034-4df343e52222"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    []



Assign a POS to a customer
--------------------------

To assign a POS to a customer using an admin token, you need to call the ``/api/<storeCode>/customer/<customer>/pos`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/<customer>/pos

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer belongs to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+
| posId                              | request        |  POS ID                                                        |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/pos \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "posId=00000000-0000-474c-1111-b0dd880c07e3"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    []



List Pushy tokens
-----------------

To list pushy tokens using an admin token, you need to call the ``/api/<storeCode>/customer/<customer>/pushy-token`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/customer/<customer>/pushy-token

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer belongs to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer's ID                                                 |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/pushy-token \
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

    {
      "tokens": [
        "pushy_token"
      ]
    }



Add a Pushy token
-----------------

To add a Pushy token to a customer using an admin token, you need to call the ``/api/<storeCode>/customer/<customer>/pushy-token`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/<customer>/pushy-token

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer belongs to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+
| customer[pushyToken]               | request        |  Customer's pushy Token                                        |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/pushy-token \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customer[pushyToken]=pushy_token"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Remove a Pushy token
--------------------

To remove a pushy token, you need to call the ``/api/<storeCode>/customer/<customer>/pushy-token/<tokenToRemove>`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/<storeCode>/customer/<customer>/pushy-token/<tokenToRemove>

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer belongs to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+
| <tokenToRemove>                    | query          |  Pushy token to remove                                         |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/pushy-token/pushy_token \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Remove a customer from a manually assigned level
------------------------------------------------

To unassign a customer from a manually assigned level using a token, you need to call the ``/api/<storeCode>/customer/<customer>/remove-manually-level`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/<customer>/remove-manually-level

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer belongs to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/remove-manually-level \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Customer status (customer)
--------------------------

To retrieve the status of a customer, you need to call the ``/api/<storeCode>/customer/customer/<customer>/status`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/customer/customer/<customer>/status

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <storeCode>          | query          | Code of the store the customer belongs to.             |
+----------------------+----------------+--------------------------------------------------------+
| <customer>           | query          | Customer UUID                                          |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/customer/00000000-0000-474c-b092-b0dd880c07e1/status \
        -X "GET" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."


.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "firstName": "John",
        "lastName": "Doe",
        "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
        "points": 161.9,
        "p2pPoints": 0,
        "totalEarnedPoints": 274.9,
        "usedPoints": 25,
        "expiredPoints": 88,
        "lockedPoints": 0,
        "level": "0.00%",
        "levelName": "level0",
        "levelConditionValue": 0,
        "nextLevel": "5.00%",
        "nextLevelName": "level1",
        "nextLevelConditionValue": 20,
        "transactionsAmountWithoutDeliveryCosts": 3,
        "transactionsAmountToNextLevel": 17,
        "averageTransactionsAmount": "1.50",
        "transactionsCount": 2,
        "transactionsAmount": 3,
        "currency": "eur",
        "pointsExpiringNextMonth": 161.9,
        "pointsExpiringBreakdown": {
            "2019-04-14": 33,
            "2019-04-15": 116.9,
            "2019-04-17": 12
        }
    }

Send an activation code to a customer as an admin
-------------------------------------------------

To send an SMS activation code to specific customer, you need to call the ``/api/<storeCode>/admin/customer/<customer>/send-sms-code`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/admin/customer/<customer>/send-sms-code

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type | Description                                        |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| <storeCode>                                    | query          | Code of the store the customer belongs to.         |
+------------------------------------------------+----------------+----------------------------------------------------+
| <customer>                                     | query          | Customer UUID                                      |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/customer/00000000-0000-474c-b092-b0dd880c07e1/send-sms-code \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When using endpoints starting with ``/api/<storeCode>/admin``, you need to authorize using admin account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK



Send an activation token as a customer
--------------------------------------

To send/resend an sms activation code, you need to call the ``/api/<storeCode>/customer/customer-phone/send-sms-code`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/customer-phone/send-sms-code

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                       |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| <storeCode>                                    | query          | Code of the store the customer belongs to.         |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/customer-phone/send-sms-code \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

Import customers
----------------

To import customers, you need to call the ``/api/<storeCode>/admin/customer/import`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/admin/customer/import

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type | Description                                        |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| <storeCode>                                    | query          | Code of the store the customers will belong to.    |
+------------------------------------------------+----------------+----------------------------------------------------+
| file[file]                                     | query          | XML file                                           |
+------------------------------------------------+----------------+----------------------------------------------------+

Example Windows
^^^^^^^^^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/customer/import \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "file[file]=C:\\fakepath\\customers.xml"

Example Unix
^^^^^^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/customer/import \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "file[file]=@/path/to/file/customers.xml"

.. warning::

    If you choose in setting a preferred communication method:
     - SMS - then the user identifier is ``phone number``. It is required data in the imported file.
     - email - it's default value - then the user identifier is ``email address``.  It is a required data in the imported file.

.. note::

    When using endpoints starting with ``/api/<storeCode>/admin``, you need to authorize using admin account credentials.

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
          "status": "success",
          "processImportResult": {
            "object": "4e2a75c2-f194-40e7-b54e-f208b2fd1732"
          },
          "identifier": "aXXX2222X1@tXXXXXXXst.pl"
        },
        {
          "status": "success",
          "processImportResult": {
            "object": "db081ad2-d035-4edd-8bda-21da198592db"
          },
          "identifier": "222b1222@test.pl"
        },
        {
          "status": "error",
          "message": "Convert exception: birthDate has invalid date format (Y-m-d required)",
          "identifier": "b22221a@st.pl"
        },
        {
          "status": "success",
          "processImportResult": {
            "object": "c4c169b0-265b-4ead-94c0-1972f181e100"
          },
          "identifier": "aa2222c@dgf.pl"
        },
        {
          "status": "error",
          "message": "Convert exception: gender is required node",
          "identifier": "bz22221z@test.pl"
        },
        {
          "status": "success",
          "processImportResult": {
            "object": "479129a4-283b-414d-b48b-4c3541f9f8d9"
          },
          "identifier": "bxx2222x@teist.pl"
        },
        {
          "status": "success",
          "processImportResult": {
            "object": "00c2f4ff-a8d0-4b31-a119-2bb3f0ec7b6e"
          },
          "identifier": "bx2222x@tetst.pl"
        },
        {
          "status": "error",
          "message": "Convert exception: gender is required node",
          "identifier": "cccc2222cc@test.pl"
        },
        {
          "status": "success",
          "processImportResult": {
            "object": "7f4d0ebd-69e5-488b-b7e2-42985792d63c"
          },
          "identifier": "vvvv111v7@test.pl"
        },
        {
          "status": "success",
          "processImportResult": {
            "object": "36c0e0e7-1231-4817-9fc9-3fd26280026f"
          },
          "identifier": "bb111bbbb@tesyyt.pl"
        },
        {
          "status": "error",
          "message": "Convert exception: gender is required node",
          "identifier": "nnnjn111n@test.pl"
        }
      ],
      "totalProcessed": 11,
      "totalSuccess": 7,
      "totalFailed": 4
    }



Register a new customer as an admin
-----------------------------------

To create a new customer, you need to call the ``/api/<storeCode>/admin/customer/register`` endpoint with the ``POST`` method.

.. note::

    This endpoint allows you to set more customer parameters than ``/api/<storeCode>/customer/self_register`` and is used when creating
    a new customer in the admin cockpit or POS cockpit. The self register endpoint is used in the client cockpit for registration
    and has some limitations.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/admin/customer/register

+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type | Description                                                                                 |
+====================================+================+=============================================================================================+
| Authorization                      | header         | Token received during authentication                                                        |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer will belong to.                                              |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[firstName]                | request        | First name                                                                                  |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[lastName]                 | request        | Last name                                                                                   |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[gender]                   | request        | *(optional)* Gender. Possible values ``male``, ``female``, ``not_disclosed``                |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[email]                    | request        | *(unique)* E-mail address                                                                   |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[phone]                    | request        | *(optional)* A phone number *(unique)*                                                      |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[birthDate]                | request        | *(optional)* Birth date in format YYYY-MM-DD HH:mm, for example ``2017-10-05``              |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[createdAt]                | request        | *(optional)* Created at in format YYYY-MM-DD HH:mm:ss, for example ``2017-01-01 14:15:16``. |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][street]          | request        | *(optional)* Street name                                                                    |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][address1]        | request        | *(optional)* Building number                                                                |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][address2]        | request        | *(optional)* Flat/Unit name                                                                 |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][postal]          | request        | *(optional)* Post code                                                                      |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][city]            | request        | *(optional)* City name                                                                      |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][province]        | request        | *(optional)* Province name                                                                  |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[address][country]         | request        | *(optional)* Country name                                                                   |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[company][name]            | request        | *(optional)* Company name                                                                   |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[company][nip]             | request        | *(optional)* Tax ID                                                                         |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[loyaltyCardNumber]        | request        | *(optional)* Loyalty card number *(unique)*                                                 |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[labels]                   | request        | *(optional)* String of labels in form of ``key1:val1;key2:val2``.                           |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[agreement1]               | request        | First agreement. Set 1 if true, otherwise 0                                                 |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[agreement2]               | request        | *(optional)* Second agreement. Set 1 if true, otherwise 0                                   |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[agreement3]               | request        | *(optional)* Third agreement. Set 1 if true, otherwise 0                                    |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| customer[referral_customer_email]  | request        | *(optional)* Referral customer e-mail address.                                              |
+------------------------------------+----------------+---------------------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/customer/register \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customer[firstName]=John" \
        -d "customer[lastName]=Kowalski" \
        -d "customer[email]=john@example.com" \
        -d "customer[phone]=0665998332" \
        -d "customer[agreement1]=1"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customerId": "e0eb0355-8aaa-4fb1-8159-f58e81b7a25c",
      "email": "john@example.com"
    }



Remove customer
---------------

To remove the customer using admin token you need to call the ``/api/<storeCode>/customer/<customer>`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/<storeCode>/customer/<customer>

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <storeCode>                        | query          | Code of the store the customer belongs to.                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/1cb6d205-8b77-40e1-a801-052185ed52d9 \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content

