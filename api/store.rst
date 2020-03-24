Store API
=========

These endpoints will allow you to see the list of stores in Open Loyalty.


Get store details
-----------------

To retrieve the details of a store, you need to call the ``/api/store/{store}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/store/<store>

+---------------+----------------+----------------------------------------------------+
| Parameter     | Parameter type | Description                                        |
+===============+================+====================================================+
| Authorization | header         | Token received during authentication               |
+---------------+----------------+----------------------------------------------------+
| <store>       | query          | Store Id                                           |
+---------------+----------------+----------------------------------------------------+

Example
^^^^^^^

To see the details of the store with id ``store = cbc362ae-aa53-46d2-bc98-422ab249ac0b``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/store/cbc362ae-aa53-46d2-bc98-422ab249ac0b \
        -X "GET" \ 
	    -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    Translatable fields (name, short description, etc.) are returned in the given locale.

.. note::

    The *cbc362ae-aa53-46d2-bc98-422ab249ac0b* id is an example value. Your value may be different.
    Check the list of all admin users if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json
    {
        "storeId": "cbc362ae-aa53-46d2-bc98-422ab249ac0b",
        "code": "UK3",
        "currency": "EUR",
        "name": "Store3",
        "active": true
	}

Update a store
--------------

To update a store, you need to call the ``/api/store/{store}`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/store/<store>

+---------------+----------------+----------------------------------------------------+
| Parameter     | Parameter type | Description                                        |
+===============+================+====================================================+
| Authorization | header         | Token received during authentication               |
+---------------+----------------+----------------------------------------------------+
| <store>       | query          | Store Id                                           |
+---------------+----------------+----------------------------------------------------+
| store[name]   | query          | Store name                                         |
+---------------+----------------+----------------------------------------------------+
| store[active] | query          | Store activity, possible values: active/inactive   |
+-- ------------+----------------+----------------------------------------------------+


Example
^^^^^^^

To update a store with id ``store = cbc362ae-aa53-46d2-bc98-422ab249ac0b``, use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/store/cbc362ae-aa53-46d2-bc98-422ab249ac0b \
        -X "PUT" \ 
	    -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
		-d "store[name] = store_name" \
		-d "store[active] = 0"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

    Translatable fields (name, short description etc.) are returned in the given locale.

.. note::

    The *cbc362ae-aa53-46d2-bc98-422ab249ac0b* id is an example value. Your value may be different.
    Check the list of all admin users if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 OK

.. code-block:: json
    (no content)


Get a collection of stores
--------------------------

To retrieve a paginated list of stores, you need to call the ``/api/store`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/store

+-------------------------------------+----------------+----------------------------------------------------+
| Parameter                           | Parameter type | Description                                        |
+=====================================+================+====================================================+
| Authorization                       | header         | Token received during authentication               |
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
| active                              | query          | *(optional)* Filter by activity                    |
+-------------------------------------+----------------+----------------------------------------------------+
| name                                | query          | *(optional)* Filter by name                        |
+-------------------------------------+----------------+----------------------------------------------------+

To see the first page of all campaigns, use the method below:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/store \
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
    "stores": [
        {
            "storeId": "484635af-cc11-48ae-bf19-8afbe5f31fc7",
            "code": "DEF_STORE",
            "currency": "EUR",
            "name": "Default store",
            "active": true
        },
        {
            "storeId": "cbc362ae-aa53-46d2-bc98-422ab249ac0b",
            "code": "UK3",
            "currency": "EUR",
            "name": "Store3",
            "active": true
        }
    ],
    "total": 2
    }


Create a new store
------------------

To create a new store, you need to call the ``/api/store`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/store

+-------------------------------------+----------------+----------------------------------------------------+
| Parameter                           | Parameter type | Description                                        |
+=====================================+================+====================================================+
| Authorization                       | header         | Token received during authentication               |
+-------------------------------------+----------------+----------------------------------------------------+
| store[code]                         | query          | Store code                                         |
+-------------------------------------+----------------+----------------------------------------------------+
| store[name]                         | query          | Store name                                         |
+-------------------------------------+----------------+----------------------------------------------------+
| store[currency]                     | query          | Store currency                                     |
+-------------------------------------+----------------+----------------------------------------------------+
| store[active]                       | query          | Store activity, possible values: active/inactive   |
+-------------------------------------+----------------+----------------------------------------------------+


To create a new store, use the method below:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/store \
        -X "POST" \
		-H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
		-d "store[active] = 1" \
        -d "store[name] = store_name" \
        -d "store[currency] = EUR" \
        -d "store[code] = store_code"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.


Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json
    {
        "storeId": "cbc362ae-aa53-46d2-bc98-422ab249ac0b"
    }
