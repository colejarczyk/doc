Structure
=========

The whole part of the application frontend is located in the frontend catalog. You will find the following subdirectories:

- ``dev`` - additional scripts used in package.json.
- ``dist`` - directory containing the result of the bundler module operation
- ``node_modules`` - directory with installed npm packages
- ``rancher`` - scripts that use rancher
- ``src`` - source of main application.

There are several additional files in the root directory.

- ``webpack.config`` - webpack configuration file
- ``package.json`` - list of packages needed to run the environment, 
- ``.sass-lint.yml`` - rules for Sass / SCSS files
- ``.eslintrc`` - ESLint configuration file. Allows you to specify the JavaScript language options you want to support.

We mainly work in the ``src`` folder, therefore we will describe its structure in a deeper way.

+---------------------+-------------------------------------------------------------------------------+
| Catalog name        | Description                                                                   |
+=====================+===============================================================================+
| components          | In the ``components folder`` there are two main components from which the     |
|                     | application is built. These are:                                              |
|                     |                                                                               |
|                     | - ``AdminFieldsetBlockDirective.js`` - block                                  |
|                     | - ``AdminFieldsetRowDirective.js`` - row                                      |
+---------------------+-------------------------------------------------------------------------------+
| fonts               | Here you can find all font files                                              |
+---------------------+-------------------------------------------------------------------------------+
| img                 | All graphic files are located here                                            |
+---------------------+-------------------------------------------------------------------------------+
| modules             | The ``modules`` directory contains all containers used in various parts of    |
|                     | the application. Each module contains controller, service and module          |
|                     | configuration file. The ``templates`` directory contains .html files that     |
|                     | represent individual pages of the application                                 | 
+---------------------+-------------------------------------------------------------------------------+
| scripts             | There are additional scripts in this directory                                |
+---------------------+-------------------------------------------------------------------------------+
| style               | Here are the application styles. We use the SCSS preprocessor to generate     |
|                     | CSS files                                                                     | 
+---------------------+-------------------------------------------------------------------------------+
| templates           | In this directory there are two main ``.html`` templates files:               |                                
|                     |                                                                               |
|                     | - ``admin.html`` - tempolate of admin cockpit app                             |
|                     | - ``pos.html`` - tempolate of point of sale app                               | 
+---------------------+-------------------------------------------------------------------------------+
| root                | In the root directory there are three main ``.js`` files, two of them are     |
|                     | the entry points of the entire application:                                   |
|                     |                                                                               |
|                     | - ``appAdmin.js`` - admin cockpit app                                         |
|                     | - ``appPos.js`` - point of sale app                                           | 
|                     |                                                                               | 
|                     | The third file is ``config.js``. The application settings are stored here     |  
+---------------------+-------------------------------------------------------------------------------+                      
