Fixtures
========

Fixtures are used mainly for testing, but also for setting up application for a first use or for demonstration purposes.

There are tree types of fixtures used in Open Loyalty.

Testing fixtures
----------------

It puts a software in certain state so we can test is application working as expected.

To load testing data run:

.. code-block:: bash

    $ bin/console doctrine:fixtures:load --env=test -n

Setup fixtures
--------------

Another type of fixtures is called “setup”. It’s meant to load a smallest possible amount of data to run
loyalty program correctly.

To load initial data run:

.. code-block:: bash

    $ bin/console doctrine:fixtures:load -n -vvv

Demo fixtures
-------------

Last type of fixtures is demo. It loads a large amount of data to show full potential of Open Loyalty.
So you will see a lot of customers, points, transactions and so on. It’s really useful when you want to
present a software to your clients and you need sample data.

To load demonstration data run:

.. code-block:: bash

    $ bin/console doctrine:fixtures:load --fixtures src/OpenLoyalty/Bundle/DemoBundle/_DataFixtures/ORM/ -n

Common tasks
------------

There is also another, simpler way to initialize Open Loyalty. We use a tool called ``phing`` which is a great tool
to run many commands in sequences. We prepared a few useful commands to automate some common tasks and make them easier.

Here are a few most used commands, but if you curious about more, check the
`build.xml <http://gitlab.divante.pl/open-loyalty/open-loyalty/blob/develop/backend/build.xml>` file


Initialize Open Loyalty, load testing data and run unit & integration tests and check coding standard at the end.

.. code-block:: bash

    $ phing ci-setup-test

Initialize Open Loyalty and load only required data

.. code-block:: bash

    $ phing basic-setup

Initialize Open Loyalty and load test data

.. code-block:: bash

    $ phing setup

Initialize Open Loyalty and load demo data

.. code-block:: bash

    $ phing demo

Initialize Open Loyalty and run specific tests

.. code-block:: bash

    $ phing test -Dsrc=src/OpenLoyalty/Bundle/TransactionBundle/Tests/Controller/Api/TransactionControllerTest.php

Run specific tests without initialization

.. code-block:: bash

    $ phing test -Dsrc=src/OpenLoyalty/Bundle/TransactionBundle/Tests/Controller/Api/TransactionControllerTest.php -Dno-build

Open Loyalty uses JWT tokens to authenticate a user in the system but also to send all required data between requests.
As we’re focused on the security, this token is encrypted using RSA keys which you should generate by yourself.
To make it easier for you, we prepared a command that automates this task for you.

.. code-block:: bash

    $ phing generate-jwt-keys
