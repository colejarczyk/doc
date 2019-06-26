Creating new Commands and Handlers
==================================

Commands are the ``C`` of the ``CQRS`` paradigm. To change the state of the domain you should use a command.
Commands should have all the data they need to be handled properly passed in their constructor parameters.

Commands should be immutable data-moving objects. All parameters should be passed by constructor.
Don't use setters when building a command.



Create a command class
-----------------

To create a command, you need to create a command class.
In the example below, the added command extends ``CampaignCommand`` to add shared methods in all of the Campaign commands.
If a shared command base exists for your bounded context, use it as needed to keep the code ``DRY``.

.. code-block:: php

    // backend/src/Application/Campaign/Command/SendNewCampaignAvailableNotification.php

    namespace OpenLoyalty\Application\Campaign\Command;

    use OpenLoyalty\Domain\Core\Id\CampaignId;
    
    /**
     * Class SendNewCampaignAvailableNotification.
     */
    class SendNewCampaignAvailableNotification extends CampaignCommand
    {
        /**
         * @var array
         */
        private $recipientTokens;

        /**
         * @var string
         */
        private $title;

        /**
         * @var string
         */
        private $message;

        /**
         * @var array
         */
        private $labels;

        /**
         * SendNewCampaignAvailableNotification constructor.
         *
         * @param CampaignId $campaignId
         * @param string     $title
         * @param string     $message
         * @param array      $labels
         * @param array      $recipientTokens
         */
        public function __construct(
            CampaignId $campaignId,
            string $title,
            string $message,
            array $labels,
            array $recipientTokens
        ) {
            parent::__construct($campaignId);
            $this->title = $title;
            $this->message = $message;
            $this->labels = $labels;
            $this->recipientTokens = $recipientTokens;
        }
    }



Create a command handler class
-----------------

The next thing to do is to create a CommandHandler class.
Notice the use of the ``Handler`` suffix in the class name.

.. code-block:: php

    // backend/src/Application/Campaign/CommandHandler/NotificationHandler.php

    namespace OpenLoyalty\Application\Campaign\CommandHandler;

    use Broadway\CommandHandling\SimpleCommandHandler;
    use OpenLoyalty\Application\Campaign\Command\SendNewCampaignAvailableNotification;
    use OpenLoyalty\Infrastructure\User\Notification\NotificationServiceInterface;

    class NotificationHandler extends SimpleCommandHandler
    {
        /**
         * @var NotificationServiceInterface
         */
        private $notificationService;

        /**
         * NotificationHandler constructor.
         *
         * @param NotificationServiceInterface $notificationService
         */
        public function __construct(
            NotificationServiceInterface $notificationService
        ) {
            $this->notificationService = $notificationService;
        }

        /**
         * @param SendNewCampaignAvailableNotification $command
         *
         * @throws \OpenLoyalty\Infrastructure\User\Notification\NotImplementedException
         */
        public function handleSendNewCampaignAvailableNotification(SendNewCampaignAvailableNotification $command): void
        {
            $this->notificationService->sendRewardAvailableNotification($command->toArray());
        }
    }

.. note:: Remember that the function name must be created with the ``handle`` prefix and command name in camel case.

====================================  ====================================
Command class                         Handler function name
====================================  ====================================
SendNewCampaignAvailableNotification  handleSendNewCampaignAvailableNotification
AnotherExampleNotification            handleAnotherExampleNotification
====================================  ====================================



Register a command handler
-----------------

Then you need to register the Command handler class in ``application.yml``

.. code-block:: yml

    // backend/src/Infrastructure/Campaign/Resources/config/application.yml

    services:
        OpenLoyalty\Application\Campaign\CommandHandler\NotificationHandler:
            tags:
                - { name: broadway.command_handler }

.. note:: If every thing is wired up and working don't forget to **write tests!**
