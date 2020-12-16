Event Sourcing
==============

Event Sourcing ensures that all changes to the state of application's parts that use it are stored as a sequence of
events. Not only can we query these events, we can also use the event log to reconstruct past states,
and as a foundation to automatically adjust the state to cope with retroactive changes.

.. image:: _images/event_sourcing.png
    :scale: 55%

To implement event sourcing we use an external library called `Broadway <https://github.com/broadway/broadway>`_.

Not everything in Open Loyalty is event sourced, and this behaviour is intended.
Event sourcing is used in change-sensitive parts of the application where full rewind capacity is needed, for example
transactions, points and customer data changes.

To read about Event Sourcing's pros and cons, go to Martin Fowler's website `here <https://martinfowler.com/eaaDev/EventSourcing.html>`_.
