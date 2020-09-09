Run a command inside docker container
===================================

The simplest way to run a command inside a container is to execute:

  docker-compose exec -it open_loyalty_backend bash

This will bring up a container bash shell where you will be able to execute any command needed.

Just make sure that you are in the correct directory (`/var/www/openloyalty`)

and now feel free to execute composer install, phing setup or any other command.
