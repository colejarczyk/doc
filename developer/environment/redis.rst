Redis
=====

Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker.

Enabling Redis in OL
--------------------

Our default configuration uses file system cache. If you want to use redis you have to change symfony configuration and
build own docker images.

Open `config/packages/prod/config.yaml` and uncomment `snc_redis` and `framework` sections.

Make sure that working redis instance is listening on host and port defined in Symfony config.
