Customer API
============

These endpoints will allow you to easily manage customers.

.. note::

    Each role in the Open Loyalty has individual endpoints to manage customers.

Activate a customer
-------------------

To activate a customer you need to call the ``/api/admin/customer/{customer}/activate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/customer/{customer}/activate

+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                                                  |
+====================================+================+===============================================================================================+
| Authorization                      | header         |  Token received during authentication                                                         |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer                           | request        |  Customer's UUID                                                                              |
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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *customer = 1bbafb37-b51b-47c5-b3e4-e0a2d028e655* id is an example value. Your value can be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    ""

Deactivate a customer
---------------------

To deactivate a customer you need to call the ``/api/admin/customer/{customer}/deactivate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/customer/{customer}/deactivate

+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                                                  |
+====================================+================+===============================================================================================+
| Authorization                      | header         |  Token received during authentication                                                         |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer                           | request        |  Customer's UUID                                                                              |
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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *customer = 1bbafb37-b51b-47c5-b3e4-e0a2d028e655* id is an example value. Your value can be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    ""

Get customer status
-------------------

To get a customer status you need to call the ``/api/admin/customer/{customer}/status`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/customer/{customer}/status

+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                                                  |
+====================================+================+===============================================================================================+
| Authorization                      | header         |  Token received during authentication                                                         |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer                           | request        |  Customer's UUID                                                                              |
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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customers": [],
      "total": 0
    }

Activate a customer using activation token
------------------------------------------

To activate a customer using a token you need to call the ``/api/customer/activate/{token}`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/activate/{token}

+------------------------------------+----------------+----------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                   |
+====================================+================+================================================================+
| Authorization                      | header         |  Token received during authentication                          |
+------------------------------------+----------------+----------------------------------------------------------------+
| token                              | request        |  Customer's token                                              |
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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *token = abcde* is an example value. Your value can be different.
    The value can be checked in the database, table ``ol_user``, field ``action_token``.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    ""

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

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

Update a customer
---------------------

To update an existing customer you need to call the ``/api/customer/<customer>`` endpoint with the ``PUT`` method.

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

    PUT /api/customer/{customer}

+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                                                  |
+====================================+================+===============================================================================================+
| Authorization                      | header         |  Token received during authentication                                                         |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| <customer>                         | query          |  Customer ID                                                                                  |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[firstName]                | request        |  *(optional)* First name                                                                      |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[lastName]                 | request        |  *(optional)* Last name                                                                       |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[gender]                   | request        |  *(optional)* Gender. Possible values ``male``, ``female``                                    |
+------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
| customer[email]                    | request        |  *(optional)* *(unique)* E-mail address                                                       |
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
| customer[agreement1]               | request        |  *(optional)* First agreement. Set 1 if true, otherwise 0                                     |
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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

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
    Use GET /api/customer/{customer} after the update to always get the up-to-date values instead.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

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
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

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
