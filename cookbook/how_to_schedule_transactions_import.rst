How to schedule transactions import
===================================

Registering transactions via API is not always possible, and importing transactions from your systems manually
might be exhausting and may introduce delays in assigning points to customers.

The solution often is to schedule a transaction import from an external filesystem, eg. AWS S3 bucket.

Crontab
-------

The system performs the transactions import as defined in crontab. To edit eg. file name, used file system
or if the system should automatically rename the file after import, edit your crontab file.

By default OL uses import_scheduled filesystem, transactions.xml filename and renames the file after import (-m option).

.. code-block:: bash

    0 * * * * su www-data -c "flock -w 0 /var/www/openloyalty/var/locks/transaction_scheduled_import.lock /usr/local/bin/php /var/www/openloyalty/bin/console --env=prod oloy:transaction:import -m import_scheduled:transactions.xml > /var/www/openloyalty/var/log/cron_ol_transaction_scheduled_import.log 2>&1"

.. note::
    You can multiply this line to set up different schedules, for example to use different file names for different
    branches of your network.


OL configuration
----------------

You can find settings of import_scheduled filesystem in ``parameters.yml`` file, ``adapter_import_scheduled`` key.
The value might be ``import_file_local``, taking the import file from ``/var/www/openloyalty/var/import`` folder,
which can be set up as a shared volume in docker/kubernetes,
or import_file_s3, which uses a folder named ``import_file_local`` on the S3 bucket shared with other adapters
and configured via ``amazon_s3.*`` parameters.

Alternatively, you might change the ``import`` filesystem adapter through ``adapter_import_file`` parameter.
This changes the place where files imported via web interface are saved, too.
If you use ``import`` filesystem to import your transactions on cron schedule, rememeber to change the command
in crontab to use ``import:`` file name prefix instead of ``import_scheduled:``.