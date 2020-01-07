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

It's strongly recommended to refresh data in Elasticsearch in batches once you have more than 50k of events. Otherwise,
you can expect a big downtime as refreshing data in Elasticsearch is time consuming process. There is also a way to
recreate indices in parallel, which will be explained further in the article.

In order to refresh data in batches, you need to execute the command with parameters: FROM and TO are numbers of
events defining the range to process and PACKAGE_SIZE is the size of the batch.

.. code-block:: bash
    $ bin/console oloy:utility:read-models:recreate FROM_EVENT TO_EVENT PACKAGE_SIZE --index NAME

There is list of all available index names:

.. code-block:: bash

    customer_details
    invitation_details
    seller_details
    account_details
    point_transfer_details
    transaction_details
    coupon_usage
    campaign_usage
    campaign_bought

Script located in backend/bin/rd-recreate.sh is helpful to speed up recreating process. This script is
responsible for executing command oloy:utility:read-models:recreate with defined parameters. It produces many
independent PHP commands instead of executing one PHP command to process all events. Running a single process may
lead to insufficient memory insufficient memory and slowing down executing script.

Each index can be recreating parallel or even packages for the same index. For example:

background process 1: recreating index customer_details from 0 to 100k events
background process 2: recreating index customer_details from 100k to 200k events
background process 3: recreating index customer_details from 200k to 300k events

background process 4: recreating index invitation_details from 0 to 10k events
background process 5: recreating index invitation_details from 10k to 20k events
background process 6: recreating index invitation_details from 20k to 30k events

We are not able to write proper scenario what way is the most efficient, because it depends on the amount of data
and distribution data in indexes. User is responsible for determining what parameters are the best for his scenario.

Here some examples:

.. code-block:: bash

  ./bin/rd-recreate.sh 0 3 customer_details

By default, the it processes 100k events in 5k packages (STEP=100000 and PACKAGE_SIZE = 5000). It means that script
spawns 3 command execution for recreate customer_details index:

1. execution: from event 0 to 100000, processed per 5000 events
2. execution: from event 100000 to 200000, processed per 5000 events
3. execution: from event 200000 to 300000, processed per 5000 events

.. code-block:: bash

  nohup ./bin/rd-recreate.sh 0 3 customer_details

This scripts will do the same, but as background process.

.. warning::

  The constants STEP and PACKAGE_SIZE are hardcoded directly in the rd-recreate script. To alter them to your needs,
  you will have to edit the file.

.. note::

    You should recreate read model indices according to the order defined above.


If you have less than 50k events in event store, you may want to use a simple phing task to upgrade Open Loyalty:

.. code-block:: bash

    $ phing migrate

Now you should have all required updates to run a new version of Open Loyalty.
Sometimes we release a new version with backwards compatibility breaks so please look at the ``UPGRADE-..md`` files.
