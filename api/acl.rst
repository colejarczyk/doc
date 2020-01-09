ACL API
=======

These endpoints will allow you to easily manage ACL for administrator.

Creating an role
----------------

To create a new role you will need to call the ``/api/admin/acl/role`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/admin/acl/role

+------------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                      |
+====================================+================+===================================================================+
| Authorization                      | header         |  Token received during authentication                             |
+------------------------------------+----------------+-------------------------------------------------------------------+
| role[name]                         | request        |  Name                                                             |
+------------------------------------+----------------+-------------------------------------------------------------------+
| role[permissions][][resource]      | request        |  Permission resource                                              |
+------------------------------------+----------------+-------------------------------------------------------------------+
| role[permissions][][access]        | request        |  Permission access type (MODIFY, VIEW)                            |
+------------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

To create a new role use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/role \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "role[name]=Super admin" \
        -d "role[permissions][0]['resource']=LEVEL" \
        -d "role[permissions][0]['access']=MODIFY" \
        -d "role[permissions][1]['resource']=EARNING_RULE" \
        -d "role[permissions][1]['access']=MODIFY" \

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 OK

Getting a single role
---------------------

To retrieve the details of a role you will need to call the ``/api/admin/acl/role/{role}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/data/<admin>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <role>        | query          | Id of the role                       |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the admin user with ``role = 37`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/role/37
        -X "GET" -H "Accept: application/json"
        -H "Content-type: application/x-www-form-urlencoded"
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "id": 38,
        "name": "Reporter admin",
        "role": "ROLE_ADMIN",
        "master": false,
        "permissions": [
            {
                "id": 57,
                "resource": "EARNING_RULE",
                "access": "VIEW"
            },
            {
                "id": 56,
                "resource": "SEGMENT_EXPORT",
                "access": "VIEW"
            },
            {
                "id": 55,
                "resource": "LEVEL",
                "access": "VIEW"
            }
        ]
    }

.. note::

    The *37* id is an exemplary value. Your value can be different.

Collection of available roles
-----------------------------

To retrieve a list of roles you will need to call the ``/api/admin/acl/role`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/acl/role

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+

To see the list of available roles use the below method:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/role \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "roles": [
        {
          "id": 37,
          "name": "Super admin",
          "role": "ROLE_ADMIN",
          "master": true,
          "permissions": []
        },
        {
          "id": 38,
          "name": "Reporter admin",
          "role": "ROLE_ADMIN",
          "master": false,
          "permissions": [
            {
              "id": 57,
              "resource": "EARNING_RULE",
              "access": "VIEW"
            },
            {
              "id": 56,
              "resource": "SEGMENT_EXPORT",
              "access": "VIEW"
            },
            {
              "id": 55,
              "resource": "LEVEL",
              "access": "VIEW"
            }
          ]
        }
      ],
      "total": 2
    }

Updating a role
---------------

To update a role you will need to call the ``/api/admin/acl/role/<role>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/admin/acl/role/<role>

+------------------------------------+----------------+-------------------------------------------------------------------+
| Parameter                          | Parameter type |  Description                                                      |
+====================================+================+===================================================================+
| Authorization                      | header         |  Token received during authentication                             |
+------------------------------------+----------------+-------------------------------------------------------------------+
| role[name]                         | request        |  Name                                                             |
+------------------------------------+----------------+-------------------------------------------------------------------+
| role[permissions][][resource]      | request        |  Permission resource                                              |
+------------------------------------+----------------+-------------------------------------------------------------------+
| role[permissions][][access]        | request        |  Permission access type (MODIFY, VIEW)                            |
+------------------------------------+----------------+-------------------------------------------------------------------+

Example
^^^^^^^

 To update the role with ``id = 37`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/role/37 \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -X "PUT" \
        -d "role[name]=Super admin" \
        -d "role[permissions][0]['resource']=LEVEL" \
        -d "role[permissions][0]['access']=MODIFY" \
        -d "role[permissions][1]['resource']=EARNING_RULE" \
        -d "role[permissions][1]['access']=MODIFY" \

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 OK

Collection of available resources
---------------------------------

To retrieve a list of available resources you will need to call the ``/api/admin/acl/resources`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/acl/resources

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+

To see the list of available resources use the below method:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/resources \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "resources": [
        {
          "code": "SEGMENT_EXPORT",
          "name": "Utilities"
        },
        {
          "code": "EARNING_RULE",
          "name": "Earning rules"
        },
        {
          "code": "LEVEL",
          "name": "Levels"
        }
      ],
      "total": 3
    }

Collection of available accesses
--------------------------------

To retrieve a list of available accesses types you will need to call the ``/api/admin/acl/accesses`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/acl/accesses

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+

To see the list of available accesses use the below method:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/resources \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "accesses": [
        {
          "code": "VIEW",
          "name": "View"
        },
        {
          "code": "MODIFY",
          "name": "Modify"
        }
      ],
      "total": 2
    }
