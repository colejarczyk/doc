POS API
=======

These endpoints will allow you to see the list of POS taken in the Open Loyalty.

Get the complete list of POS
----------------------------

To retrieve a complete list of POS you will need to call the ``/api/pos`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/pos

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

    curl http://localhost:8181/api/pos \
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
      "pos": [
        {
          "posId": "00000000-0000-474c-1111-b0dd880c07e2",
          "name": "test2",
          "identifier": "pos1",
          "description": "test",
          "location": {
            "street": "Dmowskiego",
            "address1": "21",
            "province": "Dolnośląskie",
            "city": "Wrocław",
            "postal": "50-300",
            "country": "PL",
            "geoPoint": {
              "lat": "51.1170364",
              "long": "17.0203959"
            }
          },
          "transactionsAmount": 133.4,
          "transactionsCount": 3,
          "currency": "eur"
        },
        {
          "posId": "00000000-0000-474c-1111-b0dd880c07e3",
          "name": "test1",
          "identifier": "pos2",
          "description": "test",
          "location": {
            "street": "Dmowskiego",
            "address1": "21",
            "province": "Dolnośląskie",
            "city": "Warszawa",
            "postal": "50-300",
            "country": "PL",
            "geoPoint": {
              "lat": "51.1170364",
              "long": "17.0203959"
            }
          },
          "transactionsAmount": 0,
          "transactionsCount": 0,
          "currency": "eur"
        }
      ],
      "total": 2
    }

Create new POS
--------------

To create a new POS you will need to call the ``/api/pos`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/pos


+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         |  Token received during authentication                                      |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[name]                                      | request        |  POS name                                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[identifier]                                | request        |  POS Identifier                                                            |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[description]                               | request        |  *(optional)* A short description                                          |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][street]                          | request        |  Street for POS Location                                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][address1]                        | request        |  Address1 for POS Location                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][address2]                        | request        |  *(optional)* Address2 for POS Location                                    |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][postal]                          | request        |  Post code for POS Location                                                |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][city]                            | request        |  City for POS Location                                                     |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][province]                        | request        |  Province for POS Location                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][country]                         | request        |  Country for POS Location                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][lat]                             | request        |  *(optional)* Latitude for POS Location                                    |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][long]                            | request        |  *(optional)* Longitude for POS Location                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

   curl http://localhost:8181/api/pos \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "pos[name]=testname" \
        -d "pos[identifier]=testid" \
        -d "pos[description]=testdescription" \
        -d "pos[location][street]=polna" \
        -d "pos[location][address1]=24" \
        -d "pos[location][address2]=5" \
        -d "pos[location][postal]=98-765" \
        -d "pos[location][city]=Wroclaw" \
        -d "pos[location][province]=WroclawProvince" \
        -d "pos[location][country]=Poland" \
        -d "pos[location][lat]=latitude" \
        -d "pos[location][long]=longitude"

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "posId": "fe28cf15-9c95-46ee-bc7a-c40b2f2f0d40"
    }


Get POS details
---------------

To retrieve the POS details you will need to call the ``/api/pos/identifier/{pos}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/pos/identifier/<pos>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <pos>         | query          | POS identifier                       |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the admin user with ``pos = testid9`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/identifier/testid9 \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "posId": "6235a987-1639-420f-8001-537f0f2eeafa",
      "name": "test9",
      "identifier": "testid9",
      "description": "test9description",
      "location": {
        "street": "topolowa",
        "address1": "9",
        "address2": "1",
        "province": "Warsaw",
        "city": "Warsaw",
        "postal": "99-999",
        "country": "PL"
      },
      "transactionsAmount": 0,
      "transactionsCount": 0,
      "currency": "eur"
    }



Get POS details
---------------

To retrieve the POS details you will need to call the ``/api/pos/{pos}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/pos/<pos>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <pos>         | query          | POS identifier                       |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the admin user with ``pos = 00000000-0000-474c-1111-b0dd880c07e3`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/pos/00000000-0000-474c-1111-b0dd880c07e3 \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "posId": "00000000-0000-474c-1111-b0dd880c07e3",
      "name": "test1",
      "identifier": "pos2",
      "description": "test",
      "location": {
        "street": "Dmowskiego",
        "address1": "21",
        "province": "Dolnośląskie",
        "city": "Warszawa",
        "postal": "50-300",
        "country": "PL",
        "geoPoint": {
          "lat": "51.1170364",
          "long": "17.0203959"
        }
      },
      "transactionsAmount": 0,
      "transactionsCount": 0,
      "currency": "eur"
    }



Update POS data
---------------

To update the POS data you will need to call the ``/api/pos/<pos>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/pos/<pos>

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         |  Token received during authentication                                      |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <pos>                                          | query          |  POS ID                                                                    |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[name]                                      | request        |  POS name                                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[identifier]                                | request        |  POS Identifier                                                            |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[description]                               | request        |  *(optional)* A short description                                          |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][street]                          | request        |  Street for POS Location                                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][address1]                        | request        |  Building name for POS Location                                            |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][address2]                        | request        |  *(optional)* Flat/Unit name for POS Location                              |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][postal]                          | request        |  Post code for POS Location                                                |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][city]                            | request        |  City for POS Location                                                     |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][province]                        | request        |  Province for POS Location                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][country]                         | request        |  Country for POS Location                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][lat]                             | request        |  *(optional)* Latitude for POS Location                                    |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| pos[location][long]                            | request        |  *(optional)* Longitude for POS Location                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^
 
 To fully update POS with ``id = 857b2a26-b490-4356-8828-e138deaf7912`` use the below method:
 
.. code-block:: bash

    curl http://localhost:8181/api/pos/857b2a26-b490-4356-8828-e138deaf7912 \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "pos[name]=test8" \
        -d "pos[identifier]=testid8" \
        -d "pos[description]=test8description" \
        -d "pos[location][street]=kwiatowa" \
        -d "pos[location][address1]=66" \
        -d "pos[location][address2]=33" \
        -d "pos[location][postal]=666-333" \
        -d "pos[location][city]=Honolulu" \
        -d "pos[location][province]=HonululuProvince" \
        -d "pos[location][country]=USA" \
        -d "pos[location][lat]=latitude8" \
        -d "pos[location][long]=longitude8"


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "posId": "857b2a26-b490-4356-8828-e138deaf7912"
    }


Get complete list of POS
------------------------

To retrieve the complete list of POS you will need to call the ``/api/seller/pos`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/pos


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


    curl http://localhost:8181/api/seller/pos \
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
      "pos": [
        {
          "posId": "857b2a26-b490-4356-8828-e138deaf7912",
          "name": "test8",
          "identifier": "testid8",
          "description": "test8description",
          "location": {
            "street": "kwiatowa",
            "address1": "66",
            "address2": "33",
            "province": "HonululuProvince",
            "city": "Honolulu",
            "postal": "666-333",
            "country": "USA",
            "geoPoint": {
              "lat": "latitude8",
              "long": "longitude8"
            }
          },
          "transactionsAmount": 0,
          "transactionsCount": 0,
          "currency": "eur"
        },
        {
          "posId": "f4441dc1-9788-4763-838e-f034afd51c31",
          "name": "testname",
          "identifier": "testid",
          "description": "testdescription",
          "location": {
            "street": "polna",
            "address1": "24",
            "address2": "5",
            "province": "WroclawProvince",
            "city": "Wroclaw",
            "postal": "98-765",
            "country": "Poland",
            "geoPoint": {
              "lat": "latitude",
              "long": "longitude"
            }
          },
          "transactionsAmount": 0,
          "transactionsCount": 0,
          "currency": "eur"
        }
      ],
      "total": 2
    }

Get POS details
---------------

To retrieve POS details you will need to call the ``/api/seller/pos/<pos>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/seller/pos/<pos>

+---------------+----------------+--------------------------------------+
| Parameter     | Parameter type | Description                          |
+===============+================+======================================+
| Authorization | header         | Token received during authentication |
+---------------+----------------+--------------------------------------+
| <pos>         | query          | POS Id                               |
+---------------+----------------+--------------------------------------+

Example
^^^^^^^

To see the details of the customer user with ``pos = 857b2a26-b490-4356-8828-e138deaf7912`` use the below method:

.. code-block:: bash

 curl http://localhost:8181/api/seller/pos/857b2a26-b490-4356-8828-e138deaf7912 \
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
      "posId": "857b2a26-b490-4356-8828-e138deaf7912",
      "name": "test8",
      "identifier": "testid8",
      "description": "test8description",
      "location": {
        "street": "kwiatowa",
        "address1": "66",
        "address2": "33",
        "province": "HonululuProvince",
        "city": "Honolulu",
        "postal": "666-333",
        "country": "USA",
        "geoPoint": {
          "lat": "latitude8",
          "long": "longitude8"
        }
      },
      "transactionsAmount": 0,
      "transactionsCount": 0,
      "currency": "eur"
    }
