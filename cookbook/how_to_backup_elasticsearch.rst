How to backup elasticsearch
===========================

To make backup of ElasticSearch we will use snapshot feature. You can read more about snapshots on ElasticSearch documentation (https://www.elastic.co/guide/en/elasticsearch/reference/2.2/modules-snapshots.html).

Preparing environment
---------------------

ElasticSearch needs to place where backup will be stored.

1. Create directory on container with correct permissions. You can attach volumen to bellow directory.

.. code-block:: bash

    docker exec -it open_loyalty_elk bash
    mkdir /usr/share/elasticsearch/backups
    chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/backups

2. Change ElasticSearch configuration in order to set created directory as backup place. Open file /usr/share/elasticsearch/config/elasticsearch.yml and add bellow line.

.. code-block:: bash

    path.repo: ["/usr/share/elasticsearch/backups"]

3. Restart ElasticSearch container in order to reload configuration.

Making snapshot
---------------

1. To make snapshot open ElasticSearch container and execute:

.. code-block:: bash

    docker exec -it open_loyalty_elk bash
    curl -X PUT "localhost:9200/_snapshot/my_backup/snapshot_1?wait_for_completion=true"

2. You can check all available snapshots on ElasticSearch cluster:

.. code-block:: bash

    docker exec -it open_loyalty_elk bash
    curl -X GET "localhost:9200/_snapshot/my_backup/_all?pretty"

Restoring snapshot
------------------

1. To restore backup we have to log in on container.

.. code-block:: bash

    docker exec -it open_loyalty_elk bash

2. Before making snapshot we have to make sure that all indexes are closed.

.. code-block:: bash

    curl -X POST "localhost:9200/_all/_close"

3. Restore snapshot.

.. code-block:: bash

    curl -X POST "localhost:9200/_snapshot/my_backup/snapshot_1/_restore"
