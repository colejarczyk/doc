Invitation
==========

These endpoints will allow you to easily manage Invitations.


Get a complete list of invitations
----------------------------------

To retrieve a paginated list of invitations, you need to call the ``/api/<storeCode>/invitations`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/<storeCode>/invitations

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                         | query          | Code of the store to get invitations list from.   |
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

    curl http://localhost:8181/api/DEFAULT/invitations \
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
      "invitations": [
        {
          "referrerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "recipientId": "",
          "invitationId": "22200000-0000-474c-b092-b0dd880c07e2",
          "referrerEmail": "user@example.com",
          "referrerName": "John Doe",
          "recipientEmail": "test2@example.com",
          "status": "invited",
          "token": "8e3889f08265ec0c81e511e23cab94200a7d18b7"
        },
        {
          "referrerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "recipientId": "",
          "invitationId": "22200000-0000-474c-b092-b0dd880c07e3",
          "referrerEmail": "user@example.com",
          "referrerName": "John Doe",
          "recipientEmail": "test3@example.com",
          "status": "invited",
          "token": "575c0f0435d0970853b25b967378c4155c8c0843"
        },
        {
          "referrerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "recipientId": "",
          "invitationId": "22200000-0000-474c-b092-b0dd880c07e1",
          "referrerEmail": "user@example.com",
          "referrerName": "John Doe",
          "recipientEmail": "test1@example.com",
          "status": "invited",
          "token": "ebea0309e2ca40f45b11537694270df8fc7161b7"
        },
        {
          "referrerId": "00000000-0000-474c-b092-b0dd880c07e1",
          "recipientId": "",
          "invitationId": "22200000-0000-474c-b092-b0dd880c07e4",
          "referrerEmail": "user@example.com",
          "referrerName": "John Doe",
          "recipientEmail": "test4@example.com",
          "status": "invited",
          "token": "1042654f4acd5099f54286acbb10d668173a95d0"
        }
      ],
      "total": 4
    }