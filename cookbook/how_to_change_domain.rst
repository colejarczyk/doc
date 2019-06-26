How to change the domain
====================

There are many possible ways to run Open Loyalty as a production instance. The preferred way by Open Loyalty's core
team is running Open Loyalty on Kubernetes cluster. It doesn't matter if it is Amazon ESK, Google Kubernetes Engine or
your own k8s cluster. The idea is the same. The second way, is just to run Open Loyalty as fast as it can be and
make it available for everyone. I will focus on both options.


Using Docker and Docker Compose
-------------------------------

The easiest way is to use Docker Compose and provided docker images with Open Loyalty's code and infrastructure.
To change the domain, just copy below docker-compose configuration and paste it to the docker-compose.yml file.

.. code-block:: yaml

    version: "2"

    services:
      php:
        container_name: openloyalty_backend
        image: divante/open-loyalty-fpm
        links:
          - db
          - elk
          - mail
        depends_on:
          - db
        env_file:
            - .env
        environment:
          - frontend_customer_panel_url=http://openloyalty.dev:8183/client
          - frontend_password_reset_url=openloyalty.dev:8183/client#!/password/reset
      nginx:
        container_name: openloyalty_frontend
        image: divante/open-loyalty-web
        links:
          - php
        ports:
          - "80:80"
          - "8182:3001"
          - "8183:3002"
          - "8184:3003"
        command: bash -c "sed -i -e 's@"http://openloyalty.localhost/api"@'\"http://openloyalty.dev/api\"'@g' /var/www/openloyalty/front/config.js && nginx -g 'daemon off;'"
      elk:
        container_name: openloyalty_elk
        image: elasticsearch:2.2
      db:
        container_name: openloyalty_db
        image: postgres:9
        env_file:
            - .env
      mail:
        container_name: openloyalty_mail
        image: mailhog/mailhog
        ports:
          - "8186:8025"

Then change "openloyalty.dev" with your custom domain or public IP address. The next step is to run docker-compose.

.. code-block:: bash

    docker-compose up

That's it.

But how to create different domains for admin, client and pos?
--------------------------------------------------------------

First of all, remove from the docker-compose follow ports for Nginx container and leave only port 80.

.. code-block:: yml

    ports:
      - "8182:3001"
      - "8183:3002"
      - "8184:3003"

The next step is to add a volume to the nginx container so it will mount virtual hosts files to the Nginx configuration directory.

.. code-block:: yml

    volumes:
      - './prod/web:/etc/nginx/conf.d'

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
        server_name client.openloyalty.localhost www.client.openloyalty.localhost;

        root /var/www/openloyalty/front;
        index client/index.html;
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

Here is an example of config.yml file which has ConfigMap with content of config.js and parameters.yml file.
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
              window.OpenLoyaltyConfig = {
                  "apiUrl": "https://example.com/api",
                  "dateFormat": "YYYY-MM-DD",
                  "dateTimeFormat": "YYYY-MM-DD HH:mm",
                  "perPage": 20,
                  "debug": false,
                  "modules": []
              };
      parameters.yml: |
        parameters:
            database_host: db
            database_port: null
            database_name: openloyalty
            database_user: openloyalty
            database_password: openloyalty
            database_driver: pdo_pgsql
            database_version: 9
            elastica:
                hosts:
                    - 'elk:9200'
            secret: ThisTokenIsNotSoSecretChangeIt
            jwt_private_key_path: '%kernel.root_dir%/var/jwt/private.pem'
            jwt_public_key_path: '%kernel.root_dir%/var/jwt/public.pem'
            jwt_key_pass_phrase: ''
            jwt_token_ttl: 86400
            pagination_per_page: 10
            mailer_transport: smtp
            mailer_host: smtp.example.com
            mailer_user: null
            mailer_password: null
            mailer_port: 25
            mailer_encryption: null
            mailer_from_address: open@oloy.com
            mailer_from_name: open@oloy.com
            frontend_password_reset_url: '%env(frontend_password_reset_url)%'
            frontend_activate_account_url: '%env(frontend_activate_account_url)%'
            frontend_customer_panel_url: '%env(frontend_customer_panel_url)%'
            env(frontend_password_reset_url): 'example.com:8182/#!/change-password?token='
            env(frontend_activate_account_url): '#!/customer/panel/customer/registration/activate'
            env(frontend_customer_panel_url): 'http://example.com:8182/'
            ecommerce_address: 'http://ecommerce.local'
            es_max_result_window_size: 2000000
            fallback_frontend_translations_file: english.json
            campaign_photos_adapter: campaign_photos_local
            campaign_photos_adapter_env: CAMPAIGN_PHOTOS_ADAPTER
            level_photos_adapter: level_photos_local
            level_photos_adapter_env: LEVEL_PHOTOS_ADAPTER
            earning_rule_photos_adapter: earning_rule_photos_local
            earning_rule_photos_adapter_env: EARNING_RULE_PHOTOS_ADAPTER
        ---

Now we can create a deployment for PHP container. Most of the configuration is related to run image as a container and k8s
polices but take a look at volumeMounts and volumes. volumneMounts is where we mount volume named "parameters" to the
specific file in the container. In the volumne section, volume name "parameters" is defined and it's content is
get from ConfigMap at key "parameters.yml".

We change Open Loyalty configuration using our own configuration defined in ConfigMap and just replace file at the
container with our own file.

.. code-block:: yaml

    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      labels:
        app: php
      name: php
      namespace: test
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
          - image: divante-ltd/openloyalty/fpm:2.7.1
            name: php
            env:
            - name: APP_DB_HOST
              value: db
            - name: APP_DB_PORT
              value: "5432"
            - name: APP_DB_USER
              value: openloyalty
            - name: APP_DB_PASSWORD
              value: openloyalty
            - name: APP_DB_NAME
              value: openloyalty
            - name: ELK_HOST
              value: elk
            ports:
            - containerPort: 9000
            volumeMounts:
            - mountPath: /var/www/openloyalty/app/config/parameters.yml
              name: parameters
              subPath: parameters.yml
          volumes:
          - name: parameters
            configMap:
              name: app
              items:
                - key: parameters.yml
                  path: parameters.yml
        ---

The parameters.yml file is not the only file we need to replace to change default domain "openloyalty.localhost". The
second file is config.js file, but the idea is the same. The same volumeMounts replaces config.js file with volumne named
"config" and volume named "config" is created from the configMap under key "config.js". The content is copied from configMap
to the config.js file.

.. code-block:: yaml

    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: web
      namespace: test
    spec:
      replicas: 1
      strategy:
        type: Recreate
      template:
        metadata:
          labels:
            app: web
        spec:
          imagePullSecrets:
          - name: registry
          containers:
          - image: divante-ltd/openloyalty/web:2.7.1
            name: openloyalty-web
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

This is the general idea of how to change the domain using k8s and implementing it may be a little bit different depending on which provider do you use: Amazon, Google, Alibaba or your own k8s instance.
