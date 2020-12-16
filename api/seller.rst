Seller API
==========

These endpoints will allow you to see the list of sellers in Open Loyalty.



Get list of sellers
-------------------

To retrieve a paginated list of sellers, you need to call the ``/api/<storeCode>/seller`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/seller

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <storeCode>          | query          | Code of the store to get sellers from.                 |
+----------------------+----------------+--------------------------------------------------------+
| firstName            | query          | *(optional)* First Name                                |
+----------------------+----------------+--------------------------------------------------------+
| lastName             | query          | *(optional)* Last Name                                 |
+----------------------+----------------+--------------------------------------------------------+
| phone                | query          | *(optional)* Phone                                     |
+----------------------+----------------+--------------------------------------------------------+
| email                | query          | *(optional)* E-mail                                    |
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

    curl http://localhost:8181/api/DEFAULT/seller \
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
      "sellers": [
        {
          "name": "John2 Doe2",
          "sellerId": "00000000-0000-474c-b092-b0dd880c07e5",
          "firstName": "John2",
          "lastName": "Doe2",
          "email": "john2@doe2.com",
          "phone": "0000000011",
          "posId": "00000000-0000-474c-1111-b0dd880c07e3",
          "posName": "test1",
          "posCity": "Warszawa",
          "active": true,
          "deleted": false
        },
        {
          "name": "John Doe",
          "sellerId": "00000000-0000-474c-b092-b0dd880c07e4",
          "firstName": "John",
          "lastName": "Doe",
          "email": "john@doe.com",
          "phone": "0000000011",
          "posId": "00000000-0000-474c-1111-b0dd880c07e2",
          "posName": "test2",
          "posCity": "Wrocław",
          "active": true,
          "deleted": false
        }
      ],
      "total": 2
    }



Register new seller
-------------------

To register a new seller, you need to call the ``/api/<storeCode>/seller/register`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/seller/register

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <storeCode>                                    | query          | Code of the store to register new seller in.                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[firstName]                              | request        |  First name                                                                |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[lastName]                               | request        |  Last name                                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[active]                                 | request        |  *(optional)* Set 1 if active, otherwise 0                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[email]                                  | request        |  E-mail                                                                    |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[phone]                                  | request        |  *(optional)* Phone                                                        |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[plainPassword]                          | request        |  Password                                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[posId]                                  | request        |  Type of POS                                                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/seller/register \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "seller[firstName]=John" \
        -d "seller[lastName]=Travolta" \
        -d "seller[active]=1" \
        -d "seller[email]=john@travolta.com" \
        -d "seller[phone]=999888777" \
        -d "seller[posId]=00000000-0000-474c-1111-b0dd880c07e3" \
        -d "seller[plainPassword]=admin123"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "sellerId": "8b6cf775-f87f-4150-b5f3-0e60e57e2678",
      "password": "admin123",
      "email": "john@travolta.com"
    }



Get seller details
------------------

To retrieve seller details, you need to call the ``/api/<storeCode>/seller/<seller>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/seller/<seller>


+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <storeCode>          | query          | Code of the store to get seller from.                  |
+----------------------+----------------+--------------------------------------------------------+
| <seller>             | query          | Seller ID                                              |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

To see the details of the seller user with id ``seller = 00000000-0000-474c-b092-b0dd880c07e4``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/seller/00000000-0000-474c-b092-b0dd880c07e4` \
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
      "name": "John Doe",
      "sellerId": "00000000-0000-474c-b092-b0dd880c07e4",
      "firstName": "John",
      "lastName": "Doe",
      "email": "john@doe.com",
      "phone": "0000000011",
      "posId": "00000000-0000-474c-1111-b0dd880c07e2",
      "posName": "test2",
      "posCity": "Wrocław",
      "active": true,
      "deleted": false
    }



Update seller details
---------------------

To fully update seller details for a user, you need to call the ``/api/<storeCode>/seller/<seller>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/<storeCode>/seller/<seller>

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <storeCode>                                    | query          | Code of the store the updated seller belongs to.                           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <seller>                                       | query          |  Seller ID                                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[firstName]                              | request        |  First name                                                                |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[lastName]                               | request        |  Last name                                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[active]                                 | request        |  *(optional)* Set 1 if active, otherwise 0                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[email]                                  | request        |  E-mail                                                                    |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[phone]                                  | request        |  *(optional)* Phone                                                        |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[plainPassword]                          | request        |  Password                                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| seller[posId]                                  | request        |  Type of POS                                                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/seller/00000000-0000-474c-b092-b0dd880c07e4 \
        -X "PUT" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "seller[firstName]=Jacek" \
        -d "seller[lastName]=Kowalski" \
        -d "seller[active]=0" \
        -d "seller[email]=jacek@kowalski.pl" \
        -d "seller[phone]=555444333" \
        -d "seller[posId]=00000000-0000-474c-1111-b0dd880c07e2" \
        -d "seller[plainPassword]=admin"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "sellerId": "00000000-0000-474c-b092-b0dd880c07e4"
    }



Activate seller
---------------

To activate a seller, you need to call the ``/api/<storeCode>/seller/<seller>/activate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/seller/<seller>/activate

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <storeCode>                                    | query          | Code of the store to activate the seller in.                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <seller>                                       | query          |  Seller ID                                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

To activate a seller user with id ``seller = 00000000-0000-474c-b092-b0dd880c07e4``, use the method below:


.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/seller/00000000-0000-474c-b092-b0dd880c07e4/activate \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)



Deactivate seller
-----------------

To deactivate a seller, you need to call the ``/api/<storeCode>/seller/<seller>/deactivate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/seller/<seller>/deactivate

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <storeCode>                                    | query          | Code of the store to deactivate seller in.                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <seller>                                       | query          |  Seller ID                                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

To deactivate a seller user with id ``seller = 00000000-0000-474c-b092-b0dd880c07e4``, use the method below:


.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/seller/00000000-0000-474c-b092-b0dd880c07e4/deactivate \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)


Delete seller
-------------

To delete a seller, you need to call the ``/api/<storeCode>/seller/<seller>/delete`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/seller/<seller>/delete

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <storeCode>                                    | query          | Code of the store the seller belongs to.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <seller>                                       | query          |  Seller ID                                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

To delete a seller user with id ``seller = 00000000-0000-474c-b092-b0dd880c07e4``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/seller/00000000-0000-474c-b092-b0dd880c07e4/delete \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)
