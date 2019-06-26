 Reward Campaigns API
====================

These endpoints will allow you to easily manage Reward Campaigns.

.. note::

    Each role in the Open Loyalty has individual endpoints to manage reward campaigns.

Create a new campaign
---------------------

To create a new campaign you will need to call the ``/api/campaign`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/campaign

+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| Parameter                                         | Parameter type |  Description                                                                 |
+===================================================+================+============================================================================+
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
| campaign[translations][en][usageInstruction]      | request        |  *(optional)* A short information about how to use coupons in given locale.  |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][brandDescription]      | request        |  *(optional)* A short information about brand in given locale.               |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[active]                                  | request        |  Set 1 if active, otherwise 0                                                |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[categories]                              | request        | *(optional)* Array of category IDs.                                          |
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
| campaign[daysInactive]                            | request        |  Number of days, while coupon will not be active after purchase              |
|                                                   |                |  0 means "active immediately"                                                |
|                                                   |                |  Required for all rewards besides cashback                                   |
+---------------------------------------------------+----------------+-------------------------------------------------------------------------------+
| campaign[daysValid]                               | request        |  Number of days, while coupon will be valid, after activation                |
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

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *e82c96cf-32a3-43bd-9034-4df343e5fd94* or *000096cf-32a3-43bd-9034-4df343e5fd94* id are an exemplary values.
    Your value can be different. Check in the list of all levels if you are not sure which id should be used.

.. note::

    The *testCoupon* or *DiscountCoupon* are an exemplary values. You can name code coupons as you like.

.. attention::

    If you would like to add a photos (one or many ) to the campaign you will need to call the ``/api/campaign/<campaign>/photo`` endpoint with the ``POST`` method.
    More details you can find in Add a photo to the campaign section.

Exemplary Response
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

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

Exemplary Response
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

Get the collection of campaigns
-------------------------------

To retrieve a paginated list of campaigns you will need to call the ``/api/campaign`` endpoint with the ``GET`` method.

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

To see the first page of all campaigns use the below method:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/campaign \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


.. note::

    In below example you can get all Reward Campaigns that have label with key and value. You can
    filter only by label's key or value if you want and specify as many condition as you want.

.. note::

    Translatable fields (name, short description etc.) are returned in given locale.

.. code-block:: bash

    curl http://localhost:8181/api/campaign?labels[0][key]=key&labels[0][value]=value \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
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

Update a campaign
-----------------

To fully update a campaign you will need to call the ``/api/campaign/<campaign>`` endpoint with the ``PUT`` method.

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
| campaign[translations][en][usageInstruction]      | request        |  *(optional)* A short information about how to use coupons in given locale.  |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[translations][en][brandDescription]      | request        |  *(optional)* A short information about brand in given locale.               |
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
| campaign[daysInactive]                            | request        |  Number of days, while coupon will not be active after purchase              |
|                                                   |                |  0 means "active immediately"                                                |
|                                                   |                |  Required for all rewards besides cashback                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[daysValid]                               | request        |  Number of days, while coupon will be valid, after activation                |
|                                                   |                |  0 means "valid forever"                                                     |
|                                                   |                |  Required for all rewards besides cashback                                   |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign[photos]                                  | request        |  *(optional)* Array of uploaded photos                                       |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+

Example
^^^^^^^

 To fully update a campaign with ``id = 3062c881-93f3-496b-9669-4238c0a62be8`` use the below method:

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

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *e82c96cf-32a3-43bd-9034-4df343e5fd94* or *000096cf-32a3-43bd-9034-4df343e5fd94* id are an exemplary values.
    Your value can be different. Check in the list of all levels if you are not sure which id should be used.

.. note::

    The *testCoupon* or *DiscountCoupon* are an exemplary values. You can name code coupons as you like.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "campaignId": "3062c881-93f3-496b-9669-4238c0a62be8"
    }

Get campaign details
--------------------

To retrieve the details of a campaign you will need to call the ``/api/campaign/{campaign}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaign/<campaign>

+---------------+----------------+----------------------------------------------------+
| Parameter     | Parameter type | Description                                        |
+===============+================+====================================================+
| Authorization | header         | Token received during authentication               |
+---------------+----------------+----------------------------------------------------+
| <campaign>    | query          | Id of the campaign                                 |
+---------------+----------------+----------------------------------------------------+
| format        | query          | *(optional)* Format of descriptions [html].        |
|               |                | Default is RAW.                                    |
+---------------+----------------+----------------------------------------------------+

Example
^^^^^^^

To see the details of the admin user with ``campaign = 3062c881-93f3-496b-9669-4238c0a62be8`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/3062c881-93f3-496b-9669-4238c0a62be8 \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    Translatable fields (name, short description etc.) are returned in given locale.

.. note::

    The *3062c881-93f3-496b-9669-4238c0a62be8* id is an exemplary value. Your value can be different.
    Check in the list of all admin users if you are not sure which id should be used.

Exemplary Response
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

To check which campaigns are available for a specific customer you will need to call the ``/api/admin/customer/<customer>/campaign/available`` endpoint with the ``GET`` method.

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

To see the list of campaigns for a customer with ID ``customer = 00000000-0000-474c-b092-b0dd880c07e2`` use the below method:


.. code-block:: bash

    curl http://localhost:8181/api/admin/customer/00000000-0000-474c-b092-b0dd880c07e2/campaign/available \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *00000000-0000-474c-b092-b0dd880c07e2* id is an exemplary value. Your value can be different.
    Check in the list of all customers if you are not sure which id should be used.

Exemplary Response
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

Buy reward campaign for a specific customer
-------------------------------------------

To buy reward campaign for a specific customer you will need to cal the ``/api/admin/customer/<customer>/campaign/<campaign>/buy`` endpoint with the ``POST`` method.

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

To buy reward campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` for the customer ``customer = 00000000-0000-474c-b092-b0dd880c07e2``
use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/admin/customer/00000000-0000-474c-b092-b0dd880c07e2/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/buy
        -X "POST"
        -H "Accept: application/json"
        -H "Content-type: application/x-www-form-urlencoded"
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *000096cf-32a3-43bd-9034-4df343e5fd93* id is an exemplary value. Your value can be different.
    Check in the list of all campaigns if you are not sure which id should be used.

.. note::

    The *00000000-0000-474c-b092-b0dd880c07e2* id is an exemplary value. Your value can be different.
    Check in the list of all customers if you are not sure which id should be used.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "coupons": [{
        "code": "123"
      }]
    }

Mark logged in customer coupons as used
---------------------------------------

Mark bought by logged in customer coupons as used using ``/api/admin/customer/campaign/coupons/mark_as_used`` endpoint with the ``POST`` method.

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
        -X "GET" -H "Accept: application/json" \
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

Check campaign visibility for the customers
-------------------------------------------

To check reward campaign visibility for the customers you will need to cal the ``/api/campaign/<campaign>/customers/visible`` endpoint with the ``GET`` method.

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

To check reward campaign visibility for the customers ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/customers/visible \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an exemplary value. Your value can be different.
    Check in the list of all campaigns if you are not sure which id should be used.

Exemplary Response
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
          "email": "user@oloy.com",
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
          "email": "user-temp@oloy.com",
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

Get campaign's photo
--------------------

To get campaign's photo you will need to cal the ``/api/campaign/<campaign>/photo`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaign/<campaign>/photo

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <campaign>    | query          | Campaign ID                          |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To get campaign's photo ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/photo \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an exemplary value. Your value can be different.
    Check in the list of all campaigns if you are not sure which id should be used.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. note::

    In the response you will get raw file content with a proper ``Content-Type`` header, for example:
    ``Content-Type: image/jpeg``.

Exemplary Response
^^^^^^^^^^^^^^^^^^

The campaign may not have photo at all and you will receive a below response.

.. code-block:: text

    STATUS: 404 Not Found

.. code-block:: json

    {
      "error": {
        "code": 404,
        "message": "Not Found"
      }
    }

Remove campaign's photo
-----------------------

To remove campaign's photo you will need to cal the ``/api/campaign/<campaign>/photo`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/campaign/<campaign>/photo

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <campaign>    | query          | Campaign ID                          |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To remove campaign's photo ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/photo \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an exemplary value. Your value can be different.
    Check in the list of all campaigns if you are not sure which id should be used.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

Add a photo to the campaign
---------------------------

To add a photo to the campaign you will need to cal the ``/api/campaign/<campaign>/photo`` endpoint with the ``POST`` method.

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

To get campaign's photo ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/photo \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "photo[file]=C:\fakepath\Photo.png"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an exemplary value. Your value can be different.
    Check in the list of all campaigns if you are not sure which id should be used.

.. note::

    The *photo[file]=C:\fakepath\Photo.png* is an exemplary value. Your value can be different.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

Change campaign's status
------------------------

To make campaign active or inactive you will need to cal the ``/api/campaign/<campaign>/<status>`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/campaign/<campaign>/<status>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <campaign>    | query          | Campaign ID                          |
+---------------+----------------+--------------------------------------+
| <status>      | query          | Possible values: active, inactive    |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To make campaign active ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/active \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an exemplary value. Your value can be different.
    Check in the list of all campaigns if you are not sure which id should be used.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93"
    }

Example
^^^^^^^

To make campaign inactive ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/inactive \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *campaign = 000096cf-32a3-43bd-9034-4df343e5fd93* id is an exemplary value. Your value can be different.
    Check in the list of all campaigns if you are not sure which id should be used.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaignId": "000096cf-32a3-43bd-9034-4df343e5fd93"
    }

Exemplary Not Found Response
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

Get campaign collection (seller)
--------------------------------

To retrieve a paginated list of campaigns you will need to call the ``/api/seller/campaign`` endpoint with the ``GET`` method.

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

To see the first page of all campaigns use the below method:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/campaign \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When you will use endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    As a seller you will receive less amount of information about campaign than an administrator.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

Exemplary Response
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

To retrieve the details of a campaign you will need to call the ``/api/seller/campaign/{campaign}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/campaign/<campaign>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <campaign>    | query          | Id of the campaign                   |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the admin user with ``campaign = 3062c881-93f3-496b-9669-4238c0a62be8`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/seller/campaign/3062c881-93f3-496b-9669-4238c0a62be8 \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When you will use endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *3062c881-93f3-496b-9669-4238c0a62be8* id is an exemplary value. Your value can be different.
    Check in the list of all admin users if you are not sure which id should be used.

Exemplary Response
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

To check which campaigns are available for a specific customer you will need to call the ``/api/seller/customer/<customer>/campaign/available`` endpoint with the ``GET`` method.

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

To see the list of campaigns for a customer with ID ``customer = 00000000-0000-474c-b092-b0dd880c07e2`` use the below method:


.. code-block:: bash

    curl http://localhost:8181/api/seller/customer/00000000-0000-474c-b092-b0dd880c07e2/campaign/available \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When you will use endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *00000000-0000-474c-b092-b0dd880c07e2* id is an exemplary value. Your value can be different.
    Check in the list of all customers if you are not sure which id should be used.

Exemplary Response
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

Buy reward campaign for a specific customer (seller)
----------------------------------------------------

To buy reward campaign for a specific customer you will need to cal the ``/api/seller/customer/<customer>/campaign/<campaign>/buy`` endpoint with the ``POST`` method.

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

To buy reward campaign ``campaign = 000096cf-32a3-43bd-9034-4df343e5fd93`` for the customer ``customer = 00000000-0000-474c-b092-b0dd880c07e2``
use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/seller/customer/00000000-0000-474c-b092-b0dd880c07e2/campaign/000096cf-32a3-43bd-9034-4df343e5fd93/buy
        -X "POST"
        -H "Accept: application/json"
        -H "Content-type: application/x-www-form-urlencoded"
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When you will use endpoints starting with ``/api/seller`` you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *000096cf-32a3-43bd-9034-4df343e5fd93* id is an exemplary value. Your value can be different.
    Check in the list of all campaigns if you are not sure which id should be used.

.. note::

    The *00000000-0000-474c-b092-b0dd880c07e2* id is an exemplary value. Your value can be different.
    Check in the list of all customers if you are not sure which id should be used.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "coupons": [{
        "code": "123"
      }]
    }

Get all campaigns available for logged in customer.
----------------------------------------------------

To get all campaigns available you will need to cal the ``/api/customer/campaign/available`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/customer/campaign/available

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
        -X "POST"
        -H "Accept: application/json"
        -H "Content-type: application/x-www-form-urlencoded"
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    When you will use endpoints starting with ``/api/customer/campaign/available`` you need to authorize using seller account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Change delivery status in bought campaign by customer.
----------------------------------------------------

To change delivery status ``/api/admin/customer/{customerId}/bought/coupon/{couponId}/changeDeliveryStatus`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/customer/{customerId}/bought/coupon/{couponId}/changeDeliveryStatus

+---------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                 | Parameter type | Description                                                                |
+===========================+================+============================================================================+
| Authorization             | header         | Token received during authentication                                       |
+---------------------------+----------------+----------------------------------------------------------------------------+
| deliveryStatus[status]    | query          | Available statuses: ["canceled","delivered","ordered","shipped"] (required)|
+---------------+----------------+----------------------------------------------------------------------------------------+


Example
^^^^^^^

To change delivery status for customer ID

.. code-block:: bash

    curl http://localhost:8181/api/admin/customer/00000000-0000-474c-b092-b0dd880c07e2/bought/coupon/00000000-0000-0000-0000-b0dd880c07e2/changeDeliveryStatus
        -X "POST"
        -H "Accept: application/json"
        -H "Content-type: application/x-www-form-urlencoded"
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."
        -d "deliveryStatus[status]=canceled"

.. note::

    You can get all avialable statuses via settings choice request ``/api/settings/choices/deliveryStatus``

.. note::

    When you will use endpoints starting with ``/api/admin/customer/{customerId}/bought/coupon/{couponId}/changeDeliveryStatus`` you need to authorize using admin account credentials.

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.
