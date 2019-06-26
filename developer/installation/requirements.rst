Requirements
============

Here you will find the list requirements that have to be meet to be able to use Open Loyalty.
Before you start reading, have a look at the `Symfony requirements <http://symfony.com/doc/3.4/reference/requirements.html>`_.

Operating Systems
-----------------

The recommended operating systems for running Open Loyalty are Unix systems - **Linux, MacOS**.

Running Open Loyalty
--------------------

We recommend to use docker as an abstraction layer to run Open Loyalty. Also, we do recommend to use Kubernetes for
production purpose.

If you don’t want to use Docker or Kubernetes and you want to run Open Loyalty on the server, you need to prepare and
configure all software that’s required to run OL correctly.

Web server configuration
------------------------

In the production environment we do recommend using Nginx web server

PHP Configuration
----------------

+-------------+---------+
| PHP version | >= 7.1  |
+-------------+---------+

+----------------+-------+
| PHP extensions | APCU  |
+----------------+-------+

PHP configuration settings

+---------------------------------+----------------+
| memory_limit                    | 1024M          |
+---------------------------------+----------------+
| date.timezone                   | Europe/Warsaw  |
+---------------------------------+----------------+
| upload_max_filesize             | 10M            |
+---------------------------------+----------------+
| post_max_size                   | 10M            |
+---------------------------------+----------------+
| short_open_tag                  | Off            |
+---------------------------------+----------------+
| opcache.validate_timestamps     | 0              |
+---------------------------------+----------------+
| opcache.memory_consumption      | 256            |
+---------------------------------+----------------+
| opcache.max_accelerated_files   | 20000          |
+---------------------------------+----------------+
| realpath_cache_size             | 600            |
+---------------------------------+----------------+

Database
--------

We recommend to use PostgreSQL database in version 9.x

As we use Doctrine, it should be possible to run Open Loyalty on any SQL compliant database, however it may
require additional development from your side.


Elasticsearch
-------------

We designed our software with scalability and performance in mind. That’s why we separated storage on write and read.
To read data we use Elasticsearch that contains projections of data stored in the write database optimized for reading
and views that loyalty program needs.

We recommend to use Elasticsearch in version 2.x
