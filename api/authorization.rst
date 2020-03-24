.. index::
   single: Authorization

Authorization
=============

This part of the documentation is about the authorization process in the Open Loyalty platform through the API. Open Loyalty uses two types of
authorization: JSON Web Tokens and permanent API Tokens. In order to check this configuration, please set up your local
copy of the Open Loyalty platform and change *localhost* to your address.

LDAP
----

By default Open Loyalty authenticates admin users using database. This can be changed by set environment
ADMIN_LDAP_AUTHORIZATION_ENABLED to true.

.. note::

    You can enable two authorization methods at the same time but this is not recommended.


JSON Web Token
--------------

Open Loyalty has the JWT authorization configured.

.. tip::

To learn what a JSON Web Token is and how it works, check out `Introduction to JSON Web Tokens <https://jwt.io/introduction/>`

.. note::

    The JWT authorization process is used by frontend applications.

Obtain an access token
^^^^^^^^^^^^^^^^^^^^^^

Send a request with the following parameters:

Definition
''''''''''

.. code-block:: text

    POST /api/<user_type>/login_check

+---------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter     | Parameter type | Description                                                                                                                                                         |
+===============+================+=====================================================================================================================================================================+
| _username     | request        | For <user_type>=admin use username, for <user_type>=customer use e-mail address or loyalty card number or phone number, for <user_type>=seller use e-mail address   |
+---------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _password     | request        | User password                                                                                                                                                       |
+---------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <user_type>   | query          | Use one of: admin, customer, seller                                                                                                                                 |
+---------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

    Each user type has different permissions to call API methods.

Example
'''''''

.. code-block:: bash

    curl http://localhost:8181/api/admin/login_check
        -H 'Content-Type: application/json;charset=UTF-8'
        -H 'Accept: application/json, text/plain, */*'
        --data-binary '{"_username":"admin","_password":"open"}'

Example Response
''''''''''''''''''

.. code-block:: json

    {
        "token":"eyJhbGciOiJSUzI1NiIsInR5cCI6...",
        "refresh_token":"0558f8bb29948c4e54c443f..."
    }

.. note::

    Token and refresh token have been shorten for the documentation purpose by suspension points.

Using JSON Web Token
^^^^^^^^^^^^^^^^^^^^^^

Add authorization header to each request

.. code-block:: text

    Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6...

You can now access any API method you want under the /api prefix.

Example
'''''''

.. code-block:: bash

    curl http://localhost:8181/api/admin/analytics/customers \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

Permanent token
---------------

A permanent token is a constant string value assigned to the admin account in Open Loyalty or a constant value which
is not related to a real user and is stored in the configuration.

Creating a permanent token in the configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to activate a configuration access token, you need to add to a Symfony config value

.. code-block:: text

    parameters:
        master_api_key: 371BBCF483524FD5A837B4095F7FBE96AFD46B678C0F025D5EED0316FD5D7762

Creating a permanent user token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request with the following parameters

Definition
''''''''''

.. code-block:: text

    POST /api/admin/data

+----------------------+----------------+-------------------------------------------------------------------+
| Parameter            | Parameter type |  Description                                                      |
+======================+================+===================================================================+
| admin[firstName]     | request        |  First name                                                       |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[lastName]      | request        |  Last name                                                        |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[phone]         | request        |  Phone number                                                     |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[email]         | request        |  E-mail address (required)                                        |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[plainPassword] | request        |  Plain password (required if admin[external]=0                    |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[external]      | request        |  Allows to define permanent token. Set 1 if true, otherwise 0     |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[apiKey]        | request        |  Permanent token (required if admin[external]=1                   |
+----------------------+----------------+-------------------------------------------------------------------+
| admin[isActive]      | request        |  Set account active. Set 1 if active, otherwise 0                 |
+----------------------+----------------+-------------------------------------------------------------------+

Example
'''''''

.. code-block:: bash

    curl http://localhost:8181/api/admin/data \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "admin[email]=administrator@example.com" \
        -d "admin[external]=1" \
        -d "admin[apiKey]=customPermanentToken" \
        -d "admin[isActive]=1"

Example Response
''''''''''''''''''

.. code-block:: text

    STATUS: 200 OK

Example Fail Response
'''''''''''''''''''''''

.. code-block:: text

    STATUS: 400 Bad Request

.. code-block:: json

    {
      "form": {
        "children": {
          "firstName": {},
          "lastName": {},
          "phone": {},
          "email": {
            "errors": [
              "This value is already used."
            ]
          },
          "plainPassword": {},
          "external": {},
          "apiKey": {
            "errors": [
              "This value should not be blank."
            ]
          },
          "isActive": {}
        }
      },
      "errors": []
    }

Create a permanent user token using the Admin Cockpit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new account in the administration panel.

.. note::

    The administration panel is available at http://localhost:8182/
    To log in, use the standard username "admin" and password "open".

Mark a new account as "external" and provide an "Api key".

.. image:: images/permanent_token_setting.png

How to use a permanent token
^^^^^^^^^^^^^^^^^^^^^^^^^^

A permanent token can be provided using headers or a query parameter.

Using headers
''''''''''''

.. code-block:: bash

    curl http://localhost:8181/api/admin \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "X-AUTH-TOKEN: customPermanentToken"

Using a query parameter
'''''''''''''''''''''

.. code-block:: bash

    curl http://localhost:8181/api/admin?auth_token=customPermanentToken \
        -X "GET" -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
