API
===

Used library
------------
We’re using a few libraries to serve RESTful API, it’s automatically generated documentation and JWT Tokens used
to authenticate a user. More information about API, requests and response is available at
`here <http://open-loyalty.readthedocs.io/en/latest/api/index.html>`_.

**FOSRestBundle**

This bundle provides various tools to rapidly develop RESTful API's & applications with Symfony. Features include:
A View layer to enable output and format agnostic Controllers
A custom route loader to generate url's following REST conventions
Accept header format negotiation including handling for custom mime types
RESTful decoding of HTTP request body and Accept headers
Exception controller for sending appropriate HTTP status codes

https://symfony.com/doc/master/bundles/FOSRestBundle/index.html

**NelmioDocAPI**

The NelmioApiDocBundle bundle allows you to generate documentation in the OpenAPI (Swagger) format and provides a sandbox to interactively browse the API documentation.

https://symfony.com/doc/current/bundles/NelmioApiDocBundle/index.html

**LexikJWTAuthenticationBundle**

This bundle provides JWT (Json Web Token) authentication for your Symfony API.

https://github.com/lexik/LexikJWTAuthenticationBundle/blob/master/Resources/doc/index.md

**JWTRefreshTokenBundle**

The purpose of this bundle is manage refresh tokens with JWT (Json Web Tokens) in an easy way. This bundles uses LexikJWTAuthenticationBundle. At the moment only supports Doctrine ORM.

https://github.com/gesdinet/JWTRefreshTokenBundle

RESTful API
-----------

Not described yet.

JWT tokens
----------

Not described yet.

How to authenticate
-------------------

Not described yet.

How to use
----------

Not described yet.

Contexts
--------

Open Loyalty has context which is basically three different types of users.

There is an admin context who is responsible for managing whole loyalty platform.

Second context is a customer context, a person who registered to the loyalty program and the third last context is a
seller. It’s usually a merchant with physical store that is handling customer.

Each context, an therefore each user, has different permissions and can use different API endpoints.

API assumptions
---------------

API and it’s naming follows convention from contexts by prefixing their names. So only the customer can
use ``/api/customer`` and seller can use ``/api/seller``.

If an endpoint is prefixed with ``/api/admin`` or is not prefixed with any context, by default is available only
for an administrator.

However, there are some exceptions from this convention. The best examples are endpoints from the UserBundle and
prefixed with ``/api/customer``. Most of them are available only in the administrator context,
but some of them are also available for a customer like endpoint ``/api/customer/{customer}``.
It’s available for an administrator to view any customer but it’s also available for a customer to view only
his own data. It’s restricted in the code.

Why I see 404?
--------------

Open Loyalty uses ``/api`` for all API endpoints so there is no ``/`` route in application. If route is not found,
then by default 404 is returned.
