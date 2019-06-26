Campaigns categories API
========================

These endpoints will allow you to easily manage campaign categories. Campaign categories gives possibility to group
campaigns into categories. Campaign can be assigned to many categories.

Create new campaign category
----------------------------

To create a new category you will need to call the ``/api/campaignCategory`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/campaignCategory

+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| Parameter                                         | Parameter type |  Description                                                                 |
+===================================================+================+==============================================================================+
| Authorization                                     | header         |  Token received during authentication                                        |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign_category[translations][en][name]         | request        |  Campaign category name in given locale.                                     |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign_category[active]                         | request        |  Set 1 if active, otherwise 0                                                |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign_category[sortOrder]                      | request        |  Sort order key.                                                             |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+


Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/campaign \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "campaign[translations][en][name]=Category+A" \
        -d "campaign[active]=1" \
        -d "campaign[sortOrder]=0"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "campaignCategoryId": "3062c881-93f3-496b-9669-4238c0a62be8"
    }

Get the collection of campaign categories
-----------------------------------------

To retrieve a paginated list of campaigns categories you will need to call the ``/api/campaignCategory`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaignCategory

+-------------------------------------+----------------+----------------------------------------------------+
| Parameter                           | Parameter type | Description                                        |
+=====================================+================+====================================================+
| Authorization                       | header         | Token received during authentication               |
+-------------------------------------+----------------+----------------------------------------------------+
| name                                | request        | *(optional)* Filter by name                        |
+-------------------------------------+----------------+----------------------------------------------------+
| active                              | request        | *(optional)* Filter by activity                    |
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
| format                              | query          | *(optional)* Format of descriptions [html].        |
|                                     |                | Default is RAW.                                    |
+-------------------------------------+----------------+----------------------------------------------------+
| _locale                             | query          | *(optional)* Retrieves data in given locale        |
+-------------------------------------+----------------+----------------------------------------------------+

To see the first page of all campaigns categories use the below method:

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/campaignCategories \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    Translatable fields (name) are returned in given locale.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "categories": [
        {
          "name": "Category A",
          "campaignCategoryId": "000096cf-32a3-43bd-9034-4df343e5fd99",
          "active": true,
          "sortOrder": 0,
          "translations": [
            {
              "name": "Category A",
              "id": 1,
              "locale": "en"
            },
            {
              "name": "Kategoria A",
              "id": 3,
              "locale": "pl"
            }
          ]
        },
        {
          "name": "Category B",
          "campaignCategoryId": "000096cf-32a3-43bd-9034-4df343e5fd98",
          "active": true,
          "sortOrder": 0,
          "translations": [
            {
              "name": "Category B",
              "id": 2,
              "locale": "en"
            },
            {
              "name": "Kategoria B",
              "id": 4,
              "locale": "pl"
            }
          ]
        }
      ],
      "total": 2
    }

Update a campaign
-----------------

To fully update a campaign you will need to call the ``/api/campaignCategory/<campaign>`` endpoint with the ``PUT`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    PUT /api/campaignCategory/<campaignCategory>

+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| Parameter                                         | Parameter type |  Description                                                                 |
+===================================================+================+==============================================================================+
| Authorization                                     | header         |  Token received during authentication                                        |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign_category[translations][en][name]         | request        |  Campaign category name in given locale.                                     |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign_category[active]                         | request        |  Set 1 if active, otherwise 0                                                |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+
| campaign_category[sortOrder]                      | request        |  Sort order key.                                                             |
+---------------------------------------------------+----------------+------------------------------------------------------------------------------+

Example
^^^^^^^

 To fully update a campaign category with ``id = 3062c881-93f3-496b-9669-4238c0a62be8`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/campaignCategory/3062c881-93f3-496b-9669-4238c0a62be8 \
        -X "PUT" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "campaign[translations][en][name]=Category+A" \
        -d "campaign[active]=1" \
        -d "campaign[sortOrder]=0"

.. warning::

    Remember, you must update the whole data of the campaign category.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "campaignCategoryId": "3062c881-93f3-496b-9669-4238c0a62be8"
    }

Get campaign category details
-----------------------------

To retrieve the details of a campaign category you will need to call the ``/api/campaignCategory/{campaignCategory}`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/campaignCategory/<campaignCategory>

+-----------------------+----------------+----------------------------------------------------+
| Parameter             | Parameter type | Description                                        |
+=======================+================+====================================================+
| Authorization         | header         | Token received during authentication               |
+-----------------------+----------------+----------------------------------------------------+
| <campaignCategory>    | query          | Id of the campaign category                        |
+-----------------------+----------------+----------------------------------------------------+
| _locale               | query          | *(optional)* Retrieves data in given locale        |
+-----------------------+----------------+----------------------------------------------------+

Example
^^^^^^^

To see the details of the campaign category with ``campaignCategory = 3062c881-93f3-496b-9669-4238c0a62be8`` use the below method:

.. code-block:: bash

    curl http://localhost:8181/api/campaignCategory/3062c881-93f3-496b-9669-4238c0a62be8 \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an exemplary value.
    Your value can be different. Read more about :doc:`Authorization in the </authorization>`.

.. note::

    Translatable fields (name) are returned in given locale.

Exemplary Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "name": "Category A",
      "campaignCategoryId": "000096cf-32a3-43bd-9034-4df343e5fd99",
      "active": true,
      "sortOrder": 0,
      "translations": [
        {
          "name": "Category A",
          "id": 1,
          "locale": "en"
        },
        {
          "name": "Kategoria A",
          "id": 3,
          "locale": "pl"
        }
      ]
    }
