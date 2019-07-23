Customer API
============

These endpoints allow you to easily manage customers.

.. note::

    Each role in the Open Loyalty has individual endpoints to manage customers.



Activate a customer
-------------------

To activate a customer you need to call the ``/api/admin/customer/{customer}/activate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/customer/<customer>/activate

+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                                                  |
+====================================+================+===============================================================================================+
| Authorization                      | header         |  Token received during authentication                                                         |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| <customer>                         | request        |  Customer's UUID                                                                              |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/customer/1bbafb37-b51b-47c5-b3e4-e0a2d028e655/activate \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customer = 1bbafb37-b51b-47c5-b3e4-e0a2d028e655* id is an example value. Your value can be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Deactivate a customer
---------------------

To deactivate a customer you need to call the ``/api/admin/customer/{customer}/deactivate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/customer/<customer>/deactivate

+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                                                  |
+====================================+================+===============================================================================================+
| Authorization                      | header         |  Token received during authentication                                                         |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| <customer>                         | request        |  Customer's UUID                                                                              |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/customer/1bbafb37-b51b-47c5-b3e4-e0a2d028e655/deactivate \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customer = 1bbafb37-b51b-47c5-b3e4-e0a2d028e655* id is an example value. Your value can be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Get customer status
-------------------

To get a customer status you need to call the ``/api/admin/customer/{customer}/status`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/customer/<customer>/status

+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                                                  |
+====================================+================+===============================================================================================+
| Authorization                      | header         |  Token received during authentication                                                         |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| <customer>                         | request        |  Customer's UUID                                                                              |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/customer/1bbafb37-b51b-47c5-b3e4-e0a2d028e655/status \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customer = 1bbafb37-b51b-47c5-b3e4-e0a2d028e655* id is an example value. Your value can be different.
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

To get customers list you need to call the ``/api/customer/`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer

+------------------------------------+----------------+------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                           |
+====================================+================+========================================================================+
| Authorization                      | header         |  Token received during authentication                                  |
+------------------------------------+----------------+------------------------------------------------------------------------+
| firstName                          | request        | *(optional)* Customer's first name                                     |
+------------------------------------+----------------+------------------------------------------------------------------------+
| lastName                           | request        | *(optional)* Customer's last name                                      |
+------------------------------------+----------------+------------------------------------------------------------------------+
| phone                              | request        | *(optional)* Customer's phone                                          |
+------------------------------------+----------------+------------------------------------------------------------------------+
| email                              | request        | *(optional)* Customer's email address                                  |
+------------------------------------+----------------+------------------------------------------------------------------------+
| loyaltyCardNumber                  | request        | *(optional)* Customer's loyalty card number                            |
+------------------------------------+----------------+------------------------------------------------------------------------+
| transactionsAmount                 | request        | *(optional)* Customer's transactions amount                            |
+------------------------------------+----------------+------------------------------------------------------------------------+
| averageTransactionAmount           | request        | *(optional)* Customer's average transaction amount                     |
+------------------------------------+----------------+------------------------------------------------------------------------+
| transactionsCount                  | request        | *(optional)* Customer's transactions count                             |
+------------------------------------+----------------+------------------------------------------------------------------------+
| daysFromLastTransaction            | request        | *(optional)* Customers days from last transaction                      |
+------------------------------------+----------------+------------------------------------------------------------------------+
| hoursFromLastUpdate                | request        | *(optional)* Customer's hours from last update                         |
+------------------------------------+----------------+------------------------------------------------------------------------+
| strict                             | query          | *(optional)* If true, search for exact value, otherwise like value     |
|                                    |                | For example ``1``, by default = 0                                      |
+------------------------------------+----------------+------------------------------------------------------------------------+
| page                               | query          | *(optional)* Start from page, by default 1                             |
+------------------------------------+----------------+------------------------------------------------------------------------+
| perPage                            | query          | *(optional)* Number of items to display per page,                      |
|                                    |                | by default = 10                                                        |
+------------------------------------+----------------+------------------------------------------------------------------------+
| sort                               | query          | *(optional)* Sort by column name                                       |
+------------------------------------+----------------+------------------------------------------------------------------------+
| direction                          | query          | *(optional)* Direction of sorting [ASC, DESC]                          |
+------------------------------------+----------------+------------------------------------------------------------------------+
| _locale                            | query          | *(optional)* Retrieves data in given locale                            |
+------------------------------------+----------------+------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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

    curl http://localhost:8181/api/customer \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."
        -d "email=oloy.com" \
        -d "strict=0" \
        -d "page=1" \
        -d "perPage=2" \
        -d "sort=customerId" \
        -d "direction=asc"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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
          "email": "user-temp@oloy.com",
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
          "email": "user@oloy.com",
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

    curl http://localhost:8181/api/customer \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."
        -d "email=oloy.com" \
        -d "strict=1" \
        -d "page=1" \
        -d "perPage=2" \
        -d "sort=customerId" \
        -d "direction=asc"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customers": [],
      "total": 0
    }



Get customers list as an admin
------------------------------

To get list of all customers you need to call the ``/api/admin/customer`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/customer

+------------------------------------+----------------+------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                           |
+====================================+================+========================================================================+
| Authorization                      | header         |  Token received during authentication                                  |
+------------------------------------+----------------+------------------------------------------------------------------------+
| firstName                          | request        | *(optional)* Customer's first name                                     |
+------------------------------------+----------------+------------------------------------------------------------------------+
| lastName                           | request        | *(optional)* Customer's last name                                      |
+------------------------------------+----------------+------------------------------------------------------------------------+
| phone                              | request        | *(optional)* Customer's phone                                          |
+------------------------------------+----------------+------------------------------------------------------------------------+
| email                              | request        | *(optional)* Customer's email address                                  |
+------------------------------------+----------------+------------------------------------------------------------------------+
| loyaltyCardNumber                  | request        | *(optional)* Customer's loyalty card number                            |
+------------------------------------+----------------+------------------------------------------------------------------------+
| transactionsAmount                 | request        | *(optional)* Customer's transactions amount                            |
+------------------------------------+----------------+------------------------------------------------------------------------+
| averageTransactionAmount           | request        | *(optional)* Customer's average transaction amount                     |
+------------------------------------+----------------+------------------------------------------------------------------------+
| transactionsCount                  | request        | *(optional)* Customer's transactions count                             |
+------------------------------------+----------------+------------------------------------------------------------------------+
| daysFromLastTransaction            | request        | *(optional)* Customers days from last transaction                      |
+------------------------------------+----------------+------------------------------------------------------------------------+
| hoursFromLastUpdate                | request        | *(optional)* Customer's hours from last update                         |
+------------------------------------+----------------+------------------------------------------------------------------------+
| strict                             | query          | *(optional)* If true, search for exact value, otherwise like value     |
|                                    |                | For example ``1``, by default = 0                                      |
+------------------------------------+----------------+------------------------------------------------------------------------+
| page                               | query          | *(optional)* Start from page, by default 1                             |
+------------------------------------+----------------+------------------------------------------------------------------------+
| perPage                            | query          | *(optional)* Number of items to display per page,                      |
|                                    |                | by default = 10                                                        |
+------------------------------------+----------------+------------------------------------------------------------------------+
| sort                               | query          | *(optional)* Sort by column name                                       |
+------------------------------------+----------------+------------------------------------------------------------------------+
| direction                          | query          | *(optional)* Direction of sorting [ASC, DESC]                          |
+------------------------------------+----------------+------------------------------------------------------------------------+
| _locale                            | query          | *(optional)* Retrieves data in given locale                            |
+------------------------------------+----------------+------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/customer \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "email=oloy.com" \
        -d "strict=0" \
        -d "page=1" \
        -d "perPage=2" \
        -d "sort=customerId" \
        -d "direction=asc"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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

To activate a customer using a token (sms code) you need to call the ``/api/customer/activate-sms/{token}`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/activate-sms/<token>

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <token>                            | request        |  Customer's token, SMS activation code                         |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/activate-sms/954604\
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *token = 954604* is an example value. Your value can be different.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Activate a customer using activation token
------------------------------------------

To activate a customer using a token you need to call the ``/api/customer/activate/{token}`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/activate/<token>

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <token>                            | request        |  Customer's token                                              |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/activate/abcde \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *token = abcde* is an example value. Your value can be different.
    For testing, the value can be checked in the database, table ``ol_user``, field ``action_token``.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Check if customer with given phone number or email exists
---------------------------------------------------------

To check if customer with given phone number or email exists you need to call the ``/api/customer/check`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/check

+------------------------------------+----------------+------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                           |
+====================================+================+========================================================================+
| Authorization                      | header         |  Token received during authentication                                  |
+------------------------------------+----------------+------------------------------------------------------------------------+
| emailOrPhone                       | request        |  Customer's email or phone                                             |
+------------------------------------+----------------+------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/check?emailOrPhone=899000333 \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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

To create a new customer you need to call the ``/api/customer/register`` endpoint with the ``POST`` method.

.. note::

    This endpoint allows to set more customer parameters than ``/api/customer/self_register`` and is used when creating
    a new customer in the admin cockpit or pos cockpit. Self register endpoint is used in the client cockpit for registration
    and has some limitations.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/register

+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                                                  |
+====================================+================+===============================================================================================+
| Authorization                      | header         |  Token received during authentication                                                         |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[firstName]                | request        |  First name                                                                                   |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[lastName]                 | request        |  Last name                                                                                    |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[gender]                   | request        |  *(optional)* Gender. Possible values ``male``, ``female``, ``not_disclosed``                 |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[email]                    | request        |  *(unique)* E-mail address                                                                    |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[phone]                    | request        |  *(optional)* A phone number *(unique)*                                                       |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[birthDate]                | request        |  *(optional)* Birth date in format YYYY-MM-DD HH:mm, for example ``2017-10-05``               |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[createdAt]                | request        |  *(optional)* Created at in format YYYY-MM-DD HH:mm:ss, for example ``2017-01-01 14:15:16``.  |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[address][street]          | request        |  *(optional)* Street name                                                                     |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[address][address1]        | request        |  *(optional)* Building number                                                                 |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[address][address2]        | request        |  *(optional)* Flat/Unit name                                                                  |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[address][postal]          | request        |  *(optional)* Post code                                                                       |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[address][city]            | request        |  *(optional)* City name                                                                       |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[address][province]        | request        |  *(optional)* Province name                                                                   |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[address][country]         | request        |  *(optional)* Country name                                                                    |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[company][name]            | request        |  *(optional)* Company name                                                                    |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[company][nip]             | request        |  *(optional)* Tax ID                                                                          |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[loyaltyCardNumber]        | request        |  *(optional)* Loyalty card number *(unique)*                                                  |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[labels]                   | request        | *(optional)* String of labels in form of ``key1:val1;key2:val2``.                             |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[agreement1]               | request        |  First agreement. Set 1 if true, otherwise 0                                                  |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[agreement2]               | request        |  *(optional)* Second agreement. Set 1 if true, otherwise 0                                    |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[agreement3]               | request        |  *(optional)* Third agreement. Set 1 if true, otherwise 0                                     |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[referral_customer_email]  | request        |  *(optional)* Referral customer e-mail address.                                               |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/register \
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
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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

    curl http://localhost:8181/api/customer/register \
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
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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

    curl http://localhost:8181/api/customer/register \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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
          "posId": {},
          "sellerId": {}
        }
      },
      "errors": []
    }



Get customer details
---------------------

To get details about a customer you need to call the ``/api/customer/<customer>`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/<customer>

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/00000000-0000-474c-b092-b0dd880c07e1 \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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
      "email": "user@oloy.com",
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

To update an existing customer you need to call the ``/api/customer/{customer}`` endpoint with the ``PUT`` method.

.. note::

    The fields you omit will not be affected. The fields you include and leave empty will have their current values removed.
    Eg. ``customer[email]=&customer[loyaltyCardNumber]=000012`` will set loyaltyCardNumber, erase email and leave all other fields unaffected.

.. note::

    All simple fields can be updated separately, but compound fields (address, company) must be updated whole.
    Attempt to update only one of the address' fields will result in deleting other parts of the address.
    Attempt to update only name or nip will result in error code 500.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/customer/<customer>

+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                                                |
+====================================+================+=============================================================================================+
| Authorization                      | header         | Token received during authentication                                                        |
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

    curl http://localhost:8181/api/customer/e0eb0355-8aaa-4fb1-8159-f58e81b7a25c \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customer[email]=john4@example.com" \
        -d "customer[phone]=" \
        -d "customer[agreement2]=1"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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

    curl http://localhost:8181/api/customer/e0eb0355-8aaa-4fb1-8159-f58e81b7a25c \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customer[phone]=+440000000"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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
                "posId": {},
                "sellerId": {}
            }
        },
        "errors": []
    }



Customer registrations in last 30 days
--------------------------------------

To get information about customer registrations per day in last thirty days you need to call the
``/api/customer/registrations/daily`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/registrations/daily

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/registrations/daily \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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

To remove the avatar of a customer using admin token you need to call the ``/api/customer/{customer}/avatar`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/customer/<customer>/avatar

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/avatar \
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



Get customer's avatar
---------------------

To get customer's avatar using admin token you need to call the ``/api/customer/{customer}/avatar`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/<customer>/avatar

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/avatar \
        -X "GET" \
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



Set customer's avatar
---------------------

To set customer's avatar using admin token you need to call the ``/api/customer/{customer}/avatar`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/<customer>/avatar

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+
| avatar[file]                       | request        |  Avatar file                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/avatar \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "avatar[file]=C:\\fakepath\\avatar.jpg"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *photo[file]=C:\fakepath\avatar.png* is an example value. Your value can be different.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Assign a customer to a level
----------------------------

To assign a customer to a level using admin token you need to call the ``/api/customer/{customer}/level`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/<customer>/level

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+
| levelId                            | request        |  Level ID                                                      |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/level \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "levelId=e82c96cf-32a3-43bd-9034-4df343e52222"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    []



Assign a POS to a customer
--------------------------

To assign a POS to a customer using admin token you need to call the ``/api/customer/{customer}/pos`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/<customer>/pos

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+
| posId                              | request        |  POS ID                                                        |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/pos \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "posId=00000000-0000-474c-1111-b0dd880c07e3"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    []



List Pushy tokens
-----------------

To list pushy tokens using admin token you need to call the ``/api/customer/{customer}/pushy-token`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/<customer>/pushy-token

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer's ID                                                 |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/pushy-token \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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

To add a Pushy token to a customer using admin token you need to call the ``/api/customer/{customer}/pushy-token`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/<customer>/pushy-token

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+
| customer[pushyToken]               | request        |  Customer's pushy Token                                        |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/pushy-token \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customer[pushyToken]=pushy_token"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Remove a Pushy token
--------------------

To remove a pushy token you need to call the ``/api/customer/{customer}/pushy-token/{tokenToRemove}`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/customer/<customer>/pushy-token/<tokenToRemove>

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+
| <tokenToRemove>                    | query          |  Pushy token to remove                                         |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/pushy-token/pushy_token \
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



Remove a customer from a manually assigned level
------------------------------------------------

To unassign customer from a manually assigned level using a token you need to call the ``/api/customer/{customer}/remove-manually-level`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/<customer>/remove-manually-level

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                   |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/1cb6d205-8b77-40e1-a801-052185ed52d9/remove-manually-level \
        -X "POST" \
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



Customer status (customer)
--------------------------

To retrieve a status of a customer you need to call the ``/api/customer/{customer}/status`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/<customer>/status

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <customer>           | query          | Customer UUID                                          |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/00000000-0000-474c-b092-b0dd880c07e1/status \
        -X "GET" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."


.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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



Customer status (seller)
------------------------

To retrieve a status of specific customer you need to call the ``/api/seller/customer/{customer}/status`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/customer/<customer>/status

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <customer>           | query          | Customer UUID                                          |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/customer/00000000-0000-474c-b092-b0dd880c07e1/status \
        -X "GET" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When using endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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

To send an SMS activation code to specific customer you need to call the ``/api/admin/customer/{customer}/send-sms-code`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/customer/<customer>/send-sms-code

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type | Description                                        |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| <customer>                                     | query          | Customer UUID                                      |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/customer/00000000-0000-474c-b092-b0dd880c07e1/send-sms-code \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When using endpoints starting with ``/api/admin`` you need to authorize using admin account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK



Send an activation token as a customer
--------------------------------------

To send/resend sms activation code you need to call the ``/api/customer/customer-phone/send-sms-code`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/customer-phone/send-sms-code

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                       |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/customer-phone/send-sms-code \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK



Send SMS activation code as a seller
------------------------------------

To send SMS activation code to a specific customer you need to call the ``/api/seller/customer/{customer}/send-sms-code`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/seller/customer/<customer>/send-sms-code

+---------------------------+----------------+-------------------------------------------------------------------------+
| Parameter                 | Parameter type |  Description                                                            |
+===========================+================+=========================================================================+
| Authorization             | header         | Token received during authentication                                    |
+---------------------------+----------------+-------------------------------------------------------------------------+
| <customer>                | query          |  Customer UUID                                                          |
+---------------------------+----------------+-------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/customer/00000000-0000-474c-b092-b0dd880c07e1/send-sms-code \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When using endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Assign a POS to a customer as a seller
--------------------------------------

To assign POS to specific customer you need to call the ``/api/seller/customer/{customer}/pos`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/seller/customer/<customer>/pos

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                       |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| <customer>                                     | query          | Customer UUID                                      |
+------------------------------------------------+----------------+----------------------------------------------------+
| posId                                          | query          | POS UUID                                           |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/customer/00000000-0000-474c-b092-b0dd880c07e1/pos \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "posId=00000000-0000-474c-1111-b0dd880c07e3"

.. note::

    When using endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *posId = 00000000-0000-474c-1111-b0dd880c07e3* and *customer = 00000000-0000-474c-b092-b0dd880c07e1* are example values.
    Your values can be different.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK



Activate a customer as a seller
-------------------------------

To activate a specific customer you need to call the ``/api/seller/customer/{customer}/activate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/seller/customer/<customer>/activate

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                       |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| <customer>                                     | query          | Customer UUID                                      |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/customer/00000000-0000-474c-b092-b0dd880c07e1/activate \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When using endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customerId = 00000000-0000-474c-b092-b0dd880c07e1* id is an example value. Your value can be different.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK



Deactivate a customer as a seller
---------------------------------

To deactivate a specific customer you need to call the ``/api/seller/customer/{customer}/deactivate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/seller/customer/<customer>/deactivate

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type | Description                                        |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| <customer>                                     | query          | Customer UUID                                      |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/customer/00000000-0000-474c-b092-b0dd880c07e1/deactivate \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When using endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customerId = 00000000-0000-474c-b092-b0dd880c07e1* id is an example value. Your value can be different.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK



Register new customer as a seller
---------------------------------

To register customer you need to call the ``/api/seller/customer/register`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/seller/customer/register

.. note::

    This endpoint allows to set more customer parameters than ``/api/customer/self_register`` and is used when creating
    a new customer in the admin cockpit or pos cockpit. Self register endpoint is used in the client cockpit for registration
    and has some limitations.

+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type | Description                                                                                 |
+====================================+================+=============================================================================================+
| Authorization                      | header         | Token received during authentication                                                        |
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

    curl http://localhost:8181/api/seller/customer/register \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customer[firstName]=Lady" \
        -d "customer[lastName]=Mini" \
        -d "customer[email]=test@openloyalty.com" \
        -d "customer[gender]=female" \
        -d "customer[agreement1]=1"

.. note::

    When using endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customerId": "53c16b8e-db1e-42f9-af71-3bb76f5c3aca",
      "email": "test@openloyalty.com"
    }



Search customers as a seller
----------------------------

To search customer in POS you need to call the ``/api/pos/search/customer`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/pos/search/customer

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type | Description                                                    |
+====================================+================+================================================================+
| Authorization                      | header         | Token received during authentication                           |
+------------------------------------+----------------+----------------------------------------------------------------+
| search[loyaltyCardNumber]          | query          | *(optional)* Loyalty card number                               |
+------------------------------------+----------------+----------------------------------------------------------------+
| search[phone]                      | request        | *(optional)* A phone number                                    |
+------------------------------------+----------------+----------------------------------------------------------------+
| search[email]                      | request        | *(optional)* Email address                                     |
+------------------------------------+----------------+----------------------------------------------------------------+
| search[firstName]                  | request        | *(optional)* Fisrt name                                        |
+------------------------------------+----------------+----------------------------------------------------------------+
| search[lastName]                   | request        | *(optional)* Last name                                         |
+------------------------------------+----------------+----------------------------------------------------------------+
| search[city]                       | request        | *(optional)* City name                                         |
+------------------------------------+----------------+----------------------------------------------------------------+
| search[postcode]                   | request        | *(optional)* Post code                                         |
+------------------------------------+----------------+----------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/pos/search/customer \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "search[firstName]=John" \
        -d "search[lastName]=Doe"

.. note::

    When using this endpoint you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customers": [
        {
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "active": false,
          "posId": "00000000-0000-474c-1111-b0dd880c07e3",
          "firstName": "John",
          "lastName": "Doe",
          "gender": "male",
          "email": "user@oloy.com",
          "phone": "+48234234000",
          "birthDate": "1990-09-11T02:00:00+0200",
          "lastLevelRecalculation": "2019-03-15T13:00:05+0100",
          "loyaltyCardNumber": "47834433524",
          "createdAt": "2016-08-08T10:53:14+0200",
          "levelId": "e82c96cf-32a3-43bd-9034-4df343e50000",
          "agreement1": true,
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
            "type": "blocked"
          },
          "updatedAt": "2019-03-18T14:44:49+0100",
          "campaignPurchases": [
            {
              "canBeUsed": false,
              "purchaseAt": "2019-03-18T13:45:39+0100",
              "costInPoints": 1,
              "campaignId": "f1eddc46-e985-43e8-bc2a-8007dca3df95",
              "used": true,
              "coupon": {
                "id": "83d6a65e-d237-4049-84aa-bb107cd6f9a4",
                "code": "test1"
              },
              "status": "active",
              "activeTo": "2019-06-16T13:45:39+0200",
              "deliveryStatus": "ordered",
              "usageDate": "2019-03-18T13:51:10+0100"
            },
            {
              "canBeUsed": false,
              "purchaseAt": "2019-03-18T13:45:39+0100",
              "costInPoints": 1,
              "campaignId": "f1eddc46-e985-43e8-bc2a-8007dca3df95",
              "used": true,
              "coupon": {
                "id": "6a2456ec-49b3-4970-9ac4-75ca01eab0ee",
                "code": "test2"
              },
              "status": "active",
              "activeTo": "2019-06-16T13:45:39+0200",
              "deliveryStatus": "ordered",
              "usageDate": "2019-03-18T13:51:10+0100"
            }
          ],
          "transactionsCount": 2,
          "transactionsAmount": 3,
          "transactionsAmountWithoutDeliveryCosts": 3,
          "amountExcludedForLevel": 0,
          "averageTransactionAmount": 1.5,
          "lastTransactionDate": "2019-03-16T12:53:23+0100",
          "labels": [],
          "level": {
            "levelId": {
              "id": "e82c96cf-32a3-43bd-9034-4df343e50000"
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
          "currency": "eur",
          "levelPercent": "0.00%",
          "posIdentifier": "pos2"
        },
        {
          "customerId": "11111111-0000-474c-b092-b0dd880c07e1",
          "active": true,
          "firstName": "John1",
          "lastName": "Doe1",
          "gender": "male",
          "email": "user-1@oloy.com",
          "phone": "+48456456000",
          "birthDate": "1990-09-11T02:00:00+0200",
          "lastLevelRecalculation": "2019-03-15T13:00:05+0100",
          "createdAt": "2016-08-08T10:53:14+0200",
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
          "updatedAt": "2019-03-15T12:53:18+0100",
          "campaignPurchases": [],
          "transactionsCount": 0,
          "transactionsAmount": 0,
          "transactionsAmountWithoutDeliveryCosts": 0,
          "amountExcludedForLevel": 0,
          "averageTransactionAmount": 0,
          "labels": [
            {
              "key": "test",
              "value": "test"
            }
          ],
          "level": {
            "levelId": {
              "id": "e82c96cf-32a3-43bd-9034-4df343e50000"
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
          "currency": "eur",
          "levelPercent": "0.00%"
        }
      ]
    }



Import customers
----------------

To import customers you need to call the ``/api/admin/customer/import`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/customer/import

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type | Description                                        |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| file[file]                                     | query          | XML file                                           |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/customer/import \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "file[file]=C:\\fakepath\\customers.xml"

.. note::

    When using endpoints starting with ``/api/admin`` you need to authorize using admin account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

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

To create a new customer you need to call the ``/api/admin/customer/register`` endpoint with the ``POST`` method.

.. note::

    This endpoint allows to set more customer parameters than ``/api/customer/self_register`` and is used when creating
    a new customer in the admin cockpit or pos cockpit. Self register endpoint is used in the client cockpit for registration
    and has some limitations.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/customer/register

+------------------------------------+----------------+---------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type | Description                                                                                 |
+====================================+================+=============================================================================================+
| Authorization                      | header         | Token received during authentication                                                        |
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

    curl http://localhost:8181/api/admin/customer/register \
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
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customerId": "e0eb0355-8aaa-4fb1-8159-f58e81b7a25c",
      "email": "john@example.com"
    }
