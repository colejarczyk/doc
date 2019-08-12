Kubernetes
============

Overview
--------

Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services,
that facilitates both declarative configuration and automation. It has a large, rapidly growing ecosystem.
Kubernetes services, support, and tools are widely available.

We recommend kubernetes as a production environment. Because of different clients' requirements we are not able to
provide the best configuration and each client should adjust configuration to their needs.

In this document we share general Kubernetes manifests skeleton which is runnable in Minikube. If you want to deploy Open Loyalty on
AWS you have to adjust these scripts. For example you have to replace services as standalone containers to external
services provided by AWS.

Manifests
---------

Credentials for docker registry used in other manifests

.. literalinclude:: /developer/installation/manifests/__secret.yml
   :language: yaml

Configuration files for services (e.g. parameters.yml for Symfony)

.. literalinclude:: /developer/installation/manifests/config.yml
   :language: yaml

Persistent volumes

.. literalinclude:: /developer/installation/manifests/pv.yml
   :language: yaml

Persistent volumes claims

.. literalinclude:: /developer/installation/manifests/storage.yml
   :language: yaml

Deployment and services. This file contains manifests for all services which are required to run OpenLoyalty and additional ones
like Kibana, Logstash etc. You can comment it.

.. literalinclude:: /developer/installation/manifests/deployment.yml
   :language: yaml

Ingress configuration

.. literalinclude:: /developer/installation/manifests/ingress.yml
   :language: yaml

How to run OL on Minikube
-------------------------

We assume that you have experience with kubernetes; some details were skipped.

1. Install Minikube (`go to installation guideline <https://kubernetes.io/docs/getting-started-guides/minikube/>`_)

2. Start minikube

.. code-block:: bash

    minikube start

3. Obtain minikube's IP by

.. code-block:: bash

    minikube ip

4. Add bellow addresses to /etc/hosts (replace IP addresses to obtained above)

.. code-block:: bash

    192.168.99.100 admin.example.com
    192.168.99.100 client.example.com
    192.168.99.100 pos.example.com
    192.168.99.100 api.example.com

5. Create a namespace

.. code-block:: bash

    kubectl create namespace openloyalty

6. Create new or reuse `__secret.yml` file

.. literalinclude:: manifests/__secret.yml
   :language: yaml

.. code-block:: bash

    ``kubectl create secret docker-registry registry --docker-server=<server_name:port> --docker-username=<username> --docker-password=<password> --docker-email=example@example.com --dry-run -o yaml``

7. Apply secret file

.. code-block:: bash

    kubectl -n openloyalty apply -f __secret.yml

8. Create persistant volumes. In this example we provide storages with manual class name. Make sure that persistent
volumes paths defined in manifests are empty. If not, try to log in to minikube (minikube ssh) and remove it.

.. code-block:: bash

    kubectl -n openloyalty apply -f pv.yml

9. Apply the rest of manifests. Default registry is registry-1.divante.pl:5000/openloyalty/. You can change it in
deployment.yml. Make sure that you have correct credentials.

.. code-block:: bash

    kubectl -n openloyalty apply -f storage.yml
    kubectl -n openloyalty apply -f config.yml
    kubectl -n openloyalty apply -f deployment.yml
    kubectl -n openloyalty apply -f ingress.yml

10. Make sure that all containers are running

.. code-block:: bash
    kubectl -n openloyalty get pods

11. Log in to php-* container

.. code-block:: bash
    kubectl -n openloyalty exec -it php-6c4b5b8cb9-vq252 bash

and execute bellow commands, which set proper ownership of directories:

.. code-block:: bash

    root@php-6c4b5b8cb9-vq252:/var/www/openloyalty# chown -R www-data:www-data .

Before initializing application sample data make sure that current user is www-data:

.. code-block:: bash

    root@php-6c4b5b8cb9-vq252:/var/www/openloyalty# su www-data

If you wish to set up full sample data, good for demo purposes:

.. code-block:: bash

    www-data@php-6c4b5b8cb9-vq252:~/openloyalty$ phing setup

And if you wish to initialize the application with just basic data, which is good for production purposes:

.. code-block:: bash

    www-data@php-6c4b5b8cb9-vq252:~/openloyalty$ phing basic-setup

13. Open the panels in your browser

`http://admin.example.com <http://admin.example.com>`_

`http://client.example.com <http://client.example.com>`_

`http://pos.example.com <http://pos.example.com>`_

`http://api.example.com <http://api.example.com>`_
