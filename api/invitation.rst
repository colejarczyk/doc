Invitation
==========

These endpoints will allow you to easily manage Invitations.


Get a complete list of invitations
----------------------------------

To retrieve a paginated list of invitations you will need to call the ``/api/invitations`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/invitations

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| referrerId                          | query          | *(optional)* Referrer ID                          |
+-------------------------------------+----------------+---------------------------------------------------+
| referrerEmail                       | query          | *(optional)* Referrer Email                       |
+-------------------------------------+----------------+---------------------------------------------------+
| referrerName                        | query          | *(optional)* Referrer Name                        |
+-------------------------------------+----------------+---------------------------------------------------+
| recipientId                         | query          | *(optional)* Recipient ID                         |
+-------------------------------------+----------------+---------------------------------------------------+
| recipientEmail                      | query          | *(optional)* Recipient Email                      |
+-------------------------------------+----------------+---------------------------------------------------+
| recipientPhone                      | query          | *(optional)* Recipient Phone                      |
+-------------------------------------+----------------+---------------------------------------------------+
| recipientName                       | query          | *(optional)* Recipient Name                       |
+-------------------------------------+----------------+---------------------------------------------------+
| status                              | query          | *(optional)* Possible values: All, Invited,       |
|                                     |                | Made purchase, Registered                         |
+-------------------------------------+----------------+---------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/invitations \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.


Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "invitations": [
        {
          "referrerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "recipientId": "",
          "invitationId": "22200000-0000-474c-b092-b0dd880c07e2",
          "referrerEmail": "user@oloy.com",
          "referrerName": "John Doe",
          "recipientEmail": "test2@oloy.com",
          "status": "invited",
          "token": "8e3889f08265ec0c81e511e23cab94200a7d18b7"
        },
        {
          "referrerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "recipientId": "",
          "invitationId": "22200000-0000-474c-b092-b0dd880c07e3",
          "referrerEmail": "user@oloy.com",
          "referrerName": "John Doe",
          "recipientEmail": "test3@oloy.com",
          "status": "invited",
          "token": "575c0f0435d0970853b25b967378c4155c8c0843"
        },
        {
          "referrerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "recipientId": "",
          "invitationId": "22200000-0000-474c-b092-b0dd880c07e1",
          "referrerEmail": "user@oloy.com",
          "referrerName": "John Doe",
          "recipientEmail": "test1@oloy.com",
          "status": "invited",
          "token": "ebea0309e2ca40f45b11537694270df8fc7161b7"
        },
        {
          "referrerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "recipientId": "",
          "invitationId": "22200000-0000-474c-b092-b0dd880c07e4",
          "referrerEmail": "user@oloy.com",
          "referrerName": "John Doe",
          "recipientEmail": "test4@oloy.com",
          "status": "invited",
          "token": "1042654f4acd5099f54286acbb10d668173a95d0"
        }
      ],
      "total": 4
    }


Send invitation to customer
---------------------------

To send invitation to recipient you will need to call the ``/api/invitation/invite`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/invitation/invite

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| invitation[type]                               | query          | Recipient type (mobile, email)                                             |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| invitation[recipientPhone]                     | query          | Required if type is mobile                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| invitation[recipientEmail]                     | query          | Required if type is email                                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/invitation/invite \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "translation[type]=email" \
        -d "translation[recipientEmail]=smith@example.com"

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK
