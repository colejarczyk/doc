Settings API
============

These endpoints will allow you to see the list of settings in Open Loyalty.

Get list of translations
------------------------

To retrieve a paginated list of available translations, you need to call the ``/api/admin/translations`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/translations

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/translations \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "translations": [
            {
                "code": "en",
                "name": "English",
                "default": true,
                "order": 0,
                "updatedAt": "2018-07-24T10:25:13+0200"
            }
        ],
        "total": 1
    }



Create new translations
-----------------------

To add new translations, you need to call the ``/api/admin/translations`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/translations

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| translation[name]               | query          | Translation name                                                  |
+---------------------------------+----------------+-------------------------------------------------------------------+
| translation[code]               | query          | Translation code                                                  |
+---------------------------------+----------------+-------------------------------------------------------------------+
| translation[default]            | query          | Is this translation default                                       |
+---------------------------------+----------------+-------------------------------------------------------------------+
| translation[order]              | query          | Translation order                                                 |
+---------------------------------+----------------+-------------------------------------------------------------------+
| translation[content]            | query          | Translation content                                               |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/translations \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "translation[name]=english123" \
        -d "translation[code]=en" \
        -d "translation[default]=1" \
        -d "translation[order]=0" \
        -d "translation[content]={\"key.confirmation.title\":{\"description\":\"{variable}+Title+for+that+dialog\",\"message\":+\"Hello\"}}"

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "code": "en",
        "name": "english123",
        "default": true,
        "order": 0,
        "content": "{\"key.confirmation.title\": \"description\"}"
    }



Get translations based on the locale code
-----------------------------------------

To retrieve a paginated list of translations for one of the languages, you need to call the ``/api/admin/translations/<code>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/translations/<code>

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <code>                          | query          | Translation code                                                  |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/translations/en \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "name": "english",
        "code": "en",
        "default": true,
        "order": 0,
        "content": "{\"key.confirmation.title\": \"description\"}"
        "updatedAt": "2018-02-26T12:43:01+0100"
    }



Update all translations and locale data
---------------------------------------

To update the whole locale, you need to call the ``/api/admin/translations/<code>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/admin/translations/<code>

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <code>                          | query          | Translation code                                                  |
+---------------------------------+----------------+-------------------------------------------------------------------+
| translation[name]               | query          | Translation name                                                  |
+---------------------------------+----------------+-------------------------------------------------------------------+
| translation[default]            | query          | Is this translation default                                       |
+---------------------------------+----------------+-------------------------------------------------------------------+
| translation[order]              | query          | Translation order                                                 |
+---------------------------------+----------------+-------------------------------------------------------------------+
| translation[content]            | query          | Translation content                                               |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/translations/en \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "name": "english",
        "code": "en",
        "default": true,
        "order": 0,
        "content": "{\"key.confirmation.title\": \"description\"}"
        "updatedAt": "2018-02-26T12:43:01+0100"
    }



Remove a whole locale
---------------------

To remove a whole locale along with its translations, you need to call the ``/api/admin/translations/<code>`` endpoint with the ``DELETE`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/admin/translations/<code>

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <code>                          | query          | Translation code                                                  |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/translations/en \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."


Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {}



Get all system settings
-----------------------

To retrieve a list of all system settings, you need to call the ``/api/<storeCode>/settings`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/settings

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <storeCode>                     | query          | Code of the store to get settings of.                             |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
    "settings": {
        "logo": {
            "path": "logo/logo.png",
            "mime": "image/png",
            "sizes": []
        },
        "small-logo": {
            "path": "logo/small-logo.png",
            "mime": "image/png",
            "sizes": []
        },
        "hero-image": {
            "path": "logo/hero-image.png",
            "mime": "image/png",
            "sizes": []
        },
        "admin-cockpit-logo": {
            "path": "logo/admin-cockpit-logo.png",
            "mime": "image/png",
            "sizes": []
        },
        "client-cockpit-logo-big": {
            "path": "logo/client-cockpit-logo-big.png",
            "mime": "image/png",
            "sizes": []
        },
        "client-cockpit-logo-small": {
            "path": "logo/client-cockpit-logo-small.png",
            "mime": "image/png",
            "sizes": []
        },
        "client-cockpit-hero-image": {
            "path": "logo/client-cockpit-hero-image.png",
            "mime": "image/png",
            "sizes": []
        },
        "excludedLevelCategories": [
            "category_excluded_from_level"
        ],
        "customersIdentificationPriority": [
            {
                "priority": 1,
                "field": "email"
            },
            {
                "priority": 2,
                "field": "loyaltyCardNumber"
            },
            {
                "priority": 3,
                "field": "phone"
            }
        ],
        "excludedDeliverySKUs": [],
        "excludedLevelSKUs": [
            "s"
        ],
        "returns": true,
        "allowCustomersProfileEdits": true,
        "allTimeNotLocked": true,
        "levelResetPointsOnDowngrade": false,
        "webhooks": false,
        "excludeDeliveryCostsFromTierAssignment": false,
        "pointsDaysActiveCount": 30,
        "expirePointsNotificationDays": 10,
        "expireCouponsNotificationDays": 10,
        "expireLevelsNotificationDays": 10,
        "currency": "EUR",
        "timezone": "Europe/Warsaw",
        "programName": "Loyalty Program",
        "programPointsSingular": "Point",
        "programPointsPlural": "Points",
        "pointsDaysExpiryAfter": "after_x_days",
        "tierAssignType": "transactions",
        "levelDowngradeMode": "none",
        "levelDowngradeBase": "none",
        "preferredCommunicationMethod": "email",
        "accountActivationRequired": true,
        "marketingVendorsValue": "none",
        "pushySecretKey": "",
        "programConditionsUrl": "",
        "programFaqUrl": "",
        "programUrl": "",
        "helpEmailAddress": "kkk",
        "uriWebhooks": "",
        "webhookHeaderName": "",
        "webhookHeaderValue": "",
        "accentColor": "",
        "cssTemplate": ""
    }
    }



Update system settings
----------------------

To update system settings, you need to call the ``/api/<storeCode>/settings`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/settings

+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                             | Parameter type | Description                                                                |
+=======================================================+================+============================================================================+
| Authorization                                         | header         | Token received during authentication                                       |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <storeCode>                                           | query          | Code of the store to update settings of.                                   |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[currency]                                    | request        | Currency: {"PLN":"pln","USD":"usd","EUR":"eur","HKD":"hkd","PESO":"cop",   |
|                                                       |                |     "INR": "inr","VND":"vnd"}                                              |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[timezone]                                    | request        | Timezone                                                                   |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[programName]                                 | request        | Program name                                                               |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[programUrl]                                  | request        | *(optional)*    Program URL                                                |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[programPointsSingular]                       | request        | Points singular                                                            |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[programPointsPlural]                         | request        | Points plural                                                              |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[returns]                                     | request        | *(optional)*    Returns                                                    |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[pointsDaysActiveCount]                       | request        | Required when allTimeActive=false. Points will expire after [days]         |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[allTimeActive]                               | request        | *(optional)* Is always active: true/false                                  |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[pointsDaysLocked]                            | request        | Points will be locked for N days. Required when allTimeNotLocked=false.    |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[expireCouponsNotificationDays]               | request        | Days before expiring coupons to notify user                                |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[expireLevelsNotificationDays]                | request        | Days before level recalculation to notify user                             |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[expirePointsNotificationDays]                | request        | Days before expiring points to notify user                                 |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[allTimeNotLocked]                            | request        | *(optional)* Is always not locked: true/false                              |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[levelDowngradeMode]                          | request        | Downgrade level based on specified mode: none, automatic, after_x_days     |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[levelDowngradeDays]                          | request        | Required when mode is "after_x_days"                                       |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[levelDowngradeBase]                          | request        | active_points | earned_points | earned_points_since_last_level_change      |
|                                                       |                | required when mode is "after_x_days"                                       |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[levelResetPointsOnDowngrade]                 | request        | *(optional)* Reset points option in the case of level downgrade based on   | 
|                                                       |                | the active points. Possible values : true/false                            |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[pushySecretKey]                              | request        | Pushy API secret key                                                       |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[customersIdentificationPriority][][priority] | request        | Priority to define matching transaction with customer                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[customersIdentificationPriority][][field]    | request        | Field to define matching transaction with customer                         |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[tierAssignType]                              | request        | Levels will be calculated with: transactions/points                        |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[excludeDeliveryCostsFromTierAssignment]      | request        | *(optional)* Delivery costs will not generate points: true/false           |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[excludedDeliverySKUs][]                      | request        | Required when DeliveryCostsFromTierAssignment=true                         |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[excludedLevelSKUs][]                         | request        | *(optional)* SKUs excluded from levels ...                                 |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[excludedLevelCategories][]                   | request        | *(optional)* Categories excluded from levels ...                           |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[logo]                                        | request        | Absolute path to the photo                                                 |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[accountActivationRequired]                   | request        | Whether to require activation for new customer accounts.                   |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[preferredCommunicationMethod]                | request        | Choose preferred method of communication with the customers.               |
|                                                       |                | Possible values 'email' or 'sms'.                                          |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[webhooks]                                    | request        | *(optional)* To enable/disable webhooks. Possible values : true/false      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[uriWebhooks]                                 | request        | *(optional)* URL where the webhooks will be sent                           |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[webhookHeaderName]                           | request        | Request header name                                                        |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[webhookHeaderValue]                          | request        | Request header value                                                       |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "settings[currency]=PLN" \
        -d "settings[timezone]=Europe/Warsaw" \
        -d "settings[programName]=Loyalty+Program" \
        -d "settings[programPointsSingular]=point" \
        -d "settings[programPointsPlural]=points" \
        -d "settings[returns]=0&settings[allTimeActive]=1" \
        -d "settings[customersIdentificationPriority][0][priority]=1" \
        -d "settings[customersIdentificationPriority][0][field]=email" \
        -d "settings[tierAssignType]=transactions" \
        -d "settings[excludeDeliveryCostsFromTierAssignment]=0"

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 500 Internal Server Error

.. code-block:: json

    {
      "error": {
        "code": 500,
        "message": "Internal Server Error"
      }
    }



Get lists of choices for specific select fields
-----------------------------------------------

To return a list of available choices for some specific fields, you need to call the ``/api/<storeCode>/settings/choices/<type>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

  To see a list of choices for a specific field <type>, use the method below:

.. code-block:: text

    GET /api/<storeCode>/settings/choices/<type>

+------------------------+----------------+----------------------------------------------------------------------------+
| Parameter              | Parameter type | Description                                                                |
+========================+================+============================================================================+
| Authorization          | header         | Token received during authentication                                       |
+------------------------+----------------+----------------------------------------------------------------------------+
| <storeCode>            | query          | Code of the store to get settings of.                                      |
+------------------------+----------------+----------------------------------------------------------------------------+
| <type>                 | query          | Allowed types: timezone, language, country, availableFrontendTranslations, |
|                        |                | earningRuleLimitPeriod                                                     |
+------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

 To see a list of language translations, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/choices/language \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "choices": {
        "Abkhazian": "ab",
        "Achinese": "ace",
        "Angika": "anp",
        "Ao Naga": "njo",
        "Arabic": "ar",
        "Aromanian": "rup",
        "Brazilian Portuguese": "pt_BR",
        "Breton": "br",
        "British English": "en_GB",
        "Buginese": "bug",
        "Bulgarian": "bg",
        "Bulu": "bum",
        "Buriat": "bua",
        "Burmese": "my",
        "Caddo": "cad",
        "Cajun French": "frc",
        "Canadian English": "en_CA",
        "Canadian French": "fr_CA",
        "Cantonese": "yue",
        (...)
        "Capiznon": "cps",
        "Zaza": "zza",
        "Zeelandic": "zea",
        "Zenaga": "zen",
        "Zhuang": "za",
        "Zoroastrian Dari": "gbz",
        "Zulu": "zu",
        "Zuni": "zun"
      }
    }



Get a list of available message templates
-----------------------------------------

To retrieve a complete list of available message templates, you need to call the ``/api/<storeCode>/message`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/message

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <storeCode>                     | query          | Code of the store to get message templates of.                    |
+---------------------------------+----------------+-------------------------------------------------------------------+
| page                            | query          | *(optional)* Start from page, by default 1                        |
+---------------------------------+----------------+-------------------------------------------------------------------+
| perPage                         | query          | *(optional)* Number of items to display per page,                 |
|                                 |                | by default = 10                                                   |
+---------------------------------+----------------+-------------------------------------------------------------------+
| sort                            | query          | *(optional)* Sort by column name                                  |
+---------------------------------+----------------+-------------------------------------------------------------------+
| direction                       | query          | *(optional)* Direction of sorting [ASC, DESC],                    |
|                                 |                | by default = ASC                                                  |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/message \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "messages": [
        {
          "id": "c5261111-0344-4661-9b51-b0733011b52f",
          "channel": "sms",
          "subject": "",
          "content": "New transaction matched {{ first_name }} {{ last_name }}",
          "enabled": false,
          "updatedAt": "2020-09-07T15:56:00+02:00",
          "event": "oloy.transaction.labels_were_appended",
          "target": "customer"
        },
        {
          "id": "67b4a4bc-b65a-42df-b2f3-d66c7e140ddd",
          "channel": "sms",
          "subject": "",
          "content": "You have achieved new level",
          "enabled": false,
          "updatedAt": "2020-09-07T15:56:00+02:00",
          "event": "oloy.customer.level_changed_automatically",
          "target": "customer"
        },
        {
          "id": "3fb108c9-00f4-482a-89c6-f1e069574073",
          "channel": "sms",
          "subject": "",
          "content": "You have bought a new reward",
          "enabled": false,
          "updatedAt": "2020-09-07T15:56:00+02:00",
          "event": "oloy.campaign.customer_bought_campaign",
          "target": "customer"
        },
        {
          "id": "9cbdf804-2724-4319-84e7-c8dbe7225149",
          "channel": "email",
          "subject": "New transaction labels",
          "content": "New transaction labels {{ first_name }} {{ last_name }}",
          "enabled": true,
          "updatedAt": "2020-09-07T15:56:00+02:00",
          "event": "oloy.transaction.labels_were_appended",
          "target": "customer"
        },
        {
          "id": "74236215-3bc7-4f8b-9f3a-ef23a7103307",
          "channel": "email",
          "subject": "Confirm your email change",
          "content": "Confirm your email change in {{ program_name }} (no. {{ code_number }}): {{ code }}",
          "enabled": true,
          "updatedAt": "2020-09-07T15:56:00+02:00",
          "event": "oloy.customer.email_was_changed",
          "target": "customer"
        },
        {
          "id": "3b6915cc-d960-4c6b-a65f-84df1fa3fc6b",
          "channel": "email",
          "subject": "Confirm your phone number change",
          "content": "Confirm your phone change in {{ program_name }} (no. {{ code_number }}): {{ code }}",
          "enabled": true,
          "updatedAt": "2020-09-07T15:56:00+02:00",
          "event": "oloy.customer.phone_number_was_changed",
          "target": "customer"
        }
      ],
      "total": 20
    }



Get details of a message template
---------------------------------

To retrieve details of a particular message template, you need to call the ``/api/<storeCode>/message/<messageId>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/message/<messageId>

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <storeCode>                     | query          | Code of the store the message template belongs to.                |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <messageId>                     | query          | Message template's ID                                             |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

 To see the details of a message template with ``messageId = c60f1033-b1d0-4033-b9fe-7a3c230c4479``, use the method below:
 
.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/message/c60f1033-b1d0-4033-b9fe-7a3c230c4479 \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "message": {
        "id": "c60f1033-b1d0-4033-b9fe-7a3c230c4479",
        "channel": "email",
        "target": "customer",
        "event": "oloy.account.available_points_amount_changed",
        "subject": "Your balance changed",
        "content": "Email content",
        "enabled": true,
        "updatedAt": "2018-02-19T09:45:00+0100"
      }
    }



Update message template's details
---------------------------------

To update details of a message template, you need to call the ``/api/<storeCode>/message/<messageId>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/<storeCode>/message/<messageId>

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type | Description                                        |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| <storeCode>                                    | query          | Code of the store the message template belongs to. |
+------------------------------------------------+----------------+----------------------------------------------------+
| <messageId>                                    | query          | Message template's ID                              |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[channel]                               | request        | Channel: sms, email or push                        |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[target]                                | request        | Target: customer or admin                          |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[event]                                 | request        | Event triggering the message.                      |
|                                                |                | See Get message events below.                      |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[subject]                               | request        | Message subject                                    |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[content]                               | request        | Message content                                    |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[enabled]                               | request        | If the messages generated from this template       |
|                                                |                | should be sent or not.                             |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/message/f4f0e1f9-3677-4bdb-9685-416a961bc319 \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "message[key]=oloy.account.available_points_amount_changed" \
        -d "message[channel]=sms" \
        -d "message[target]=customer" \
        -d "message[subject]=Your+balance+changed" \
        -d "message[content]=test" \
        -d "message[enabled]=1"

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "id": "f4f0e1f9-3677-4bdb-9685-416a961bc319"
    }



Activate a message
------------------

To enable sending a message, you need to call the ``/api/<storeCode>/message/<messageId>/activate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/message/<messageId>/activate

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type | Description                                        |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| <storeCode>                                    | query          | Code of the store the message template belongs to. |
+------------------------------------------------+----------------+----------------------------------------------------+
| <messageId>                                    | query          | Message template's ID                              |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/message/f4f0e1f9-3677-4bdb-9685-416a961bc319/activate \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "id": "f4f0e1f9-3677-4bdb-9685-416a961bc319"
    }



Deactivate a message
--------------------

To disable sending a message, you need to call the ``/api/<storeCode>/message/<messageId>/deactivate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/message/<messageId>/deactivate

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type | Description                                        |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| <storeCode>                                    | query          | Code of the store the message template belongs to. |
+------------------------------------------------+----------------+----------------------------------------------------+
| <messageId>                                    | query          | Message template's ID                              |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/message/f4f0e1f9-3677-4bdb-9685-416a961bc319/deactivate \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "id": "f4f0e1f9-3677-4bdb-9685-416a961bc319"
    }



Create a new message template
-----------------------------

To create a message template, you need to call the ``/api/<storeCode>/message`` endpoint with the ``POST`` method.

You can create only one message template addressed to a given target, for a given event, per channel.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/message

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type | Description                                        |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+
| <storeCode>                                    | query          | Code of the store to create message template in.   |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[channel]                               | request        | Channel: sms, email or push                        |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[target]                                | request        | Target: customer or admin                          |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[event]                                 | request        | Event triggering the message.                      |
|                                                |                | See Get message events below.                      |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[subject]                               | request        | Message subject                                    |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[content]                               | request        | Message content                                    |
+------------------------------------------------+----------------+----------------------------------------------------+
| message[enabled]                               | request        | If the messages generated from this template       |
|                                                |                | should be sent or not.                             |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/message \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "message[key]=oloy.account.available_points_amount_changed" \
        -d "message[channel]=sms" \
        -d "message[target]=customer" \
        -d "message[subject]=Your+balance+changed" \
        -d "message[content]=test" \
        -d "message[enabled]=1"

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "id": "c4f0e1f9-d33a-4b3b-9a4a-416a961bc319"
    }



Get message events
------------------

To retrieve a list of events a message can be triggered upon, you need to call the ``/api/message/events`` endpoint with the ``GET`` method.

The list contains the form values, their human-readable labels and a list of snippets available to use in a template.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/message/events

+------------------------------------------------+----------------+----------------------------------------------------+
| Parameter                                      | Parameter type | Description                                        |
+================================================+================+====================================================+
| Authorization                                  | header         | Token received during authentication               |
+------------------------------------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/message/events \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "events": [
        {
          "value": "oloy.account.available_points_amount_changed",
          "label": "Earned points",
          "snippets": [
            "{{ program_name }}",
            "{{ customer_url }} ",
            "{{ added_points_amount }} ",
            "{{ active_points_amount }} "
          ]
        },
        {
          "value": "oloy.customer.level_changed_automatically",
          "label": "Gained new level",
          "snippets": [
            "{{ program_name }}",
            "{{ customer_url }}",
            "{{ level_name }}",
            "{{ level_discount }}"
          ]
        },
        {
          "value": "oloy.campaign.has_become_available",
          "label": "Campaign has become available",
          "snippets": [
            "{{ program_name }}",
            "{{ customer_url }}",
            "{{ title }}",
            "{{ message }}"
          ]
        }
      ]
    }



Return all public system settings
---------------------------------

To retrieve a list of all public system settings, you need to call the ``/api/<storeCode>/settings/public`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/settings/public

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <storeCode>                     | query          | Code of the store to get settings of.                             |
+---------------------------------+----------------+-------------------------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/public \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "settings": {
        "allowCustomersProfileEdits": false
      }
    }



Remove logo
-----------

To remove the site logo, you need to call the ``/api/<storeCode>/settings/logo`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/<storeCode>/settings/logo

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <storeCode>                     | query          | Code of the store to delete logo of.                              |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/logo \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Get logo
--------

To retrieve the logo, you need to call the ``/api/<storeCode>/settings/logo`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/settings/logo

+----------------------------+----------------+------------------------------------------------------------------------+
| Parameter                  | Parameter type | Description                                                            |
+============================+================+========================================================================+
| Authorization              | header         | Token received during authentication                                   |
+----------------------------+----------------+------------------------------------------------------------------------+
| <storeCode>                | query          | Code of the store to get logo of.                                      |
+----------------------------+----------------+------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/logo \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    <svg version="1.1" id="openLoyaltyLogo" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 70" style="enable-background:new 0 0 200 70;" xml:space="preserve"><style type="text/css">    .st0{fill:#FFFFFF;}    .st1{opacity:0.7;}</style><g>    <path class="st0" d="M109.2,27.4c3.9,0,7,3.2,7,7c0,3.9-3.2,7-7,7c-3.9,0-7-3.2-7-7S105.3,27.4,109.2,27.4 M109.2,26.4        c-4.5,0-8.1,3.6-8.1,8.1s3.6,8.1,8.1,8.1s8.1-3.6,8.1-8.1C117.3,30,113.6,26.4,109.2,26.4"></path>    <path class="st0" d="M55.4,31.2c0,1.7-0.6,3-1.7,3.9C52.6,36,51,36.4,49,36.4h-1.7v6h-2.6v-16h4.6c2,0,3.5,0.4,4.5,1.2        C54.9,28.4,55.4,29.6,55.4,31.2 M47.4,34.2h1.4c1.4,0,2.3-0.2,3-0.7c0.6-0.5,0.9-1.2,0.9-2.2c0-0.9-0.3-1.6-0.8-2.1        c-0.6-0.5-1.4-0.7-2.6-0.7h-1.8v5.7C47.5,34.2,47.4,34.2,47.4,34.2z"></path>    <polygon class="st0" points="67.8,42.5 58.7,42.5 58.7,26.4 67.8,26.4 67.8,28.6 61.3,28.6 61.3,33 67.4,33 67.4,35.2 61.3,35.2         61.3,40.2 67.8,40.2     "></polygon>    <path class="st0" d="M85.4,42.5h-3.2l-7.9-12.9h-0.1l0.1,0.7c0.1,1.4,0.2,2.6,0.2,3.8v8.4h-2.4V26.4h3.2l7.9,12.8h0.1        c0-0.2,0-0.8-0.1-1.8c0-1.1-0.1-1.9-0.1-2.5v-8.5h2.4L85.4,42.5L85.4,42.5z"></path>    <polygon class="st0" points="92,42.5 92,26.4 93.1,26.4 93.1,41.4 100.8,41.4 100.8,42.5     "></polygon>    <polygon class="st0" points="124.5,35.2 129.2,26.4 130.5,26.4 125.1,36.3 125.1,42.5 123.9,42.5 123.9,36.4 118.5,26.4         119.8,26.4     "></polygon>    <path class="st0" d="M140.5,36.8H134l-2.3,5.7h-1.2l6.5-16.2h0.7l6.4,16.2h-1.3L140.5,36.8z M134.4,35.8h5.8L138,30        c-0.2-0.5-0.4-1.1-0.7-1.9c-0.2,0.7-0.4,1.3-0.7,1.9L134.4,35.8z"></path>    <polygon class="st0" points="147.6,42.5 147.6,26.4 148.8,26.4 148.8,41.4 156.5,41.4 156.5,42.5     "></polygon>    <polygon class="st0" points="162.1,42.5 161,42.5 161,27.4 155.7,27.4 155.7,26.4 167.3,26.4 167.3,27.4 162.1,27.4     "></polygon>    <polygon class="st0" points="174.8,35.2 179.5,26.4 180.7,26.4 175.3,36.3 175.3,42.5 174.2,42.5 174.2,36.4 168.8,26.4         170.1,26.4     "></polygon>    <g class="st1">        <circle class="st0" cx="30.3" cy="33" r="1.7"></circle>    </g>    <g class="st1">        <path class="st0" d="M22.6,42.2l1.3-2.2c-1.3-1.5-2.1-3.5-2.1-5.6c0-4.7,3.9-8.6,8.6-8.6s8.6,3.9,8.6,8.6c0,2.2-0.8,4.1-2.1,5.6            l1.3,2.2c2-2,3.3-4.8,3.3-7.8c0-6.1-4.9-11-11-11s-11,4.9-11,11C19.3,37.4,20.5,40.2,22.6,42.2z"></path>    </g>    <g class="st1">        <polygon class="st0" points="35.6,46.6 30.8,38.2 29.8,38.2 25,46.6 22.9,45.4 28.4,35.8 32.2,35.8 37.7,45.4         "></polygon>    </g></g></svg>



Add logo
--------

To add the site logo, you need to call the ``/api/<storeCode>/settings/logo`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/settings/logo

+----------------------------+----------------+------------------------------------------------------------------------+
| Parameter                  | Parameter type | Description                                                            |
+============================+================+========================================================================+
| Authorization              | header         | Token received during authentication                                   |
+----------------------------+----------------+------------------------------------------------------------------------+
| <storeCode>                | query          | Code of the store to add logo to.                                      |
+----------------------------+----------------+------------------------------------------------------------------------+
| photo[file]                | request        | Path of logo file                                                      |
+----------------------------+----------------+------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/logo \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "photo[file]=C:\fakepath\Photo.png"

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Get a small logo
----------------

To retrieve a small logo, you need to call the ``/api/<storeCode>/settings/small-logo`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/settings/small-logo

+---------------------------+----------------+-------------------------------------------------------------------------+
| Parameter                 | Parameter type | Description                                                             |
+===========================+================+=========================================================================+
| Authorization             | header         |  Token received during authentication                                   |
+---------------------------+----------------+-------------------------------------------------------------------------+
| <storeCode>               | query          | Code of the store to get small logo of.                                 |
+---------------------------+----------------+-------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/small-logo \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

	<svg version="1.1" id="openLoyaltyLogo" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 70" style="enable-background:new 0 0 200 70;" xml:space="preserve"><style type="text/css">	.st0{fill:#FFFFFF;}	.st1{opacity:0.7;}</style><g>	<path class="st0" d="M109.2,27.4c3.9,0,7,3.2,7,7c0,3.9-3.2,7-7,7c-3.9,0-7-3.2-7-7S105.3,27.4,109.2,27.4 M109.2,26.4		c-4.5,0-8.1,3.6-8.1,8.1s3.6,8.1,8.1,8.1s8.1-3.6,8.1-8.1C117.3,30,113.6,26.4,109.2,26.4"></path>	<path class="st0" d="M55.4,31.2c0,1.7-0.6,3-1.7,3.9C52.6,36,51,36.4,49,36.4h-1.7v6h-2.6v-16h4.6c2,0,3.5,0.4,4.5,1.2		C54.9,28.4,55.4,29.6,55.4,31.2 M47.4,34.2h1.4c1.4,0,2.3-0.2,3-0.7c0.6-0.5,0.9-1.2,0.9-2.2c0-0.9-0.3-1.6-0.8-2.1		c-0.6-0.5-1.4-0.7-2.6-0.7h-1.8v5.7C47.5,34.2,47.4,34.2,47.4,34.2z"></path>	<polygon class="st0" points="67.8,42.5 58.7,42.5 58.7,26.4 67.8,26.4 67.8,28.6 61.3,28.6 61.3,33 67.4,33 67.4,35.2 61.3,35.2 		61.3,40.2 67.8,40.2 	"></polygon>	<path class="st0" d="M85.4,42.5h-3.2l-7.9-12.9h-0.1l0.1,0.7c0.1,1.4,0.2,2.6,0.2,3.8v8.4h-2.4V26.4h3.2l7.9,12.8h0.1		c0-0.2,0-0.8-0.1-1.8c0-1.1-0.1-1.9-0.1-2.5v-8.5h2.4L85.4,42.5L85.4,42.5z"></path>	<polygon class="st0" points="92,42.5 92,26.4 93.1,26.4 93.1,41.4 100.8,41.4 100.8,42.5 	"></polygon>	<polygon class="st0" points="124.5,35.2 129.2,26.4 130.5,26.4 125.1,36.3 125.1,42.5 123.9,42.5 123.9,36.4 118.5,26.4 		119.8,26.4 	"></polygon>	<path class="st0" d="M140.5,36.8H134l-2.3,5.7h-1.2l6.5-16.2h0.7l6.4,16.2h-1.3L140.5,36.8z M134.4,35.8h5.8L138,30		c-0.2-0.5-0.4-1.1-0.7-1.9c-0.2,0.7-0.4,1.3-0.7,1.9L134.4,35.8z"></path>	<polygon class="st0" points="147.6,42.5 147.6,26.4 148.8,26.4 148.8,41.4 156.5,41.4 156.5,42.5 	"></polygon>	<polygon class="st0" points="162.1,42.5 161,42.5 161,27.4 155.7,27.4 155.7,26.4 167.3,26.4 167.3,27.4 162.1,27.4 	"></polygon>	<polygon class="st0" points="174.8,35.2 179.5,26.4 180.7,26.4 175.3,36.3 175.3,42.5 174.2,42.5 174.2,36.4 168.8,26.4 		170.1,26.4 	"></polygon>	<g class="st1">		<circle class="st0" cx="30.3" cy="33" r="1.7"></circle>	</g>	<g class="st1">		<path class="st0" d="M22.6,42.2l1.3-2.2c-1.3-1.5-2.1-3.5-2.1-5.6c0-4.7,3.9-8.6,8.6-8.6s8.6,3.9,8.6,8.6c0,2.2-0.8,4.1-2.1,5.6			l1.3,2.2c2-2,3.3-4.8,3.3-7.8c0-6.1-4.9-11-11-11s-11,4.9-11,11C19.3,37.4,20.5,40.2,22.6,42.2z"></path>	</g>	<g class="st1">		<polygon class="st0" points="35.6,46.6 30.8,38.2 29.8,38.2 25,46.6 22.9,45.4 28.4,35.8 32.2,35.8 37.7,45.4 		"></polygon>	</g></g></svg>



Get a named photo
-----------------

To retrieve a named photo, you need to call the ``/api/<storeCode>/settings/photo/<name>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/settings/photo/<name>

+----------------+----------------+---------------------------------------------------------------------------------------+
| Parameter      | Parameter type | Description                                                                           |
+================+================+=======================================================================================+
| Authorization  | header         | Token received during authentication                                                  |
+----------------+----------------+---------------------------------------------------------------------------------------+
| <storeCode>    | query          | Code of the store to get photo of.                                                    |
+----------------+----------------+---------------------------------------------------------------------------------------+
| <name>         | path           | *(required)* photo name  (logo, small-logo, hero-image, admin-cockpit-logo,           |
|                |                | client-cockpit-logo-big, client-cockpit-logo-small, client-cockpit-hero-image)        |
+----------------+----------------+---------------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/photo/small-logo \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

	<svg version="1.1" id="openLoyaltyLogo" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 70" style="enable-background:new 0 0 200 70;" xml:space="preserve"><style type="text/css">	.st0{fill:#FFFFFF;}	.st1{opacity:0.7;}</style><g>	<path class="st0" d="M109.2,27.4c3.9,0,7,3.2,7,7c0,3.9-3.2,7-7,7c-3.9,0-7-3.2-7-7S105.3,27.4,109.2,27.4 M109.2,26.4		c-4.5,0-8.1,3.6-8.1,8.1s3.6,8.1,8.1,8.1s8.1-3.6,8.1-8.1C117.3,30,113.6,26.4,109.2,26.4"></path>	<path class="st0" d="M55.4,31.2c0,1.7-0.6,3-1.7,3.9C52.6,36,51,36.4,49,36.4h-1.7v6h-2.6v-16h4.6c2,0,3.5,0.4,4.5,1.2		C54.9,28.4,55.4,29.6,55.4,31.2 M47.4,34.2h1.4c1.4,0,2.3-0.2,3-0.7c0.6-0.5,0.9-1.2,0.9-2.2c0-0.9-0.3-1.6-0.8-2.1		c-0.6-0.5-1.4-0.7-2.6-0.7h-1.8v5.7C47.5,34.2,47.4,34.2,47.4,34.2z"></path>	<polygon class="st0" points="67.8,42.5 58.7,42.5 58.7,26.4 67.8,26.4 67.8,28.6 61.3,28.6 61.3,33 67.4,33 67.4,35.2 61.3,35.2 		61.3,40.2 67.8,40.2 	"></polygon>	<path class="st0" d="M85.4,42.5h-3.2l-7.9-12.9h-0.1l0.1,0.7c0.1,1.4,0.2,2.6,0.2,3.8v8.4h-2.4V26.4h3.2l7.9,12.8h0.1		c0-0.2,0-0.8-0.1-1.8c0-1.1-0.1-1.9-0.1-2.5v-8.5h2.4L85.4,42.5L85.4,42.5z"></path>	<polygon class="st0" points="92,42.5 92,26.4 93.1,26.4 93.1,41.4 100.8,41.4 100.8,42.5 	"></polygon>	<polygon class="st0" points="124.5,35.2 129.2,26.4 130.5,26.4 125.1,36.3 125.1,42.5 123.9,42.5 123.9,36.4 118.5,26.4 		119.8,26.4 	"></polygon>	<path class="st0" d="M140.5,36.8H134l-2.3,5.7h-1.2l6.5-16.2h0.7l6.4,16.2h-1.3L140.5,36.8z M134.4,35.8h5.8L138,30		c-0.2-0.5-0.4-1.1-0.7-1.9c-0.2,0.7-0.4,1.3-0.7,1.9L134.4,35.8z"></path>	<polygon class="st0" points="147.6,42.5 147.6,26.4 148.8,26.4 148.8,41.4 156.5,41.4 156.5,42.5 	"></polygon>	<polygon class="st0" points="162.1,42.5 161,42.5 161,27.4 155.7,27.4 155.7,26.4 167.3,26.4 167.3,27.4 162.1,27.4 	"></polygon>	<polygon class="st0" points="174.8,35.2 179.5,26.4 180.7,26.4 175.3,36.3 175.3,42.5 174.2,42.5 174.2,36.4 168.8,26.4 		170.1,26.4 	"></polygon>	<g class="st1">		<circle class="st0" cx="30.3" cy="33" r="1.7"></circle>	</g>	<g class="st1">		<path class="st0" d="M22.6,42.2l1.3-2.2c-1.3-1.5-2.1-3.5-2.1-5.6c0-4.7,3.9-8.6,8.6-8.6s8.6,3.9,8.6,8.6c0,2.2-0.8,4.1-2.1,5.6			l1.3,2.2c2-2,3.3-4.8,3.3-7.8c0-6.1-4.9-11-11-11s-11,4.9-11,11C19.3,37.4,20.5,40.2,22.6,42.2z"></path>	</g>	<g class="st1">		<polygon class="st0" points="35.6,46.6 30.8,38.2 29.8,38.2 25,46.6 22.9,45.4 28.4,35.8 32.2,35.8 37.7,45.4 		"></polygon>	</g></g></svg>



Add a named photo
-----------------

To add a named photo, you need to call the ``/api/<storeCode>/settings/photo/<name>`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/settings/photo/<name>

+----------------+----------------+------------------------------------------------------------------------------------+
| Parameter      | Parameter type | Description                                                                        |
+================+================+====================================================================================+
| Authorization  | header         | Token received during authentication                                               |
+----------------+----------------+------------------------------------------------------------------------------------+
| <storeCode>    | query          | Code of the store to add photo to.                                                 |
+----------------+----------------+------------------------------------------------------------------------------------+
| photo[file]    | request        | Path of logo file                                                                  |
+----------------+----------------+------------------------------------------------------------------------------------+
| <name>         | path           | *(required)* photo name  (logo, small-logo, hero-image, admin-cockpit-logo,        |
|                |                | client-cockpit-logo-big, client-cockpit-logo-small, client-cockpit-hero-image)     |
+----------------+----------------+------------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/photo/small-logo \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "photo[file]=C:\fakepath\Photo.png"

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Remove a named photo
--------------------

To remove a named photo, you need to call the ``/api/<storeCode>/settings/photo/<name>`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/<storeCode>/settings/photo/<name>

+--------------------+----------------+--------------------------------------------------------------------------------+
| Parameter          | Parameter type | Description                                                                    |
+====================+================+================================================================================+
| Authorization      | header         | Token received during authentication                                           |
+--------------------+----------------+--------------------------------------------------------------------------------+
| <storeCode>        | query          | Code of the store to delete photo of.                                          |
+--------------------+----------------+--------------------------------------------------------------------------------+
| <name>             | path           | *(required)* photo name  (logo, small-logo, hero-image, admin-cockpit-logo,    |
|                    |                | client-cockpit-logo-big, client-cockpit-logo-small, client-cockpit-hero-image) |
+--------------------+----------------+--------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/photo/small-logo \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Get the hero image
------------------

To retrieve the client cockpit hero image, you need to call the ``/api/<storeCode>/settings/hero-image`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/settings/hero-image

+---------------------------+----------------+-------------------------------------------------------------------------+
| Parameter                 | Parameter type | Description                                                             |
+===========================+================+=========================================================================+
| Authorization             | header         | Token received during authentication                                    |
+---------------------------+----------------+-------------------------------------------------------------------------+
| <storeCode>               | query          | Code of the store to get hero image of.                                 |
+---------------------------+----------------+-------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/hero-image \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

	<svg version="1.1" id="openLoyaltyLogo" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 70" style="enable-background:new 0 0 200 70;" xml:space="preserve"><style type="text/css">	.st0{fill:#FFFFFF;}	.st1{opacity:0.7;}</style><g>	<path class="st0" d="M109.2,27.4c3.9,0,7,3.2,7,7c0,3.9-3.2,7-7,7c-3.9,0-7-3.2-7-7S105.3,27.4,109.2,27.4 M109.2,26.4		c-4.5,0-8.1,3.6-8.1,8.1s3.6,8.1,8.1,8.1s8.1-3.6,8.1-8.1C117.3,30,113.6,26.4,109.2,26.4"></path>	<path class="st0" d="M55.4,31.2c0,1.7-0.6,3-1.7,3.9C52.6,36,51,36.4,49,36.4h-1.7v6h-2.6v-16h4.6c2,0,3.5,0.4,4.5,1.2		C54.9,28.4,55.4,29.6,55.4,31.2 M47.4,34.2h1.4c1.4,0,2.3-0.2,3-0.7c0.6-0.5,0.9-1.2,0.9-2.2c0-0.9-0.3-1.6-0.8-2.1		c-0.6-0.5-1.4-0.7-2.6-0.7h-1.8v5.7C47.5,34.2,47.4,34.2,47.4,34.2z"></path>	<polygon class="st0" points="67.8,42.5 58.7,42.5 58.7,26.4 67.8,26.4 67.8,28.6 61.3,28.6 61.3,33 67.4,33 67.4,35.2 61.3,35.2 		61.3,40.2 67.8,40.2 	"></polygon>	<path class="st0" d="M85.4,42.5h-3.2l-7.9-12.9h-0.1l0.1,0.7c0.1,1.4,0.2,2.6,0.2,3.8v8.4h-2.4V26.4h3.2l7.9,12.8h0.1		c0-0.2,0-0.8-0.1-1.8c0-1.1-0.1-1.9-0.1-2.5v-8.5h2.4L85.4,42.5L85.4,42.5z"></path>	<polygon class="st0" points="92,42.5 92,26.4 93.1,26.4 93.1,41.4 100.8,41.4 100.8,42.5 	"></polygon>	<polygon class="st0" points="124.5,35.2 129.2,26.4 130.5,26.4 125.1,36.3 125.1,42.5 123.9,42.5 123.9,36.4 118.5,26.4 		119.8,26.4 	"></polygon>	<path class="st0" d="M140.5,36.8H134l-2.3,5.7h-1.2l6.5-16.2h0.7l6.4,16.2h-1.3L140.5,36.8z M134.4,35.8h5.8L138,30		c-0.2-0.5-0.4-1.1-0.7-1.9c-0.2,0.7-0.4,1.3-0.7,1.9L134.4,35.8z"></path>	<polygon class="st0" points="147.6,42.5 147.6,26.4 148.8,26.4 148.8,41.4 156.5,41.4 156.5,42.5 	"></polygon>	<polygon class="st0" points="162.1,42.5 161,42.5 161,27.4 155.7,27.4 155.7,26.4 167.3,26.4 167.3,27.4 162.1,27.4 	"></polygon>	<polygon class="st0" points="174.8,35.2 179.5,26.4 180.7,26.4 175.3,36.3 175.3,42.5 174.2,42.5 174.2,36.4 168.8,26.4 		170.1,26.4 	"></polygon>	<g class="st1">		<circle class="st0" cx="30.3" cy="33" r="1.7"></circle>	</g>	<g class="st1">		<path class="st0" d="M22.6,42.2l1.3-2.2c-1.3-1.5-2.1-3.5-2.1-5.6c0-4.7,3.9-8.6,8.6-8.6s8.6,3.9,8.6,8.6c0,2.2-0.8,4.1-2.1,5.6			l1.3,2.2c2-2,3.3-4.8,3.3-7.8c0-6.1-4.9-11-11-11s-11,4.9-11,11C19.3,37.4,20.5,40.2,22.6,42.2z"></path>	</g>	<g class="st1">		<polygon class="st0" points="35.6,46.6 30.8,38.2 29.8,38.2 25,46.6 22.9,45.4 28.4,35.8 32.2,35.8 37.7,45.4 		"></polygon>	</g></g></svg>



Remove the hero image
---------------------

To remove the client cockpit hero image, you need to call the ``/api/<storeCode>/settings/hero-image`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/<storeCode>/settings/hero-image

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <storeCode>                     | query          | Code of the store to delete hero image of.                        |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/hero-image \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Get terms and conditions file
-----------------------------

To retrieve a terms and conditions file, you need to call the ``/terms-conditions`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /terms-conditions
	
+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/terms-conditions


Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK



Add terms and conditions file
-----------------------------

To add a terms and conditions file, you need to call the ``/api/<storeCode>/settings/conditions-file`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/settings/conditions-file

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <storeCode>                     | query          | Code of the store to add terms and conditions file to.            |
+---------------------------------+----------------+-------------------------------------------------------------------+
| conditions[file]                | request        | Path of logo file                                                 |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/conditions-file \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "conditions[file]=C:\fakepath\conditions.pdf"

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Remove a conditions file
------------------------

To remove a terms and conditions file, you need to call the ``/api/<storeCode>/settings/conditions-file`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/<storeCode>/settings/conditions-file

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <storeCode>                     | query          | Code of the store to delete terms and conditions of.              |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/conditions-file \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Get current translations
------------------------

To return current translations, you need to call the ``/api/translations`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/translations

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/translations \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "global": {
        "configuration": "Configuration",
        "users": "Users",
        "cancel": "Cancel",
        "save": "Save",
        "yes": "Yes",
        "no": "No",
        # ...
      },
      "users": {
        # ...
      },
      # ...
      "Your password must be at least 8 characters long.": "Your password must be at least 8 characters long",
      "Your password must include both upper and lower case letters.": "Your password must include both upper and lower case letters",
      "Your password must include at least one number.": "Your password must include at least one number",
      "Your password must contain at least one special character.": "Your password must contain at least one special character",
      "Your password must include at least one letter.": "Your password must include at least one letter"
    }



Get custom css
--------------

These endpoints will allow you to provide a customized CSS file which can be used in frontend application.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/settings/css

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <storeCode>                     | query          | Code of the store to edit custom css.                             |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/css \
        -X "GET" \
        -H "Accept: text/css"

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: css

    .text { color: #123123; }



Return activation configuration and method
------------------------------------------

To check activation method, you need to call the ``/api/<storeCode>/settings/activation`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/settings/activation

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <storeCode>                     | query          | Code of the store to get activation method of.                    |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/activation \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "method": "sms",
      "required": true
    }



Get the manifest file
---------------------

To get the manifest file, you need to call the ``/api/<storeCode>/settings/manifest`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/settings/manifest

+---------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                       | Parameter type | Description                                                       |
+=================================+================+===================================================================+
| Authorization                   | header         | Token received during authentication                              |
+---------------------------------+----------------+-------------------------------------------------------------------+
| <storeCode>                     | query          | Code of the store to get the manifest file.                       |
+---------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/settings/manifest \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "name": "Loyalty Program",
      "short_name": "Loyalty Program",
      "icons": [
        {
          "src": "backend.openloyalty3.test.openloyalty.io/api/settings/small-logo",
          "sizes": "192x192",
          "type": "image/png"
        },
        {
          "src": "backend.openloyalty3.test.openloyalty.io/api/settings/logo",
          "sizes": "512x512",
          "type": "image/png"
        }
      ],
      "start_url": "/",
      "display": "standalone",
      "scope": "/",
      "background_color": "#FFFFFF",
      "theme_color": "#FFFFFF"
    }
