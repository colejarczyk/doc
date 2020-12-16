How to change the domain
====================

There are many possible ways to run Open Loyalty as a production instance. The preferred way by Open Loyalty's core
team is running Open Loyalty on Kubernetes cluster. It doesn't matter if it is Amazon ESK, Google Kubernetes Engine or
your own k8s cluster. The idea is the same. The second way, is just to run Open Loyalty as fast as it can be and
make it available for everyone. I will focus on both options.


Using Docker and Docker Compose
-------------------------------

The easiest way is to use Docker Compose and provided docker images with Open Loyalty's code and infrastructure.
To change the domain, just add bellow environments to your php container in docker-compose.yml file.

.. code-block:: yaml

    services:
      php:
        ...
        environment:
          - api_url=http://openloyalty.dev/api
          - admin_url=http://openloyalty.dev:8182/
          - customer_url=http://openloyalty.dev:8183/

Then change "openloyalty.dev" with your custom domain or public IP address. The next step is to restart containers
defined in  docker-compose.

But how to create different domains for admin, client and pos?
--------------------------------------------------------------

First of all, remove from the docker-compose follow ports for Nginx container and leave only port 80.

.. code-block:: yml

    ports:
      - "8182:3001"
      - "8184:3003"

The next step is to add a volume to the nginx container so it will mount virtual hosts files to the Nginx configuration directory.

.. code-block:: yml

    volumes:
      - './prod/web:/etc/nginx/conf.d/front.conf'

Final configuration for Nginx container should look like

.. code-block:: yml

      nginx:
        container_name: openloyalty_frontend
        image: divante/open-loyalty-web
        links:
          - php
        ports:
          - "80:80"
        volumes:
          - './prod/web:/etc/nginx/conf.d'
        command: bash -c "sed -i -e 's@"http://openloyalty.localhost/api"@'\"http://openloyalty.dev/api\"'@g' /var/www/openloyalty/front/config.js && nginx -g 'daemon off;'"

The last step is to adjust frontend.conf configuration file

.. code-block:: json

    server {
        listen 80;
        listen [::]:80;
        server_name admin.openloyalty.localhost www.admin.openloyalty.localhost;

        root /var/www/openloyalty/front;
        index admin/index.html;
        location ~* \.(?:js|css|jpg|jpeg|gif|png|svg|ico|pdf|html|htm)$ {
        }
    }

    server {
        listen 80;
        listen [::]:80;
        server_name pos.openloyalty.localhost www.pos.openloyalty.localhost;

        root /var/www/openloyalty/front;
        index pos/index.html;
        location ~* \.(?:js|css|jpg|jpeg|gif|png|svg|ico|pdf|html|htm)$ {
        }
    }

Using k8s cluster
-----------------

We recommend to use k8s for real production usage. The idea behind k8s is that it allows to mount a single file which
docker and docker-compose doesn't.

Here is an example of config.yml file which has ConfigMap with content of config.js and Symfony config files.
This content will be used in the deployment file to replace existing files with configuration from ConfigMap.

.. code-block::

    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: app
      namespace: test
    data:
      config.js: |-
              const config = {
                  "apiUrl": "https://example.com/api",
                  "dateFormat": "YYYY-MM-DD",
                  "dateTimeFormat": "YYYY-MM-DD HH:mm",
                  "perPage": 20,
                  "debug": false,
                  "modules": []
              };
              window.OpenLoyaltyConfig = config;
      .env.prod: |
        APP_ENV=prod
        api_url=http://openloyalty.localhost/api
        admin_url=http://openloyalty.localhost:8182/
        customer_url=http://openloyalty.localhost:8183/
        ---

Now we can create a deployment for PHP container. Most of the configuration is related to run image as a container and k8s
polices but take a look at volumeMounts and volumes. volumeMounts is where we mount volume named "parameters" to the
specific file in the container. In the volume section, volume name "parameters" is defined and it's content is
get from ConfigMap at key ".env.prod".

We change Open Loyalty configuration using our own configuration defined in ConfigMap and just replace file at the
container with our own file.

.. code-block:: yaml

    apiVersion: extensions/v1
    kind: Deployment
    metadata:
      labels:
        app: php
      name: php
      namespace: openloyalty
    spec:
      replicas: 1
      strategy:
        type: Recreate
      template:
        metadata:
          labels:
            app: php
        spec:
          imagePullSecrets:
            - name: registry
          containers:
            - image: registry-1.divante.pl:5000/openloyalty/fpm-framework:4.2.0
              name: php
              ports:
                - containerPort: 9000
              volumeMounts:

                ...

                - mountPath: /var/www/openloyalty/.env.prod
                  name: parameters
                  subPath: .env.prod

                ...
          restartPolicy: Always
          volumes:

            ...

            - name: parameters
              configMap:
                name: app
                items:
                  - key: .env.prod
                    path: .env.prod

            ...
        ---

The .env.prod file is not the only file we need to replace to change default domain "openloyalty.localhost". The
second file is config.js file, but the idea is the same. The same volumeMounts replaces config.js file with volumne named
"config" and volume named "config" is created from the configMap under key "config.js". The content is copied from configMap
to the config.js file.

.. code-block:: yaml

    apiVersion: extensions/v1
    kind: Deployment
    metadata:
      name: frontend
      namespace: openloyalty
    spec:
      replicas: 1
      strategy:
        type: Recreate
      template:
        metadata:
          labels:
            app: frontend
        spec:
          imagePullSecrets:
            - name: registry
          containers:
            - image: registry-1.divante.pl:5000/openloyalty/frontend:4.2.0
              name: openloyalty-frontend
              ports:
                - containerPort: 80
              volumeMounts:
                - mountPath: /var/www/openloyalty/front/config.js
                  name: config
                  subPath: config.js
          restartPolicy: Always
          volumes:
            - name: config
              configMap:
                name: app
                items:
                  - key: config.js
                    path: config.js
    ---

This is the general idea of how to change the domain using k8s and implementing it may be a little bit different
depending on which provider do you use: Amazon, Google, Alibaba or your own k8s instance.
