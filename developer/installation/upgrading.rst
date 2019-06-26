Upgrading
=========

Each new release has a `CHANGELOG.md <https://github.com/DivanteLtd/open-loyalty/blob/master/CHANGELOG.md>`_ and sometimes, when
upgrading may be difficult it has a file `UPGRADE.md <https://github.com/DivanteLtd/open-loyalty/blob/master/UPGRADE-2.2.md>`_.

To update your project you need to update ``divante-ltd/open-loyalty-framework`` library in ``composer.json`` file

.. code-block:: yaml

    "require": {
        "divante-ltd/open-loyalty-framework": "^4.0"
    }

Then run command ``composer update``

.. code-block:: bash

    $ composer update divante-ltd/open-loyalty-framework

If this results in a dependency error, it may mean that other dependencies also have to be upgraded.
Using this command may help you upgrade dependencies.

.. code-block:: bash

    $ composer update divante-ltd/open-loyalty-framework --with-dependencies

You should run the following commands:

.. code-block:: bash

    $ bin/console cache:clear

It clears cache

.. code-block:: bash

    $ bin/console doctrine:schema:update --force

It's a command to update schema in PostgreSQL without losing data.

.. code-block:: bash

    $ bin/console oloy:user:projections:index:create --drop-old -n

It deletes all indexes in ElasticSearch and creates new ones.

.. code-block:: bash

    $ bin/console oloy:utility:read-models:recreate

It recreates all data from event store to ElasticSearch, so the read model is up-to-date.

If you don't want to focus on details you can use phing task to upgrade Open Loyalty:

.. code-block:: bash

    $ phing migrate

Now you should have all required updates to run a new version of Open Loyalty.
Sometimes we release a new version with backwards compatibility breaks so please look at the ``UPGRADE-..md`` files.
