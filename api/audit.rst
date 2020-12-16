Audit API
=========

These endpoints will allow you to see the list of actions taken in Open Loyalty.

Getting log
-----------

To retrieve the action log, you need to call the ``/api/audit/log`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/audit/log

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| entityType           | query          | *(optional)* Narrow results to given entity type       |
|                      |                | for example: ``customer``                              |
+----------------------+----------------+--------------------------------------------------------+
| eventType            | query          | *(optional)* Narrow results to given event type        |
|                      |                | for example: ``RegisterCustomer``                      |
+----------------------+----------------+--------------------------------------------------------+
| entityId             | query          | *(optional)* Narrow results to given entity ID         |
+----------------------+----------------+--------------------------------------------------------+
| username             | query          | *(optional)* Narrow results to given username          |
+----------------------+----------------+--------------------------------------------------------+
| auditLogId           | query          | *(optional)* Narrow results to given audit log ID      |
+----------------------+----------------+--------------------------------------------------------+
| createdAtFrom        | query          | *(optional)* For example ``2017-09-27``                |
+----------------------+----------------+--------------------------------------------------------+
| createdAtTo          | query          | *(optional)* For example ``2017-09-27``                |
+----------------------+----------------+--------------------------------------------------------+
| page                 | query          | *(optional)* Start from page, by default 1             |
+----------------------+----------------+--------------------------------------------------------+
| perPage              | query          | *(optional)* Number of items to display per page,      |
|                      |                | by default = 10                                        |
+----------------------+----------------+--------------------------------------------------------+
| sort                 | query          | *(optional)* Sort by column name,                      |
|                      |                | by default = firstName                                 |
+----------------------+----------------+--------------------------------------------------------+
| direction            | query          | *(optional)* Direction of sorting [ASC, DESC],         |
|                      |                | by default = ASC                                       |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/audit/log \
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
      "logs": [
        {
          "auditLogId": {
            "auditLogId": "916e963e-dd14-4ef8-849a-e5b54779657d"
          },
          "createdAt": "2017-09-21T13:54:05+0200",
          "eventType": "MoveCustomerToLevel",
          "entityType": "customer",
          "entityId": "00000000-0000-474c-b092-b0dd880c07e1",
          "username": "<notlogged>",
          "data": [
            "000096cf-32a3-43bd-9034-4df343e5fd93"
          ]
        },
        {
          "auditLogId": {
            "auditLogId": "1efe9c57-c42f-41a1-988c-c4f5b65382d8"
          },
          "createdAt": "2017-09-21T13:54:05+0200",
          "eventType": "RegisterCustomer",
          "entityType": "customer",
          "entityId": "00000000-0000-474c-b092-b0dd880c07e1",
          "username": "<notlogged>",
          "data": {
            "firstName": "John",
            "lastName": "Doe",
            "gender": "male",
            "phone": "11111",
            "email": "user@example.com",
            "birthDate": 653011200,
            "createdAt": 1470646394,
            "company": {
              "name": "test",
              "nip": "nip"
            },
            "loyaltyCardNumber": "000000",
            "address": {
              "street": "Dmowskiego",
              "address1": "21",
              "city": "Wrocław",
              "country": "pl",
              "postal": "50-300",
              "province": "Dolnośląskie"
            }
          }
        }
      ],
      "total": 92
    }

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/audit/log \
        -G \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "entityType=customer" \
        -d "page=2" \
        -d "perPage=2" \
        -d "sort=username" \
        -d "direction=DESC"

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "logs": [
        {
          "auditLogId": {
            "auditLogId": "b6781066-a292-4043-bd14-52998ee10691"
          },
          "createdAt": "2017-09-21T13:54:05+0200",
          "eventType": "ActivateCustomer",
          "entityType": "customer",
          "entityId": "00000000-0000-474c-b092-b0dd880c07e1",
          "username": "<notlogged>",
          "data": []
        },
        {
          "auditLogId": {
            "auditLogId": "4574e09b-280c-4e5d-bdd2-327589c714da"
          },
          "createdAt": "2017-09-21T13:54:05+0200",
          "eventType": "MoveCustomerToLevel",
          "entityType": "customer",
          "entityId": "00000000-0000-474c-b092-b0dd880c07e2",
          "username": "<notlogged>",
          "data": [
            "000096cf-32a3-43bd-9034-4df343e5fd93"
          ]
        }
      ],
      "total": 92
    }



Exporting the view
------------------

To export the audit logs view you need to call ``/api/audit/log/export`` endpoint with the ``GET`` method and the same parameters.
Pagination does not work in this endpoint, you can only sort the exported entries.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/audit/log/export

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| entityType           | query          | *(optional)* Narrow results to given entity type       |
|                      |                | for example: ``customer``                              |
+----------------------+----------------+--------------------------------------------------------+
| eventType            | query          | *(optional)* Narrow results to given event type        |
|                      |                | for example: ``RegisterCustomer``                      |
+----------------------+----------------+--------------------------------------------------------+
| entityId             | query          | *(optional)* Narrow results to given entity ID         |
+----------------------+----------------+--------------------------------------------------------+
| username             | query          | *(optional)* Narrow results to given username          |
+----------------------+----------------+--------------------------------------------------------+
| auditLogId           | query          | *(optional)* Narrow results to given audit log ID      |
+----------------------+----------------+--------------------------------------------------------+
| createdAtFrom        | query          | *(optional)* For example ``2017-09-27``                |
+----------------------+----------------+--------------------------------------------------------+
| createdAtTo          | query          | *(optional)* For example ``2017-09-27``                |
+----------------------+----------------+--------------------------------------------------------+
| sort                 | query          | *(optional)* Sort by column name,                      |
|                      |                | by default = firstName                                 |
+----------------------+----------------+--------------------------------------------------------+
| direction            | query          | *(optional)* Direction of sorting [ASC, DESC],         |
|                      |                | by default = ASC                                       |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/audit/log/export \
        -G \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "entityType=user" \
        -d "sort=username" \
        -d "direction=DESC"

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: csv

    "Log ID",Username,"User type","User ID","Event type","Entity type","Entity ID","Created at","Additional information",IP
    ff9817cd-f393-4e12-9319-4fe7207bd80b,admin,admin,22200000-0000-474c-b092-b0dd880c07e2,AuthenticationSuccess,user,,2020-03-13T12:12:58+01:00,[],172.22.0.1
    39e25450-0969-4b5e-82ff-d083e5b9c7e1,,admin,,AuthenticationFailure,user,,2020-03-13T12:12:29+01:00,[],172.22.0.1



Creating an archive
-------------------

To dump all audit log data older than a year counting from today's midnight into an archived file
in the server's archives storage, use ``/api/audit/log/archive`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/audit/log/archive

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| archive[beforeDate]  | request        | Date to which logs are archived                        |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/audit/log/archive \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "archive[beforeDate]=2019-03-10"

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "totalArchived": 92,
      "filename": "audit_log_archive_before_2019_05_20.xml"
    }

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "totalArchived": 0,
      'message': "No logs to archive from this time range. The file was not created."
    }

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "totalArchived": 0,
      "filename": "audit_log_archive_before_2019_05_20.xml",
      "message": "Archive for this date range has already been generated.",
    }



Getting an archive list
-----------------------

To retrieve all archived files in the server's archives storage, use ``/api/audit/log/archive`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/audit/log/archive

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/audit/log/archive \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "archives": [
        "audit_log_archive_before_2019_03_11.xml",
        "audit_log_archive_before_2019_05_20.xml"
      ],
      "total": 2
    }



Downloading an archive
----------------------

To download an archived file in the server's archives storage, use ``/api/audit/log/archive/{filename}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/audit/log/archive/<filename>

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <filename>           | query          | Archive file name, with .xml extension                 |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/audit/log/archive/audit_log_archive_before_2019_03_11.xml \
        -X "GET" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <log>
     <entry id="39e25450-0969-4b5e-82ff-d083e5b9c7e1" createdAt="2019-03-06T12:12:29+01:00">
      <user>admin</user>
      <userId>56a91360-1100-cc5c-83fe-c7199e88c723</userId>
      <userType>admin</userType>
      <event>AuthenticationFailure</event>
      <entityType>user</entityType>
      <entityId/>
      <data>[]</data>
      <origin>8.8.8.8</origin>
     </entry>
    </log>
