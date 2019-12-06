How to add new field to entity
==============================

Open Loyalty contains two main types of entities: ORM and Event source aggregate entities (according to CQRS pattern).
More details about architecture solutions you can find in architecture section of our documentation.

ORM entities ane entities which are stored to database (PostgreSQL). Doctrine is persistence manager for that entities.
Event source aggregate entities are managed by Brodway library and object of these type are stored in ElasticSearch as
projections and in database (PostgreSQL) as event store.

ORM entity
----------

One of an example of ORM entity in Open Loyalty is Campaign object. Let's assume that we want to add new field to
campaign entity with name ``title`` and type string.

Entity object
^^^^^^^^^^^^^

Add property to ``src/Domain/Campaign/Campaign.php``.

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
    If you want to add translatable field you have to include instructions from ``How to create a translatable field``
    during adding field.

Then we have to extend functions responsible creation object from array data.

.. code-block:: php

    public function setFromArray(array $data)
    {
        ...
        if (array_key_exists('title', $data)) {
            $this->title = $data['title'];
        }
        ...
    }

Next open class ``src/Infrastructure/Campaign/Model/Campaign.php`` where we have to extend function responsible for
Campaign's deserialization.

.. code-block:: php

    public function toArray(): array
    {
        ...
        'title' => $this->title,
        ...
    }

.. note::
    Not all classes requires extend these functions.

Doctrine
^^^^^^^^

In this step we have to inform doctrine about new field. Localize file
``src/Infrastructure/Campaign/Persistence/Doctrine/ORM/Campaign.orm.yml`` and in ``fields`` section add:

.. code-block:: yaml

    title:
        type: string
        nullable: true
        column: title

Now we can persist schema changes to database. Execute symfony command in console:

.. code-block:: bash

    bin/console doctrine:schema:update --force

After successfully execution fields is ready to use by backend application, but is not used for controllers
and is not visible on frontend application.

Serialization
^^^^^^^^^^^^^

Next we have to inform serialization about our new field. Add to file
``src/Infrastructure/Campaign/Resources/config/serializer/Campaign.yml`` in section ``properties`` if new fields are
excluded as default.

.. code-block:: yaml

    title:
      exclude: false

.. note::
    Modification serialization config files usually requires remove cache in order to work.

Controllers
^^^^^^^^^^^

Campaign entity has possibility to store new data in field, but now we have to pass some values from UI. In order to do
it we have to find controller and action responsible for for example add new campaign.

In first line of ``src/Ui/Rest/Controller/Campaign/Post.php`` file we see that data is taken from ``CampaignFormType``
object. Let's open it and add to ``build`` function:

.. code-block:: php

        $builder->add('title', TextType::class, [
            'required' => false,
        ]);

Add field to UI
^^^^^^^^^^^^^^^

Add to file ``frontend/src/modules/admin.campaign/templates/add-campaign.html``

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

Add to file ``frontend/src/modules/admin.campaign/templates/edit-campaign.html``

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

Example of a event source aggregate entity in Open Loyalty is Customer object. Let's assume that we want to add new field to
customer entity with name ``code`` and type string.

Domain entity
^^^^^^^^^^^^^

Like in above example, let's start from domain object ``src/Domain/User/Customer.php``. As you can noticed this class extend `SnapableEventSourcedAggregateRoot`, so it's
confirmation that this entity is aggregate entity and use CQRS pattern. Add to this entity property `code` with getter.

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

Additionally let's assume that we want to set value of this field only during registration process. So we have to find
method responsible for applying changes to domain object when customer is being registered. Bellow method is executed
when application will be going to register customer.

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

Controller responsible for registering customer is located in file ``backend/src/Ui/Rest/Controller/User/Customer/PostRegister.php``.
FormType associated with register customer is ``src/Infrastructure/User/Form/Type/CustomerRegistrationFormType.php``.
There we have to add our a new field:

.. code-block:: php

        $builder->add(
            'code',
            TextType::class,
            [
                'label' => 'Code',
                'required' => true,
            ]
        );

Now Open Loyalty is ready to persist a new field when customer is being registered, but we have to make more adjustments.

Projections
^^^^^^^^^^^

When event CustomerWasRegistered is throw then projectors handle this event and update/create projections. In order to
find all listeners which listening for this event then you have to find all services with tag
`broadway.domain.event_listener` and with a method ``applyCustomerWasRegistered``. One of that listener is
``src/Domain/User/ReadModel/CustomerDetailsProjector.php``. Projector does not persist a domain object, but operate on
a read model object. For example ``Customer`` is persisted in projections using ``src/Domain/User/ReadModel/CustomerDetails.php``.

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

Last thing is update Elastic Search index for Customer Details projection. Go to
``backend/src/Infrastructure/User/Repository/Elasticsearch/CustomerIndex.php`` and add a new field to an index.

.. code-block:: php

    'code' => [
        'type' => 'keyword',
    ],

.. note::
    Changing index in Elastic Search requires recreating all read models in order to apply changes to an index.

.. code-block:: bash
    bin/console oloy:user:projections:index:create --drop-old
    bin/console oloy:utility:read-models:recreate --force

Add field to UI
^^^^^^^^^^^^^^^

Adding field to UI is similar like in ORM Entities.
