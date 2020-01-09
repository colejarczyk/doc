Segment API
===========

These endpoints will allow you to retrieve information and manage the segments used in your instance of Open Loyalty.



Get segments list
-----------------

To retrieve a paginated list of segments you need to call the ``/api/segment`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/segment

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

    curl http://localhost:8181/api/segment \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "segments": [
        {
          "segmentId": "00000000-0000-0000-0000-000000000005",
          "name": "transaction amount 10-50",
          "description": "desc",
          "active": false,
          "parts": [
            {
              "segmentPartId": "00000000-0000-0000-0000-000000000055",
              "criteria": [
                {
                  "criterionId": "00000000-0000-0000-0000-000000000055",
                  "fromAmount": 10,
                  "toAmount": 50,
                  "type": "transaction_amount"
                }
              ]
            }
          ],
          "createdAt": "2018-02-19T09:45:06+0100",
          "customersCount": 0
        },
        {
          "segmentId": "00000000-0000-0000-0000-000000000000",
          "name": "test",
          "description": "desc",
          "active": false,
          "parts": [
            {
              "segmentPartId": "00000000-0000-0000-0000-000000000000",
              "criteria": [
                {
                  "criterionId": "00000000-0000-0000-0000-000000000002",
                  "min": 10,
                  "max": 20,
                  "type": "transaction_count"
                },
                {
                  "criterionId": "00000000-0000-0000-0000-000000000001",
                  "fromAmount": 1,
                  "toAmount": 10000,
                  "type": "average_transaction_amount"
                },
                {
                  "criterionId": "00000000-0000-0000-0000-000000000000",
                  "posIds": [
                    "00000000-0000-474c-1111-b0dd880c07e2"
                  ],
                  "type": "bought_in_pos"
                }
              ]
            }
          ],
          "createdAt": "2018-02-19T09:45:06+0100",
          "customersCount": 0
        }
      ],
      "total": 2
    }



Create new segment
------------------

To create a new segment you need to call the ``/api/segment`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/segment

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[name]                                  | request        | Segment name                                                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[active]                                | request        | *(optional)* Set 1 if active, otherwise 0                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[description]                           | request        | *(optional)* A short description                                           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][type]           | request        | Criterion type. It can be one of the following:                            |
|                                                |                | ``anniversary``, ``bought_in_pos``, ``transaction_count``,                 |
|                                                |                | ``transaction_amount``, ``average_transaction_amount``,                    |
|                                                |                | ``last_purchase_n_days_before``, ``purchase_period``,                      |
|                                                |                | ``transaction_percent_in_pos``, ``bought_skus``, ``bought_makers``,        |
|                                                |                | ``bought_labels``, ``customer_has_labels``,                                |
|                                                |                | ``customer_has_labels_with_values``, ``customer_list``.                    |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][days]           | request        | Segment width in days. If set to 1, only customers with anniversary on     |
|                                                |                | this exact date are in the segment.                                        |
|                                                |                | *(required)* for ``anniversary`` criterion type.                           |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][anniversaryType]| request        | Anniversary type: ``birthday`` or ``registration``.                        |
|                                                |                | *(required)* for ``anniversary`` criterion type.                           |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][fromAmount]     | request        | Minimum value of transactions.                                             |
|                                                |                | *(required)* for ``average_transaction_amount`` and ``transaction_amount`` |
|                                                |                | criterion type.                                                            |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][toAmount]       | request        | Maximum value of transactions.                                             |
|                                                |                | *(required)* for ``average_transaction_amount`` and ``transaction_amount`` |
|                                                |                | criterion type.                                                            |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][posIds][]       | request        | One or more UUIDs of POS.                                                  |
|                                                |                | *(required)* minimum 1 in collection for ``bought_in_pos`` criterion type. |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][posId]          | request        | Exactly one UUID of POS.                                                   |
|                                                |                | *(required)* for ``transaction_percent_in_pos`` criterion type.            |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][percent]        | request        | Treshold percent value.                                                    |
|                                                |                | *(required)* for ``transaction_percent_in_pos`` criterion type.            |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][makers][]       | request        | One of more brands.                                                        |
|                                                |                | *(required)* minimum 1 in collection for ``bought_makers`` criterion type. |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][skuIds][]       | request        | One or more SKUs.                                                          |
|                                                |                | *(required)* minimum 1 in collection for ``bought_skus`` criterion type.   |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][labels][]       | request        | One or more Labels, which apply either to the product or the customer.     |
|                                                |                | Each label is an array of key and value elements:                          |
|                                                |                | ``...[labels][0][key]=key_one&...[labels][0][value]=value_one`` .          |
|                                                |                | For ``customer_has_labels`` criterions, there should be no value element.  |
|                                                |                | *(required)* minimum 1 in collection for ``bought_labels``,                |
|                                                |                | ``customer_has_labels`` and ``customer_has_labels_with_values``            |
|                                                |                | criterion types.                                                           |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][days]           | request        | Segment includes customers who shopped at least this days ago.             |
|                                                |                | 1 is yesterday.                                                            |
|                                                |                | *(required)* for ``last_purchase_n_days_before`` criterion type.           |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][fromDate]       | request        | Start of date range.                                                       |
|                                                |                | *(required)* for ``purchase_period`` criterion type.                       |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][toDate]         | request        | End of time range.                                                         |
|                                                |                | *(required)* for ``purchase_period`` criterion type.                       |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][min]            | request        | Minimum transaction count.                                                 |
|                                                |                | *(required)* for ``transaction_count`` criterion type.                     |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][max]            | request        | Maximum transaction count.                                                 |
|                                                |                | *(required)* for ``transaction_count`` criterion type.                     |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][customers][]    | request        | One or more Customers, identified by UUID, phone, loyalty card number,     |
|                                                |                | or e-mail address. Identifiers don't have to be of the same type.          |
|                                                |                | *(required)* minimum 1 in collection for ``customer_list`` criterion type. |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/segment/00000000-0000-0000-0000-000000000002` \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."
        -d "segment[name]=testsm" \
        -d "segment[active]=1" \
        -d "segment[description]=testsmdescription" \
        -d "segment[parts][0][criteria][0][type]=anniversary" \
        -d "segment[parts][0][criteria][0][days]=2" \
        -d "segment[parts][0][criteria][0][anniversaryType]=registration"

.. note::

    To create OR condition, add another ``SegmentPart`` element in ``segment[parts]`` array.
    To create AND condition, add another ``Criterion`` element in ``segment[parts][<part_element>][criteria]`` array.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "segmentId": "17347292-0aaf-4c25-9118-17eb2c55b58b"
    }



Delete segment
--------------

To delete segment you need to call the ``/api/segment/<segment>`` endpoint with the ``DELETE`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    DELETE /api/segment/<segment>

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

    curl http://localhost:8181/api/segment/f9a64320-0e93-42b9-882c-43cd477156cf \
        -X "DELETE" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *f9a64320-0e93-42b9-882c-43cd477156cf* segment ID is an example value.
    Your value can be different. Check in the list of all segments if you are not sure which id should be used.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 OK

.. code-block:: json

    No Content



Get segment details
-------------------

To retrieve segment details you need to call the ``/api/segment/<segment>`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/segment/<segment>

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <segment>            | query          | Segment ID                                             |
+----------------------+----------------+--------------------------------------------------------+

Example
^^^^^^^

To see the details of the customer user with ``segment = 00000000-0000-0000-0000-000000000002`` use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/segment/00000000-0000-0000-0000-000000000002` \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "segmentId": "00000000-0000-0000-0000-000000000002",
      "name": "anniversary",
      "description": "desc",
      "active": false,
      "parts": [
        {
          "segmentPartId": "00000000-0000-0000-0000-000000000001",
          "criteria": [
            {
              "criterionId": "00000000-0000-0000-0000-000000000011",
              "anniversaryType": "birthday",
              "days": 10,
              "type": "anniversary"
            }
          ]
        }
      ],
      "createdAt": "2018-02-19T09:45:06+0100",
      "customersCount": 0
    }



Update segment data
-------------------

To fully update segment data for user you need to call the ``/api/segment/<segment>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/segment/<segment>

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <segment>                                      | query          | Segment ID                                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[name]                                  | request        | Segment name                                                               |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[active]                                | request        | *(optional)* Set 1 if active, otherwise 0                                  |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[description]                           | request        | *(optional)* A short description                                           |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][type]           | request        | Criterion type. It can be one of the following:                            |
|                                                |                | ``anniversary``, ``bought_in_pos``, ``transaction_count``,                 |
|                                                |                | ``transaction_amount``, ``average_transaction_amount``,                    |
|                                                |                | ``last_purchase_n_days_before``, ``purchase_period``,                      |
|                                                |                | ``transaction_percent_in_pos``, ``bought_skus``, ``bought_makers``,        |
|                                                |                | ``bought_labels``, ``customer_has_labels``,                                |
|                                                |                | ``customer_has_labels_with_values``, ``customer_list``.                    |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][days]           | request        | Segment width in days. If set to 1, only customers with anniversary on     |
|                                                |                | this exact date are in the segment.                                        |
|                                                |                | *(required)* for ``anniversary`` criterion type.                           |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][anniversaryType]| request        | Anniversary type: ``birthday`` or ``registration``.                        |
|                                                |                | *(required)* for ``anniversary`` criterion type.                           |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][fromAmount]     | request        | Minimum value of transactions.                                             |
|                                                |                | *(required)* for ``average_transaction_amount`` and ``transaction_amount`` |
|                                                |                | criterion type.                                                            |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][toAmount]       | request        | Maximum value of transactions.                                             |
|                                                |                | *(required)* for ``average_transaction_amount`` and ``transaction_amount`` |
|                                                |                | criterion type.                                                            |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][posIds][0]      | request        | One or more UUIDs of POS.                                                  |
|                                                |                | *(required)* minimum 1 in collection for ``bought_in_pos`` criterion type. |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][posId]          | request        | Exactly one UUID of POS.                                                   |
|                                                |                | *(required)* for ``transaction_percent_in_pos`` criterion type.            |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][percent]        | request        | Treshold percent value.                                                    |
|                                                |                | *(required)* for ``transaction_percent_in_pos`` criterion type.            |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][makers][0]      | request        | One of more brands.                                                        |
|                                                |                | *(required)* minimum 1 in collection for ``bought_makers`` criterion type. |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][skuIds][0]      | request        | One or more SKUs.                                                          |
|                                                |                | *(required)* minimum 1 in collection for ``bought_skus`` criterion type.   |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][labels][0]      | request        | One or more Labels, which apply either to the product or the customer.     |
|                                                |                | Each label is an array of key and value elements:                          |
|                                                |                | ``...[labels][0][key]=key_one&...[labels][0][value]=value_one`` .          |
|                                                |                | For ``customer_has_labels`` criterions, there should be no value element.  |
|                                                |                | *(required)* minimum 1 in collection for ``bought_labels``,                |
|                                                |                | ``customer_has_labels`` and ``customer_has_labels_with_values``            |
|                                                |                | criterion types.                                                           |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][days]           | request        | Segment includes customers who shopped at least this days ago.             |
|                                                |                | 1 is yesterday.                                                            |
|                                                |                | *(required)* for ``last_purchase_n_days_before`` criterion type.           |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][fromDate]       | request        | Start of date range.                                                       |
|                                                |                | *(required)* for ``purchase_period`` criterion type.                       |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][toDate]         | request        | End of time range.                                                         |
|                                                |                | *(required)* for ``purchase_period`` criterion type.                       |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][min]            | request        | Minimum transaction count.                                                 |
|                                                |                | *(required)* for ``transaction_count`` criterion type.                     |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][max]            | request        | Maximum transaction count.                                                 |
|                                                |                | *(required)* for ``transaction_count`` criterion type.                     |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| segment[parts][0][criteria][0][customers][0]   | request        | One or more Customer UUIDs.                                                |
|                                                |                | *(required)* minimum 1 in collection for ``customer_list`` criterion type. |
|                                                |                | *(forbidden)* for other criterion types.                                   |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^
To update the details of a segment with ``segment = 17347292-0aaf-4c25-9118-17eb2c55b58b`` use the method below:

.. code-block:: bash

    curl http://localhost:8181/api/segment/17347292-0aaf-4c25-9118-17eb2c55b58b \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "segment[name]=tests" \
        -d "segment[active]=0" \
        -d "segment[description]=tests" \
        -d "segment[parts][0][criteria][0][type]=anniversary" \
        -d "segment[parts][0][criteria][0][days]=2" \
        -d "segment[parts][0][criteria][0][anniversaryType]=birthday"

.. note::

    To create OR condition, add another ``SegmentPart`` element in ``segment[parts]`` array.
    To create AND condition, add another ``Criterion`` element in ``segment[parts][<part_element>][criteria]`` array.

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "segmentId": "17347292-0aaf-4c25-9118-17eb2c55b58b"
    }



Activate segment
--------------

To activate segment you need to call the ``/api/segment/<segment>/activate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/segment/<segment>/activate

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <segment>                                      | query          | Segment ID                                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/segment/63afec60-5e74-43fc-a5e1-81bbc03421ca/activate \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 OK

.. code-block:: json

    No Content



Get customers assigned to specific segment
------------------------------------------

To retrieve a paginated list of customers assigned to specific segment you need to call the ``/api/segment/<segment>/customers`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/segment/<segment>/customers

+----------------------+----------------+--------------------------------------------------------+
| Parameter            | Parameter type |  Description                                           |
+======================+================+========================================================+
| Authorization        | header         | Token received during authentication                   |
+----------------------+----------------+--------------------------------------------------------+
| <segment>            | query          | Segment ID                                             |
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

    curl http://localhost:8181/api/segment/63afec60-5e74-43fc-a5e1-81bbc03421ca/customers \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "customers": [
        {
          "segmentId": "63afec60-5e74-43fc-a5e1-81bbc03421ca",
          "customerId": "57524216-c059-405a-b951-3ab5c49bae14",
          "segmentName": "test123",
          "firstName": "Tomasz",
          "lastName": "Test80",
          "email": "tomasztest80@wp.pl",
          "active": true,
          "address": [],
          "createdAt": "2018-02-20T08:22:11+0100",
          "levelId": "000096cf-32a3-43bd-9034-4df343e5fd94",
          "manuallyAssignedLevelId": {
            "levelId": "000096cf-32a3-43bd-9034-4df343e5fd94"
          },
          "agreement1": true,
          "agreement2": false,
          "agreement3": false,
          "status": {
            "availableTypes": [
              "new",
              "active",
              "blocked",
              "deleted"
            ],
            "availableStates": [
              "no-card",
              "card-sent",
              "with-card"
            ],
            "type": "active",
            "state": "no-card"
          },
          "updatedAt": "2018-02-20T08:22:12+0100",
          "campaignPurchases": [],
          "transactionsCount": 1,
          "transactionsAmount": 44.97,
          "transactionsAmountWithoutDeliveryCosts": 44.97,
          "amountExcludedForLevel": 0,
          "averageTransactionAmount": 44.97,
          "lastTransactionDate": "2018-02-20T07:24:19+0100",
          "currency": "eur",
          "levelPercent": "20.00%"
        }
      ],
      "total": 1
    }



Deactivate segment
----------------

To deactivate segment you need to call the ``/api/segment/<segment>/deactivate`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/segment/<segment>/deactivate

+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| Parameter                                      | Parameter type |  Description                                                               |
+================================================+================+============================================================================+
| Authorization                                  | header         | Token received during authentication                                       |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+
| <segment>                                      | query          | Segment ID                                                                 |
+------------------------------------------------+----------------+----------------------------------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/segment/63afec60-5e74-43fc-a5e1-81bbc03421ca/deactivate \
        -X "POST" \
        -H "Accept:\ application/json" \
        -H "Content-type:\ application/x-www-form-urlencoded" \
        -H "Authorization:\ Bearer\ eyJhbGciOiJSUzI1NiIsInR5cCI6..." \

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 204 OK

.. code-block:: json

    No Content
