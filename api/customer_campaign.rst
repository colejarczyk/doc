Customer Campaign API
=========

These endpoints will allow you to see and use Reward Campaigns for a customer.

Get all campaigns bought by a customer
--------------------------------------

To retrieve list of bought rewards by a specific customer use ``api/admin/customer/{customer}/campaign/bought`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/customer/{customer}/campaign/bought

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| customer             | request        | Customer UUID                                          |
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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *customer = 00000000-0000-474c-b092-b0dd880c07e1* id is an example value. Your value can be different.
    Check in the list of all customers if you are not sure which id should be used.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *customer = 00000000-0000-474c-b092-b0dd880c07e1* id is an example value. Your value can be different.
    Check in the list of all customers if you are not sure which id should be used.

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

Get all campaigns available for logged in customer
--------------------------------------------------

To get all campaign available for logged in customer use ``/api/customer/campaign/available`` endpoint with the ``GET`` method.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. warning::

    Calling this endpoint is meaningful only when you call it with authorization token that belongs to the logged in customer.
    Otherwise it will return ``403 Forbidden`` error response.

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

Get all campaigns bought by logged in customer
----------------------------------------------

To get all campaign bought by logged in customer use ``/api/customer/campaign/bought`` endpoint with the ``POST`` method.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. warning::

    Calling this endpoint is meaningful only when you call it with authorization token that belongs to the logged in customer.
    Otherwise it will return ``403 Forbidden`` error response.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. warning::

    Calling this endpoint is meaningful only when you call it with authorization token that belongs to the logged in customer.
    Otherwise it will return ``403 Forbidden`` error response.

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

Mark logged in customer coupons as used
---------------------------------------

Mark bought by logged in customer coupons as used using ``/api/customer/campaign/coupons/mark_as_used`` endpoint with the ``POST`` method.

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
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "coupons[0][campaignId]=00000000-0000-0000-0000-000000000001" \
        -d "coupons[0][couponId]=00000000-0000-0000-0000-000000000002" \
        -d "coupons[0][code]=WINTER" \
        -d "coupons[0][used]=1" \
        -d "coupons[0][transactionId]=00000000-0000-0000-0000-000000000003"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *campaignId = 00000000-0000-0000-0000-000000000001* id is an example value. Your value can be different.

.. note::

    The *couponId = 00000000-0000-0000-0000-000000000002* id is an example value. Your value can be different.

.. note::

    The *transactionId = 00000000-0000-0000-0000-000000000003* id is an example value. Your value can be different.

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

If there is no more coupons left, you'll receive follow responses.

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "error": {
        "code": 400,
        "message": "Bad Request"
      }
    }

Buy campaign by logged in customer
----------------------------------

Buy campaign bought by logged in customer use ``/api/customer/campaign/{campaign}/buy`` endpoint with the ``POST`` method.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. warning::

    Calling this endpoint is meaningful only when you call it with authorization token that belongs to the logged in customer.
    Otherwise it will return ``403 Forbidden`` error response.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "coupons": [{
        "code": "123"
      }]
    }

Example Error Response
^^^^^^^^^^^^^^^^^^^^^^

If there is no more coupons left, you'll receive follow responses.

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "error": "No coupons left"
    }

Example Error Response
^^^^^^^^^^^^^^^^^^^^^^

If you don't have enough points to buy a reward, you'll receive follow responses.

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "error": "Not enough points"
    }

Get all campaigns bought by a customer (seller)
-----------------------------------------------

To retrieve list of bought rewards by a specific customer use ``api/seller/customer/{customer}/campaign/bought`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/customer/{customer}/campaign/bought

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| customer             | request        | Customer UUID                                          |
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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *customer = 00000000-0000-474c-b092-b0dd880c07e1* id is an example value. Your value can be different.
    Check in the list of all customers if you are not sure which id should be used.

.. note::

    When you will use endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    As a seller you will receive less amount of information about campaign than an administrator.

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
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *customer = 00000000-0000-474c-b092-b0dd880c07e1* id is an example value. Your value can be different.
    Check in the list of all customers if you are not sure which id should be used.

.. note::

    When you will use endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    As a seller you will receive less amount of information about campaign than an administrator.

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
