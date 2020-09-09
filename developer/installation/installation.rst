Installation
============

Development environment
-----------------------

This project has full support for running in Docker. Make sure that you have installed docker and docker-composer and
you are using compatible environment.

Use Open Loyalty skeleton application for Open Loyalty customization. Composer is responsible for providing Open Loyalty
Framework in given version which can be overridden by developers and adjusted to your business requirements. The latest
version of Open Loyalty is available on our packagist (access only for Enterprise Clients).

You can find more details how to override Symfony components in `documentation <https://symfony.com/doc/4.4/bundles/override.html>`_.

Since 4.1, frontend project is built independently from the backend.

Backend (API)
^^^^^^^^^^^^^

Open skeleton project and build base images:

.. code-block:: bash

  ./docker/base/build_dev.sh

and run containers:

.. code-block:: bash

  docker-compose -f docker/docker-compose.dev.yml --project-name=PROJECT_NAME up

Then use another command to setup database, Elasticsearch and load some demo data:

.. code-block:: bash

  docker-compose -f docker/docker-compose.dev.yml --project-name=PROJECT_NAME exec --user=www-data php phing setup

After the example data is loaded, the following should be available:

 * http://openloyalty.localhost/api - RESTful API port
 * http://openloyalty.localhost/doc - swagger-like API doc
 * http://openloyalty.localhost/api/healthcheck - Health check status (return 204 means OK)

Before you start using Open Loyalty you need to define hosts in your local environment.
Add host ``openloyalty.localhost`` as ``127.0.0.1`` in your system configuration file.
On the Linux it would be ``/etc/hosts``.

.. note::

    After running docker-compose up you may wonder when it’s ready to use because you’ve got a message that keeps
    appearing all the time. It’s perfectly fine to see message ``open_loyalty_mail | [APIv1] KEEPALIVE /api/v1/events``.
    This message is shown by MailHog which is listening for incoming e-mail messages. Open Loyalty in the development mode
    doesn't send e-mails to the wider network – all e-mails are caught by MailHog. To learn more about
    `MailHog, click here <https://github.com/mailhog/MailHog>`_.

If you don’t want to see messages from running containers run a docker-compose as a daemon ``docker-compose up -d``

Frontend
^^^^^^^^

Open frontend project and build base images:

.. code-block:: bash

  ./docker/base/build_dev.sh

and run containers:

.. code-block:: bash

  docker-compose -f docker/docker-compose.dev.yml --project-name=PROJECT_NAME up

Application should be available under slightly different URLs:

 * http://openloyalty.localhost:8081/admin - the administration panel
 * http://openloyalty.localhost:8081/pos - the merchant panel

Preparing docker images
-----------------------

Before deploy application in production you need to build docker images. Currently we support
`Gitlab CI <https://about.gitlab.com/product/continuous-integration/>`_ in order to build images automatically. If you
need to build images in different way then you should ADJUST and execute bellow commands:

.. code-block:: bash

  # API (from backend project)
  docker build -t openloyalty/api-NAME:VERSION -f ./docker/prod/web/api-dockerfile .;

  # FPM (from backend project)
  docker build -t openloyalty/fpm-NAME:VERSION -f ./docker/prod/php/fpm-dockerfile .;

  # WORKER (from backend project)
  docker build -t openloyalty/worker-NAME:VERSION -f ./docker/prod/php/worker-dockerfile .;

  # FRONTEND (from frontend project)
  docker build -t openloyalty/frontend-NAME:VERSION -f ./docker/prod/frontend/frontend-dockerfile .;

Kubernetes
----------

We recommend running Open Loyalty projects in production using docker orchestration system like Kubernetes.

Read more about deploying application using Kubernetes `here <./kubernetes.rst>`_.
