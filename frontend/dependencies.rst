Dependencies
============

We use a lot of dependencies in the whole project. In this section you will find out what we use them in our application.

Installation
------------

.. code-block:: PowerShell

    $ yarn install
    
is used to install all dependencies for a project. The dependencies are retrieved from package.json file, and stored in the ``yarn.lock`` file.

List of dependencies:

- "@uirouter/angularjs" - standard for routing in AngularJS
- "ace-angular" - powerful code editor for Web environments.
- "angular" - open-source front-end web framework mainly maintained by Google
- "angular-animate" - animation system based on CSS functionality
- "angular-chart.js" - we use this module to create charts (requires Chart.js)
- "angular-flash-alert" - A simple lightweight flash message module
- "angular-jwt" - This library provides an HttpInterceptor which automatically attaches a JSON Web Token to HttpClient requests.
- "angular-legacy-sortablejs-maintained" - helps us with sorting items in a list
- "angular-loading-bar" - automatic loading bar in top of the page
- "angular-mm-foundation" - thanks to this module, we can more easily use the Foundation framework.
- "angular-moment" - parsing, validating, manipulating, and displaying dates and times in JavaScript. (requires moment.js)
- "angular-sanitize" - sanitizes an html string by stripping all potentially dangerous tokens.
- "angular-translate" - makes your life much easier when it comes to i18n and l10n including lazy loading and pluralization.
- "autoprefixer" - PostCSS plugin to parse CSS and add vendor prefixes to CSS rules
- "chart.js" - needed for "angular-chart"
- "font-awesome" - icon pack
- "foundation" - advanced responsive front-end framework
- "foundation-sites" - Foundation for Sites provides you with HTML, CSS, & JavaScript to help you quickly prototype.
- "jquery" - JavaScript library
- "jquery-datetimepicker" - jQuery plugin for date, time, or datetime manipulation in form
- "jsoneditor" - needed for "ng-jsoneditor"
- "lodash" - library that helps write more concise and easier to maintain JavaScript.
- "microplugin" - keep code modularized & extensible
- "moment" - needed for "angular-moment"
- "motion-ui" - a Sass library for creating flexible CSS transitions and animations.
- "ng-jsoneditor" - we use it to edit translations
- "ng-pattern-restrict" - allowing certain inputs based on a regex pattern, preventing the user from inputting anything invalid.
- "ng-showdown" - Markdown to HTML converter
- "ng-simplemde" - Markdown editor (requires simplemde)
- "ng-table" - table with sorting and filtering
- "pickadate" - jQuery date & time input picker.
- "restangular" - AngularJS service to handle Rest API Restful Resources properly and easily,
- "select2" - a customizable select box with support for searching, tagging, remote data sets
- "selectize" - custom selectboxes
- "sifter" - Sifter is a client and server-side library for textually searching arrays and hashes of objects by property
- "simplemde" - needed for "ng-simplemde"
- "sortablejs" - library for reorderable drag-and-drop lists
- "ui-select" - a native AngularJS implementation of Select2/Selectize

Scripts:
------------

To start the development server enter:

.. code-block:: PowerShell

    $ npm run start

To start build production package:

.. code-block:: PowerShell

    $ npm run build
    
or for win32 systems:
 
.. code-block:: PowerShell

    $ npm run build:win32
    
