ACL API
=======

These endpoints will allow you to easily manage ACL for administrator.

Creating an role
----------------

To create a new role you need to call the ``/api/admin/acl/role`` endpoint with the ``POST`` method.

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

To create a new role use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/role \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "role[name]=Super admin" \
        -d "role[permissions][0][resource]=LEVEL" \
        -d "role[permissions][0][access]=MODIFY" \
        -d "role[permissions][1][resource]=EARNING_RULE" \
        -d "role[permissions][1][access]=MODIFY"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Getting a single role
---------------------

To retrieve the details of a role you need to call the ``/api/admin/acl/role/{role}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/acl/role/<role>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <role>        | query          | Id of the role                       |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the admin user with ``role = 37`` use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/role/37
        -X "GET" -H "Accept: application/json"
        -H "Content-type: application/x-www-form-urlencoded"
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "id": 37,
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

    The *37* id is an example value. Your value can be different.

Collection of available roles
-----------------------------

To retrieve a list of roles you need to call the ``/api/admin/acl/role`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/acl/role

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+

To see the list of available roles use the method below:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/role \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."
        
.. note::

   The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
   Your value can be different. Read more about Authorization :doc:`here </api/authorization>`.
    

Example Response
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

To update a role you need to call the ``/api/admin/acl/role/<role>`` endpoint with the ``PUT`` method.

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

 To update the role with ``id = 37`` use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/role/37 \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -X "PUT" \
        -d "role[name]=Super admin" \
        -d "role[permissions][0][resource]=LEVEL" \
        -d "role[permissions][0][access]=MODIFY" \
        -d "role[permissions][1][resource]=EARNING_RULE" \
        -d "role[permissions][1][access]=MODIFY" \

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 No Content



Collection of available resources
---------------------------------

To retrieve a list of available resources you need to call the ``/api/admin/acl/resources`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/acl/resources

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+

To see the list of available resources use the method below:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/resources \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
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

To retrieve a list of available accesses types you need to call the ``/api/admin/acl/accesses`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/admin/acl/accesses

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+

To see the list of available accesses use the method below:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/accesses \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
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
    
  
Deleting a single role
----------------------

To delete specific role you need to call the ``/api/admin/acl/role/{role}`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/admin/acl/role/{role}

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <role>        | query          | Id of the role                       |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/admin/acl/role/37
        -X "DELETE" -H "Accept: application/json"
        -H "Content-type: application/x-www-form-urlencoded"
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    204 No Content

.. note::

    The *37* id is an example value. Your value can be different.
