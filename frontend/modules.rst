How to create new module/page
=============================

For the purposes of this tutorial we create a module named 'admin.fooBar'. More information about `AngularJS modules <https://docs.angularjs.org/guide/module>`_.
Each module, in addition to the controller, service and template, has a file named module.js, which contains its configuration.

1. Go to ``src/modules/`` and create folder named ``admin.foo-bar``
2. Create .js file named ``module.js`` and paste below code.

.. code-block:: JavaScript

    import FooBarController from './FooBarController'; // import controller
    import FooBarService from './FooBarService'; // import service

    const MODULE_NAME = 'admin.foo-bar'; // module name

    angular.module(MODULE_NAME, [])
        .config($stateProvider => {
            $stateProvider // set state provider
                .state('admin.foo-bar', {
                    url: "/foo-bar", // URL under which the page will be available
                    views: {
                        'extendTop@': { // page header
                            templateUrl: 'templates/foo-bar-extend-top.html',
                            controller: 'FooBarController',
                            controllerAs: 'FooBarCtrl'
                        },
                        'main@': { // main template
                            templateUrl: require('./templates/foo-bar.html'),
                            controller: 'FooBarController',
                            controllerAs: 'FooBarCtrl'
                        },
                        'extendBottom@': { // page footer
                            templateUrl: 'templates/foo-bar-extend-bottom.html',
                            controller: 'FooBarController',
                            controllerAs: 'FooBarCtrl'
                        }
                    },
                })
        })
        .run(($templateCache, $http) => {
            let catchErrorTemplate = () => {
                throw `${MODULE_NAME} has missing template`
            };

            $templateCache.put('templates/foo-bar-extend-top.html', ''); // putting top into $templateCache
            $templateCache.put('templates/foo-bar-extend-bottom.html', ''); // putting footer into $templateCache

            $http.get(`templates/foo-bar.html`) // template request
                .then(
                    response => {
                        $templateCache.put('templates/foo-bar.html', response.data); // putting main template into $templateCache
                    }
                )
                .catch(catchErrorTemplate);
        })
        .controller('FooBarController', FooBarController) // set controller
        .service('FooBarService', FooBarService); // set service
    try {
        window.OpenLoyaltyConfig.modules.push(MODULE_NAME); // register module
    } catch (err) {
        throw `${MODULE_NAME} will not be registered`
    }

3. If you do not need to download additional data, we do not need to create a service. We use `Restangular <https://github.com/mgonto/restangular>`_ for GET, POST, DELETE, and UPDATE requests. In root of module create service file ``FooBarService.js``. Inside file we need to create class ``FooBarService`` with methods like ``getFooBarItems(params)``. At the end of file don't forget to add ``$inject`` property with array of services to inject. In our example, we need to inject ``['Restangular', 'EditableMap']``. ``EditableMap`` is used for data mapping. 

Service
-----------------------------

.. code-block:: JavaScript

    export default class FooBarService {

        constructor(Restangular, EditableMap) {
            this.Restangular = Restangular;
            this.EditableMap = EditableMap;
        }

        getFooBarItems() { // method returns object
            return this.Restangular.one('foo').one('bar').one('resources').get();
        }
    }

    FooBarService.$inject = ['Restangular', 'EditableMap'];

4. Now we need to create controller for our module. Create file named ``FooBarController.js``

Controller
-----------------------------

.. code-block:: JavaScript

    export default class FooBarController { // create Class
        constructor($scope, AuthService, FooBarService, Flash, $filter, EditableMap) { // create constructor
            if (!AuthService.isGranted('ROLE_ADMIN')) { // check role (who has access)
                AuthService.logout();
            }
            this.$scope = $scope;
            this.FooBarService = FooBarService;
            this.EditableMap = EditableMap;
            this.AuthService = AuthService;
            this.Flash = Flash;
            this.$filter = $filter;
            this.loaderStates = { // full page loader
                coverLoader: true // default enabled
            }
        }

    getFooBarData() { // our get data method
        let self = this;

            self.FooBarService.getFooBarItems() // fire getFooBarItems method from FooBarService
                .then(
                    res => {
                        self.$scope.fooList = res.resources; // assign response data
                        self.loaderStates.coverLoader = false; // turn off loader
                    },
                    () => {
                        let message = self.$filter('translate')('xhr.get_fooBar.error'); // set message from translations
                        self.Flash.create('danger', message); // display error message
                        self.loaderStates.coverLoader = false; // turn off loader
                    }
                )
            }

    }

    FooBarController.$inject = ['$scope', 'AuthService', 'FooBarService', 'Flash', '$filter', 'EditableMap'];
    
    
5. The next thing we should do is create a template. To do that, create folder ``templates``. In our case inside this folde we create only one ``.html`` template file named ``foo-bar.html``

Template
-----------------------------

.. code-block:: HTML

    <box-loader loading="FooBarCtrl.loaderStates.coverLoader" cover="1" class="cover" delay="100"></box-loader>

    <div class="heading" ng-init="FooBarCtrl.getFooBarData()">
        <h1>{{ "fooBar.heading" | translate }}</h1>
    </div>
    <div style="clear:both;"></div>
    <div class="fooBar-list box">
        <div class="box-title">
            <h1 class="text-left">{{ "fooBar.list" | translate }}</h1>
        </div>
        <div class="box-content">
            <ul>
                <li ng-repeat="item in fooList">
                    <p ng-bind="item.name"></p>
                </li>
            </ul>
        </div>
    </div>

6. Now we must register module. Go to ``app*.js`` file and paste:

Module registration
-----------------------------

.. code-block:: JavaScript

    require('./modules/admin.foo-bar/module.js');

and here:

.. code-block:: JavaScript

    angular.module('OpenLoyalty', [
         'admin.foo-bar',
    ])
    
You can now save all changes and restart dev server. Your new page should be visible on ``/admin.html#!/admin/foo-bar``.

7. Adding page to left navigation

You can add new page into left navigation by editing ``left-nav.html`` on path ``src/modules/admin.partials/templates/``
Find the selected category or create a new one, then paste code:

.. code-block:: HTML

    <ul class="menu vertical nested">
        ...
        <li><a ui-sref="admin.foo-bar">{{ "fooBar.foo_bar" | translate }}</a></li>
        ...
    </ul>

8. Adding page to top navigation

You can also add new item into top navigation by editing ``top-nav.html`` on path ``src/modules/admin.partials/templates/``

.. code-block:: HTML

    <ul class="menu settings">
        ...
        <li ng-show="RootCtrl.AuthService.hasPermission('ADMIN', 'VIEW')"> // you can set role (who can see this)
            <a ui-sref="admin.foo-bar">
                {{ "fooBar.foo_bar" | translate }}
            </a>
        </li>
        ...
    </ul>
    
 
