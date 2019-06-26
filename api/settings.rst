Settings API
============

These endpoints will allow you to see the list of settings taken in the Open Loyalty.


Get list of available customer statuses
---------------------------------------

To return list of available customer statuses you will need to call the ``/api/admin/customer-statuses`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/customer-statuses

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/customer-statuses \
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
      "statuses": [
        "new",
        "active",
        "blocked",
        "deleted"
      ],
      "total": 4
    }


Get list of translations
------------------------

To retrieve a paginated list of available translations you will need to call the ``/api/admin/translations`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/translations

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/translations \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
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

To add new translations you will need to call the ``/api/admin/translations`` endpoint with the ``POST`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/translations

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| translation[name]                              | query          | Translation name                                                           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| translation[code]                              | query          | Translation code                                                           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| translation[default]                           | query          | Is this translation default                                                |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| translation[order]                             | query          | Translation order                                                          |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| translation[content]                           | query          | Translation content                                                        |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

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

Exemplary Response
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


Get translations based on the code
----------------------------------

To retrieve a paginated list of translations you will need to call the ``/api/admin/translations/<key>`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/translations/<code>

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <code>                                         | query          | Translation code                                                           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/translations/en \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
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


Update translations based on the code
-------------------------------------

To update specific translations you will need to call the ``/api/admin/translations/<code>`` endpoint with the ``PUT``
method.


Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/admin/translations/<code>

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| translation[name]                              | query          | Translation name                                                           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| translation[default]                           | query          | Is this translation default                                                |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| translation[order]                             | query          | Translation order                                                          |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| translation[content]                           | query          | Translation content                                                        |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/translations/en \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."



Exemplary Response
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

Remove translations based on the code
-------------------------------------

To remove specific translations you will need to call the ``/api/admin/translations/<code>`` endpoint with the
``DELETE`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/admin/translations/<code>

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| translation[code]                              | query          | Translation code                                                           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/translations/en \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."



Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {}


Get all system settings
-----------------------

To retrieve a paginated list of settings you will need to call the ``/api/settings`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/settings

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "settings": {
        "excludedLevelCategories": [
          "category_excluded_from_level"
        ],
        "customerStatusesEarning": [
          "active"
        ],
        "customerStatusesSpending": [
          "active"
        ],
        "returns": true,
        "pointsDaysActive": 30,
        "pointsDaysLocked": 3,
        "levelDowngradeMode": "none",
        "currency": "eur",
        "timezone": "Europe/Warsaw",
        "programName": "Loyalty Program",
        "programPointsSingular": "Point",
        "programPointsPlural": "Points",
        "tierAssignType": "transactions",
        "excludedDeliverySKUs": [],
        "excludedLevelSKUs": [],
        "allTimeActive": false,
        "excludeDeliveryCostsFromTierAssignment": false,
        "marketingVendorsValue": "none",
        "customersIdentificationPriority": [
          {
            "priority": 1,
            "field": "email"
          },
          {
            "priority": 2,
            "field": "loyaltyCardNumber"
          }
        ],
        "logo": {
          "path": "logo/045a0a8e8d02c32427f7f1e6734f4eec.html",
          "originalName": "logo.svg",
          "mime": "image/svg+xml"
        }
      }
    }



Update system settings
----------------------

To update system settings you will need to call the ``/api/settings`` endpoint with the ``POST`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/settings

+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                             | Parameter type |  Description                                                               |
+=======================================================+================+============================================================================+
| Authorization                                         | header         | Token received during authentication                                       |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[currency]                                    | request        | Currency: {"PLN":"pln","USD":"usd","EUR":"eur","HKD":"hkd","PESO":"cop"}   |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[customerStatusesEarning][]                   | request        | Options:    "new","active","blocked","deleted"                             |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[customerStatusesSpending][]                  | request        | Options:    "new","active","blocked","deleted"                             |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[timezone]                                    | request        | Timezone                                                                   |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[programName]                                 | request        | Program name                                                               |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[programConditionsUrl]                        | request        | *(optional)*    TO DO                                                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[programFaqUrl]                               | request        | *(optional)*    TO DO                                                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[programUrl]                                  | request        | *(optional)*    TO DO                                                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[programPointsSingular]                       | request        | TO DO                                                                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[programPointsPlural]                         | request        | TO DO                                                                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[helpEmailAddress]                            | request        | *(optional)*    TO DO                                                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[returns]                                     | request        | *(optional)*    TO DO                                                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[pointsDaysActive]                            | request        | Required when allTimeActive=false. Points will expire after [days]         |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[allTimeActive]                               | request        | *(optional)* Is always active: true/false                                  |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[pointsDaysLocked]                            | request        | Points will be locked for N days. Required when allTimeNotLocked=false.    |
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
| settings[customersIdentificationPriority][]           | request        | TO DO                                                                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[customersIdentificationPriority][][priority] | request        | TO DO                                                                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[customersIdentificationPriority][][field]    | request        | TO DO                                                                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[tierAssignType]                              | request        | Levels will be calculated with: transactions/points                        |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[excludeDeliveryCostsFromTierAssignment]      | request        | *(optional)* Delivery costs will not be generating points: true/false      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[excludedDeliverySKUs][]                      | request        | Required when DeliveryCostsFromTierAssignment=true                         |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[excludedLevelSKUs][]                         | request        | *(optional)* SKUs excluded from levels ...                                 |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[excludedLevelCategories][]                   | request        | TO DO                                                                      |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[logo]                                        | request        | Absolute path to the photo                                                 |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[marketingVendorsValue]                       | request        | *(optional)* Choose marketing automation integration.                      |
|                                                       |                | Possible values 'none' or 'sales_manago'                                   |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[sales_manago][api_url]                       | request        | *(optional)* Required if Sales Manago integration enabled.                 |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[sales_manago][api_key]                       | request        | *(optional)* Required if Sales Manago integration enabled.                 |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[sales_manago][api_secret]                    | request        | *(optional)* Required if Sales Manago integration enabled.                 |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[sales_manago][customer_id]                   | request        | *(optional)* Required if Sales Manago integration enabled.                 |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+
| settings[sales_manago][email]                         | request        | *(optional)* Required if Sales Manago integration enabled.                 |
+-------------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "settings[currency]=PLN" \
        -d "settings[customerStatusesEarning][0]=active" \
        -d "settings[customerStatusesSpending][0]=active" \
        -d "settings[timezone]=Europe/Warsaw" \
        -d "settings[programName]=Loyalty+Program" \
        -d "settings[programPointsSingular]=point" \
        -d "settings[programPointsPlural]=points" \
        -d "settings[returns]=0&settings[allTimeActive]=1" \
        -d "settings[customersIdentificationPriority][0][priority]=1" \
        -d "settings[customersIdentificationPriority][0][field]=email" \
        -d "settings[tierAssignType]=transactions" \
        -d "settings[excludeDeliveryCostsFromTierAssignment]=0"

Exemplary Response
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


Get data needed for specific select fields
------------------------------------------

To return list of translations you will need to call the ``/api/settings/choices/<type>`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

  To see list of translations use the below method:

.. code-block:: text

    GET /api/settings/choices/<type>

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <type>                                         | query          | Allowed types: timezone, language, country, availableFrontendTranslations, |
|                                                |                | earningRuleLimitPeriod, availableCustomerStatuses                          |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

 To see list of language translations use the below method: 

.. code-block:: bash

    curl http://localhost:8181/api/settings/choices/language \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
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

Get list of available email settings
------------------------------------

To retrieve a complete list of available email settings you will need to call the ``/api/settings/emails`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/settings/emails

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings/emails \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "emails": [
        {
          "id": "c60f1033-b1d0-4033-b9fe-7a3c230c4479",
          "key": "OpenLoyaltyUserBundle:email:registration.html.twig",
          "subject": "Account created",
          "content": "Email content",
          "sender_name": "open@oloy.com",
          "sender_email": "open@oloy.com",
          "updatedAt": "2018-02-19T09:45:00+0100"
        },
         {
          "id": "cf83d86a-538c-42f7-8d8d-3b46109a864d",
          "key": "OpenLoyaltyUserBundle:email:registration_with_temporary_password.html.twig",
          "subject": "Account created",
          "content": "Email content",
          "sender_name": "open@oloy.com",
          "sender_email": "open@oloy.com",
          "updatedAt": "2018-02-19T09:45:00+0100"
        },
        {
          "id": "d08481f5-7e79-4e80-9e74-5a8cf776849d",
          "key": "OpenLoyaltyUserBundle:email:password_reset.html.twig",
          "subject": "Password reset requested",
          "content": "Email content",
          "sender_name": "open@oloy.com",
          "sender_email": "open@oloy.com",
          "updatedAt": "2018-02-19T09:45:00+0100"
        },
        {
          "id": "f4f0e1f9-3677-4bdb-9685-416a961bc319",
          "key": "OpenLoyaltyUserBundle:email:customer_reward_bought.html.twig",
          "subject": "{{ program_name }} - new reward",
          "content": "Email content",
          "sender_name": "open@oloy.com",
          "sender_email": "open@oloy.com",
          "updatedAt": "2018-02-19T09:45:00+0100"
        },
        {
          "id": "a9964f68-d2af-4db2-88ba-de99af707aec",
          "key": "OpenLoyaltyUserBundle:email:new_points.html.twig",
          "subject": "{{ program_name }} - new points",
          "content": "Email content",
          "sender_name": "open@oloy.com",
          "sender_email": "open@oloy.com",
          "updatedAt": "2018-02-19T09:45:00+0100"
        },
        {
          "id": "7824f1fb-9dee-45a8-b8c7-434f5130da60",
          "key": "OpenLoyaltyUserBundle:email:new_level.html.twig",
          "subject": "{{ program_name }} - new level",
          "content": "Email content",
          "sender_name": "open@oloy.com",
          "sender_email": "open@oloy.com",
          "updatedAt": "2018-02-19T09:45:00+0100"
        }
        ],
        "total": 6
    }



Get details of email setting
----------------------------

To retrieve details of particular email setting you will need to call the ``/api/settings/emails/<emailId>`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/settings/emails/<emailId>

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <emailId>                                      | query          | Email ID                                                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+


Example
^^^^^^^

 To see details of ``emailId = c60f1033-b1d0-4033-b9fe-7a3c230c4479``email use the below method:
 
.. code-block:: bash

    curl http://localhost:8181/api/settings/emails/c60f1033-b1d0-4033-b9fe-7a3c230c4479 \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "entity": {
        "id": "c60f1033-b1d0-4033-b9fe-7a3c230c4479",
        "key": "OpenLoyaltyUserBundle:email:registration.html.twig",
        "subject": "Account created",
        "content": "Email content",
        "sender_name": "open@oloy.com",
        "sender_email": "open@oloy.com",
        "updatedAt": "2018-02-19T09:45:00+0100"
      },
      "additional": {
        "variables": [
        "url"
       ],
      "preview": "Email preview"
      }
    }


Update email details
--------------------

To update email details you will need to call the ``/api/settings/emails/<email>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/settings/emails/<email>

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <email>                                        | query          |  Email ID                                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| email[key]                                     | request        |  Email keys                                                                |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| email[subject]                                 | request        |  Email subject                                                             |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| email[content]                                 | request        |  Email content                                                             |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| email[sender_name]                             | request        |  Sender name                                                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| email[sender_email]                            | request        |  Sender email                                                              |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings/emails/f4f0e1f9-3677-4bdb-9685-416a961bc319 \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "email[key]=OpenLoyaltyUserBundle:email:registration.html.twig" \
        -d "email[subject]=Account+created" \
        -d "email[content]=test" \
        -d "email[sender_name]=testol@divante.pl" \
        -d "email[sender_email]=testol@divante.pl" \


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "id": "f4f0e1f9-3677-4bdb-9685-416a961bc319"
    }



Remove logo
-----------

To remove a logo you will need to call the ``/api/settings/logo`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/settings/logo

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings/logo \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    No Content




Get logo
--------

To retrieve a logo you will need to call the ``/api/settings/logo`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/settings/logo/{size}

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <size>                                         | query          | *(optional)* Allowed sizes: 192x192, 512x512 (by default from config)      |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings/logo \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    <svg version="1.1" id="openLoyaltyLogo" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 70" style="enable-background:new 0 0 200 70;" xml:space="preserve"><style type="text/css">    .st0{fill:#FFFFFF;}    .st1{opacity:0.7;}</style><g>    <path class="st0" d="M109.2,27.4c3.9,0,7,3.2,7,7c0,3.9-3.2,7-7,7c-3.9,0-7-3.2-7-7S105.3,27.4,109.2,27.4 M109.2,26.4        c-4.5,0-8.1,3.6-8.1,8.1s3.6,8.1,8.1,8.1s8.1-3.6,8.1-8.1C117.3,30,113.6,26.4,109.2,26.4"></path>    <path class="st0" d="M55.4,31.2c0,1.7-0.6,3-1.7,3.9C52.6,36,51,36.4,49,36.4h-1.7v6h-2.6v-16h4.6c2,0,3.5,0.4,4.5,1.2        C54.9,28.4,55.4,29.6,55.4,31.2 M47.4,34.2h1.4c1.4,0,2.3-0.2,3-0.7c0.6-0.5,0.9-1.2,0.9-2.2c0-0.9-0.3-1.6-0.8-2.1        c-0.6-0.5-1.4-0.7-2.6-0.7h-1.8v5.7C47.5,34.2,47.4,34.2,47.4,34.2z"></path>    <polygon class="st0" points="67.8,42.5 58.7,42.5 58.7,26.4 67.8,26.4 67.8,28.6 61.3,28.6 61.3,33 67.4,33 67.4,35.2 61.3,35.2         61.3,40.2 67.8,40.2     "></polygon>    <path class="st0" d="M85.4,42.5h-3.2l-7.9-12.9h-0.1l0.1,0.7c0.1,1.4,0.2,2.6,0.2,3.8v8.4h-2.4V26.4h3.2l7.9,12.8h0.1        c0-0.2,0-0.8-0.1-1.8c0-1.1-0.1-1.9-0.1-2.5v-8.5h2.4L85.4,42.5L85.4,42.5z"></path>    <polygon class="st0" points="92,42.5 92,26.4 93.1,26.4 93.1,41.4 100.8,41.4 100.8,42.5     "></polygon>    <polygon class="st0" points="124.5,35.2 129.2,26.4 130.5,26.4 125.1,36.3 125.1,42.5 123.9,42.5 123.9,36.4 118.5,26.4         119.8,26.4     "></polygon>    <path class="st0" d="M140.5,36.8H134l-2.3,5.7h-1.2l6.5-16.2h0.7l6.4,16.2h-1.3L140.5,36.8z M134.4,35.8h5.8L138,30        c-0.2-0.5-0.4-1.1-0.7-1.9c-0.2,0.7-0.4,1.3-0.7,1.9L134.4,35.8z"></path>    <polygon class="st0" points="147.6,42.5 147.6,26.4 148.8,26.4 148.8,41.4 156.5,41.4 156.5,42.5     "></polygon>    <polygon class="st0" points="162.1,42.5 161,42.5 161,27.4 155.7,27.4 155.7,26.4 167.3,26.4 167.3,27.4 162.1,27.4     "></polygon>    <polygon class="st0" points="174.8,35.2 179.5,26.4 180.7,26.4 175.3,36.3 175.3,42.5 174.2,42.5 174.2,36.4 168.8,26.4         170.1,26.4     "></polygon>    <g class="st1">        <circle class="st0" cx="30.3" cy="33" r="1.7"></circle>    </g>    <g class="st1">        <path class="st0" d="M22.6,42.2l1.3-2.2c-1.3-1.5-2.1-3.5-2.1-5.6c0-4.7,3.9-8.6,8.6-8.6s8.6,3.9,8.6,8.6c0,2.2-0.8,4.1-2.1,5.6            l1.3,2.2c2-2,3.3-4.8,3.3-7.8c0-6.1-4.9-11-11-11s-11,4.9-11,11C19.3,37.4,20.5,40.2,22.6,42.2z"></path>    </g>    <g class="st1">        <polygon class="st0" points="35.6,46.6 30.8,38.2 29.8,38.2 25,46.6 22.9,45.4 28.4,35.8 32.2,35.8 37.7,45.4         "></polygon>    </g></g></svg>

Add logo
--------

To add a logo you will need to call the ``/api/settings/logo`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/settings/logo

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| photo[file]                                    | request        |  Path of logo file                                                         |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings/logo \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "photo[file]=C:\fakepath\Photo.png"

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    No Content


Get small logo
--------

To retrieve a logo you will need to call the ``/api/settings/small-logo`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/settings/small-logo/{size}

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| <size>                                         | query          | *(optional)* Allowed sizes: 192x192, 512x512 (by default from config)      |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

	curl http://localhost:8181/api/settings/small-logo \
	    -X "GET" \
	    -H "Accept: application/json" \
	    -H "Content-type: application/x-www-form-urlencoded" \
	    -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

	<svg version="1.1" id="openLoyaltyLogo" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 70" style="enable-background:new 0 0 200 70;" xml:space="preserve"><style type="text/css">	.st0{fill:#FFFFFF;}	.st1{opacity:0.7;}</style><g>	<path class="st0" d="M109.2,27.4c3.9,0,7,3.2,7,7c0,3.9-3.2,7-7,7c-3.9,0-7-3.2-7-7S105.3,27.4,109.2,27.4 M109.2,26.4		c-4.5,0-8.1,3.6-8.1,8.1s3.6,8.1,8.1,8.1s8.1-3.6,8.1-8.1C117.3,30,113.6,26.4,109.2,26.4"></path>	<path class="st0" d="M55.4,31.2c0,1.7-0.6,3-1.7,3.9C52.6,36,51,36.4,49,36.4h-1.7v6h-2.6v-16h4.6c2,0,3.5,0.4,4.5,1.2		C54.9,28.4,55.4,29.6,55.4,31.2 M47.4,34.2h1.4c1.4,0,2.3-0.2,3-0.7c0.6-0.5,0.9-1.2,0.9-2.2c0-0.9-0.3-1.6-0.8-2.1		c-0.6-0.5-1.4-0.7-2.6-0.7h-1.8v5.7C47.5,34.2,47.4,34.2,47.4,34.2z"></path>	<polygon class="st0" points="67.8,42.5 58.7,42.5 58.7,26.4 67.8,26.4 67.8,28.6 61.3,28.6 61.3,33 67.4,33 67.4,35.2 61.3,35.2 		61.3,40.2 67.8,40.2 	"></polygon>	<path class="st0" d="M85.4,42.5h-3.2l-7.9-12.9h-0.1l0.1,0.7c0.1,1.4,0.2,2.6,0.2,3.8v8.4h-2.4V26.4h3.2l7.9,12.8h0.1		c0-0.2,0-0.8-0.1-1.8c0-1.1-0.1-1.9-0.1-2.5v-8.5h2.4L85.4,42.5L85.4,42.5z"></path>	<polygon class="st0" points="92,42.5 92,26.4 93.1,26.4 93.1,41.4 100.8,41.4 100.8,42.5 	"></polygon>	<polygon class="st0" points="124.5,35.2 129.2,26.4 130.5,26.4 125.1,36.3 125.1,42.5 123.9,42.5 123.9,36.4 118.5,26.4 		119.8,26.4 	"></polygon>	<path class="st0" d="M140.5,36.8H134l-2.3,5.7h-1.2l6.5-16.2h0.7l6.4,16.2h-1.3L140.5,36.8z M134.4,35.8h5.8L138,30		c-0.2-0.5-0.4-1.1-0.7-1.9c-0.2,0.7-0.4,1.3-0.7,1.9L134.4,35.8z"></path>	<polygon class="st0" points="147.6,42.5 147.6,26.4 148.8,26.4 148.8,41.4 156.5,41.4 156.5,42.5 	"></polygon>	<polygon class="st0" points="162.1,42.5 161,42.5 161,27.4 155.7,27.4 155.7,26.4 167.3,26.4 167.3,27.4 162.1,27.4 	"></polygon>	<polygon class="st0" points="174.8,35.2 179.5,26.4 180.7,26.4 175.3,36.3 175.3,42.5 174.2,42.5 174.2,36.4 168.8,26.4 		170.1,26.4 	"></polygon>	<g class="st1">		<circle class="st0" cx="30.3" cy="33" r="1.7"></circle>	</g>	<g class="st1">		<path class="st0" d="M22.6,42.2l1.3-2.2c-1.3-1.5-2.1-3.5-2.1-5.6c0-4.7,3.9-8.6,8.6-8.6s8.6,3.9,8.6,8.6c0,2.2-0.8,4.1-2.1,5.6			l1.3,2.2c2-2,3.3-4.8,3.3-7.8c0-6.1-4.9-11-11-11s-11,4.9-11,11C19.3,37.4,20.5,40.2,22.6,42.2z"></path>	</g>	<g class="st1">		<polygon class="st0" points="35.6,46.6 30.8,38.2 29.8,38.2 25,46.6 22.9,45.4 28.4,35.8 32.2,35.8 37.7,45.4 		"></polygon>	</g></g></svg>


Get named photo
--------

To retrieve a named photo you will need to call the ``/api/settings/photo/{name}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/settings/photo/{name}/{size}


+------------------------------------------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                                                                                                               |
+================================================+================+============================================================================================================================================================+
| <size>                                         | path           | *(optional)* Allowed sizes: 192x192, 512x512 (by default from config)                                                                                      |
+------------------------------------------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <name>                                         | path           | *(required)* photo name  (logo, small-logo, hero-image, admin-cockpit-logo, client-cockpit-logo-big, client-cockpit-logo-small, client-cockpit-hero-image) |
+------------------------------------------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

	curl http://localhost:8181/api/settings/photo/{name} \
	    -X "GET" \
	    -H "Accept: application/json" \
	    -H "Content-type: application/x-www-form-urlencoded" \
	    -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

	<svg version="1.1" id="openLoyaltyLogo" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 70" style="enable-background:new 0 0 200 70;" xml:space="preserve"><style type="text/css">	.st0{fill:#FFFFFF;}	.st1{opacity:0.7;}</style><g>	<path class="st0" d="M109.2,27.4c3.9,0,7,3.2,7,7c0,3.9-3.2,7-7,7c-3.9,0-7-3.2-7-7S105.3,27.4,109.2,27.4 M109.2,26.4		c-4.5,0-8.1,3.6-8.1,8.1s3.6,8.1,8.1,8.1s8.1-3.6,8.1-8.1C117.3,30,113.6,26.4,109.2,26.4"></path>	<path class="st0" d="M55.4,31.2c0,1.7-0.6,3-1.7,3.9C52.6,36,51,36.4,49,36.4h-1.7v6h-2.6v-16h4.6c2,0,3.5,0.4,4.5,1.2		C54.9,28.4,55.4,29.6,55.4,31.2 M47.4,34.2h1.4c1.4,0,2.3-0.2,3-0.7c0.6-0.5,0.9-1.2,0.9-2.2c0-0.9-0.3-1.6-0.8-2.1		c-0.6-0.5-1.4-0.7-2.6-0.7h-1.8v5.7C47.5,34.2,47.4,34.2,47.4,34.2z"></path>	<polygon class="st0" points="67.8,42.5 58.7,42.5 58.7,26.4 67.8,26.4 67.8,28.6 61.3,28.6 61.3,33 67.4,33 67.4,35.2 61.3,35.2 		61.3,40.2 67.8,40.2 	"></polygon>	<path class="st0" d="M85.4,42.5h-3.2l-7.9-12.9h-0.1l0.1,0.7c0.1,1.4,0.2,2.6,0.2,3.8v8.4h-2.4V26.4h3.2l7.9,12.8h0.1		c0-0.2,0-0.8-0.1-1.8c0-1.1-0.1-1.9-0.1-2.5v-8.5h2.4L85.4,42.5L85.4,42.5z"></path>	<polygon class="st0" points="92,42.5 92,26.4 93.1,26.4 93.1,41.4 100.8,41.4 100.8,42.5 	"></polygon>	<polygon class="st0" points="124.5,35.2 129.2,26.4 130.5,26.4 125.1,36.3 125.1,42.5 123.9,42.5 123.9,36.4 118.5,26.4 		119.8,26.4 	"></polygon>	<path class="st0" d="M140.5,36.8H134l-2.3,5.7h-1.2l6.5-16.2h0.7l6.4,16.2h-1.3L140.5,36.8z M134.4,35.8h5.8L138,30		c-0.2-0.5-0.4-1.1-0.7-1.9c-0.2,0.7-0.4,1.3-0.7,1.9L134.4,35.8z"></path>	<polygon class="st0" points="147.6,42.5 147.6,26.4 148.8,26.4 148.8,41.4 156.5,41.4 156.5,42.5 	"></polygon>	<polygon class="st0" points="162.1,42.5 161,42.5 161,27.4 155.7,27.4 155.7,26.4 167.3,26.4 167.3,27.4 162.1,27.4 	"></polygon>	<polygon class="st0" points="174.8,35.2 179.5,26.4 180.7,26.4 175.3,36.3 175.3,42.5 174.2,42.5 174.2,36.4 168.8,26.4 		170.1,26.4 	"></polygon>	<g class="st1">		<circle class="st0" cx="30.3" cy="33" r="1.7"></circle>	</g>	<g class="st1">		<path class="st0" d="M22.6,42.2l1.3-2.2c-1.3-1.5-2.1-3.5-2.1-5.6c0-4.7,3.9-8.6,8.6-8.6s8.6,3.9,8.6,8.6c0,2.2-0.8,4.1-2.1,5.6			l1.3,2.2c2-2,3.3-4.8,3.3-7.8c0-6.1-4.9-11-11-11s-11,4.9-11,11C19.3,37.4,20.5,40.2,22.6,42.2z"></path>	</g>	<g class="st1">		<polygon class="st0" points="35.6,46.6 30.8,38.2 29.8,38.2 25,46.6 22.9,45.4 28.4,35.8 32.2,35.8 37.7,45.4 		"></polygon>	</g></g></svg>


Add named photo
--------

To add a named photo you will need to call the ``/api/settings/photo/{name}`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/settings/photo/{name}

+------------------------------------------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                                                                                                               |
+================================================+================+============================================================================================================================================================+
| Authorization                                  | header         | Token received during authentication                                                                                                                       |
+------------------------------------------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| photo[file]                                    | request        |  Path of logo file                                                                                                                                         |
+------------------------------------------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <name>                                         | path           | *(required)* photo name  (logo, small-logo, hero-image, admin-cockpit-logo, client-cockpit-logo-big, client-cockpit-logo-small, client-cockpit-hero-image) |
+------------------------------------------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings/photo/{name} \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "photo[file]=C:\fakepath\Photo.png"

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    No Content


Remove named photo
-----------

To remove a named photo you will need to call the ``/api/settings/photo/{name}`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/settings/photo/{name}

+------------------------------------------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                                                                                                               |
+================================================+================+============================================================================================================================================================+
| Authorization                                  | header         | Token received during authentication                                                                                                                       |
+------------------------------------------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <name>                                         | path           | *(required)* photo name  (logo, small-logo, hero-image, admin-cockpit-logo, client-cockpit-logo-big, client-cockpit-logo-small, client-cockpit-hero-image) |
+------------------------------------------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings/photo/{name} \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    No Content


Get hero image
--------

To retrieve a logo you will need to call the ``/api/settings/hero-image`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/settings/hero-image/{size}

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| <size>                                         | query          | *(optional)* Allowed sizes: 192x192, 512x512 (by default from config)      |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

	curl http://localhost:8181/api/settings/hero-image \
	    -X "GET" \
	    -H "Accept: application/json" \
	    -H "Content-type: application/x-www-form-urlencoded" \
	    -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

	<svg version="1.1" id="openLoyaltyLogo" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 70" style="enable-background:new 0 0 200 70;" xml:space="preserve"><style type="text/css">	.st0{fill:#FFFFFF;}	.st1{opacity:0.7;}</style><g>	<path class="st0" d="M109.2,27.4c3.9,0,7,3.2,7,7c0,3.9-3.2,7-7,7c-3.9,0-7-3.2-7-7S105.3,27.4,109.2,27.4 M109.2,26.4		c-4.5,0-8.1,3.6-8.1,8.1s3.6,8.1,8.1,8.1s8.1-3.6,8.1-8.1C117.3,30,113.6,26.4,109.2,26.4"></path>	<path class="st0" d="M55.4,31.2c0,1.7-0.6,3-1.7,3.9C52.6,36,51,36.4,49,36.4h-1.7v6h-2.6v-16h4.6c2,0,3.5,0.4,4.5,1.2		C54.9,28.4,55.4,29.6,55.4,31.2 M47.4,34.2h1.4c1.4,0,2.3-0.2,3-0.7c0.6-0.5,0.9-1.2,0.9-2.2c0-0.9-0.3-1.6-0.8-2.1		c-0.6-0.5-1.4-0.7-2.6-0.7h-1.8v5.7C47.5,34.2,47.4,34.2,47.4,34.2z"></path>	<polygon class="st0" points="67.8,42.5 58.7,42.5 58.7,26.4 67.8,26.4 67.8,28.6 61.3,28.6 61.3,33 67.4,33 67.4,35.2 61.3,35.2 		61.3,40.2 67.8,40.2 	"></polygon>	<path class="st0" d="M85.4,42.5h-3.2l-7.9-12.9h-0.1l0.1,0.7c0.1,1.4,0.2,2.6,0.2,3.8v8.4h-2.4V26.4h3.2l7.9,12.8h0.1		c0-0.2,0-0.8-0.1-1.8c0-1.1-0.1-1.9-0.1-2.5v-8.5h2.4L85.4,42.5L85.4,42.5z"></path>	<polygon class="st0" points="92,42.5 92,26.4 93.1,26.4 93.1,41.4 100.8,41.4 100.8,42.5 	"></polygon>	<polygon class="st0" points="124.5,35.2 129.2,26.4 130.5,26.4 125.1,36.3 125.1,42.5 123.9,42.5 123.9,36.4 118.5,26.4 		119.8,26.4 	"></polygon>	<path class="st0" d="M140.5,36.8H134l-2.3,5.7h-1.2l6.5-16.2h0.7l6.4,16.2h-1.3L140.5,36.8z M134.4,35.8h5.8L138,30		c-0.2-0.5-0.4-1.1-0.7-1.9c-0.2,0.7-0.4,1.3-0.7,1.9L134.4,35.8z"></path>	<polygon class="st0" points="147.6,42.5 147.6,26.4 148.8,26.4 148.8,41.4 156.5,41.4 156.5,42.5 	"></polygon>	<polygon class="st0" points="162.1,42.5 161,42.5 161,27.4 155.7,27.4 155.7,26.4 167.3,26.4 167.3,27.4 162.1,27.4 	"></polygon>	<polygon class="st0" points="174.8,35.2 179.5,26.4 180.7,26.4 175.3,36.3 175.3,42.5 174.2,42.5 174.2,36.4 168.8,26.4 		170.1,26.4 	"></polygon>	<g class="st1">		<circle class="st0" cx="30.3" cy="33" r="1.7"></circle>	</g>	<g class="st1">		<path class="st0" d="M22.6,42.2l1.3-2.2c-1.3-1.5-2.1-3.5-2.1-5.6c0-4.7,3.9-8.6,8.6-8.6s8.6,3.9,8.6,8.6c0,2.2-0.8,4.1-2.1,5.6			l1.3,2.2c2-2,3.3-4.8,3.3-7.8c0-6.1-4.9-11-11-11s-11,4.9-11,11C19.3,37.4,20.5,40.2,22.6,42.2z"></path>	</g>	<g class="st1">		<polygon class="st0" points="35.6,46.6 30.8,38.2 29.8,38.2 25,46.6 22.9,45.4 28.4,35.8 32.2,35.8 37.7,45.4 		"></polygon>	</g></g></svg>


Remove conditions terms file
-----------

To remove a conditions terms file you will need to call the ``/api/settings/logo`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/settings/logo

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings/logo \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    No Content




Get conditions terms file
--------

To retrieve a logo you will need to call the ``/terms-conditions`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /terms-conditions


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/terms-conditions


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK


Add conditions terms file
--------

To add a logo you will need to call the ``/api/settings/conditions-file`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/settings/conditions-file

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| conditions[file]                                    | request        |  Path of logo file                                                         |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings/logo \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "conditions[file]=C:\fakepath\conditions.pdf"

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    No Content

Get current translations
------------------------

To return current translations you will need to call the ``/api/translations`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/translations

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/translations \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
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
        "admin_footer": "2018 Open Loyalty",
        "true": "True",
        "false": "False",
        "edit": "Edit",
        "change": "Change",
        "show": "Show",
        "not_set": "Not set",
        "settings": "Settings",
        "logout": "Logout",
        "menu": "Menu",
        "and": "AND",
        "or": "OR",
        "logs": "System logs",
        "confirm": "Yes",
        "active": "Active",
        "inactive": "Inactive",
        "translations": "Translations",
        "emails": "Emails",
        "account": "Account",
        "unlimited": "Unlimited",
        "search": "Search",
        "no_rows_to_display": "There is no rows to display",
        "all_time_active": "Is all time active",
        "level": "Level",
        "segment": "Segment",
        "start_typing_an_email": "enter email to search",
        "loading": "loading",
        "home": "Home",
        "upload": "Upload",
        "remove": "Remove"
      },
      "users": {
        "heading": "Users",
        "list": "Users list",
        "name": "Name",
        "surname": "Surname",
        "email": "E-mail",
        "active": "Active",
        "actions": "Actions",
        "external": "External",
        "add": "Add",
        "create_heading": "Add user",
        "first_name": "Name",
        "last_name": "Surname",
        "phone": "Phone",
        "edit": "Editing user",
        "create": "Create user",
        "password": "Password",
        "api_key": "Api key",
        "active_prompt": "",
        "edit_heading": "Edit user"
      },
      "nav": {
        "referred_customer": "Referred customers",
        "home": "Home",
        "customers": "Customers",
        "all_customers": "All customers",
        "add_customer": "Add customer",
        "levels": "Levels",
        "all_levels": "All levels",
        "add_level": "Add level",
        "transfers": "Points transfers",
        "all_transfers": "All points transfers",
        "transactions": "Transactions",
        "all_transactions": "All transactions",
        "earning_rules": "Earning points rules",
        "all_earning_rules": "All earning points rules",
        "add_earning_rule": "Add earning points rule",
        "pos": "POS",
        "all_pos": "All POS",
        "add_pos": "Add POS",
        "sellers": "Merchants",
        "all_sellers": "All merchants",
        "add_seller": "Add merchant",
        "segments": "Segments",
        "all_segments": "All segments",
        "add_segment": "Add segment",
        "campaigns": "Reward campaigns",
        "all_campaigns": "All reward campaigns",
        "add_campaign": "Add reward campaign",
        "support": "Support",
        "guide": "Guide",
        "retention_matrix": "Retention matrix",
        "dashboard": "Dashboard"
          },
      "customer_nav": {
        "logo1": "Loyalty",
        "logo2": "Program",
        "copyrights": "",
        "home": "Home",
        "my_rewards": "My rewards",
        "earning_points": "My points",
        "my_transactions": "My transactions",
        "match_with_ecommerce": "Match with eCommerce",
        "my_profile": "My profile"
      },
      "customer_campaign": {
        "more_information": {
          "button": "Click here for more info"
        },
        "coupon_used": "This coupon has been used",
        "not_enough_points": "Not enough points",
        "will_be_active_dates": "This reward campaign will be active from {{from}} to {{to}}",
        "will_be_active_all_time": "This campaign will be active all time",
        "will_be_active_soon": "Not active yet",
        "list": "My rewards",
        "bought_list": "My redeemed rewards",
        "points": "Points",
        "redeem": "Redeem reward",
        "footer": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent eget tincidunt est. Sed fringilla dapibus venenatis.",
        "no_rewards": "There are no available rewards",
        "no_bought_rewards": "There are no redeemed rewards",
        "all_time_Active": "All time active",
        "see_bought": "See rewards you have already redeemed",
        "reward_congratulations": "Congratulations!",
        "reward_ready": "Your reward is ready to receive.",
        "reward_code": "CODE OF REWARD",
        "active_points": "Redeem new rewards, you can use <b>{{points}}</b> active points",
        "reward_footer": "Instruction for reward, lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent eget tincidunt est. Sed fringilla dapibus venenatis.",
        "no_desc": "Reward description is not set",
        "no_name": "No name of reward campaign",
        "used_confirmation": "Confirm reward usage",
        "used_confirmation_description": "Please confirm reward usage",
        "singleCoupon_prompt": "To redeem customers will be able to use the same coupon"
      },
      "customer_transaction": {
        "customer_loyalty_card_number": "Loyalty card number",
        "customer_phone_number": "Phone number",
        "empty_transactions": "There is no transactions to display",
        "list": "Transactions list",
        "id": "Transaction ID",
        "document_number": "Document number",
        "document_type": "Document type",
        "revised_document": "Revised document",
        "purchase_date": "Purchase date",
        "purchase_place": "POS",
        "actions": "Actions",
        "details": "Transaction details",
        "customer_name": "Customer name",
        "phone": "Phone",
        "email": "E-mail",
        "loyaltyCardNumber": "Loyalty card number",
        "city": "City",
        "state": "State",
        "street": "Street",
        "building_name": "Building name",
        "unit_name": "Flat/Unit name",
        "postal_code": "Postal code",
        "country": "Country",
        "item_details": "Item details",
        "name": "Name",
        "quantity": "Quantity",
        "sku": "SKU",
        "category": "Category",
        "gross": "Gross value",
        "labels": "Labels",
        "maker": "Brand",
        "link_modal": "Match customer with transaction",
        "customer_email": "E-mail",
        "customer_id": "Customer ID",
        "transaction_document_number": "Document number",
        "customer_email_prompt": "Find customer by e-mail",
        "transaction_document_number_prompt": "Find transaction by document number",
        "customer_id_prompt": "Put customer unique ID",
        "link": "Match with customer",
        "heading": "Transactions",
        "transaction_id": "Transaction id",
        "points_earned": "Points earned",
        "pos_name": "POS name",
        "sum": "SUM",
        "amount": "Amount",
        "document_types": {
          "return": "Return",
          "sell": "Sell",
          "both": "Both"
        }
      },
      "Your password must be at least 8 characters long.": "Your password must be at least 8 characters long",
      "Your password must include both upper and lower case letters.": "Your password must include both upper and lower case letters",
      "Your password must include at least one number.": "Your password must include at least one number",
      "Your password must contain at least one special character.": "Your password must contain at least one special character",
      "Your password must include at least one letter.": "Your password must include at least one letter",
      "Ta wartość nie powinna być pusta.": "This value should not be empty",
      "Plik nie mógł zostać odnaleziony.": "File could not be found",
      "Ten plik nie jest obrazem.": "This file is not image",
      "customer with such phone already exists": "Customer with such phone already exists",
      "customer with such loyalty card number already exists": "Customer with such loyalty card number already exists",
      "Bad credentials": "Bad credentials"
    }

Get custom css
--------------

These endpoints will allow you to provide customized CSS file which can be used in frontend application.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/settings/css

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/settings/css \
        -X "GET" \
        -H "Accept: text/css" \

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: css

    .text { color: #123123; }
