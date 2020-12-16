How to enable LDAP authorization
================================

Open Loyalty supports two authorization methods for admin: database and LDAP. Database authorization is default.

.. note::

    LDAP authorization is only supported for administrator users


.. note::

    If administrator authenticated successfully and account doesn't exist in the database, then an account for
this admin will be created.

Enable LDAP
-----------

1. Add these lines to **.env.prod** or create the file if it does not exist:

.. code-block:: yaml

    ADMIN_BASIC_AUTHORIZATION_ENABLED=false
    ADMIN_LDAP_AUTHORIZATION_ENABLED=true

.. note::

    You can enable database and LDAP authorization at the same time but this is not recommended.

2. Set LDAP configuration in the same file

.. code-block:: yaml

    LDAP_HOST=ldap-server
    LDAP_PORT=389
    LDAP_PROTOCOL_VERSION=3
    LDAP_BASE_DN=dc=example,dc=org
    LDAP_SEARCH_DN=cn=admin,dc=example,dc=org
    LDAP_SEARCH_PASSWORD=admin
    LDAP_DN_STRING=cn={username},dc=example,dc=org

Development work
----------------

If you want to work with a mock LDAP server you can add services below to your docker-compose file. The first one is
LDAP server and the second is simple administrator panel to manage LDAP server.

.. code-block:: yaml

  ldap-server:
    container_name: open_loyalty_framework_ldap
    image: osixia/openldap:1.3.0
    ports:
      - 389:389
      - 636:636
    environment:
      LDAP_TLS: "false"

  ldap-panel:
    container_name: open_loyalty_framework_ldap_panel
    image: osixia/phpldapadmin:0.9.0
    environment:
      PHPLDAPADMIN_LDAP_HOSTS: "ldap-server"
      PHPLDAPADMIN_HTTPS: "false"
    ports:
      - 6443:80
    depends_on:
      - ldap-server
