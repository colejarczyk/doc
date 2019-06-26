How to create new component/directive
=====================================

For the purposes of this tutorial we create a directive named 'fooBar'. More information about `AngularJS directives <https://docs.angularjs.org/guide/directive>`_.

1. Go to ``src/component/global``
2. Create new folder ``fooBar``
3. Create ``.js`` file ``fooBarDirective``
4. Inside ``fooBarDirective.js`` export custom class ``FooBarDirective`` with constructor
5. At the end of file don't forget to add ``$inject`` property with array of services to inject. In our example, we do not inject anything.
6. You can create custom .html template in path ``fooBar/templates/fooBar.html``

.. code-block:: JavaScript

   /**
    * Defines fooBar directive
    *
    * @class FooBarDirective
    * @constructor
    */

   export default class FooBarDirective {
       constructor() {
           this.restrict = 'A';
           this.require = '?ngModel';
           this.templateUrl = require('./templates/fooBar.html');
           this.scope = {
               value: '=ngModel'
           };
           this.link = function (scope, element, attrs, ctrl) {
             // here function body
           };
       }
       
       // additional metods
   }

   FooBarDirective.$inject = [];

7. Now we must import this class to our main .js file ``appAdmin.js`` or ``posApp.js`` or both if needed.

.. code-block:: javaScript

   import FooBarDirective from './component/global/fooBar/fooBarDirective';

8. Register directive in app*.js file (it's necessary to start directive name with lowercase)

.. code-block:: javaScript

   .directive('fooBar', () => new FooBarDirective());
   
9. Now you can use your custome directive in .html templates

.. code-block:: HTML
   
   <input type="text" ng-model="myModelName" fooBar/>

