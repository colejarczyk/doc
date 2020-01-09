Utility API
===========

These endpoints will allow you to see the csv taken in the Open Loyalty.

Get csv with customers assigned to specific level
-------------------------------------------------

To retrieve a csv with customers assigned to level you will need to call the ``/api/csv/level/<level>`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/csv/level/<level>

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <level>                                        | query          |  Level ID                                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/csv/level/000096cf-32a3-43bd-9034-4df343e5fd93 \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    "First name","Last name","E-mail address",Gender,Telephone,"Loyalty card number",Birthdate,"Created at","Legal agreement","Marketing agreement","Data processing agreement"
    John,Doe,user@oloy.com,male,11111,,"1990-09-11 02:00:00","2016-08-08 10:53:14",,,
    Jane,Doe,user-temp@oloy.com,male,111112222,0000,"1990-09-11 02:00:00","2016-08-08 10:53:14",,,
    alina,test,qwe@test.pl,male,1212121212,,"2018-03-19 00:00:00","2018-02-19 14:24:18",1,,
    Tomasz,Test7,tomasztest7@wp.pl,,,,,"2018-02-20 08:21:39",1,,
    user,user,user@user.pl,male,123456789876543,,"2018-02-23 00:00:00","2018-02-23 13:29:11",1,,


Get csv with customers assigned to specific segment
---------------------------------------------------

To retrieve a csv with customers assigned to segment you will need to call the ``/api/csv/segment/<segment>`` endpoint with the ``GET`` method.


Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/csv/segment/<segment>

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <segment>            | query          | Segment ID                                             |
+----------------------+----------------+--------------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/csv/segment/63afec60-5e74-43fc-a5e1-81bbc03421ca \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    "First name","Last name","E-mail address",Gender,Telephone,"Loyalty card number",Birthdate,"Created at","Legal agreement","Marketing agreement","Data processing agreement"
