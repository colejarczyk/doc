Level API
=========

These endpoints will allow you to see the list of levels taken in the Open Loyalty.

Get the complete list of levels
-------------------------------

To retrieve a paginated list of levels you will need to call the ``/api/level`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/level

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| page                 | query          | *(optional)* Start from page, by default 1             |
+----------------------+----------------+--------------------------------------------------------+
| perPage              | query          | *(optional)* Number of items to display per page,      |
|                      |                | by default = 10                                        |
+----------------------+----------------+--------------------------------------------------------+
| sort                 | query          | *(optional)* Sort by column name,                      |
|                      |                | by default = name                                      |
+----------------------+----------------+--------------------------------------------------------+
| direction            | query          | *(optional)* Direction of sorting [ASC, DESC],         |
|                      |                | by default = ASC                                       |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/level \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    Translatable fields (name, description etc.) are returned in given locale.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "levels": [
        {
          "id": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "name": "Bronze",
          "description": "Bronze level description",
          "active": true,
          "conditionValue": 0,
          "reward": {
          "name": "test reward",
          "value": 0.14,
          "code": "abc",
          "hasPhoto": false,
          "translations": [
              {
                  "name": "Bronze",
                  "description": "Bronze level description",
                  "id": 16,
                  "locale": "en"
              },
              {
                  "name": "Brązowy",
                  "description": "Opis poziomu brązowego",
                  "id": 17,
                  "locale": "pl"
              }
          ]
        },
      "specialRewards": [],
      "customersCount": 4
    },
        {
          "id": "e82c96cf-32a3-43bd-9034-4df343e5fd94",
          "name": "Silver",
          "description": "Example silver level",
          "active": true,
          "conditionValue": 20,
          "hasPhoto": false,
          "reward": {
            "name": "test reward",
            "value": 0.15,
            "code": "abc"
          },
          "specialRewards": [],
          "customersCount": 2,
          "translations": [
              {
                  "name": "Silver",
                  "description": "Example silver level",
                  "id": 16,
                  "locale": "en"
              },
              {
                  "name": "Srebrny",
                  "description": "Przykładowy poziom srebrny",
                  "id": 17,
                  "locale": "pl"
              }
          ]
        }
      ],
      "total": 2
    }


Create new level
----------------

To create a new level you will need to call the ``/api/level/create`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/level/create

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[translations][en][name]                  | request        |  Level name in given locale.                                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[active]                                  | request        |  *(optional)* Set 1 if active, otherwise 0                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[translations][en][description]           | request        |  *(optional)* Level description in given locale.                           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[conditionValue]                          | request        |  Condition value                                                           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[minOrder]                                | request        |  *(optional)* Minimum order value                                          |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[reward][name]                            | request        |  Reward name                                                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[reward][value]                           | request        |  Reward value                                                              |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[reward][code]                            | request        |  Reward code                                                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][active]                | request        |  *(optional)* Set 1 if active, otherwise 0                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][code]                  | request        |  First special reward code                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][name]                  | request        |  First special reward name                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][startAt]               | request        |  First special reward visible from YYYY-MM-DD HH:mm, for example           | 
|                                                |                |   ``2018-02-01 8:33``. *(required only if ``allTimeVisible=0``)*           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][endAt]                 | request        |  First special reward visible to YYYY-MM-DD HH:mm, for example             |
|                                                |                |   ``2017-10-15 11:07``. *(required only if ``allTimeVisible=0``)*          |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][value]                 | request        |  First special reward value                                                |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/level/create \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "level[translations][en][name]=Silver" \
        -d "level[active]=1" \
        -d "level[conditionValue]=4" \
        -d "level[minOrder]=1" \
        -d "level[translations][en][description]=Silver+description" \
        -d "level[reward][name]=reward4name" \
        -d "level[reward][value]=4" \
        -d "level[reward][code]=4" \
        -d "level[specialRewards][0][name]=specialreward4" \
        -d "level[specialRewards][0][value]=4" \
        -d "level[specialRewards][0][code]=4" \
        -d "level[specialRewards][0][active]=1" \
        -d "level[specialRewards][0][startAt]=2018-02-01+08:33" \
        -d "level[specialRewards][0][endAt]=2018-02-15+11:27"

.. note::
    To add new special reward for level you will need to add special reward.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "id": "46284528-de11-4049-af2e-d2540c6fd8c7"
    }



Get level details
-----------------

To retrieve the details of a level you will need to call the ``/api/level/{level}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/level/<level>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <level>       | query          | Id of the level                      |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the admin user with ``level = 000096cf-32a3-43bd-9034-4df343e5fd93`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/level/000096cf-32a3-43bd-9034-4df343e5fd93 \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "id": "000096cf-32a3-43bd-9034-4df343e5fd93",
      "name": "Gold",
      "description": "Gold level description",
      "active": true,
      "conditionValue": 0,
      "reward": {
        "name": "test reward",
        "value": 0.14,
        "code": "abc"
      },
      "specialRewards": [],
      "customersCount": 4,
      "translations": [
          {
              "name": "Gold",
              "description": "Gold level description",
              "id": 16,
              "locale": "en"
          },
          {
              "name": "Złoty",
              "description": "Opis poziomu złotego",
              "id": 17,
              "locale": "pl"
          }
      ]
    }


Edit existing level
-------------------

To edit existing level you will need to call the ``/api/level/<level>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/level/<level>

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <level>                                        | query          |  Level ID                                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[translations][en][name]                  | request        |  Level name in given locale.                                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[active]                                  | request        |  *(optional)* Set 1 if active, otherwise 0                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[translations][en][description]           | request        |  *(optional)* Level description in given locale                            |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[conditionValue]                          | request        |  Condition value                                                           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[minOrder]                                | request        |  *(optional)* Minimum order value                                          |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[reward][name]                            | request        |  Reward name                                                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[reward][value]                           | request        |  Reward value                                                              |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[reward][code]                            | request        |  Reward code                                                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][active]                | request        |  *(optional)* Set 1 if active, otherwise 0                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][code]                  | request        |  First special reward code                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][name]                  | request        |  First special reward name                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][startAt]               | request        |  First special reward visible from YYYY-MM-DD HH:mm, for example           | 
|                                                |                |  ``2018-02-01 8:33``. *(required only if ``allTimeVisible=0``)*            |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][endAt]                 | request        |  First special reward visible to YYYY-MM-DD HH:mm, for example             |
|                                                |                |    ``2017-10-15 11:07``. *(required only if ``allTimeVisible=0``)*         |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| level[specialRewards][][value]                 | request        |  First special reward value                                                |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^
To see the details of the admin user with ``level = c343a12d-b4dd-4dee-b2cd-d6fe1b021115`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/level/c343a12d-b4dd-4dee-b2cd-d6fe1b021115 \
        -X "PUT" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "level[translations][en][name]=Gold" \
        -d "level[active]=1" \
        -d "level[conditionValue]=3" \
        -d "level[minOrder]=3" \
        -d "level[translations][en][description]=gold-level-description" \
        -d "level[reward][name]=reward3xyzname" \
        -d "level[reward][value]=3" \
        -d "level[reward][code]=3" \
        -d "level[specialRewards][0][name]=special-reward-for-customer" \
        -d "level[specialRewards][0][value]=3" \
        -d "level[specialRewards][0][code]=3" \
        -d "level[specialRewards][0][active]=1" \
        -d "level[specialRewards][0][startAt]=2018-02-01+8:20" \
        -d "level[specialRewards][0][endAt]=2017-10-15+13:07"


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "id": "c343a12d-b4dd-4dee-b2cd-d6fe1b021115"
    }




Activate or deactivate level
----------------------------

To activate od deactivate level you will need to call the ``/api/level/<level>/activate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/level/<level>/activate

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <level>                                        | query          |  Level ID                                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| active                                         | query          |  Set 1 if active, otherwise 0                                              |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^
To see the activated user with ``level = c343a12d-b4dd-4dee-b2cd-d6fe1b021115`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/level/c343a12d-b4dd-4dee-b2cd-d6fe1b021115/activate \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content

.. code-block:: json

    active = 1




Get list of customers assigned to specific level
------------------------------------------------

To retrieve the list of customers assigned to level you will need to call the ``/api/level/{level}/customers`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/level/<level>/customers

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <level>       | query          | Id of the level                      |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the list of campaigns for a level with ID ``customer = 000096cf-32a3-43bd-9034-4df343e5fd93`` use the below method:

.. code-block:: bash
    
    curl http://localhost:8181/api/admin/level/000096cf-32a3-43bd-9034-4df343e5fd93/customers \
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
      "customers": [
        {
          "customerId": "e7306b21-0732-42e5-9f88-ccf311a0f43d",
          "firstName": "Tomasz",
          "lastName": "Test7",
          "email": "tomasztest7@wp.pl"
        },
        {
          "customerId": "b9af6a8c-9cc5-4924-989c-e4af614ab2a3",
          "firstName": "alina",
          "lastName": "test",
          "email": "qwe@test.pl"
        },
        {
          "customerId": "00000000-0000-474c-b092-b0dd880c07e2",
          "firstName": "Jane",
          "lastName": "Doe",
          "email": "user-temp@oloy.com"
        },
        {
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "firstName": "John",
          "lastName": "Doe",
          "email": "user@oloy.com"
        }
      ],
      "total": 4
    }


Get complete list of levels
---------------------------

To retrieve the complete list of levels you will need to call the ``/api/seller/level`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/level

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| page                 | query          | *(optional)* Start from page, by default 1             |
+----------------------+----------------+--------------------------------------------------------+
| perPage              | query          | *(optional)* Number of items to display per page,      |
|                      |                | by default = 10                                        |
+----------------------+----------------+--------------------------------------------------------+
| sort                 | query          | *(optional)* Sort by column name,                      |
|                      |                | by default = name                                      |
+----------------------+----------------+--------------------------------------------------------+
| direction            | query          | *(optional)* Direction of sorting [ASC, DESC],         |
|                      |                | by default = ASC                                       |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/seller/level \
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
      "levels": [
        {
          "id": "000096cf-32a3-43bd-9034-4df343e5fd94",
          "name": "Gold",
          "description": "Gold level description",
          "active": true,
          "conditionValue": 200,
          "hasPhoto": false,
          "reward": {
            "name": "test reward",
            "value": 0.2,
            "code": "abc"
          },
          "specialRewards": [
            {
              "name": "special reward 2",
              "value": 0.11,
              "code": "spec2",
              "id": "e82c96cf-32a3-43bd-9034-4df343e50094",
              "active": false,
              "createdAt": "2018-02-19T09:45:00+0100",
              "startAt": "2016-09-10T00:00:00+0200",
              "endAt": "2016-11-10T00:00:00+0100"
            },
            {
              "name": "special reward",
              "value": 0.22,
              "code": "spec",
              "id": "e82c96cf-32a3-43bd-9034-4df343e5fd00",
              "active": true,
              "createdAt": "2018-02-19T09:45:00+0100",
              "startAt": "2016-10-10T00:00:00+0200",
              "endAt": "2016-11-10T00:00:00+0100"
            }
          ],
          "customersCount": 1
        },
        {
          "id": "e82c96cf-32a3-43bd-9034-4df343e5fd94",
          "name": "Silver",
          "description": "Silver level description",
          "active": true,
          "conditionValue": 20,
          "hasPhoto": false,
          "reward": {
            "name": "test reward",
            "value": 0.15,
            "code": "abc"
          },
          "specialRewards": [],
          "customersCount": 1
        }
      ],
      "total": 2
    }



Get level details
-----------------

To retrieve level details you will need to call the ``/api/seller/level/<level>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/level/<level>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <level>       | query          | Id of the level                      |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the customer user with ``level = 000096cf-32a3-43bd-9034-4df343e5fd94`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/seller/level/000096cf-32a3-43bd-9034-4df343e5fd94 \
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
      "id": "000096cf-32a3-43bd-9034-4df343e5fd94",
      "name": "Gold",
      "description": "Gold level description",
      "active": true,
      "conditionValue": 200,
      "hasPhoto": false,
      "reward": {
        "name": "test reward",
        "value": 0.2,
        "code": "abc"
      },
      "specialRewards": [
        {
          "name": "special reward 2",
          "value": 0.11,
          "code": "spec2",
          "id": "e82c96cf-32a3-43bd-9034-4df343e50094",
          "active": false,
          "createdAt": "2018-02-19T09:45:00+0100",
          "startAt": "2016-09-10T00:00:00+0200",
          "endAt": "2016-11-10T00:00:00+0100"
        },
        {
          "name": "special reward",
          "value": 0.22,
          "code": "spec",
          "id": "e82c96cf-32a3-43bd-9034-4df343e5fd00",
          "active": true,
          "createdAt": "2018-02-19T09:45:00+0100",
          "startAt": "2016-10-10T00:00:00+0200",
          "endAt": "2016-11-10T00:00:00+0100"
        }
      ],
      "customersCount": 1
    }

Get level's photo
--------------------

To get level's photo you will need to cal the ``/api/level/<level>/photo`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/level/<level>/photo

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <level>       | query          | level ID                             |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To get level's photo ``level = 00096cf-32a3-43bd-9034-4df343e5fd94`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/level/00096cf-32a3-43bd-9034-4df343e5fd94/photo \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *level = 00096cf-32a3-43bd-9034-4df343e5fd94* id is an exemplary value. Your value can be different.
    Check in the list of all levels if you are not sure which id should be used.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. note::

    In the response you will get raw file content with a proper ``Content-Type`` header, for example:
    ``Content-Type: image/jpeg``.

Exemplary Response
^^^^^^^^^^^^^^^^^^

The level may not have photo at all and you will receive a below response.

.. code-block:: text

    STATUS: 404 Not Found

.. code-block:: json

    {
      "error": {
        "code": 404,
        "message": "Not Found"
      }
    }

Remove level's photo
-----------------------

To remove level's photo you will need to cal the ``/api/level/<level>/photo`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/level/<level>/photo

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <level>       | query          | level ID                             |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To remove level's photo ``level = 00096cf-32a3-43bd-9034-4df343e5fd94`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/level/00096cf-32a3-43bd-9034-4df343e5fd94/photo \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *level = 00096cf-32a3-43bd-9034-4df343e5fd94* id is an exemplary value. Your value can be different.
    Check in the list of all levels if you are not sure which id should be used.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

Add a photo to the level
---------------------------

To add a photo to the level you will need to cal the ``/api/level/<level>/photo`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/level/<level>/photo

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <level>       | query          | level ID                             |
+---------------+----------------+--------------------------------------+
| photo[file]   | request        | Absolute path to the photo           |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To get level's photo ``level = 00096cf-32a3-43bd-9034-4df343e5fd94`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/level/00096cf-32a3-43bd-9034-4df343e5fd94/photo \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "photo[file]=C:\fakepath\Photo.png"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    The *level = 00096cf-32a3-43bd-9034-4df343e5fd94* id is an exemplary value. Your value can be different.
    Check in the list of all levels if you are not sure which id should be used.

.. note::

    The *photo[file]=C:\fakepath\Photo.png* is an exemplary value. Your value can be different.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK
