Customer Campaign API
=========

These endpoints will allow you to see and use Reward Campaigns for a customer.



Get all campaigns bought by a customer
--------------------------------------

To retrieve a list of rewards bought by a specific customer use the ``api/admin/customer/{customer}/campaign/bought`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/customer/<customer>/campaign/bought

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <customer>           | request        | Customer UUID                                          |
+----------------------+----------------+--------------------------------------------------------+
| includeDetails       | query          | *(optional)* Include details about bought campaign     |
|                      |                | For example ``1``                                      |
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

    curl http://localhost:8181/api/admin/customer/00000000-0000-474c-b092-b0dd880c07e1/campaign/bought \
        -X "GET" \
        -H "Accept:application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customer = 00000000-0000-474c-b092-b0dd880c07e1* id is an example value. Your value may be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [],
      "total": 0
    }

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [
        {
          "purchaseAt": "2018-01-30T18:23:24+0100",
          "costInPoints": 20,
          "campaignId": {
            "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93"
          },
          "used": false,
          "coupon": {
            "code": "123"
          }
        }
      ],
      "total": 1
    }

Example
^^^^^^^

.. code-block:: bash
    curl http://localhost:8181/api/admin/customer/00000000-0000-474c-b092-b0dd880c07e1/campaign/bought \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "includeDetails=1" \
        -d "page=1" \
        -d "perPage=1" \
        -d "sort=used" \
        -d "direction=DESC"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customer = 00000000-0000-474c-b092-b0dd880c07e1* id is an example value. Your value may be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [
        {
          "purchaseAt": "2018-01-30T18:23:24+0100",
          "costInPoints": 20,
          "campaignId": {
            "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93"
          },
          "campaign": {
            "levels": [
              "000096cf-32a3-43bd-9034-4df343e5fd93",
              "e82c96cf-32a3-43bd-9034-4df343e5fd94",
              "000096cf-32a3-43bd-9034-4df343e5fd94",
              "0f0d346e-9fd0-492a-84aa-2a2b61419c97"
            ],
            "segments": [],
            "coupons": [
              "123"
            ],
            "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93",
            "reward": "discount_code",
            "name": "tests",
            "active": true,
            "costInPoints": 20,
            "singleCoupon": false,
            "unlimited": false,
            "limit": 10,
            "limitPerUser": 2,
            "campaignActivity": {
              "allTimeActive": true
            },
            "campaignVisibility": {
              "allTimeVisible": true
            },
            "segmentNames": [],
            "levelNames": {
              "000096cf-32a3-43bd-9034-4df343e5fd93": "level0",
              "e82c96cf-32a3-43bd-9034-4df343e5fd94": "level1",
              "000096cf-32a3-43bd-9034-4df343e5fd94": "level2",
              "0f0d346e-9fd0-492a-84aa-2a2b61419c97": "level3"
            },
            "usageLeft": 0,
            "visibleForCustomersCount": 6,
            "usersWhoUsedThisCampaignCount": 1
          },
          "used": false,
          "coupon": {
            "code": "123"
          }
        }
      ],
      "total": 1
    }



Get all campaigns available for a logged-in customer
----------------------------------------------------

To get all campaigns available for a logged-in customer, use the ``/api/customer/campaign/available`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/campaign/available

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| isPublic             | query          | *(optional)* Filter by whether the campaign is public  |
|                      |                | or hidden; omit for all campaigns.                     |
+----------------------+----------------+--------------------------------------------------------+
| isFeatured           | query          | *(optional)* Filter by featured tag                    |
+----------------------+----------------+--------------------------------------------------------+
| hasSegment           | query          | *(optional)* 1 to return only campaigns offered        |
|                      |                | exclusively to some segments, 0 for campaigns          |
|                      |                | offered only to all segments; omit for all campaigns   |
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
| categoryId[]         | query          | *(optional)* Array of category UUIDs to filter by.     |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/campaign/available \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. warning::

    Calling this endpoint is meaningful only when you call it with an authorization token that belongs to the logged-in customer.
    Otherwise, it will return a ``403 Forbidden`` error response.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [
        {
          "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd92",
          "reward": "discount_code",
          "name": "for test",
          "active": true,
          "costInPoints": 10,
          "singleCoupon": false,
          "unlimited": false,
          "limit": 10,
          "limitPerUser": 2,
          "campaignActivity": {
            "allTimeActive": true
          },
          "campaignVisibility": {
            "allTimeVisible": true
          },
          "segmentNames": [],
          "levelNames": {
            "000096cf-32a3-43bd-9034-4df343e5fd93": "level0",
            "e82c96cf-32a3-43bd-9034-4df343e5fd94": "level1",
            "000096cf-32a3-43bd-9034-4df343e5fd94": "level2",
            "0f0d346e-9fd0-492a-84aa-2a2b61419c97": "level3"
          },
          "usageLeft": 1,
          "usageLeftForCustomer": 1,
          "canBeBoughtByCustomer": true,
          "visibleForCustomersCount": 6,
          "usersWhoUsedThisCampaignCount": 0
        }
      ],
      "total": 1
    }



Get all campaigns bought by a logged-in customer
------------------------------------------------

To get all campaigns bought by a logged-in customer, use the ``/api/customer/campaign/bought`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/campaign/bought

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| includeDetails       | query          | *(optional)* Include details about bought campaign     |
|                      |                | For example ``1``                                      |
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

    curl http://localhost:8181/api/customer/campaign/bought \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. warning::

    Calling this endpoint is meaningful only when you call it with an authorization token that belongs to the logged-in customer.
    Otherwise, it will return a ``403 Forbidden`` error response.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [
        {
          "purchaseAt": "2018-01-30T18:23:24+0100",
          "costInPoints": 20,
          "campaignId": {
            "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93"
          },
          "used": false,
          "coupon": {
            "code": "123"
          }
        }
      ],
      "total": 1
    }

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/campaign/bought \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "includeDetails=1"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. warning::

    Calling this endpoint is meaningful only when you call it with an authorization token that belongs to the logged-in customer.
    Otherwise, it will return a ``403 Forbidden`` error response.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [
        {
          "purchaseAt": "2018-01-30T18:23:24+0100",
          "costInPoints": 20,
          "campaignId": {
            "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93"
          },
          "campaign": {
            "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93",
            "reward": "discount_code",
            "name": "tests",
            "active": true,
            "costInPoints": 20,
            "singleCoupon": false,
            "unlimited": false,
            "limit": 10,
            "limitPerUser": 2,
            "campaignActivity": {
              "allTimeActive": true
            },
            "campaignVisibility": {
              "allTimeVisible": true
            },
            "segmentNames": [],
            "levelNames": {
              "000096cf-32a3-43bd-9034-4df343e5fd93": "level0",
              "e82c96cf-32a3-43bd-9034-4df343e5fd94": "level1",
              "000096cf-32a3-43bd-9034-4df343e5fd94": "level2",
              "0f0d346e-9fd0-492a-84aa-2a2b61419c97": "level3"
            },
            "usageLeft": 0,
            "visibleForCustomersCount": 6,
            "usersWhoUsedThisCampaignCount": 1
          },
          "used": false,
          "coupon": {
            "code": "123"
          }
        }
      ],
      "total": 1
    }



Mark multiple coupons as used/unused by a customer.
---------------------------------------------------

Mark customer coupons as used/unused using the ``/api/admin/campaign/coupons/mark_as_used`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/campaign/coupons/mark_as_used

+---------------------------+----------------+-------------------------------------------------------------+
| Parameter                 | Parameter type |  Description                                                |
+===========================+================+=============================================================+
| Authorization             | header         | Token received during authentication                        |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][campaignId]     | request        | Campaign UUID                                               |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][couponId]       | request        | Coupon UUID                                                 |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][code]           | request        | Coupon code                                                 |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][used]           | request        | Is coupon used, 1 if true, 0 if not used                    |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][transactionId]  | request        | *(optional)* Transaction ID for which coupon has been used  |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][customerId]     | request        | Customer UUID                                               |
+---------------------------+----------------+-------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/campaign/coupons/mark_as_used \
        -X "POST" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "coupons[0][campaignId]=f1eddc46-e985-43e8-bc2a-8007dca3df95" \
        -d "coupons[0][couponId]=83d6a65e-d237-4049-84aa-bb107cd6f9a4" \
        -d "coupons[0][code]=test1" \
        -d "coupons[0][used]=1" \
        -d "coupons[0][customerId]=00000000-0000-474c-b092-b0dd880c07e1" \
        -d "coupons[0][campaignId]=f1eddc46-e985-43e8-bc2a-8007dca3df95" \
        -d "coupons[0][couponId]=6a2456ec-49b3-4970-9ac4-75ca01eab0ee" \
        -d "coupons[0][code]=test2" \
        -d "coupons[0][used]=1" \
        -d "coupons[0][customerId]=00000000-0000-474c-b092-b0dd880c07e1"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaignId = f1eddc46-e985-43e8-bc2a-8007dca3df95* id is an example value. Your value may be different.

.. note::

    The *couponId = 6a2456ec-49b3-4970-9ac4-75ca01eab0ee* id is an example value. Your value may be different.

.. note::

    The *customerId = 00000000-0000-474c-b092-b0dd880c07e1* id is an example value. Your value may be different.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "coupons": [
        {
          "name": "test1",
          "used": true,
          "campaignId": "f1eddc46-e985-43e8-bc2a-8007dca3df95",
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1"
        },
        {
          "name": "test2",
          "used": true,
          "campaignId": "f1eddc46-e985-43e8-bc2a-8007dca3df95",
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1"
        }
      ]
    }



Mark a logged-in customer's coupons as used
-------------------------------------------

Mark coupons bought by a logged-in customer as used using the ``/api/customer/campaign/coupons/mark_as_used`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/campaign/coupons/mark_as_used

+---------------------------+----------------+-------------------------------------------------------------+
| Parameter                 | Parameter type |  Description                                                |
+===========================+================+=============================================================+
| Authorization             | header         | Token received during authentication                        |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][campaignId]     | request        | Campaign UUID                                               |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][couponId]       | request        | Coupon UUID                                                 |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][code]           | request        | Coupon code                                                 |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][used]           | request        | Is coupon used, 1 if true, 0 if not used                    |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][transactionId]  | request        | *(optional)* Transaction ID for which coupon has been used  |
+---------------------------+----------------+-------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/campaign/coupons/mark_as_used \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "coupons[0][campaignId]=00000000-0000-0000-0000-000000000001" \
        -d "coupons[0][couponId]=00000000-0000-0000-0000-000000000002" \
        -d "coupons[0][code]=WINTER" \
        -d "coupons[0][used]=1" \
        -d "coupons[0][transactionId]=00000000-0000-0000-0000-000000000003"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaignId = 00000000-0000-0000-0000-000000000001*, *couponId = 00000000-0000-0000-0000-000000000002*,
    *transactionId = 00000000-0000-0000-0000-000000000003* are example values. Your values can be different.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "coupons": [
        {
          "name": "123",
          "used": true,
          "campaignId": "00000000-0000-0000-0000-000000000001",
          "customerId": "00000000-0000-0000-0000-000000000004"
        }
      ]
    }

Example Error Response
^^^^^^^^^^^^^^^^^^^^^^

If there are no more coupons left, you will receive the following responses.

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "error": {
        "code": 400,
        "message": "Bad Request"
      }
    }



Buy a campaign by the logged-in customer
----------------------------------------

To buy a campaign bought by the logged-in customer, use ``/api/customer/campaign/{campaign}/buy`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/campaign/{campaign}/buy

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| campaign             | request        | Campaign UUID                                          |
+----------------------+----------------+--------------------------------------------------------+
| quantity             | query          | *(optional)* default 1 - number                        |
|                      |                | of coupons to buy (not valid for                       |
|                      |                | cashback and percentage_discount_code)                 |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/campaign/000096cf-32a3-43bd-9034-4df343e5fd92/buy
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. warning::

    Calling this endpoint is meaningful only when you call it with an authorization token that belongs to the logged-in customer.
    Otherwise, it will return a ``403 Forbidden`` error response.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "coupons": [{
        "code": "123",
        "id": "ceb169c7-4fe2-4b49-9f2a-5a18634d7236"
      }]
    }

Example Error Response
^^^^^^^^^^^^^^^^^^^^^^

If there are no more coupons left, you will receive the following responses.

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "error": "No coupons left"
    }

Example Error Response
^^^^^^^^^^^^^^^^^^^^^^

If you don't have enough points to buy a reward, you will receive following responses.

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "error": "Not enough points"
    }



Get all campaigns bought by a customer (seller)
-----------------------------------------------

To retrieve a list of rewards bought by a specific customer, use the ``api/seller/customer/{customer}/campaign/bought`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/customer/<customer>/campaign/bought

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <customer>           | request        | Customer UUID                                          |
+----------------------+----------------+--------------------------------------------------------+
| includeDetails       | query          | *(optional)* Include details about bought campaign     |
|                      |                | For example ``1``                                      |
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

    curl http://localhost:8181/api/seller/customer/00000000-0000-474c-b092-b0dd880c07e1/campaign/bought \
        -X "GET" \
        -H "Accept:application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customer = 00000000-0000-474c-b092-b0dd880c07e1* id is an example value. Your value may be different.
    Check the list of all customers if you are not sure which id should be used.

.. note::

    When using endpoints starting with ``/api/seller``, you need to authorize using seller account credentials.

.. note::

    As a seller, you will receive less information about campaigns than an administrator.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [],
      "total": 0
    }

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [
        {
          "purchaseAt": "2018-01-30T18:23:24+0100",
          "costInPoints": 20,
          "campaignId": {
            "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93"
          },
          "used": false,
          "coupon": {
            "code": "123"
          }
        }
      ],
      "total": 1
    }

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/customer/00000000-0000-474c-b092-b0dd880c07e1/campaign/bought \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "includeDetails=1" \
        -d "page=1" \
        -d "perPage=1" \
        -d "sort=used" \
        -d "direction=DESC"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *customer = 00000000-0000-474c-b092-b0dd880c07e1* id is an example value. Your value may be different.
    Check the list of all customers if you are not sure which id should be used.

.. note::

    When using endpoints starting with ``/api/seller``, you need to authorize using seller account credentials.

.. note::

    As a seller, you will receive less information about campaigns than an administrator.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [
        {
          "purchaseAt": "2018-01-30T18:23:24+0100",
          "costInPoints": 20,
          "campaignId": {
            "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93"
          },
          "campaign": {
            "levels": [
              "000096cf-32a3-43bd-9034-4df343e5fd93",
              "e82c96cf-32a3-43bd-9034-4df343e5fd94",
              "000096cf-32a3-43bd-9034-4df343e5fd94",
              "0f0d346e-9fd0-492a-84aa-2a2b61419c97"
            ],
            "segments": [],
            "coupons": [
              "123"
            ],
            "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93",
            "reward": "discount_code",
            "name": "tests",
            "active": true,
            "costInPoints": 20,
            "singleCoupon": false,
            "unlimited": false,
            "limit": 10,
            "limitPerUser": 2,
            "campaignActivity": {
              "allTimeActive": true
            },
            "campaignVisibility": {
              "allTimeVisible": true
            },
            "segmentNames": [],
            "levelNames": {
              "000096cf-32a3-43bd-9034-4df343e5fd93": "level0",
              "e82c96cf-32a3-43bd-9034-4df343e5fd94": "level1",
              "000096cf-32a3-43bd-9034-4df343e5fd94": "level2",
              "0f0d346e-9fd0-492a-84aa-2a2b61419c97": "level3"
            },
            "usageLeft": 0,
            "visibleForCustomersCount": 6,
            "usersWhoUsedThisCampaignCount": 1
          },
          "used": false,
          "coupon": {
            "code": "123"
          }
        }
      ],
      "total": 1
    }
