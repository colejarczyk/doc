Security
========

These endpoints will allow you to easily manage password and token-related matters.



Password reset request (customer)
---------------------------------

Invoking this method will send a message to the user with a password reset URL.
You need to call the ``/api/<storeCode>/customer/password/reset/request`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/password/reset/request

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                         | query          | Code of the store the customer belongs to.        |
+-------------------------------------+----------------+---------------------------------------------------+
| username                            | string         | Customer's e-mail address                         |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/password/reset/request \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "username=user@example.com"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "success": true
    }



Set new password after requesting a new password
------------------------------------------------

To reset the password for a customer who requested a new password,, you need to call the ``/api/password/reset`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/password/reset

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| token                               | query          | Token received during resetting the password      |
+-------------------------------------+----------------+---------------------------------------------------+
| reset[plainPassword]                | query          | New password                                      |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/password/reset \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "reset[plainPassword]=example123!@#" \
        -d "token=AIENe11JjR2kj3XGiWuZmQ88gZYAgM7VR5inxtbswaY"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* or *AIENe11JjR2kj3XGiWuZmQ8...* authorization token are an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

     Your password must be at least 8 characters long.
     Your password must include both upper and lower case letters.
     Your password must include at least one number.
     Your password must contain at least one special character.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "success": true
    }



Change logged-in customer's password
------------------------------------

To change a logged-in customer's password, you need to call the ``/api/<storeCode>/customer/password/change`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/customer/password/change

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                         | query          | Code of the store the customer belongs to.        |
+-------------------------------------+----------------+---------------------------------------------------+
| currentPassword                     | query          | Current password                                  |
+-------------------------------------+----------------+---------------------------------------------------+
| plainPassword                       | query          | New password                                      |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/customer/password/change \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "currentPassword=example123!@#" \
        -d "plainPassword=example321!@#"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

     Your password must be at least 8 characters long.
     Your password must include both upper and lower case letters.
     Your password must include at least one number.
     Your password must contain at least one special character.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "success": true
    }

Change logged-in admin's password
---------------------------------

To change a logged-in admin's password, you need to call the ``/api/<storeCode>/admin/password/change`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/<storeCode>/admin/password/change

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| <storeCode>                         | query          | Code of the store to chance password.             |
+-------------------------------------+----------------+---------------------------------------------------+
| currentPassword                     | query          | Current password                                  |
+-------------------------------------+----------------+---------------------------------------------------+
| plainPassword                       | query          | New password                                      |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/DEFAULT/admin/password/change \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "currentPassword=example123!@#" \
        -d "plainPassword=example321!@#"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

.. note::

     Your password must be at least 8 characters long.
     Your password must include both upper and lower case letters.
     Your password must include at least one number.
     Your password must contain at least one special character.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "success": true
    }



Password reset request (admin)
------------------------------

Invoking this method will send a message to the admin user's email with the password reset URL.
You need to call the ``/api/password/reset/request`` endpoint with the ``POST`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    POST /api/password/reset/request

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+
| username                            | query          | User name who recovers the password               |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/password/reset/request \
        -X "POST" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..." \
        -d "username=admin"

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    {
      "success": true
    }



Log out current user
--------------------

To log out the current user, you need to call the ``/api/token/revoke`` endpoint with the ``GET`` method.

Definition
^^^^^^^^^^

.. code-block:: text

    GET /api/token/revoke

+-------------------------------------+----------------+---------------------------------------------------+
| Parameter                           | Parameter type | Description                                       |
+=====================================+================+===================================================+
| Authorization                       | header         | Token received during authentication              |
+-------------------------------------+----------------+---------------------------------------------------+

Example
^^^^^^^

.. code-block:: bash

    curl http://localhost:8181/api/token/revoke \
        -X "GET" \
        -H "Accept: application/json" \
        -H "Content-type: application/x-www-form-urlencoded" \
        -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6..."

.. note::

    The *eyJhbGciOiJSUzI1NiIsInR5cCI6...* authorization token is an example value.
    Your value may be different. Read more about Authorization :doc:`here </api/authorization>`.

Example Response
^^^^^^^^^^^^^^^^^^

.. code-block:: text

    STATUS: 200 OK

.. code-block:: json

    (no content)
