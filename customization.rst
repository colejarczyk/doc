Campaign photos storage
=======================

Currently all campaign photos are stored in app/uploads directory.

It can be easily changed to other directory or even to cloud storage.

In order to do that change `adapter_*` entry in Symfony config to your adapter defined
in src/Infrastructure/Core/Resources/config/config.yml at knp_gaufrette.adapters.

Complete reference on how to define adapter can be found in `KnpGaufretterBundle documentation <https://github.com/KnpLabs/KnpGaufretteBundle>`_

Listening for system events
===========================

In many places of this system some system events are dispatched, e.g. `oloy.account.available_points_amount_changed` is dispatched when available points
amount is changed.

It is possible to write listener for that events and perform some custom actions.

Defining listener:

.. code:: php

    oloy.my_custom_listener
        class: 'OpenLoyalty\Bundle\MyBundle\EventListener\MyCustomListener
        tags:
          - { name: broadway.event_listener, event: `oloy.account.available_points_amount_changed`, method: onPointsChanged}
