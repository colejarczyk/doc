Reward Campaigns API
====================

These endpoints will allow you to easily manage Reward Campaigns.

.. note::

    Each role in Open Loyalty has individual endpoints to manage reward campaigns.



Reedem cashback (admin)
-----------------------

To reedem cashback, you need to call the ``/api/admin/campaign/cashback/redeem`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/campaign/cashback/redeem

+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| Parameter                                         | Parameter type |  Description                                                                 |
+===================================================+================+==============================================================================+
| Authorization                                     | header         | Token received during authentication                                         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| customerId                                        | request        |  Customer ID                                                                 |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| pointsAmount                                      | request        |  Number of points to spend                                                      |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| cashbackId                                        | request        |  *(optional)* Cashback id                                                    |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+



Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/campaign/cashback/redeem \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customerId=6102cef9-d263-46de-974d-ad2e89f6e81d" \
		-d "pointsAmount=5" 

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "customerId": "6102cef9-d263-46de-974d-ad2e89f6e81d",
        "pointsAmount": 5,
        "pointValue": 10,
        "rewardAmount": 100
    }



Reedem cashback (customer)
--------------------------

To reedem cashback, you need to call the ``/api/customer/campaign/cashback/redeem`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/campaign/cashback/redeem

+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| Parameter                                         | Parameter type |  Description                                                                 |
+===================================================+================+==============================================================================+
| Authorization                                     | header         | Token received during authentication                                         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| pointsAmount                                      | request        |  Number of points to spend                                                      |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| cashbackId                                        | request        |  Cashback id                                                                 |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+



Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/customer/campaign/cashback/redeem \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "cashbackId=972012b8-633d-41e8-be5a-5125c1a5be63" \
		-d "pointsAmount=5" 

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "customerId": "6102cef9-d263-46de-974d-ad2e89f6e81d",
        "pointsAmount": 5,
        "pointValue": 10,
        "rewardAmount": 50,
		"cashbackId" : "972012b8-633d-41e8-be5a-5125c1a5be63"
    }



Simulate cashback
-----------------

To simulate cashback, you need to call the ``/api/admin/campaign/cashback/simulate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/campaign/cashback/simulate
	
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| Parameter                                         | Parameter type |  Description                                                                 |
+===================================================+================+==============================================================================+
| Authorization                                     | header         | Token received during authentication                                         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| customerId                                        | request        |  Customer ID                                                                 |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| pointsAmount                                      | request        |  Number of points to spend                                                      |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/campaign/cashback/simulate \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "customerId=5bfded09-0931-4eac-baad-0d663cfd8976" \
		-d "pointsAmount=10" 

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "customerId": "5bfded09-0931-4eac-baad-0d663cfd8976",
        "pointsAmount": 10,
        "pointValue": "3.00",
        "rewardAmount": 30
    }



Cashback provider callback
--------------------------

To run a cashback provider callback, you need to call the ``/api/campaign/cashback/callback/{provider}`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/campaign/cashback/callback/{provider}
	
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| Parameter                                         | Parameter type |  Description                                                                 |
+===================================================+================+==============================================================================+
| Authorization                                     | header         | Token received during authentication                                         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| <provider>                                        | request        |  Provider, possible value: paytm                                             |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/campaign/cashback/callback/paytm \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
		-H "Content: {"type":null,"requestGuid":null,"orderId":"f0b9914e-cd54-4a85-bc3f-d36e0c37edaa_1c50ef53-ab5b-4d24-9d03-f93c7ec042fe","status":null,"statusCode":"ACCEPTED","statusMessage":"ACCEPTED","response":null,"metadata":null}" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." 

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The data in the Content is an example value and depends on the [Cashback][PayTM] Requested PayTM cashback message after redeeming cashback.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "couponId": "1c50ef53-ab5b-4d24-9d03-f93c7ec042fe",
        "id": "f0b9914e-cd54-4a85-bc3f-d36e0c37edaa_1c50ef53-ab5b-4d24-9d03-f93c7ec042fe",
        "customerId": "f0b9914e-cd54-4a85-bc3f-d36e0c37edaa",
        "code": "ACCEPTED",
        "message": "ACCEPTED",
        "provider": "paytm",
        "failed": false
    }


Create a new campaign
---------------------

To create a new campaign, you need to call the ``/api/campaign`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/campaign

+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| Parameter                                         | Parameter type |  Description                                                                 |
+===================================================+================+==============================================================================+
| Authorization                                     | header         | Token received during authentication                                         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[reward]                                  | request        |  Campaign type. Possible types:                                              |
|                                                   |                |  discount_code, free_delivery_code, gift_code, event_code, value_code.       |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][name]                  | request        |  Campaign name in given locale.                                              |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][shortDescription]      | request        |  *(optional)* A short description in given locale.                           |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][conditionsDescription] | request        |  *(optional)* A description of required conditions to apply in given locale. |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][usageInstruction]      | request        |  *(optional)* A little information about how to use coupons in given locale. |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][brandDescription]      | request        |  *(optional)* A little information about brand in given locale.              |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[active]                                  | request        |  Set 1 if active, otherwise 0                                                |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[categories]                              | request        | *(optional)* Array of category IDs.                                          |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[pushNotificationText]                    | request        | Push message sent to a customer on this campaign becoming available to them  |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[pointValue]                              | request        | Each point will be exchanged for provided value (in current currency) for    |
|                                                   |                | cashback                                                                     |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[cashbackProvider]                        | request        | Cashback campaigns can automatically send funds using the listed APIs.       |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[costInPoints]                            | request        |  How many points it costs                                                    |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[target]                                  | request        |  Set ``level`` to choose target from defined levels.                         |
|                                                   |                |  Set ``segment`` to choose target from defined segments                      |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[levels]                                  | request        |  Array of level IDs. *(required only if ``target=level``)*                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[segments]                                | request        |  Array of segment IDs. *(required only if ``target=segment``)*               |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[labels]                                  | request        | *(optional)* Informational labels in format "key:value;key1:value1"          |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[unlimited]                               | request        |  Set 1 if unlimited, otherwise 0                                             |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[singleCoupon]                            | request        |  Set 1 if single coupon, otherwise 0                                         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[limit]                                   | request        |  Global campaign usage limit. *(required only if ``unlimited=0``)*           |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[limitPerUser]                            | request        |  Customer campaign usage limit. *(required only if ``unlimited=0``)*         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[coupons]                                 | request        |  Array of coupon codes.                                                      |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignVisibility][allTimeVisible]      | request        |  Set 1 if always visible, otherwise 0                                        |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignVisibility][visibleFrom]         | request        |  Campaign visible from YYYY-MM-DD HH:mm, for example ``2017-10-05 10:59``.   |
|                                                   |                |  *(required only if ``allTimeVisible=0``)*                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignVisibility][visibleTo]           | request        |  Campaign visible to YYYY-MM-DD HH:mm, for example ``2017-10-05 10:59``.     |
|                                                   |                |  *(required only if ``allTimeVisible=0``)*                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignActivity][allTimeActive]         | request        |  Set 1 if always active, otherwise 0                                         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignActivity][activeFrom]            | request        |  Campaign active from YYYY-MM-DD HH:mm, for example ``2017-10-05 10:59``.    |
|                                                   |                |  *(required only if ``allTimeActive=0``)*                                    |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignActivity][activeTo]              | request        |  Campaign visible to YYYY-MM-DD HH:mm, for example ``2017-10-05 10:59``.     |
|                                                   |                |  *(required only if ``allTimeVisible=0``)*                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[daysInactive]                            | request        |  Number of days, during which coupon will not be active after purchase       |
|                                                   |                |  0 means "active immediately"                                                |
|                                                   |                |  Required for all rewards besides cashback                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[daysValid]                               | request        |  Number of days, during which coupon will be valid, after activation         |
|                                                   |                |  0 means "valid forever"                                                     |
|                                                   |                |  Required for all rewards besides cashback                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/campaign \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "campaign[translations][en][reward]=discount_code" \
        -d "campaign[translations][en][name]=Discount+Code+Campaign" \
        -d "campaign[translations][en][shortDescription]=A+short+description+of+discount+code+campaign" \
        -d "campaign[translations][en][conditionsDescription]=Discount+code+for+registration" \
        -d "campaign[translations][en][usageInstruction]=Use+discount+code+as+you+like" \
        -d "campaign[translations][en][brandDescription]=Some+brand+description" \
        -d "campaign[active]=1" \
        -d "campaign[costInPoints]=100" \
        -d "campaign[target]=level" \
        -d "campaign[labels]=type:promotion;type:cashback" \
        -d "campaign[levels][0]=e82c96cf-32a3-43bd-9034-4df343e5fd94" \
        -d "campaign[levels][1]=000096cf-32a3-43bd-9034-4df343e5fd94" \
        -d "campaign[unlimited]=0" \
        -d "campaign[singleCoupon]=0" \
        -d "campaign[limit]=10" \
        -d "campaign[limitPerUser]=1" \
        -d "campaign[daysValid]=0" \
        -d "campaign[daysInactive]=0" \
        -d "campaign[coupons][0]=testCoupon" \
        -d "campaign[coupons][1]=DiscountCoupon" \
        -d "campaign[campaignVisibility][allTimeVisible]=0" \
        -d "campaign[campaignVisibility][visibleFrom]=2017-10-05+10:59" \
        -d "campaign[campaignVisibility][visibleTo]=2018-10-05+10:59" \
        -d "campaign[campaignActivity][allTimeActive]=0" \
        -d "campaign[campaignActivity][activeFrom]=2017-09-05+10:59" \
        -d "campaign[campaignActivity][activeTo]=2017-12-05+10:59"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *e82c96cf-32a3-43bd-9034-4df343e5fd94* or *000096cf-32a3-43bd-9034-4df343e5fd94* id are example values.
    Your value may be different. Check the list of all levels if you are not sure which id should be used.

.. note::

    The *testCoupon* or *DiscountCoupon* are example values. You can name code coupons as you like.

.. attention::

    If you would like to add photos (one or many) to the campaign, you need to call the ``/api/campaign/<campaign>/photo`` endpoint with the ``POST`` method.
    You can find more details in the *Add a photo to the campaign* section.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaignId": "3062c881-93f3-496b-9669-4238c0a62be8"
    }

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/campaign \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "form": {
        "children": {
          "reward": {},
          "translations": {
              "children": {
                  "en": {
                      "children": {
                          "name": {
                              "errors": [
                                  "This value should not be blank."
                              ]
                          },
                          "shortDescription": {},
                          "conditionsDescription": {},
                          "usageInstruction": {},
                          "brandDescription": {}
                      }
                  },
                  "pl": {
                      "children": {
                          "name": {},
                          "shortDescription": {},
                          "conditionsDescription": {},
                          "usageInstruction": {},
                          "brandDescription": {}
                      }
                  }
              }
          },
          "active": {},
          "costInPoints": {},
          "target": {},
          "levels": {},
          "segments": {},
          "unlimited": {},
          "singleCoupon": {},
          "limit": {},
          "limitPerUser": {},
          "coupons": {},
          "daysInactive": {},
          "daysValid": {},
          "campaignVisibility": {
            "children": {
              "allTimeVisible": {},
              "visibleFrom": {},
              "visibleTo": {}
            }
          },
          "campaignActivity": {
            "children": {
              "allTimeActive": {},
              "activeFrom": {},
              "activeTo": {}
            }
          }
        }
      },
      "errors": []
    }



Get a collection of campaigns
-----------------------------

To retrieve a paginated list of campaigns, you need to call the ``/api/campaign`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaign

+-------------------------------------+----------------+----------------------------------------------------+
| Parameter                           | Parameter type | Description                                        |
+=====================================+================+====================================================+
| Authorization                       | header         | Token received during authentication               |
+-------------------------------------+----------------+----------------------------------------------------+
| labels                              | request        | *(optional)* Array of labels with key and/or value |
|                                     |                | ie. labels[0][key]=key&labels[0][value]=value      |
+-------------------------------------+----------------+----------------------------------------------------+
| page                                | query          | *(optional)* Start from page, by default 1         |
+-------------------------------------+----------------+----------------------------------------------------+
| perPage                             | query          | *(optional)* Number of items to display per page,  |
|                                     |                | by default = 10                                    |
+-------------------------------------+----------------+----------------------------------------------------+
| sort                                | query          | *(optional)* Sort by column name                   |
+-------------------------------------+----------------+----------------------------------------------------+
| direction                           | query          | *(optional)* Direction of sorting [ASC, DESC],     |
|                                     |                | by default = ASC                                   |
+-------------------------------------+----------------+----------------------------------------------------+
| format                              | query          | *(optional)* Format of descriptions [html].        |
|                                     |                | Default is RAW.                                    |
+-------------------------------------+----------------+----------------------------------------------------+
| categoryId[]                        | query          | *(optional)* Array of category Ids                 |
+-------------------------------------+----------------+----------------------------------------------------+

To see the first page of all campaigns, use the method below:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/campaign \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.


.. note::

    In the example below, you can get all Reward Campaigns that have a label with a key and value. You can
    filter by a label's key or value if you want and specify as many condition as you want.

.. note::

    Translatable fields (name, short description, etc.) are returned in given locale.

.. code-block:: bash

    curl http://localhost:8181/api/campaign?labels[0][key]=key&labels[0][value]=value \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [
        {
          "levels": [
            "000096cf-32a3-43bd-9034-4df343e5fd94"
          ],
          "segments": [
            "00000000-0000-0000-0000-000000000002"
          ],
          "coupons": [
            "123"
          ],
          "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "reward": "discount_code",
          "name": "tests",
          "active": true,
          "costInPoints": 10,
          "singleCoupon": false,
          "unlimited": false,
          "limit": 10,
          "limitPerUser": 2,
          "daysValid": 0,
          "daysInactive": 0,
          "campaignActivity": {
            "allTimeActive": false,
            "activeFrom": "2016-01-01T00:00:00+0100",
            "activeTo": "2018-01-01T00:00:00+0100"
          },
          "campaignVisibility": {
            "allTimeVisible": false,
            "visibleFrom": "2016-01-01T00:00:00+0100",
            "visibleTo": "2018-01-01T00:00:00+0100"
          },
          "segmentNames": {
            "00000000-0000-0000-0000-000000000002": "anniversary"
          },
          "levelNames": {
            "000096cf-32a3-43bd-9034-4df343e5fd94": "level2"
          },
          "labels": [
            {
              "key": "type",
              "value": "promotion"
            }
          ],
          "usageLeft": 1,
          "visibleForCustomersCount": 0,
          "usersWhoUsedThisCampaignCount": 0,
          "hasPhoto": false,
          "translations": [
              {
                  "name": "Promotion campaign",
                  "shortDescription": "_Campaign_ short description",
                  "conditionsDescription": "Some conditions description",
                  "usageInstruction": "Usage of coupon instruction",
                  "brandDescription": "Brand description",
                  "id": 32,
                  "locale": "en"
              },
              {
                  "name": "Promocyjna kampania",
                  "shortDescription": "Opis promocyjnej kampanii",
                  "id": 33,
                  "locale": "pl"
              }
          ]
        },
        {
          "levels": [
            "000096cf-32a3-43bd-9034-4df343e5fd94"
          ],
          "segments": [
            "00000000-0000-0000-0000-000000000002"
          ],
          "coupons": [
            "123"
          ],
          "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd92",
          "reward": "discount_code",
          "name": "for test",
          "active": false,
          "costInPoints": 10,
          "singleCoupon": false,
          "unlimited": false,
          "limit": 10,
          "limitPerUser": 2,
          "daysValid": 0,
          "daysInactive": 0,
          "campaignActivity": {
            "allTimeActive": false,
            "activeFrom": "2016-01-01T00:00:00+0100",
            "activeTo": "2018-01-01T00:00:00+0100"
          },
          "campaignVisibility": {
            "allTimeVisible": false,
            "visibleFrom": "2016-01-01T00:00:00+0100",
            "visibleTo": "2018-01-01T00:00:00+0100"
          },
          "segmentNames": {
            "00000000-0000-0000-0000-000000000002": "anniversary"
          },
          "levelNames": {
            "000096cf-32a3-43bd-9034-4df343e5fd94": "level2"
          },
          "will_be_active_from": "2016-01-01T00:00:00+0100",
          "will_be_active_to": "2018-01-01T00:00:00+0100",
          "usageLeft": 1,
          "visibleForCustomersCount": 0,
          "usersWhoUsedThisCampaignCount": 0,
          "hasPhoto": false,
          "translations": [
              {
                  "name": "tests",
                  "shortDescription": "_shortdescription_",
                  "conditionsDescription": "_conditionsdescription_",
                  "usageInstruction": "_usageinstruction_",
                  "brandDescription": "_branddescription_",
                  "id": 32,
                  "locale": "en"
              },
              {
                  "name": "tests_pl",
                  "shortDescription": "short desc test pl",
                  "id": 33,
                  "locale": "pl"
              }
          ]
        },
        {
          "levels": [
            "e82c96cf-32a3-43bd-9034-4df343e5fd94",
            "000096cf-32a3-43bd-9034-4df343e5fd94"
          ],
          "segments": [],
          "coupons": [
            "testCoupon",
            "DiscountCoupon"
          ],
          "campaignId": "3062c881-93f3-496b-9669-4238c0a62be8",
          "reward": "discount_code",
          "name": "Discount Code Campaign",
          "shortDescription": "A short description of discount code campaign",
          "conditionsDescription": "Discount code for registration",
          "active": true,
          "costInPoints": 100,
          "singleCoupon": false,
          "unlimited": false,
          "limit": 10,
          "limitPerUser": 1,
          "daysValid": 0,
          "daysInactive": 0,
          "campaignActivity": {
            "allTimeActive": false,
            "activeFrom": "2017-09-05T10:59:00+0200",
            "activeTo": "2017-12-05T10:59:00+0100"
          },
          "campaignVisibility": {
            "allTimeVisible": false,
            "visibleFrom": "2017-10-05T10:59:00+0200",
            "visibleTo": "2018-10-05T10:59:00+0200"
          },
          "usageInstruction": "Use discount code as you like",
          "segmentNames": [],
          "levelNames": {
            "e82c96cf-32a3-43bd-9034-4df343e5fd94": "level1",
            "000096cf-32a3-43bd-9034-4df343e5fd94": "level2"
          },
          "usageLeft": 2,
          "visibleForCustomersCount": 0,
          "usersWhoUsedThisCampaignCount": 0,
          "hasPhoto": false,
          "translations": [
              {
                  "name": "tests",
                  "shortDescription": "_shortdescription_",
                  "conditionsDescription": "_conditionsdescription_",
                  "usageInstruction": "_usageinstruction_",
                  "brandDescription": "_branddescription_",
                  "id": 32,
                  "locale": "en"
              },
              {
                  "name": "tests_pl",
                  "shortDescription": "short desc test pl",
                  "id": 33,
                  "locale": "pl"
              }
          ]
        }
      ],
      "total": 3
    }



Get a collection of active campaigns
------------------------------------

To retrieve a paginated list of active campaigns, you need to call the ``/api/campaign/active`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaign/active	
	
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| Parameter                                         | Parameter type |  Description                                                                 |
+===================================================+================+==============================================================================+
| Authorization                                     | header         | Token received during authentication                                         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| format                                            | query          |  If set to html, the descriptions will be in HTML format                     |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+

Example
^^^^^^^

To see the first page of all campaigns, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/active \
        -X "GET" \
	    -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json
    
   	{
    "campaigns": [
    {
      "id": "000096cf-6361-4d70-e169-676e00000001",
      "name": "Test configured campaign"
    },
    {
      "id": "000096cf-6361-4d70-e169-676e00000003",
      "name": "Test reward campaign"
    },
    {
      "id": "000096cf-6361-4d70-e169-676e11111111",
      "name": "cashback"
    },
    {
      "id": "000096cf-6361-4d70-e169-676e22222222",
      "name": "Percentage discount code"
    },
    {
      "id": "000096cf-6361-4d70-e169-676e55555555",
      "name": "Percentage discount code"
    },
    {
      "id": "000096cf-6361-4d70-e169-676e66666666",
      "name": "Percentage discount code"
    },
    {
      "id": "000096cf-6361-4d70-e169-676e44444444",
      "name": "GEO custom campaign"
    },
    {
      "id": "fce61034-a48e-39f5-af3b-c8aa294601f9"
    },
    {
      "id": "a58388e4-bf99-34d7-9d4a-848efd5b6687",
      "name": "2"
    },
    {
      "id": "8500766f-1aa3-3117-9423-70c6851294c7",
      "name": "4"
    },
    {
      "id": "9ea077ae-6d9f-3547-b43f-cb89471ce4d3",
      "name": "6"
    },
    {
      "id": "0c1f68bc-529f-39b5-99df-b5740048a84a",
      "name": "8"
    },
    {
      "id": "1942beff-5375-3455-ad1d-f608c18b0707",
      "name": "10"
    },
    {
      "id": "2bca67fd-2ece-47ea-a556-2ec0b3faeba3",
      "name": "tertrt"
    },
    {
      "id": "5413dff3-47ba-4342-a669-cc9bb54ea1fa",
      "name": "dddddd"
    },
    {
      "id": "4cd1415d-6c20-4642-a2eb-cd985c1f88aa",
      "name": "testowe"
    },
    {
      "id": "40d4b8c5-3be4-4f76-8804-d1dc3c9a9732",
      "name": "test"
    },
    {
      "id": "110d39ce-47ab-4c2c-b0f8-a71c95e0520a",
      "name": "cashback"
    }
    ]}



Get a collection of bought campaigns
------------------------------------

To retrieve a paginated list of bought campaigns, you need to call the ``/api/campaign/bought`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaign/bought
	
+-------------------------------------+----------------+----------------------------------------------------+
| Parameter                           | Parameter type | Description                                        |
+=====================================+================+====================================================+
| Authorization                       | header         | Token received during authentication               |
+-------------------------------------+----------------+----------------------------------------------------+
| used                                | request        | *(optional)* Possible values : true/false          |
+-------------------------------------+----------------+----------------------------------------------------+
| page                                | query          | *(optional)* Start from page, by default 1         |
+-------------------------------------+----------------+----------------------------------------------------+
| perPage                             | query          | *(optional)* Number of items to display per page,  |
|                                     |                | by default = 10                                    |
+-------------------------------------+----------------+----------------------------------------------------+
| sort                                | query          | *(optional)* Sort by column name                   |
+-------------------------------------+----------------+----------------------------------------------------+
| direction                           | query          | *(optional)* Direction of sorting [ASC, DESC],     |
|                                     |                | by default = ASC                                   |
+-------------------------------------+----------------+----------------------------------------------------+
| purchasedAtFrom                     | query          | *(optional)* Purchase date from filter             |
+-------------------------------------+----------------+----------------------------------------------------+
| purchasedAtTo                       | query          | *(optional)* Purchase date to filter               |
+-------------------------------------+----------------+----------------------------------------------------+
| usageDateFrom                       | query          | *(optional)* Usage date from filter                |
+-------------------------------------+----------------+----------------------------------------------------+
| usageDateTo                         | query          | *(optional)* Usage date to filter                  |
+-------------------------------------+----------------+----------------------------------------------------+
| activeSinceFrom                     | query          | *(optional)* Active since date from filter         |
+-------------------------------------+----------------+----------------------------------------------------+
| activeToFrom                        | query          | *(optional)* Active since date to filter           |
+-------------------------------------+----------------+----------------------------------------------------+
| activeToTo                          | query          | *(optional)* Active to date to filter              |
+-------------------------------------+----------------+----------------------------------------------------+
| deliveryStatus                      | query          | *(optional)* Delivery status filter                |
|                                     |                |  Possible values: ordered, canceled, shipped,      |   
|                                     |                |  delivered                                         |
+-------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

To see the first page of all bought campaigns, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/bought \
        -X "GET" \
	-H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
    "boughtCampaigns": [
    {
      "canBeUsed": true,
      "rewardCampaignId": "000096cf-6361-4d70-e169-676e22222222",
      "campaignId": "000096cf-6361-4d70-e169-676e22222222",
      "customerId": "7ae0712b-f029-4839-9c53-278c37c6fd35",
      "purchasedAt": "2019-03-14T10:29:05+0100",
      "coupon": {
        "code": "10",
        "id": "d481c4f2-fa88-476a-9e12-a39f728d94d8"
      },
      "campaignType": "percentage_discount_code",
      "campaignName": "Percentage discount code",
      "customerEmail": "maxnowacki690711@test.pl",
      "customerName": "Max",
      "customerLastname": "Nowacki",
      "campaignShippingAddress": {},
      "costInPoints": 0,
      "currentPointsAmount": 100,
      "used": false,
      "status": "active",
      "transactionId": {
        "transactionId": "33fbedb5-ff71-4a18-9711-4352d3b9e317"
      },
      "returnedAmount": 0,
      "deliveryStatus": {
        "status": ""
      }
    },
	{
      "canBeUsed": true,
      "rewardCampaignId": "000096cf-6361-4d70-e169-676e11111111",
      "campaignId": "000096cf-6361-4d70-e169-676e11111111",
      "customerId": "6102cef9-d263-46de-974d-ad2e89f6e81d",
      "purchasedAt": "2019-03-14T13:45:21+0100",
      "coupon": {
        "code": "",
        "id": "6797ed0a-65eb-4a75-b1a2-500b18077dc3"
      },
      "campaignType": "cashback",
      "campaignName": "cashback",
      "customerEmail": "maxnowacki209528@test.pl",
      "customerName": "Max",
      "customerLastname": "Nowacki",
      "campaignShippingAddress": {},
      "costInPoints": 0,
      "currentPointsAmount": 100,
      "used": false,
      "status": "active",
      "returnedAmount": 0,
      "deliveryStatus": {
        "status": ""
      }
    },
    {
      "canBeUsed": true,
      "rewardCampaignId": "000096cf-6361-4d70-e169-676e22222222",
      "campaignId": "000096cf-6361-4d70-e169-676e22222222",
      "customerId": "79b5c229-5f9a-4c4b-9acc-7620fb95b38a",
      "purchasedAt": "2019-03-14T13:48:11+0100",
      "coupon": {
        "code": "40",
        "id": "1a4d7e14-fffc-4049-be41-60e824b5102e"
      },
      "campaignType": "percentage_discount_code",
      "campaignName": "Percentage discount code",
      "customerEmail": "test@test.pl",
      "customerName": "alajna",
      "customerLastname": "user",
      "campaignShippingAddress": {},
      "costInPoints": 0,
      "currentPointsAmount": 100,
      "used": false,
      "status": "active",
      "transactionId": {
        "transactionId": "98b15ef5-94ad-43ef-9984-0d41197d14e6"
      },
      "returnedAmount": 0,
      "deliveryStatus": {
        "status": ""
      }
    }
    ],
    "total": 3
    }



Get a collection of campaigns exported to a CSV file
----------------------------------------------------

To retrieve a paginated list of campaigns exported to a CSV file, you need to call the ``/api/campaign/bought/export/csv`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaign/bought/export/csv
	
+-------------------------------------+----------------+----------------------------------------------------+
| Parameter                           | Parameter type | Description                                        |
+=====================================+================+====================================================+
| Authorization                       | header         | Token received during authentication               |
+-------------------------------------+----------------+----------------------------------------------------+
| purchasedAtFrom                     | query          | *(optional)* Purchase date from filter             |
+-------------------------------------+----------------+----------------------------------------------------+
| purchasedAtTo                       | query          | *(optional)* Purchase date to filter               |
+-------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

To see the first page of all campaigns in CSV file format,, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/bought/export/csv \
        -X "GET" \
	-H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json
   
   0.Name,1.Date,2.Cost,"3.Tax value",4.email,5.phone,6.Firstname,7.Surname,"8.Points balance","9.Is used"
   "Percentage discount code","2019-03-14 10:29:05",0,,maxnowacki690711@test.pl,,Max,Nowacki,100,
   "Percentage discount code","2019-03-14 10:30:18",0,,maxnowacki974845@test.pl,,Max,Nowacki,340,
   "Percentage discount code","2019-03-14 10:20:01",0,,test@test.pl,,alajna,user,100,
   "Percentage discount code","2019-03-14 10:29:32",0,,maxnowacki856039@test.pl,,Max,Nowacki,340,
    gift123,"2019-03-15 08:40:24",3,,maxnowacki209528@test.pl,,Max,Nowacki,95,1
    test,"2019-03-15 08:15:14",10,,maxnowacki160093@test.pl,,Max,Nowacki,290,
    testowe,"2019-03-14 10:28:20",10,,maxnowacki160093@test.pl,,Max,Nowacki,300,
    "Percentage discount code","2019-03-14 09:29:50",0,,user-return@example.com,,TestUser,ForCouponTest,2410,
    cashback,"2019-03-14 13:45:21",0,,maxnowacki209528@test.pl,,Max,Nowacki,100,
   "Percentage discount code","2019-03-14 13:48:11",0,,test@test.pl,,alajna,user,100,



Get a collection of publicly available campaigns
------------------------------------------------

To retrieve a paginated list of campaigns that are publicly available, you need to call the ``/api/campaign/public/available`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaign/public/available

+-------------------------------------+----------------+----------------------------------------------------+
| Parameter                           | Parameter type | Description                                        |
+=====================================+================+====================================================+
| Authorization                       | header         | Token received during authentication               |
+-------------------------------------+----------------+----------------------------------------------------+
| labels                              | request        | *(optional)* Filter by labels                      |
+-------------------------------------+----------------+----------------------------------------------------+
| isFeatured                          | request        | *(optional)* Filter by featured tag                |
+-------------------------------------+----------------+----------------------------------------------------+
| campaignType                        | request        | *(optional)* Filter by campaign type               |
+-------------------------------------+----------------+----------------------------------------------------+
| name                                | request        | *(optional)* Filter by campaign name               |
+-------------------------------------+----------------+----------------------------------------------------+
| page                                | query          | *(optional)* Start from page, by default 1         |
+-------------------------------------+----------------+----------------------------------------------------+
| perPage                             | query          | *(optional)* Number of items to display per page,  |
|                                     |                | by default = 10                                    |
+-------------------------------------+----------------+----------------------------------------------------+
| sort                                | query          | *(optional)* Sort by column name                   |
+-------------------------------------+----------------+----------------------------------------------------+
| direction                           | query          | *(optional)* Direction of sorting [ASC, DESC],     |
|                                     |                | by default = ASC                                   |
+-------------------------------------+----------------+----------------------------------------------------+
| categoryId[]                        | query          | *(optional)* Array of category Ids                 |
+-------------------------------------+----------------+----------------------------------------------------+
| format                              | query          | *(optional)* Format of descriptions [html].        |
|                                     |                | Default is RAW.                                    |
+-------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

To see the first page of all publicly available campaigns, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/public/available \
        -X "GET" \
	-H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json
   	{
     "campaigns": [
     {
      "name": "testowe",
      "brandIcon": false,
      "rewardCampaignId": "4cd1415d-6c20-4642-a2eb-cd985c1f88aa",
      "campaignId": "4cd1415d-6c20-4642-a2eb-cd985c1f88aa",
      "reward": "gift_code",
      "active": true,
      "costInPoints": 10,
      "singleCoupon": false,
      "unlimited": true,
      "campaignActivity": {
        "allTimeActive": true
      },
      "campaignVisibility": {
        "allTimeVisible": true
      },
      "labels": [],
      "daysInactive": 28,
      "daysValid": 90,
      "featured": false,
      "photos": [],
      "public": true,
      "fulfillmentTracking": false,
      "createdAt": "2019-03-14T10:27:38+0100",
      "translations": [
        {
          "name": "testowe",
          "id": 42,
          "locale": "en"
        }
      ],
      "segmentNames": {},
      "levelNames": {
        "e82c96cf-32a3-43bd-9034-4df343e50000": "level0"
      },
      "categoryNames": [],
      "usageLeft": 0,
      "visibleForCustomersCount": 12,
      "usersWhoUsedThisCampaignCount": 1,
      "brandDescription": null,
      "shortDescription": null,
      "conditionsDescription": null,
      "usageInstruction": null
    },
	{
      "name": "Test reward campaign",
      "brandIcon": false,
      "rewardCampaignId": "000096cf-6361-4d70-e169-676e00000003",
      "campaignId": "000096cf-6361-4d70-e169-676e00000003",
      "reward": "discount_code",
      "active": true,
      "costInPoints": 5,
      "singleCoupon": false,
      "unlimited": false,
      "limit": 10,
      "limitPerUser": 2,
      "campaignActivity": {
        "allTimeActive": false,
        "activeFrom": "2016-01-01T00:00:00+0100",
        "activeTo": "2037-01-01T00:00:00+0100"
      },
      "campaignVisibility": {
        "allTimeVisible": false,
        "visibleFrom": "2016-01-01T00:00:00+0100",
        "visibleTo": "2037-01-01T00:00:00+0100"
      },
      "labels": [
        {
          "key": "type",
          "value": "test"
        }
      ],
      "daysInactive": 10,
      "daysValid": 20,
      "featured": false,
      "photos": [],
      "public": true,
      "fulfillmentTracking": false,
      "createdAt": "2019-03-14T08:29:42+0100",
      "translations": [
        {
          "name": "Test reward campaign",
          "id": 5,
          "locale": "en"
        },
        {
          "name": "Testowa kampania z nagrodą",
          "id": 6,
          "locale": "pl"
        }
      ],
      "segmentNames": {
        "00000000-0000-0000-0000-000000000011": "customer list with label",
        "873407dd-c434-4b6a-aa8c-a9418ce68abf": "anniversary_testowe"
      },
      "levelNames": {},
      "categoryNames": [],
      "usageLeft": 3,
      "visibleForCustomersCount": 1,
      "usersWhoUsedThisCampaignCount": 0,
      "brandDescription": null,
      "shortDescription": null,
      "conditionsDescription": null,
      "usageInstruction": null
    }
    ],
    "total": 2
    }  



Update a campaign
-----------------

To fully update a campaign, you need to call the ``/api/campaign/<campaign>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/campaign/<campaign>

+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| Parameter                                         | Parameter type |  Description                                                                 |
+===================================================+================+==============================================================================+
| Authorization                                     | header         | Token received during authentication                                         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| <campaign>                                        | query          |  Campaign ID                                                                 |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[reward]                                  | request        |  Campaign type. Possible types:                                              |
|                                                   |                |  discount_code, free_delivery_code, gift_code, event_code, value_code.       |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][name]                  | request        |  Campaign name in given locale.                                              |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][shortDescription]      | request        |  *(optional)* A short description in given locale.                           |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][conditionsDescription] | request        |  *(optional)* A description of required conditions to apply in given locale. |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][usageInstruction]      | request        |  *(optional)* A little information about how to use coupons in given locale.  |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][brandDescription]      | request        |  *(optional)* A little information about brand in given locale.               |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[active]                                  | request        |  Set 1 if active, otherwise 0                                                |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[costInPoints]                            | request        |  How many points it costs                                                    |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[target]                                  | request        |  Set ``level`` to choose target from defined levels.                         |
|                                                   |                |  Set ``segment`` to choose target from defined segments                      |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[categories]                              | request        | *(optional)* Array of category IDs.                                          |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[labels]                                  | request        | *(optional)* Informational labels in format "key:value;key1:value1"          |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[levels]                                  | request        |  Array of level IDs. *(required only if ``target=level``)*                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[segments]                                | request        |  Array of segment IDs. *(required only if ``target=segment``)*               |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[unlimited]                               | request        |  Set 1 if unlimited, otherwise 0                                             |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[singleCoupon]                            | request        |  Set 1 if single coupon, otherwise 0                                         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[limit]                                   | request        |  Global campaign usage limit. *(required only if ``unlimited=0``)*           |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[limitPerUser]                            | request        |  Customer campaign usage limit. *(required only if ``unlimited=0``)*         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[coupons]                                 | request        |  Array of coupon codes.                                                      |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignVisibility][allTimeVisible]      | request        |  Set 1 if always visible, otherwise 0                                        |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignVisibility][visibleFrom]         | request        |  Campaign visible from YYYY-MM-DD HH:mm, for example ``2017-10-05 10:59``.   |
|                                                   |                |  *(required only if ``allTimeVisible=0``)*                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignVisibility][visibleTo]           | request        |  Campaign visible to YYYY-MM-DD HH:mm, for example ``2017-10-05 10:59``.     |
|                                                   |                |  *(required only if ``allTimeVisible=0``)*                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignActivity][allTimeActive]         | request        |  Set 1 if always active, otherwise 0                                         |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignActivity][activeFrom]            | request        |  Campaign active from YYYY-MM-DD HH:mm, for example ``2017-10-05 10:59``.    |
|                                                   |                |  *(required only if ``allTimeActive=0``)*                                    |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[campaignActivity][activeTo]              | request        |  Campaign visible to YYYY-MM-DD HH:mm, for example ``2017-10-05 10:59``.     |
|                                                   |                |  *(required only if ``allTimeVisible=0``)*                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[daysInactive]                            | request        |  Number of days, during which coupon will not be active after purchase       |
|                                                   |                |  0 means "active immediately"                                                |
|                                                   |                |  Required for all rewards besides cashback                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[daysValid]                               | request        |  Number of days, during which coupon will be valid, after activation         |
|                                                   |                |  0 means "valid forever"                                                     |
|                                                   |                |  Required for all rewards besides cashback                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[photos]                                  | request        |  *(optional)* Array of uploaded photos                                       |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+

Example
^^^^^^^

 To fully update a campaign with ``id = 3062c881-93f3-496b-9669-4238c0a62be8``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/3062c881-93f3-496b-9669-4238c0a62be8 \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "campaign[reward]=discount_code" \
        -d "campaign[translations][en][reward]=discount_code" \
        -d "campaign[translations][en][name]=Discount+Code+Campaign" \
        -d "campaign[translations][en][shortDescription]=A+short+description+of+discount+code+campaign" \
        -d "campaign[translations][en][conditionsDescription]=Discount+code+for+registration" \
        -d "campaign[translations][en][usageInstruction]=Use+discount+code+as+you+like" \
        -d "campaign[translations][en][brandDescription]=Some+brand+description" \
        -d "campaign[active]=1" \
        -d "campaign[costInPoints]=100" \
        -d "campaign[target]=level" \
        -d "campaign[labels]=type:promotion;type:cashback" \
        -d "campaign[levels][0]=e82c96cf-32a3-43bd-9034-4df343e5fd94" \
        -d "campaign[levels][1]=000096cf-32a3-43bd-9034-4df343e5fd94" \
        -d "campaign[unlimited]=0" \
        -d "campaign[singleCoupon]=0" \
        -d "campaign[limit]=10" \
        -d "campaign[limitPerUser]=1" \
        -d "campaign[daysInactive]=0" \
        -d "campaign[daysValid]=1" \
        -d "campaign[coupons][0]=testCoupon" \
        -d "campaign[coupons][1]=DiscountCoupon" \
        -d "campaign[campaignVisibility][allTimeVisible]=0" \
        -d "campaign[campaignVisibility][visibleFrom]=2017-10-05+10:59" \
        -d "campaign[campaignVisibility][visibleTo]=2018-10-05+10:59" \
        -d "campaign[campaignActivity][allTimeActive]=0" \
        -d "campaign[campaignActivity][activeFrom]=2017-09-05+10:59" \
        -d "campaign[campaignActivity][activeTo]=2017-12-05+10:59"
        -f "campaign[photos][0]=@/FILE_PATH/FILE_NAME"

.. warning::

    Remember, you must update the whole data of the campaign.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *e82c96cf-32a3-43bd-9034-4df343e5fd94* or *000096cf-32a3-43bd-9034-4df343e5fd94* id are example values.
    Your value may be different. Check the list of all levels if you are not sure which id should be used.

.. note::

    The *testCoupon* or *DiscountCoupon* are example values. You can name code coupons as you like.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "campaignId": "3062c881-93f3-496b-9669-4238c0a62be8"
    }



Remove campaign's brand icon
----------------------------

To remove a campaign's brand icon from the campaign, you need to call the ``/api/campaign/{campaign}/brand_icon`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/campaign/<campaign>/brand_icon

+-----------------+----------------+--------------------------------------+
| Parameter       | Parameter type | Description                          |
+=================+================+======================================+
| Authorization   | header         | Token received during authentication |
+-----------------+----------------+--------------------------------------+
| <campaign>      | query          | Campaign ID                          |
+-----------------+----------------+--------------------------------------+

Example
^^^^^^^

To remove a brand icon from the campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/brand_icon \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an example value. Your value may be different.
    Check the list of all campaigns if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Get a campaign's brand icon
-------------------------

To get a campaign's brand icon, you need to call the ``/api/campaign/{campaign}/brand_icon`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaign/<campaign>/brand_icon

+-----------------+----------------+--------------------------------------+
| Parameter       | Parameter type | Description                          |
+=================+================+======================================+
| Authorization   | header         | Token received during authentication |
+-----------------+----------------+--------------------------------------+
| <campaign>      | query          | Campaign ID                          |
+-----------------+----------------+--------------------------------------+

Example
^^^^^^^

To get a brand icon for the campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/brand_icon \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an example value. Your value may be different.
    Check the list of all campaigns if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK



Add a brand icon to the campaign
---------------------------------

To add a brand icon to the campaign, you need to call the ``/api/campaign/{campaign}/brand_icon`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/campaign/<campaign>/brand_icon

+-----------------+----------------+--------------------------------------+
| Parameter       | Parameter type | Description                          |
+=================+================+======================================+
| Authorization   | header         | Token received during authentication |
+-----------------+----------------+--------------------------------------+
| <campaign>      | query          | Campaign ID                          |
+-----------------+----------------+--------------------------------------+
| brand_icon[file]| request        | Absolute path to the photo           |
+-----------------+----------------+--------------------------------------+

Example
^^^^^^^

To add a brand icon for the campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/brand_icon \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "brand_icon[file]=C:\fakepath\Photo.png"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an example value. Your value may be different.
    Check the list of all campaigns if you are not sure which id should be used.

.. note::

    The *brand_icon[file]=C:\fakepath\Photo.png* is an example value. Your value may be different.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Get campaign details
--------------------

To retrieve the details of a campaign, you need to call the ``/api/campaign/{campaign}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaign/<campaign>

+---------------+----------------+----------------------------------------------------+
| Parameter     | Parameter type | Description                                        |
+===============+================+====================================================+
| Authorization | header         | Token received during authentication               |
+---------------+----------------+----------------------------------------------------+
| <campaign>    | query          | Campaign ID                                        |
+---------------+----------------+----------------------------------------------------+
| format        | query          | *(optional)* Format of descriptions [html].        |
|               |                | Default is RAW.                                    |
+---------------+----------------+----------------------------------------------------+

Example
^^^^^^^

To see the details of the admin user with ``campaign = 3062c881-93f3-496b-9669-4238c0a62be8``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/3062c881-93f3-496b-9669-4238c0a62be8 \
        -X "GET" \ 
	    -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    Translatable fields (name, short description etc.) are returned in given locale.

.. note::

    The *3062c881-93f3-496b-9669-4238c0a62be8* id is an example value. Your value may be different.
    Check the list of all admin users if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "levels": [
        "e82c96cf-32a3-43bd-9034-4df343e5fd94",
        "000096cf-32a3-43bd-9034-4df343e5fd94"
      ],
      "segments": [],
      "coupons": [
        "testCoupon",
        "DiscountCoupon"
      ],
      "campaignId": "3062c881-93f3-496b-9669-4238c0a62be8",
      "reward": "discount_code",
      "name": "Discount Code Campaign 1",
      "shortDescription": "A short description of discount code campaign",
      "conditionsDescription": "Discount code for registration",
      "active": true,
      "costInPoints": 100,
      "singleCoupon": false,
      "unlimited": false,
      "limit": 10,
      "limitPerUser": 1,
      "daysValid": 1,
      "daysInactive": 0,
      "campaignActivity": {
        "allTimeActive": false,
        "activeFrom": "2017-09-05T10:59:00+0200",
        "activeTo": "2017-12-05T10:59:00+0100"
      },
      "campaignVisibility": {
        "allTimeVisible": false,
        "visibleFrom": "2017-10-05T10:59:00+0200",
        "visibleTo": "2018-10-05T10:59:00+0200"
      },
      "labels": [
        {
          "key": "type",
          "value": "promotion"
        }
      ],
      "usageInstruction": "Use discount code as you like",
      "segmentNames": [],
      "levelNames": {
        "e82c96cf-32a3-43bd-9034-4df343e5fd94": "level1",
        "000096cf-32a3-43bd-9034-4df343e5fd94": "level2"
      },
      "usageLeft": 2,
      "visibleForCustomersCount": 0,
      "usersWhoUsedThisCampaignCount": 0,
      "hasPhoto": false,
      "translations": [
          {
              "name": "Discount Code Campaign 1",
              "shortDescription": "A short description of discount code campaign",
              "id": 65,
              "locale": "en"
          },
          {
              "name": "Discount Code Campaign 1 in polish",
              "shortDescription": "A short description of discount code campaign in polish",
              "id": 66,
              "locale": "pl"
          }
      ],
      "photos" :[
            {
                "photoId" : "e82c96cf-32a3-43bd-9034-4df343e5f23ed",
                "path"  : "campaign_photos/e82c96cf-32a3-43bd-9034-4df343e5fd322294",
                "orginalName" : "my_image.png",
                "mimeType" : "image/png"
            }
       ]
    }



Get available campaign for a customer
-------------------------------------

To check which campaigns are available for a specific customer, you need to call the ``/api/admin/customer/<customer>/campaign/available`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/customer/<customer>/campaign/available

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <customer>                          | query          | Customer ID                                       |
+-------------------------------------+----------------+---------------------------------------------------+
| isFeatured                          | query          | *(optional)* Filter by featured tag               |
+-------------------------------------+----------------+---------------------------------------------------+
| hasSegment                          | query          | *(optional)* 1 to return only campaigns offered   |
|                                     |                | exclusively to some segments, 0 for campaigns     |
|                                     |                | offered only to all segments; omit to return all  |
|                                     |                | campaigns                                         |
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
| categoryId[]                        | query          | *(optional)* Array of category Ids                |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

To see the list of campaigns for a customer with ID ``customer = 00000000-0000-474c-b092-b0dd880c07e2``, use the method below:


.. code-block:: bash

    curl http://localhost:8181/api/admin/customer/00000000-0000-474c-b092-b0dd880c07e2/campaign/available \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *00000000-0000-474c-b092-b0dd880c07e2* id is an example value. Your value may be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [
        {
          "levels": [
            "000096cf-32a3-43bd-9034-4df343e5fd93",
            "e82c96cf-32a3-43bd-9034-4df343e5fd94",
            "000096cf-32a3-43bd-9034-4df343e5fd94"
          ],
          "segments": [],
          "coupons": [
            "123"
          ],
          "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "reward": "discount_code",
          "name": "tests",
          "active": true,
          "costInPoints": 10,
          "singleCoupon": false,
          "unlimited": false,
          "limit": 10,
          "limitPerUser": 2,
          "daysValid": 0,
          "daysInactive": 0,
          "campaignActivity": {
            "allTimeActive": false,
            "activeFrom": "2016-01-01T00:00:00+0100",
            "activeTo": "2018-01-01T00:00:00+0100"
          },
          "campaignVisibility": {
            "allTimeVisible": false,
            "visibleFrom": "2016-01-01T00:00:00+0100",
            "visibleTo": "2018-01-01T00:00:00+0100"
          },
          "segmentNames": [],
          "levelNames": {
            "000096cf-32a3-43bd-9034-4df343e5fd93": "level0",
            "e82c96cf-32a3-43bd-9034-4df343e5fd94": "level1",
            "000096cf-32a3-43bd-9034-4df343e5fd94": "level2"
          },
          "usageLeft": 1,
          "usageLeftForCustomer": 1,
          "canBeBoughtByCustomer": true,
          "visibleForCustomersCount": 2,
          "usersWhoUsedThisCampaignCount": 0,
          "hasPhoto": false,
          "labels": [
            {
              "key": "type",
              "value": "promotion"
            }
          ],
        }
      ],
      "total": 1
    }



Buy reward campaign for a specific customer (admin)
---------------------------------------------------

To buy a reward campaign for a specific customer, you need to call the ``/api/admin/customer/<customer>/campaign/<campaign>/buy`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/customer/<customer>/campaign/<campaign>/buy

+---------------+----------------+---------------------------------------+
| Parameter     | Parameter type | Description                           |
+===============+================+=======================================+
| Authorization | header         | Token received during authentication  |
+---------------+----------------+---------------------------------------+
| <customer>    | query          | Customer ID                           |
+---------------+----------------+---------------------------------------+
| <campaign>    | query          | Campaign ID                           |
+---------------+----------------+---------------------------------------+
| withoutPoints | query          | *(optional)* true|false - if set to   |
|               |                | true, customer points will not        |
|               |                | be used                               |
+---------------+----------------+---------------------------------------+
| quantity      | query          | *(optional)* default 1 - number       |
|               |                | of coupons to buy (not valid for      |
|               |                | cashback and percentage_discount_code)|
+---------------+----------------+---------------------------------------+

Example
^^^^^^^

To buy a reward campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` for the customer ``customer = 00000000-0000-474c-b092-b0dd880c07e2``
use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/admin/customer/00000000-0000-474c-b092-b0dd880c07e2/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/buy
        -X "POST"
        -H "Accept: application/json"
        -H "Content-type: application/x-www-form-urlencoded"
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *000096cf-32a3-43bd-9034-4df343e5fd93* id is an example value. Your value may be different.
    Check the list of all campaigns if you are not sure which id should be used.

.. note::

    The *00000000-0000-474c-b092-b0dd880c07e2* id is an example value. Your value may be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "coupons": [{
        "code": "123",
        "id": "ceb169c7-4fe2-4b49-9f2a-5a18634d7236
      }]
    }



Mark logged-in customer coupons as used
---------------------------------------

Mark coupons bought by logged-in customers as used using the ``/api/admin/customer/campaign/coupons/mark_as_used`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/customer/campaign/coupons/mark_as_used

+---------------------------+----------------+-------------------------------------------------------------+
| Parameter                 | Parameter type |  Description                                                |
+===========================+================+=============================================================+
| Authorization             | header         | Token received during authentication                        |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][campaignId]     | request        | Campaign UUID                                               |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][couponId]       | request        | Coupon UUID                                                 |
+---------------------------+----------------+-------------------------------------------------------------+
| coupons[][customerId]     | request        | Customer UUID                                               |
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

    curl http://localhost:8181/api/admin/customer/campaign/coupons/mark_as_used \
        -X "POST" \
	    -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "coupons[0][campaignId]=00000000-0000-0000-0000-000000000001" \
        -d "coupons[0][couponId]=00000000-0000-0000-0000-000000000002" \
        -d "coupons[0][customerId]=00000000-0000-0000-0000-000000000004" \
        -d "coupons[0][code]=WINTER" \
        -d "coupons[0][used]=1" \
        -d "coupons[0][transactionId]=00000000-0000-0000-0000-000000000003"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaignId = 00000000-0000-0000-0000-000000000001* id is an example value. Your value may be different.

.. note::

    The *couponId = 00000000-0000-0000-0000-000000000002* id is an example value. Your value may be different.

.. note::

    The *transactionId = 00000000-0000-0000-0000-000000000003* id is an example value. Your value may be different.

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



Check campaign visibility for customers
---------------------------------------

To check reward campaign visibility for customers, you need to call the ``/api/campaign/<campaign>/customers/visible`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaign/<campaign>/customers/visible

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <campaign>    | query          | Campaign ID                          |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To check reward campaign visibility for customers ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/customers/visible \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an example value. Your value may be different.
    Check the list of all campaigns if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customers": [
        {
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "active": true,
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
          "updatedAt": "2017-09-21T13:54:04+0200",
          "campaignPurchases": [],
          "transactionsCount": 1,
          "transactionsAmount": 3,
          "transactionsAmountWithoutDeliveryCosts": 3,
          "amountExcludedForLevel": 0,
          "averageTransactionAmount": 3,
          "lastTransactionDate": "2017-09-22T13:54:08+0200",
          "currency": "eur",
          "levelPercent": "14.00%"
        },
        {
          "customerId": "00000000-0000-474c-b092-b0dd880c07e2",
          "active": true,
          "firstName": "Jane",
          "lastName": "Doe",
          "gender": "male",
          "email": "user-temp@example.com",
          "phone": "111112222",
          "birthDate": "1990-09-11T00:00:00+0200",
          "address": {
            "street": "Test",
            "address1": "1",
            "province": "Mazowieckie",
            "city": "Warszawa",
            "postal": "00-000",
            "country": "PL"
          },
          "loyaltyCardNumber": "0000",
          "createdAt": "2016-08-08T10:53:14+0200",
          "levelId": "e82c96cf-32a3-43bd-9034-4df343e5fd94",
          "manuallyAssignedLevelId": {
            "levelId": "e82c96cf-32a3-43bd-9034-4df343e5fd94"
          },
          "agreement1": true,
          "agreement2": false,
          "agreement3": false,
          "updatedAt": "2017-10-02T11:49:25+0200",
          "campaignPurchases": [
            {
              "purchaseAt": "2017-10-02T12:03:34+0200",
              "costInPoints": 10,
              "campaignId": {
                "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93"
              },
              "used": false,
              "coupon": {
                "code": "123"
              }
            }
          ],
          "transactionsCount": 1,
          "transactionsAmount": 3,
          "transactionsAmountWithoutDeliveryCosts": 3,
          "amountExcludedForLevel": 0,
          "averageTransactionAmount": 3,
          "lastTransactionDate": "2017-09-22T13:54:08+0200",
          "currency": "eur",
          "levelPercent": "15.00%"
        }
      ],
      "total": 2
    }



Get a campaign's photo
----------------------

To get a campaign's photo, you need to call the ``/api/campaign/<campaign>/photo/{photoId}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaign/<campaign>/photo/<photoId>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <campaign>    | query          | Campaign ID                          |
+---------------+----------------+--------------------------------------+
| <photoId>     | query          | Photo ID                             |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To get the photo ``photoId = 08ae48fd-04b0-4a08-a2a7-fcfca3c4caf5`` for campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/photo/08ae48fd-04b0-4a08-a2a7-fcfca3c4caf5 \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id and *photoId = 08ae48fd-04b0-4a08-a2a7-fcfca3c4caf5* are example values. Your values may be different.
    Check the list of all campaigns if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. note::

    In the response you will get raw file content with a proper ``Content-Type`` header, for example:
    ``Content-Type: image/jpeg``.

Example Response
^^^^^^^^^^^^^^^^^^

The campaign may not have a photo at all and you will receive the following response.

.. code-block:: text

    STATUS: 404 Not Found

.. code-block:: json

    {
      "error": {
        "code": 404,
        "message": "Not Found"
      }
    }



Remove a campaign's photo
-------------------------

To remove a campaign's photo, you need to call the ``/api/campaign/<campaign>/photo/{photoId}`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/campaign/<campaign>/photo/<photoId>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <campaign>    | query          | Campaign ID                          |
+---------------+----------------+--------------------------------------+
| <photoId>     | query          | Photo ID                             |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To remove the photo ``photoId = 08ae48fd-04b0-4a08-a2a7-fcfca3c4caf5`` for campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/photo/08ae48fd-04b0-4a08-a2a7-fcfca3c4caf5 \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id and *photoId = 08ae48fd-04b0-4a08-a2a7-fcfca3c4caf5* are example values. Your values may be different.
    Check the list of all campaigns if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Add a photo to a campaign
-------------------------

To add a photo to a campaign, you need to call the ``/api/campaign/<campaign>/photo`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/campaign/<campaign>/photo

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <campaign>    | query          | Campaign ID                          |
+---------------+----------------+--------------------------------------+
| photo[file]   | request        | Absolute path to the photo           |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To add a photo to the campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/photo \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "photo[file]=C:\fakepath\Photo.png"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an example value. Your value may be different.
    Check the list of all campaigns if you are not sure which id should be used.

.. note::

    The *photo[file]=C:\fakepath\Photo.png* is an example value. Your value may be different.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK



Change a campaign's state
-----------------------

To make a campaign active or inactive, you need to call the ``/api/campaign/<campaign>/<active>`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/campaign/<campaign>/<active>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <campaign>    | query          | Campaign ID                          |
+---------------+----------------+--------------------------------------+
| <active>      | query          | Possible values: active, inactive    |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To make the campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` active, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/active \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an example value. Your value may be different.
    Check the list of all campaigns if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93"
    }

Example
^^^^^^^

To make the campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` inactive, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/inactive \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an example value. Your value may be different.
    Check the list of all campaigns if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93"
    }

Example Not Found Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 404 Not Found

.. code-block:: json

    {
      "error": {
        "code": 404,
        "message": "Not Found"
      }
    }



Get a campaign collection (seller)
--------------------------------

To retrieve a paginated list of campaigns, you need to call the ``/api/seller/campaign`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/campaign

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
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

To see the first page of all campaigns, use the method below:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/campaign \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When using endpoints starting with ``/api/seller``, you need to authorize using seller account credentials.

.. note::

    As a seller, you will receive less information about a campaign than an administrator.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [
        {
          "levels": [
            "000096cf-32a3-43bd-9034-4df343e5fd93",
            "e82c96cf-32a3-43bd-9034-4df343e5fd94",
            "000096cf-32a3-43bd-9034-4df343e5fd94"
          ],
          "segments": [],
          "coupons": [
            "123"
          ],
          "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "reward": "discount_code",
          "name": "tests",
          "active": true,
          "costInPoints": 10,
          "singleCoupon": false,
          "unlimited": false,
          "limit": 10,
          "limitPerUser": 2,
          "campaignActivity": {
            "allTimeActive": false,
            "activeFrom": "2016-01-01T00:00:00+0100",
            "activeTo": "2018-01-01T00:00:00+0100"
          },
          "campaignVisibility": {
            "allTimeVisible": false,
            "visibleFrom": "2016-01-01T00:00:00+0100",
            "visibleTo": "2018-01-01T00:00:00+0100"
          },
          "segmentNames": [],
          "levelNames": {
            "000096cf-32a3-43bd-9034-4df343e5fd93": "level0",
            "e82c96cf-32a3-43bd-9034-4df343e5fd94": "level1",
            "000096cf-32a3-43bd-9034-4df343e5fd94": "level2"
          },
          "labels": [
            {
              "key": "type",
              "value": "promotion"
            }
          ],
          "usageLeft": 0,
          "visibleForCustomersCount": 2,
          "usersWhoUsedThisCampaignCount": 1
        },
        {
          "levels": [
            "000096cf-32a3-43bd-9034-4df343e5fd94"
          ],
          "segments": [
            "00000000-0000-0000-0000-000000000002"
          ],
          "coupons": [
            "123"
          ],
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
            "allTimeActive": false,
            "activeFrom": "2016-01-01T00:00:00+0100",
            "activeTo": "2018-01-01T00:00:00+0100"
          },
          "campaignVisibility": {
            "allTimeVisible": false,
            "visibleFrom": "2016-01-01T00:00:00+0100",
            "visibleTo": "2018-01-01T00:00:00+0100"
          },
          "segmentNames": {
            "00000000-0000-0000-0000-000000000002": "anniversary"
          },
          "levelNames": {
            "000096cf-32a3-43bd-9034-4df343e5fd94": "level2"
          },
          "usageLeft": 1,
          "visibleForCustomersCount": 0,
          "usersWhoUsedThisCampaignCount": 0
        }
      ],
      "total": 2
    }



Get campaign details (seller)
-----------------------------

To retrieve the details of a campaign, you need to call the ``/api/seller/campaign/{campaign}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/campaign/<campaign>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <campaign>    | query          | Campaign ID                          |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the admin user with ``campaign = 3062c881-93f3-496b-9669-4238c0a62be8``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/seller/campaign/3062c881-93f3-496b-9669-4238c0a62be8 \
        -X "GET" \
	    -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When using endpoints starting with ``/api/seller``, you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *3062c881-93f3-496b-9669-4238c0a62be8* id is an example value. Your value may be different.
    Check the list of all admin users if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "levels": [
        "e82c96cf-32a3-43bd-9034-4df343e5fd94",
        "000096cf-32a3-43bd-9034-4df343e5fd94"
      ],
      "segments": [],
      "coupons": [
        "testCoupon",
        "DiscountCoupon"
      ],
      "campaignId": "3062c881-93f3-496b-9669-4238c0a62be8",
      "reward": "discount_code",
      "name": "Discount Code Campaign 1",
      "shortDescription": "A short description of discount code campaign",
      "conditionsDescription": "Discount code for registration",
      "active": true,
      "costInPoints": 100,
      "singleCoupon": false,
      "unlimited": false,
      "limit": 10,
      "limitPerUser": 1,
      "labels": [
        {
          "key": "type",
          "value": "promotion"
        }
      ],
      "campaignActivity": {
        "allTimeActive": false,
        "activeFrom": "2017-09-05T10:59:00+0200",
        "activeTo": "2017-12-05T10:59:00+0100"
      },
      "campaignVisibility": {
        "allTimeVisible": false,
        "visibleFrom": "2017-10-05T10:59:00+0200",
        "visibleTo": "2018-10-05T10:59:00+0200"
      },
      "usageInstruction": "Use discount code as you like",
      "segmentNames": [],
      "levelNames": {
        "e82c96cf-32a3-43bd-9034-4df343e5fd94": "level1",
        "000096cf-32a3-43bd-9034-4df343e5fd94": "level2"
      },
      "usageLeft": 2,
      "visibleForCustomersCount": 0,
      "usersWhoUsedThisCampaignCount": 0
    }



Get available campaigns for a customer (seller)
-----------------------------------------------

To check which campaigns are available for a specific customer, you need to call the ``/api/seller/customer/<customer>/campaign/available`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/customer/<customer>/campaign/available

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <customer>                          | query          | Customer ID                                       |
+-------------------------------------+----------------+---------------------------------------------------+
| isFeatured                          | query          | *(optional)* Filter by featured tag               |
+-------------------------------------+----------------+---------------------------------------------------+
| hasSegment                          | query          | *(optional)* 1 to return only campaigns offered   |
|                                     |                | exclusively to some segments, 0 for campaigns     |
|                                     |                | offered only to all segments; omit to return all  |
|                                     |                | campaigns                                         |
+-------------------------------------+----------------+---------------------------------------------------+
| page                                | query          | *(optional)* Start from page, by default 1        |
+-------------------------------------+----------------+---------------------------------------------------+
| perPage                             | query          | *(optional)* Number of items to display per page, |
|                                     |                | by default = 10                                   |
+-------------------------------------+----------------+---------------------------------------------------+
| sort                                | query          | *(optional)* Sort by column name. Also available  |
|                                     |                | to sort by child fields like                      |
|                                     |                | `campaignVisibility.visibleFrom`                  |
+-------------------------------------+----------------+---------------------------------------------------+
| direction                           | query          | *(optional)* Direction of sorting [ASC, DESC],    |
|                                     |                | by default = ASC                                  |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

To see the list of campaigns for a customer with the ID ``customer = 00000000-0000-474c-b092-b0dd880c07e2``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/seller/customer/00000000-0000-474c-b092-b0dd880c07e2/campaign/available \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When using endpoints starting with ``/api/seller``, you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *00000000-0000-474c-b092-b0dd880c07e2* id is an example value. Your value may be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaigns": [
        {
          "levels": [
            "000096cf-32a3-43bd-9034-4df343e5fd93",
            "e82c96cf-32a3-43bd-9034-4df343e5fd94",
            "000096cf-32a3-43bd-9034-4df343e5fd94"
          ],
          "segments": [],
          "coupons": [
            "123"
          ],
          "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "reward": "discount_code",
          "name": "tests",
          "active": true,
          "costInPoints": 10,
          "singleCoupon": false,
          "unlimited": false,
          "limit": 10,
          "limitPerUser": 2,
          "campaignActivity": {
            "allTimeActive": false,
            "activeFrom": "2016-01-01T00:00:00+0100",
            "activeTo": "2018-01-01T00:00:00+0100"
          },
          "campaignVisibility": {
            "allTimeVisible": false,
            "visibleFrom": "2016-01-01T00:00:00+0100",
            "visibleTo": "2018-01-01T00:00:00+0100"
          },
          "labels": [
            {
              "key": "type",
              "value": "promotion"
            }
          ],
          "segmentNames": [],
          "levelNames": {
            "000096cf-32a3-43bd-9034-4df343e5fd93": "level0",
            "e82c96cf-32a3-43bd-9034-4df343e5fd94": "level1",
            "000096cf-32a3-43bd-9034-4df343e5fd94": "level2"
          },
          "usageLeft": 1,
          "usageLeftForCustomer": 1,
          "canBeBoughtByCustomer": true,
          "visibleForCustomersCount": 2,
          "usersWhoUsedThisCampaignCount": 0
        }
      ],
      "total": 1
    }



Buy a reward campaign for a specific customer (seller)
----------------------------------------------------

To buy a reward campaign for a specific customer, you need to call the ``/api/seller/customer/<customer>/campaign/<campaign>/buy`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/seller/customer/<customer>/campaign/<campaign>/buy

+---------------+----------------+---------------------------------------+
| Parameter     | Parameter type | Description                           |
+===============+================+=======================================+
| Authorization | header         | Token received during authentication  |
+---------------+----------------+---------------------------------------+
| <customer>    | query          | Customer ID                           |
+---------------+----------------+---------------------------------------+
| <campaign>    | query          | Campaign ID                           |
+---------------+----------------+---------------------------------------+
| quantity      | query          | *(optional)* default 1 - number       |
|               |                | of coupons to buy (not valid for      |
|               |                | cashback and percentage_discount_code)|
+---------------+----------------+---------------------------------------+

Example
^^^^^^^

To buy the reward campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` for the customer ``customer = 00000000-0000-474c-b092-b0dd880c07e2``
use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/seller/customer/00000000-0000-474c-b092-b0dd880c07e2/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/buy
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When using endpoints starting with ``/api/seller``, you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *000096cf-32a3-43bd-9034-4df343e5fd93* id is an example value. Your value may be different.
    Check the list of all campaigns if you are not sure which id should be used.

.. note::

    The *00000000-0000-474c-b092-b0dd880c07e2* id is an example value. Your value may be different.
    Check the list of all customers if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "coupons": [{
        "code": "123",
        "id": "ceb169c7-4fe2-4b49-9f2a-5a18634d7236"
      }]
    }



Get all campaigns available for a logged-in customer
--------------------------------------------------

To get all campaigns available, you need to call the ``/api/customer/campaign/available`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/customer/campaign/available

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| isFeatured    | query          | *(optional)* IsFeatured              |
+---------------+----------------+--------------------------------------+
| page          | query          | *(optional)* Page                    |
+---------------+----------------+--------------------------------------+
| perPage       | query          | Number of elements per page          |
+---------------+----------------+--------------------------------------+
| sort          | query          | Field to sort by                     |
+---------------+----------------+--------------------------------------+
| direction     | query          | Sorting direction                    |
+---------------+----------------+--------------------------------------+
| categoryId    | query          | Sorting direction                    |
+---------------+----------------+--------------------------------------+


Example
^^^^^^^

Get all campaigns available for logged in customer.

.. code-block:: bash

    curl http://localhost:8181/api/customer/campaign/available
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When using endpoints starting with ``/api/customer``, you need to authorize using customer account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.


Change delivery status in a campaign bought by a customer
---------------------------------------------------------

To change delivery status, use the ``/api/admin/customer/{customer}/bought/coupon/{coupon}/changeDeliveryStatus`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/admin/customer/{customer}/bought/coupon/{coupon}/changeDeliveryStatus

+---------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                 | Parameter type | Description                                                                |
+===========================+================+============================================================================+
| Authorization             | header         | Token received during authentication                                       |
+---------------------------+----------------+----------------------------------------------------------------------------+
| <customer>                | query          | Customer ID                                                                |
+---------------------------+----------------+----------------------------------------------------------------------------+
| <coupon>                  | query          | Coupon ID                                                                  |
+---------------------------+----------------+----------------------------------------------------------------------------+
| deliveryStatus[status]    | query          | Available statuses: ["canceled","delivered","ordered","shipped"] (required)|
+---------------------------+----------------+----------------------------------------------------------------------------+


Example
^^^^^^^

To change delivery status for a customer with ``id = 5bdab759-5b31-48d6-a38b-ba4628ca1a91`` and coupon with ``id = 42d74422-ca0b-46f4-8871-be26f5a0497e``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/admin/customer/5bdab759-5b31-48d6-a38b-ba4628ca1a91/bought/coupon/42d74422-ca0b-46f4-8871-be26f5a0497e/changeDeliveryStatus
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "deliveryStatus[status]=canceled"

.. note::

    You can get all available statuses via a settings choice request ``/api/settings/choices/deliveryStatus``

.. note::

    When using endpoints starting with ``/api/admin/customer/{customer}/bought/coupon/{couponId}/changeDeliveryStatus``, you need to authorize using admin account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "success": "Delivery status changed!"
    }
