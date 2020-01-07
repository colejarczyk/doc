How to work with queues
====================

OpenLoyalty uses queue system to process tasks in an asynchronous way. We have chosen RabbitMQ as a queue provider.
In case you need to create a process which uses queue you have to create a consumer and a producer. The producer is
responsible for either creating a request to run the process or running this process immediately when queue processing
is disabled. The consumer is a class which processes elements from queue.

Configuration
-------------------------------

In Symfony config files a simple default configuration is defined. Administrators can enable the queue by setting queue_enabled to true.

.. code-block:: yaml

    queue_enabled: false
    queue_host: queue
    queue_port: 5672
    queue_user: guest
    queue_password: guest


Example how to use queue along with CQRS
----------------------------------------

Below you may find a description on how to a producer for recreating segments. This is a real use case from the application.

1. *You don't have to create a consumer.* The general Consumer class already exists at src/OpenLoyalty/Component/Core/Infrastructure/Queue/RabbitMq/Consumer.php
This Consumer uses CommandBus to dispatch Commands taken from queue.

2. *Next, create a producer for sync and async processing.* Classes OpenLoyalty\Component\Segment\Infrastructure\Queue\Producer
should implement a specific interface SegmentProducerInterface). The only required dependency is on the queue connection that
implements QueueProducerConnectionInterface

Now, you have to configure connection and Producer class in the container.

.. code-block:: yaml

    oloy.segment.rabbitmq.connection:
        class: OpenLoyalty\Infrastructure\Core\Queue\RabbitMq\Producer
        arguments:
            $connection: '@old_sound_rabbit_mq.segment_producer'
        calls:
            - [setLogger, ['@logger']]

    OpenLoyalty\Component\Segment\Infrastructure\Queue\Producer:
        arguments:
            $queueProducerConnection: '@oloy.segment.rabbitmq.connection'
            $queueEnabled: '%queue_enabled%'

3. Third step is to create configuration of the connection between application and the queue system (RabbitMq in our case).

.. code-block:: yaml

    old_sound_rabbit_mq:
        producers:
            segment:
                connection:       default
                exchange_options: {name: 'segment', type: direct}
                enable_logger: true
        consumers:
            segment-dead-letters:
                connection:       default
                exchange_options: { name: 'segment-dead-letters', type: fanout }
                queue_options:    { name: 'segment-dead-letters' }
                callback:         OpenLoyalty\Infrastructure\Core\Queue\RabbitMq\DeadLetter
        multiple_consumers:
            segment:
                connection:       default
                exchange_options: {name: 'segment', type: direct}
                enable_logger: true
                queues:
                    recreate-segment:
                        name: recreate-segment
                        arguments:
                            x-dead-letter-exchange:    ['S', 'segment-dead-letters']
                            x-dead-letter-routing-key: ['S', 'segment-dead-letters']
                        callback: OpenLoyalty\Infrastructure\Core\Queue\RabbitMq\Consumer
                        routing_keys:
                            - recreate-segment

The name of this service MUST be of `old_sound_rabbit_mq.{producer_attribute_value}_producer` format.

4. Finally, the consumer should be registered as a supervisord worker. Add your configuration to
the directories named: docker/dev/php/conf/supervisord/conf.d/ and docker/prod/php/conf/supervisord/conf.d/

Example of such a file is docker/dev/php/conf/supervisord/conf.d/segment-consumer.conf.

Run the consumer manually
-------------------------

In order to run the consumer manually in the console, type:

.. code-block:: bash

    bin/console rabbitmq:multiple-consumer segment

Example how to use queue without CQRS
-------------------------------------

The above example strongly uses CQRS pattern and dispatches commands to the command bus. However, sometimes you need a custom consumer for unusual cases.

Below you may find a description on how to create both consumer and a producer for sending emails. This is also a real use case from the application.

1. *First, create a consumer.* This class must implements OldSound\RabbitMqBundle\RabbitMq\ConsumerInterface.
The consumer must be registered in container as simple service with injected dependencies.

In this case

.. code-block:: yaml

    OpenLoyalty\Infrastructure\Email\Queue\RabbitMq\Consumer:
        arguments:
            $logger: '@logger'
            $mailer: '@oloy.mailer'

2. *Next, create a producer.* This step is the same like in the above example with CQRS. So let's see how the configuration
looks like for sending emails.

.. code-block:: yaml

    oloy.email.rabbitmq.connection:
        class: OpenLoyalty\Infrastructure\Core\Queue\RabbitMq\Producer
        arguments:
            $connection: '@old_sound_rabbit_mq.email_producer'
        calls:
            - [setLogger, ['@logger']]

    OpenLoyalty\Infrastructure\Email\Queue\RabbitMq\Producer:
        arguments:
            $mailer: '@oloy.mailer'
            $queueProducerConnection: '@oloy.email.rabbitmq.connection'
            $queueEnabled: '%queue_enabled%'

Nothing different than in the previous example.

3. Third step is to create configuration of the connection between application and the queue system (RabbitMq in our case).
In this case, the only difference is the "callback" for multiple consumers. We don't use general Consumer from Core
to dispatch commands to the command bus but rather our own implementation from the step 1.

.. code-block:: yaml

    old_sound_rabbit_mq:
        producers:
            email:
                connection:       default
                exchange_options: {name: 'email', type: direct}
                enable_logger: true
        consumers:
            email-dead-letters:
                connection:       default
                exchange_options: { name: 'email-dead-letters', type: fanout }
                queue_options:    { name: 'email-dead-letters' }
                callback:         OpenLoyalty\Infrastructure\Core\Queue\RabbitMq\DeadLetter
        multiple_consumers:
            email:
                connection:       default
                exchange_options: {name: 'email', type: direct}
                enable_logger: true
                queues:
                    email-queue:
                        name: email-queue
                        arguments:
                            x-dead-letter-exchange:    ['S', 'email-dead-letters']
                            x-dead-letter-routing-key: ['S', 'email-dead-letters']
                        callback: OpenLoyalty\Infrastructure\Email\Queue\RabbitMq\Consumer
                        routing_keys:
                            - email-queue

The name of this service MUST be of `old_sound_rabbit_mq.{producer_attribute_value}_producer` format.

4. Finally, the consumer should be registered as a supervisord worker. Add your configuration to
the directories named: docker/dev/php/conf/supervisord/conf.d/ and docker/prod/php/conf/supervisord/conf.d/

Example of such a file is docker/dev/php/conf/supervisord/conf.d/segment-consumer.conf.

Run the consumer manually
-------------------------

In order to run the consumer manually in the console, type:

.. code-block:: bash

    bin/console rabbitmq:multiple-consumer email
