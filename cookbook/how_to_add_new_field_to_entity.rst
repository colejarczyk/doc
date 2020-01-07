How to add a new field to an entity
===================================

Open Loyalty contains two main types of entities: ORM and Event source aggregate entities (according to CQRS pattern).
You can find more details about architecture solutions in architecture section of our documentation.

ORM entities ane entities which are stored in database (PostgreSQL). Doctrine is persistence manager for that entities.
Event source aggregate entities are managed by Broadway library and objects of this type are stored in ElasticSearch as
projections and in database (PostgreSQL) as event store.

ORM entity
----------

One of examples of ORM entity in Open Loyalty is the Campaign object. Let's assume that we want to add a new field to
the campaign entity with name ``title`` and type string.

Entity object
^^^^^^^^^^^^^

Add a property to ``src/Domain/Campaign/Campaign.php``.

.. code-block:: php

    /**
     * @var string|null
     */
    protected $title;

    /**
     * @return string|null
     */
    public function getTitle(): ?string
    {
        return $this->title;
    }

    /**
     * @param string|null $title
     */
    public function setTitle(?string $title): void
    {
        $this->title = $title;
    }

.. note::
    If you want to add a translatable field you will need to follow instructions from ``How to create a
    translatable field``

Then we have to extend the functions responsible for creation of an object from array data.

.. code-block:: php

    public function setFromArray(array $data)
    {
        ...
        if (array_key_exists('title', $data)) {
            $this->title = $data['title'];
        }
        ...
    }

Next open the class ``src/Infrastructure/Campaign/Model/Campaign.php`` to extend the function responsible for

.. code-block:: php

    public function toArray(): array
    {
        ...
        'title' => $this->title,
        ...
    }

.. note::
    Not all classes require extending these functions.

Doctrine
^^^^^^^^

Next, we have to let Doctrine know about the new field. Find the file
``src/Infrastructure/Campaign/Persistence/Doctrine/ORM/Campaign.orm.yml`` and in the ``fields`` section add:

.. code-block:: yaml

    title:
        type: string
        nullable: true
        column: title

Now we can persist schema changes to the database. Execute the following Symfony command in the console:

.. code-block:: bash

    bin/console doctrine:schema:update --force

After successful execution, the field is ready to use by the backend application, but it is not used in controllers
and is not visible in the frontend application.

Serialization
^^^^^^^^^^^^^

In the next step, we will let serialization know how to treat our new field. In the file
``src/Infrastructure/Campaign/Resources/config/serializer/Campaign.yml`` in section ``properties``, add a clause to
publicize the new field, as they are excluded as default.

.. code-block:: yaml

    title:
      exclude: false

.. note::
    Modification serialization config files usually requires remove cache in order to work.

Controllers
^^^^^^^^^^^

Campaign entity has a possibility to store data in the new field, but now we need a way to pass its value from the user
interface. In order to do that we need to find controllers and actions responsible for adding and editing new campaigns.

In the first line of ``src/Ui/Rest/Controller/Campaign/Post.php`` file we see that data is taken from
``CampaignFormType`` object. Let's open it and add the following to the ``build`` function:

.. code-block:: php

        $builder->add('title', TextType::class, [
            'required' => false,
        ]);

Add a field to UI
^^^^^^^^^^^^^^^^^

Add the following to the ``frontend/src/modules/admin.campaign/templates/add-campaign.html`` file:

.. code-block:: html

    <div class="row">
        <div class="medium-2 small-3 columns">
            <label>{{ "campaign.more_information_title" | translate }} </label>
        </div>
        <div class="medium-10 small-9 columns" form-validation="validate.title.errors">
            <input type="text" ng-model="newCampaign.title"/>
            <span class="prompt">{{ "campaign.title_prompt" | translate }} </span>
        </div>
    </div>

To the file ``frontend/src/modules/admin.campaign/templates/edit-campaign.html`` add:

.. code-block:: html

    <div class="row">
        <div class="medium-2 small-3 columns">
            <label>{{ "campaign.more_information_title" | translate }} </label>
        </div>
        <div class="medium-10 small-9 columns" form-validation="validate.title.errors">
            <input type="text" ng-model="editableFields.title"/>
            <span class="prompt">{{ "campaign.title_prompt" | translate }} </span>
        </div>
    </div>




Event source aggregate entities
-------------------------------

An example of an event source aggregate entity in Open Loyalty is Customer object. Let's assume that we want to add a
new field to the Customer entity with name ``code`` and type string.

Domain entity
^^^^^^^^^^^^^

Like in the example above, let's start with domain object ``src/Domain/User/Customer.php``. As you might have noticed
this class extends `SnapableEventSourcedAggregateRoot` - it's confirmation that this entity is an aggregate entity
and uses CQRS pattern. Add an entity property `code` with getter to this class.

.. code-block:: php

    /**
     * @var string|null
     */
    protected $code;

    /**
     * @return string|null
     */
    public function getCode(): ?string
    {
        return $this->code;
    }

Additionally, let's assume that we want to set the value of this field only during the registration process. To do
that, we need to find the method responsible for applying changes to domain object when customer is being registered.
The method below is executed when application is going to register a customer.

.. code-block:: php

    private function register(CustomerId $userId, array $customerData): void

Calling this method delegates control to another method which should update domain object:

.. code-block:: php

    protected function applyCustomerWasRegistered(CustomerWasRegistered $event): void
    {
        ...
        if (array_key_exists('code', $data)) {
            $this->code = $data['code'];
        }
        ...
    }

Controllers
^^^^^^^^^^^

Controller responsible for registering a customer is located in the file ``backend/src/Ui/Rest/Controller/User/Customer/PostRegister.php``.
FormType associated with register customer is ``src/Infrastructure/User/Form/Type/CustomerRegistrationFormType.php``.
There, we need to add our new field:

.. code-block:: php

        $builder->add(
            'code',
            TextType::class,
            [
                'label' => 'Code',
                'required' => true,
            ]
        );

Now Open Loyalty is ready to persist the new field when customer is being registered, but we have to make a
few more adjustments.

Projections
^^^^^^^^^^^

When event CustomerWasRegistered is thrown, projectors handle the event and update/create projections. In order to find
all listeners which are listening for this event, you have to find all services with tag `broadway.domain.event_listener`
and with method ``applyCustomerWasRegistered`` in them. One of that listeners is
``src/Domain/User/ReadModel/CustomerDetailsProjector.php``. Projector does not persist a domain object, but operates
on a read model object. For example ``Customer`` is persisted in projections using ``src/Domain/User/ReadModel/CustomerDetails.php``.

Let's open this file and update it.

.. code-block:: php

    /**
     * @var string|null
     */
    protected $code;

    /**
     * @return string|null
     */
    public function getCode(): ?string
    {
        return $this->code;
    }

    /**
     * @param string|null $code
     */
    public function setCode(?string $code): void
    {
        $this->code = $code;
    }

.. code-block:: php

    public function serialize(): array
    {
        ...
        'code' => $this->getCode(),
        ...
    }

.. code-block:: php

    public static function deserialize(array $data)
    {
        ...
        if (array_key_exists('code', $data)) {
            $customer->code = $data['code'];
        }
        ...
    }

Then we have to update projector:

.. code-block:: php

    protected function applyCustomerWasRegistered(CustomerWasRegistered $event): void
    {
        ...
        $readModel->setCode($customer->getCode());
        ...
    }

Last thing is to update ElasticSearch index for Customer Details projection. Go to
``backend/src/Infrastructure/User/Repository/Elasticsearch/CustomerIndex.php`` and add a new field to the index.

.. code-block:: php

    'code' => [
        'type' => 'keyword',
    ],

.. note::
    Changing the index in ElasticSearch requires recreating the read models in order to apply changes to an index.

.. code-block:: bash
    bin/console oloy:user:projections:index:create --drop-old
    bin/console oloy:utility:read-models:recreate --force

Add field to UI
^^^^^^^^^^^^^^^

Adding the field to the user interface is analogous to the process presented in ORM Entites section above.
