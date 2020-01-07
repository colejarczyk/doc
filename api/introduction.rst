.. index::
   single: Introduction

Introduction to Open Loyalty REST API
=====================================

This part of the documentation is about RESTful JSON API for the Open Loyalty platform.

.. note::

    To use this documentation should have some basic knowledge of `REST APIs <http://symfony.com/doc/current/quick_tour>`_.

Get current version
-------------------

To retrieve current version of OpenLoyalty you need to call ``/api/`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/ \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/json" \

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
        "name": "OpenLoyalty",
        "version": "4.1.0"
    }

Health check endpoint
---------------------

OpenLoyalty API provides special endpoint for checking application status. Endpoint verifies status of critical services
like database, Elasticsearch etc. Calling ``/api/healthcheck`` endpoint with the ``GET`` method returns 204 code when
all services works correctly otherwise returns 503 with details about statuses of each services.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/healthcheck

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/healthcheck \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/json" \

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 503 Unavailable

.. code-block:: json

    [
        {
            "name": "PostgreSQL",
            "status": "Problem",
            "message": "An exception occurred in driver: SQLSTATE[08006] [7] could not translate host name \"db\" to address: Name or service not known"
        },
        {
            "name": "Elasticsearch",
            "status": "OK"
        },
        {
            "name": "RabbitMQ",
            "status": "OK"
        }
    ]
