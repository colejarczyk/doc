Level API
=========

These endpoints will allow you to see the list of levels taken in Open Loyalty.



Get the complete list of levels
-------------------------------

To retrieve a paginated list of levels, you need to call the ``/api/<storeCode>/level`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/level

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <storeCode>          | query          | Code of the store to get levels of.                    |
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

    curl http://localhost:8181/api/DEFAULT/level \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    Translatable fields (name, description etc.) are returned in the given locale.


Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "levels": [
        {
          "levelId": "000096cf-32a3-43bd-9034-4df343e5fd93",
          "name": "Bronze",
          "description": "Bronze level description",
          "hasPhoto": false,
          "active": true,
          "conditionValue": 0,
          "reward": {
            "name": "test reward",
            "value": 0.14,
            "code": "abc"
          },
          "specialRewards": [],
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
        {
          "levelId": "e82c96cf-32a3-43bd-9034-4df343e5fd94",
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

.. note::

    There may be legacy key names in objects returned (``id``, ``customersCount``).
    These are deprecated and may be removed without further notice. Please don't use them in new applications.



Create a new level
------------------

To create a new level, you need to call the ``/api/<storeCode>/level/create`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/level/create

+--------------------------------------+----------------+--------------------------------------------------------------+
| Parameter                            | Parameter type | Description                                                  |
+======================================+================+==============================================================+
| Authorization                        | header         | Token received during authentication                         |
+--------------------------------------+----------------+--------------------------------------------------------------+
| <storeCode>                          | query          | Code of the store to create level in.                        |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[translations][en][name]        | request        | Level name in given locale.                                  |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[translations][en][description] | request        | *(optional)* Level description in given locale.              |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[active]                        | request        | *(optional)* Set 1 if active, otherwise 0                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[conditionValue]                | request        | Condition value                                              |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[minOrder]                      | request        | *(optional)* Minimum order value                             |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[reward][name]                  | request        | Reward name                                                  |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[reward][value]                 | request        | Reward value                                                 |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[reward][code]                  | request        | Reward code                                                  |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][active]      | request        | *(optional)* Set 1 if active, otherwise 0                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][code]        | request        | First special reward code                                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][name]        | request        | First special reward name                                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][startAt]     | request        | First special reward visible from YYYY-MM-DD HH:mm,          |
|                                      |                | for example ``2019-02-01 8:33``.                             |
|                                      |                | *(required only if ``allTimeVisible=0``)*                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][endAt]       | request        | First special reward visible to YYYY-MM-DD HH:mm,            |
|                                      |                | for example ``2019-10-15 11:07``.                            |
|                                      |                | *(required only if ``allTimeVisible=0``)*                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][value]       | request        | First special reward value                                   |
+--------------------------------------+----------------+--------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/level/create \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "level[translations][en][name]=Silver" \
        -d "level[translations][en][description]=Silver+description" \
        -d "level[active]=1" \
        -d "level[conditionValue]=4" \
        -d "level[minOrder]=1" \
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

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "levelId": "46284528-de11-4049-af2e-d2540c6fd8c7"
    }

.. note::

    There may be another, legacy key in the object returned (``id``).
    This ``id`` key is deprecated and may be removed without further notice.
    Please don't use it in new applications.



Get level details
-----------------

To retrieve the details of a level, you need to call the ``/api/<storeCode>/level/<level>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/level/<level>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <storeCode>   | query          | Code of the store to get level from. |
+---------------+----------------+--------------------------------------+
| <level>       | query          | Level ID                             |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the level with id ``level = 000096cf-32a3-43bd-9034-4df343e5fd93``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/level/000096cf-32a3-43bd-9034-4df343e5fd93 \
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
      "levelId": "000096cf-32a3-43bd-9034-4df343e5fd93",
      "name": "Gold",
      "description": "Gold level description",
      "hasPhoto": false,
      "active": true,
      "conditionValue": 0,
      "reward": {
        "name": "test reward",
        "value": 0.14,
        "code": "abc"
      },
      "specialRewards": [],
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

.. note::

    There may be legacy key names in the object returned (``id``, ``customersCount``).
    These are deprecated and may be removed without further notice. Please don't use them in new applications.



Edit existing level
-------------------

To edit an existing level, you need to call the ``/api/<storeCode>/level/<level>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/<storeCode>/level/<level>

+--------------------------------------+----------------+--------------------------------------------------------------+
| Parameter                            | Parameter type | Description                                                  |
+======================================+================+==============================================================+
| Authorization                        | header         | Token received during authentication                         |
+--------------------------------------+----------------+--------------------------------------------------------------+
| <storeCode>                          | query          | Code of the store the updated level belongs to.              |
+--------------------------------------+----------------+--------------------------------------------------------------+
| <level>                              | query          | Level ID                                                     |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[translations][en][name]        | request        | Level name in given locale.                                  |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[translations][en][description] | request        | *(optional)* Level description in given locale.              |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[active]                        | request        | *(optional)* Set 1 if active, otherwise 0                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[conditionValue]                | request        | Condition value                                              |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[minOrder]                      | request        | *(optional)* Minimum order value                             |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[reward][name]                  | request        | Reward name                                                  |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[reward][value]                 | request        | Reward value                                                 |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[reward][code]                  | request        | Reward code                                                  |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][active]      | request        | *(optional)* Set 1 if active, otherwise 0                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][code]        | request        | First special reward code                                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][name]        | request        | First special reward name                                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][startAt]     | request        | First special reward visible from YYYY-MM-DD HH:mm,          |
|                                      |                | for example ``2019-02-01 8:33``.                             |
|                                      |                | *(required only if ``allTimeVisible=0``)*                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][endAt]       | request        | First special reward visible to YYYY-MM-DD HH:mm,            |
|                                      |                | for example ``2019-10-15 11:07``.                            |
|                                      |                | *(required only if ``allTimeVisible=0``)*                    |
+--------------------------------------+----------------+--------------------------------------------------------------+
| level[specialRewards][][value]       | request        | First special reward value                                   |
+--------------------------------------+----------------+--------------------------------------------------------------+

Example
^^^^^^^
To change the level with id ``level = c343a12d-b4dd-4dee-b2cd-d6fe1b021115``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/level/c343a12d-b4dd-4dee-b2cd-d6fe1b021115 \
        -X "PUT" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "level[translations][en][name]=Gold" \
        -d "level[translations][en][description]=gold-level-description" \
        -d "level[active]=1" \
        -d "level[conditionValue]=3" \
        -d "level[minOrder]=3" \
        -d "level[reward][name]=reward3xyzname" \
        -d "level[reward][value]=3" \
        -d "level[reward][code]=3" \
        -d "level[specialRewards][0][name]=special-reward-for-customer" \
        -d "level[specialRewards][0][value]=3" \
        -d "level[specialRewards][0][code]=3" \
        -d "level[specialRewards][0][active]=1" \
        -d "level[specialRewards][0][startAt]=2018-02-01+8:20" \
        -d "level[specialRewards][0][endAt]=2017-10-15+13:07"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "levelId": "c343a12d-b4dd-4dee-b2cd-d6fe1b021115"
    }

.. note::

    There may be another, legacy key in the object returned (``id``).
    This ``id`` key is deprecated and may be removed without further notice.
    Please don't use it in new applications.



Activate or deactivate level
----------------------------

To activate or deactivate a level, you need to call the ``/api/<storeCode>/level/<level>/activate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/level/<level>/activate

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <storeCode>                                    | query          | Code of the store the level belongs to.                                    |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <level>                                        | query          |  Level ID                                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| active                                         | query          |  Set 1 if active, otherwise 0                                              |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^
To activate the level with id ``level = c343a12d-b4dd-4dee-b2cd-d6fe1b021115``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/level/c343a12d-b4dd-4dee-b2cd-d6fe1b021115/activate \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "active=1"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Delete a level
--------------

To remove a level from database, you need to call the ``/api/<storeCode>/level/<level>`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/<storeCode>/level/<level>

+---------------+----------------+-----------------------------------------+
| Parameter     | Parameter type | Description                             |
+===============+================+=========================================+
| Authorization | header         | Token received during authentication    |
+---------------+----------------+-----------------------------------------+
| <storeCode>   | query          | Code of the store the level belongs to. |
+---------------+----------------+-----------------------------------------+
| <level>       | query          | Level ID                                |
+---------------+----------------+-----------------------------------------+

Example
^^^^^^^

To remove the level with id ``level = 000096cf-32a3-43bd-9034-4df343e5fd93``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/level/000096cf-32a3-43bd-9034-4df343e5fd93 \
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



Get a list of customers assigned to specific level
--------------------------------------------------

To retrieve a list of customers assigned to a level, you need to call the ``/api/<storeCode>/level/<level>/customers`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/level/<level>/customers

+---------------+----------------+-----------------------------------------+
| Parameter     | Parameter type | Description                             |
+===============+================+=========================================+
| Authorization | header         | Token received during authentication    |
+---------------+----------------+-----------------------------------------+
| <storeCode>   | query          | Code of the store the level belongs to. |
+---------------+----------------+-----------------------------------------+
| <level>       | query          | Level ID                                |
+---------------+----------------+-----------------------------------------+

Example
^^^^^^^

To see the list of customers for the level with id ``level = 000096cf-32a3-43bd-9034-4df343e5fd93``, use the method below:

.. code-block:: bash
    
    curl http://localhost:8181/api/DEFAULT/admin/level/000096cf-32a3-43bd-9034-4df343e5fd93/customers \
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
          "email": "user-temp@example.com"
        },
        {
          "customerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "firstName": "John",
          "lastName": "Doe",
          "email": "user@example.com"
        }
      ],
      "total": 4
    }



Get level's photo
-----------------

To get a level's photo, you need to call the ``/api/<storeCode>/level/<level>/photo`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/level/<level>/photo

+---------------+----------------+-----------------------------------------+
| Parameter     | Parameter type | Description                             |
+===============+================+=========================================+
| Authorization | header         | Token received during authentication    |
+---------------+----------------+-----------------------------------------+
| <storeCode>   | query          | Code of the store the level belongs to. |
+---------------+----------------+-----------------------------------------+
| <level>       | query          | Level ID                                |
+---------------+----------------+-----------------------------------------+

Example
^^^^^^^

To get a photo of the level with id ``level = 00096cf-32a3-43bd-9034-4df343e5fd94``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/level/00096cf-32a3-43bd-9034-4df343e5fd94/photo \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *level = 00096cf-32a3-43bd-9034-4df343e5fd94* id is an example value. Your value may be different.
    Check the list of all levels if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. note::

    In the response you will get a raw file content with a proper ``Content-Type`` header, for example:
    ``Content-Type: image/jpeg``.

Example Response
^^^^^^^^^^^^^^^^^^

The level may not have a photo at all. In that case, you will receive the following response:

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

To remove a photo of a level, you need to call the ``/api/<storeCode>/level/<level>/photo`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/<storeCode>/level/<level>/photo

+---------------+----------------+--------------------------------------------+
| Parameter     | Parameter type | Description                                |
+===============+================+============================================+
| Authorization | header         | Token received during authentication       |
+---------------+----------------+--------------------------------------------+
| <storeCode>   | query          | Code of the store the level belongs to.    |
+---------------+----------------+--------------------------------------------+
| <level>       | query          | Level ID                                   |
+---------------+----------------+--------------------------------------------+

Example
^^^^^^^

To remove a photo for the level ``level = 00096cf-32a3-43bd-9034-4df343e5fd94``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/level/00096cf-32a3-43bd-9034-4df343e5fd94/photo \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *level = 00096cf-32a3-43bd-9034-4df343e5fd94* id is an example value. Your value may be different.
    Check in the list of all levels if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK



Add a photo to a level
----------------------

To add a photo to a level, you need to call the ``/api/<storeCode>/level/<level>/photo`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/level/<level>/photo

+---------------+----------------+-----------------------------------------+
| Parameter     | Parameter type | Description                             |
+===============+================+=========================================+
| Authorization | header         | Token received during authentication    |
+---------------+----------------+-----------------------------------------+
| <storeCode>   | query          | Code of the store the level belongs to. |
+---------------+----------------+-----------------------------------------+
| <level>       | query          | Level ID                                |
+---------------+----------------+-----------------------------------------+
| photo[file]   | request        | Absolute path to the photo              |
+---------------+----------------+-----------------------------------------+

Example
^^^^^^^

To get a photo for the level ``level = 00096cf-32a3-43bd-9034-4df343e5fd94``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/level/00096cf-32a3-43bd-9034-4df343e5fd94/photo \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "photo[file]=C:\fakepath\Photo.png"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    The *level = 00096cf-32a3-43bd-9034-4df343e5fd94* id is an example value. Your value may be different.
    Check in the list of all levels if you are not sure which id should be used.

.. note::

    The *photo[file]=C:\fakepath\Photo.png* is an example value. Your value may be different.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK
