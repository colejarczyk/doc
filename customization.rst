Campaign photos storage
=======================

Currently, all campaign photos are stored in the app/uploads directory.

This can be easily changed to another directory or even to cloud storage.

In order to do that, change the `adapter_*` entry in the Symfony config to your adapter defined
in src/Infrastructure/Core/Resources/config/config.yml at knp_gaufrette.adapters.

The complete reference on how to define an adapter can be found in the `KnpGaufretterBundle documentation <https://github.com/KnpLabs/KnpGaufretteBundle>`_

Listening for system events
===========================

In many places of this system some system events are dispatched, e.g. `oloy.account.available_points_amount_changed` is dispatched when the available points
amount is changed.

It is possible to write a listener for such events and perform some custom actions.

Defining a listener:

.. code:: php

    oloy.my_custom_listener
        class: 'OpenLoyalty\Bundle\MyBundle\EventListener\MyCustomListener
        tags:
          - { name: broadway.event_listener, event: `oloy.account.available_points_amount_changed`, method: onPointsChanged}
