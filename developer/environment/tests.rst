Unit & integration tests in PHPStorm
====================================

This guideline is about how to configure PHPStorm to run unit & integration tests locally.



Requirements
------------
- docker-compose (>= 1.21)
- docker (>= 18.06)
- PHPStorm (>= 2018.1)



Setup
-----

1. Enter settings: File → Settings → Build, Execution, Deployment → Docker

.. image:: _images/tests_1.png
    :scale: 100%

2. File → Settings → Languages & Frameworks → PHP

a) Configure CLI Interpreter

.. image:: _images/tests_2.png
    :scale: 100%

b) Configure PHP settings

.. image:: _images/tests_3.png
    :scale: 100%

3. File → Settings → Languages & Frameworks → PHP → Test Frameworks and then configure PHPUnit by adding Remote Interpreter

.. image:: _images/tests_4.png
    :scale: 100%

4. Run/Debug Configuration

.. image:: _images/tests_5.png
    :scale: 100%

Now you are able to execute all tests via IDE using green ``Play`` button or ``Run`` menu.
