How to create a new bundle
==========================

Up until 3.x branch, Open Loyalty used standard Symfony division of application into Bundles and Components.
Starting with 4.0, we decided to embrace Domain Driven Design and Hexagonal Architecture principles.
That means every class in the system is placed according to its layer (Domain, Application, User Interface or
Infrastructure) and its bounded context (Core, User, Campaign, Level, Segment, EarningRule and so on).

Bundles are used to group the classes by their bounded context for discoverability and order – and to
group the configuration files by their area of influence.

Creating a new bundle in Open Loyalty is as simple as creating a new bundle in Symfony Framework
(see `Symfony documentation on bundles<https://symfony.com/doc/3.4/bundles.html>`_).
The only difference is the placement of the classes – all of the Symfony-required files will be placed
in the Infrastructure layer.
The bundles in Open Loyalty's core use ``OpenLoyalty<name>Bundle`` name convention, with ``<name>`` being
the bounded context and directory's name.

Create a bundle
---------------

Let’s create OpenLoyaltyAppBundle that will contain our logic.

First of all, create a new directory: ``src/Infrastructure/App`` and then create a class named ``OpenLoyaltyAppBundle``:

.. code-block:: php

    // src/Infrastructure/App/OpenLoyaltyAppBundle.php
    namespace OpenLoyalty\Infrastructure\App;

    use Symfony\Component\HttpKernel\Bundle\Bundle;

    class OpenLoyaltyAppBundle extends Bundle
    {
    }

Then you need to register your newly created bundle in the framework.
Go to ``app/AppKernel.php`` file and add an instance of your bundle to ``$bundles`` array.

.. code-block:: php

    // app/AppKernel.php
    public function registerBundles()
    {
        $bundles = [
            // ...

            // register your bundle
            new OpenLoyalty\Infrastructure\App\OpenLoyaltyAppBundle(),
        ];
        // ...

        return $bundles;
    }

Let’s verify that the bundle has been registered properly, assuming you use Docker:

.. code-block:: bash

    $ docker exec -it --user=www-data open_loyalty_backend bin/console debug:config

Somewhere in the table, you should see the newly created ``OpenLoyaltyAppBundle``

.. code-block:: rst

    Available registered bundles with their extension alias if available
    ====================================================================

     --------------------------------- ------------------------------
      Bundle name                       Extension alias
     --------------------------------- ------------------------------
      ...
      OpenLoyaltyAppBundle             open_loyalty_app
      ...



Configure the new bundle
------------------------

To add configuration to your new bundle, you need to create an Extension for it.
The process is explained thoroughly in `Symfony docs<https://symfony.com/doc/3.4/bundles/extension.html>`_,
but a brief explanation is provided below.

To make the extension visible to symfony, it needs to be in ``DependencyInjection`` directory inside the directory
which has the ``OpenLoyalty<name>Bundle`` class in it.
The name of the extension is the name of the bundle with ``Bundle`` replaced by ``Extension``.

In our example, this means a new directory, ``src/Infrastructure/App/DependencyInjection``, and a new file,
``OpenLoyaltyAppExtension``.
The extension is mostly used to load configuration from a file, but it can also add parameters and more to a container.
To do that you need to import several classes that are included in a file below:

.. code-block:: php

    // src/Infrastructure/App/DependencyInjection/OpenLoyaltyAppExtension.php
    namespace OpenLoyalty\Infrastructure\App/DependencyInjection;

    use Symfony\Component\Config\FileLocator;
    use Symfony\Component\DependencyInjection\ContainerBuilder;
    use Symfony\Component\DependencyInjection\Loader;
    use Symfony\Component\HttpKernel\DependencyInjection\Extension;

    class OpenLoyaltyAppExtension extends Extension
    {
        public function load(array $configs, ContainerBuilder $container)
        {
            $loader = new Loader\YamlFileLoader($container, new FileLocator(__DIR__.'/../Resources/config'));
            $loader->load('services.yml');
        }
    }

The example uses an Open Loyalty convention of creating configuration files in
``src/Infrastructure/<bounded_context>/Resources/config/`` directory.
By convention, the application uses YAML files for their brevity.



Add persistence configuration with Doctrine
-------------------------------------------

Open Loyalty uses PostgreSQL as its main data store and a write DB with Elasticsearch as a read DB.
To make operations on database easier, Doctrine's DBAL and ORM are used.

This means you will sometimes need to create configuration files for your DB entities in order to save and read them.

Entities themselves are placed in Domain layer; the Doctrine configuration belongs to Infrastructure layer
and is placed in the same directory as the bundle class, in ``Persistence/Doctrine/ORM`` subdirectory.

This is also where declarations of Types (``Persistence/Doctrine/Type``) and concrete implementations of repositories
(``Persistence/Doctrine/Repository``) live.

To add configuration to Doctrine, you need to add Doctrine's compiler pass to your bundle's build method:

.. code-block:: php

    use Doctrine\Bundle\DoctrineBundle\DependencyInjection\Compiler\DoctrineOrmMappingsPass;
    use Symfony\Component\DependencyInjection\ContainerBuilder;
    use Symfony\Component\HttpKernel\Bundle\Bundle;

    class OpenLoyaltyAppBundle extends Bundle
    {
        public function build(ContainerBuilder $container)
        {
            // ...

            $container->addCompilerPass($this->buildMappingCompilerPass());

            // ...
        }

        public function buildMappingCompilerPass()
        {
            return DoctrineOrmMappingsPass::createYamlMappingDriver(
                [__DIR__.'/Persistence/Doctrine/ORM' => 'OpenLoyalty\Domain\App'],
                [],
                false,
                ['OpenLoyaltyApp' => 'OpenLoyalty\Domain\App']
            );
        }
    }

An example file can look like this:

.. code-block:: yaml

    OpenLoyalty\Domain\App\SomeRecord:
      type: entity
      repositoryClass: OpenLoyalty\Infrastructure\App\Persistence\Doctrine\Repository\DoctrineSomeRecordRepository
      table: app_some_records
      id:
        recordId:
          type: record_id # This type will be defined in Persistence/Type/RecordIdDoctrineType.php
          column: record_id
      fields:
        someField:
          type: string
        createdAt:
          type: datetime
      uniqueConstraints:
        app_some_record_some_field_idx:
          columns:
            - someField

You can use other files in the current structure as examples.
