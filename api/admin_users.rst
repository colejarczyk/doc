Admin Users API
===============

These endpoints will allow you to easily manage admin users.

Creating an Admin User
----------------------

To create a new admin user you will need to call the ``/api/admin/data`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/data

+----------------------+----------------+-------------------------------------------------------------------+
| Parameter            | Parameter type |  Description                                                      |
+======================+================+===================================================================+
| Authorization        | header         | Token received during authentication                              |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[firstName]     | request        |  First name                                                       |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[lastName]      | request        |  Last name                                                        |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[phone]         | request        |  Phone number                                                     |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[email]         | request        |  E-mail address (required)                                        |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[plainPassword] | request        |  Plain password (required if admin[external]=0                    |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[external]      | request        |  Allows to define permanent token. Set 1 if true, otherwise 0     |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[apiKey]        | request        |  Permanent token (required if admin[external]=1                   |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[isActive]      | request        |  Set account active. Set 1 if active, otherwise 0                 |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[roles][]       | request        |  Role IDs assigned to this administrator (max 1 role)             |
+----------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

To create a new admin user use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/admin/data \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "admin[email]=administrator@example.com" \
        -d "admin[external]=0" \
        -d "admin[plainPassword]=password1234" \
        -d "admin[isActive]=1" \
        -d "admin[roles][0]=37"

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/data \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "form": {
        "children": {
          "firstName": {},
          "lastName": {},
          "phone": {},
          "email": {},
          "plainPassword": {},
          "external": {},
          "apiKey": {},
          "isActive": {}
        }
      },
      "errors": []
    }

Getting a Single Admin User
---------------------------

To retrieve the details of an admin user you will need to call the ``/api/admin/data/{admin}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/data/<admin>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <admin>       | query          | Id of the admin user                 |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the admin user with ``admin = 22200000-0000-474c-b092-b0dd880c07e2`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/admin/data/22200000-0000-474c-b092-b0dd880c07e2
        -X "GET" -H "Accept: application/json"
        -H "Content-type: application/x-www-form-urlencoded"
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "id": "22200000-0000-474c-b092-b0dd880c07e2",
      "username": "admin",
      "isActive": true,
      "createAt": "2017-09-21T13:54:04+0200",
      "email": "admin@oloy.com",
      "external": false,
      "dtype": "admin"
    }

.. note::

    The *22200000-0000-474c-b092-b0dd880c07e2* id is an exemplary value. Your value can be different.
    Check in the list of all admin users if you are not sure which id should be used.

Collection of Admin Users
-------------------------

To retrieve a paginated list of admin users you will need to call the ``/api/admin`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin

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
| sort                                | query          | *(optional)* Sort by column name,                 |
|                                     |                | by default = firstName                            |
+-------------------------------------+----------------+---------------------------------------------------+
| direction                           | query          | *(optional)* Direction of sorting [ASC, DESC],    |
|                                     |                | by default = ASC                                  |
+-------------------------------------+----------------+---------------------------------------------------+

To see the first page of all admin users use the below method:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "users": [
        {
          "id": "01b7a62a-640a-4c24-b182-c9f2852cae71",
          "username": "01b7a62a-640a-4c24-b182-c9f2852cae71",
          "isActive": true,
          "createAt": "2017-09-25T09:28:49+0200",
          "email": "administrator@example.com",
          "external": true,
          "apiKey": "customPernamentToken",
          "dtype": "admin",
          "roles": [
                {
                    "id": 38,
                    "name": "Reporter admin",
                    "role": "ROLE_ADMIN",
                    "master": false
                }
            ],
        },
        {
          "id": "22200000-0000-474c-b092-b0dd880c07e2",
          "username": "admin",
          "isActive": true,
          "createAt": "2017-09-21T13:54:04+0200",
          "email": "admin@oloy.com",
          "external": false,
          "dtype": "admin",
          "roles": [
                {
                    "id": 38,
                    "name": "Reporter admin",
                    "role": "ROLE_ADMIN",
                    "master": false
                }
            ],
        },
        {
          "id": "4383c58e-ff64-4e03-8364-5b716cb3e9e5",
          "username": "4383c58e-ff64-4e03-8364-5b716cb3e9e5",
          "isActive": true,
          "createAt": "2017-09-25T09:33:45+0200",
          "email": "administrato123r@example.com",
          "external": true,
          "apiKey": "customPernamentToken123",
          "dtype": "admin",
          "roles": [
                {
                    "id": 38,
                    "name": "Reporter admin",
                    "role": "ROLE_ADMIN",
                    "master": false
                }
            ],
        }
      ],
      "total": 3
    }

Updating an Admin User
----------------------

To fully update an admin user you will need to call the ``/api/admin/data/<admin>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/admin/data/<admin>

+----------------------+----------------+-------------------------------------------------------------------+
| Parameter            | Parameter type | Description                                                       |
+======================+================+===================================================================+
| Authorization        | header         | Token received during authentication                              |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[firstName]     | request        |  First name                                                       |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[lastName]      | request        |  Last name                                                        |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[phone]         | request        |  Phone number                                                     |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[email]         | request        |  E-mail address (required)                                        |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[plainPassword] | request        |  Plain password (required if admin[external]=0                    |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[external]      | request        |  Allows to define permanent token. Set 1 if true, otherwise 0     |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[apiKey]        | request        |  Permanent token (required if admin[external]=1                   |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[isActive]      | request        |  Set account active. Set 1 if active, otherwise 0                 |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[roles][]       | request        |  Role IDs assigned to this administrator (max 1 role)             |
+----------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

 To fully update the admin user with ``id = 22200000-0000-474c-b092-b0dd880c07e2`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/admin/data/01b7a62a-640a-4c24-b182-c9f2852cae71 \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -X "PUT" \
        -d "admin[firstName]=first+name" \
        -d "admin[lastName]=last+name" \
        -d "admin[phone]=00000000000" \
        -d "admin[email]=administrator@example.com" \
        -d "admin[plainPassword]=newPassword12!" \
        -d "admin[external]=0" \
        -d "admin[roles][0]=37"

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. warning::

    Remember, you must update the whole data of the admin user. If you don't want to change e-mail address, you must pass current
    value.

.. tip::

    It's not possible to delete an admin user. Set ``isActive=0`` if you want to disable access to the Open Loyalty.

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/data/01b7a62a-640a-4c24-b182-c9f2852cae71 \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -X "PUT"

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "form": {
        "children": {
          "firstName": {},
          "lastName": {},
          "phone": {},
          "email": {},
          "plainPassword": {},
          "external": {},
          "apiKey": {},
          "isActive": {}
        }
      },
      "errors": []
    }
