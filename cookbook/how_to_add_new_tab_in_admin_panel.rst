How to add a new tab in the admin panel
=======================================

In this tutorial we will describe how to add a new simple tab (`mock`) to admin panel.

Create a module
---------------

Let's create a new `admin.mock` directory in ``frontend/src/modules``. Module contains `templates` directory for html
templates and minimum 3 files.

 - MockController.js - responsible for controlling views,
 - MockService.js - providing logic or data,
 - module.js - entry point for module, defining routing, controllers, services etc.

Create `module.js` with content:

.. code-block:: js

    import MockController from './MockController';
    import MockService from './MockService';

    const MODULE_NAME = 'admin.mock';

    angular.module(MODULE_NAME, [])
        .config($stateProvider => {
            $stateProvider
                .state('admin.mock-list', {
                    url: "/mock-list",
                    views: {
                        'extendTop@': {
                            templateUrl: 'templates/mock-list-extend-top.html',
                            controller: 'MockController',
                            controllerAs: 'MockCtrl'
                        },
                        'main@': {
                            templateUrl: require('./templates/mock-list.html'),
                            controller: 'MockController',
                            controllerAs: 'MockCtrl'
                        },
                        'extendBottom@': {
                            templateUrl: 'templates/mock-list-extend-bottom.html',
                            controller: 'MockController',
                            controllerAs: 'MockCtrl'
                        }
                    }
                })
        })
        .run(($templateCache, $http) => {
            let catchErrorTemplate = () => {
                throw `${MODULE_NAME} has missing template`
            };
            $templateCache.put('templates/mock-list-extend-bottom.html', '');
            $templateCache.put('templates/mock-list-extend-top.html', '');

            $http.get(`templates/mock-list.html`)
                .then(
                    response => {
                        $templateCache.put('templates/mock-list.html', response.data);
                    }
                )
                .catch(catchErrorTemplate);
        })
        .controller('MockController', MockController)
        .service('MockService', MockService);

    try {
        window.OpenLoyaltyConfig.modules.push(MODULE_NAME);
    } catch (err) {
        throw `${MODULE_NAME} will not be registered`
    }

And finally we have to register our module in ``frontend/src/appAdmin.js`` by adding:

.. code-block:: js

    ...
    require('./modules/admin.mock/module.js');
    ...
    angular.module('OpenLoyalty', [
    ...
      'admin.mock'
    ...
    ]

Service and controller
----------------------

Create service `MockService.js` with content:

.. code-block:: js

    export default class MockService {

        constructor(Restangular) {
            this.Restangular = Restangular;
        }

        getLevels(params) {
            return this.Restangular.all('level').getList(params);
        }
    }

    MockService.$inject = ['Restangular'];

Create controller `MockController.js` with content:

.. code-block:: js

    export default class MockController {
        constructor($scope, MockService, Flash, NgTableParams, $q, ParamsMap, $filter, DataService, PaginationSettings) {
            this.MockService = MockService;
            this.$scope = $scope;
            this.Flash = Flash;
            this.PaginationSettings = PaginationSettings;
            this.NgTableParams = NgTableParams;
            this.ParamsMap = ParamsMap;
            this.$q = $q;
            this.$filter = $filter;
            this.config = DataService.getConfig();

            this.loaderStates = {
                levelList: true,
            }
        }

        getData() {
            let self = this;

            self.tableParams = new self.NgTableParams({
                count: self.config.perPage
            }, {
                getData: function (params) {
                    let dfd = self.$q.defer();

                    self.loaderStates.levelList = true;
                    self.MockService.getLevels(self.ParamsMap.params(params.url()))
                        .then(
                            res => {
                                self.$scope.levels = res;
                                let realTotal = res.total;
                                params.realTotal = () => realTotal;
                                params.total(self.PaginationSettings.getTotal(res.total));
                                self.loaderStates.levelList = false;
                                self.loaderStates.coverLoader = false;
                                dfd.resolve(res);
                            },
                            () => {
                                let message = self.$filter('translate')('xhr.get_levels_list.error');
                                self.Flash.create('danger', message);
                                self.loaderStates.levelList = false;
                                self.loaderStates.coverLoader = false;
                                dfd.reject();
                            }
                        );

                    return dfd.promise;
                }
            });
        }
    }

    MockController.$inject = ['$scope', 'MockService', 'Flash', 'NgTableParams', '$q', 'ParamsMap', '$filter', 'DataService', 'PaginationSettings'];

Templates
---------

Create template `mock-list.js` in `templates` directory with content:

.. code-block:: html

    <box-loader loading="MockCtrl.loaderStates.coverLoader" cover="1" class="cover" delay="100"></box-loader>

    <div class="heading" ng-init="MockCtrl.getData()">
        <h1>{{ "mock.heading" | translate }}</h1>
    </div>
    <div style="clear:both;"></div>

    <div class="client-list box">
        <div class="box-title">
            <h1 class="text-left">{{ "mock.list" | translate }}</h1>
        </div>
        <div class="box-content">
            <box-loader loading="MockCtrl.loaderStates.mockList"></box-loader>
            <table ng-table="MockCtrl.tableParams" class="default" template-pagination="templatePagination.html">
                <tr ng-repeat="row in $data">
                    <td data-title="'mock.name'|translate" sortable="'name'">
                        <span ng-bind="row.name"></span>
                    </td>
                    <td data-title="'mock.description'|translate"
                        sortable="'description'"
                    >
                        <span ng-bind="row.description || ('global.not_set'|translate)"></span>
                    </td>
                    <td data-title="'Actions'">
                        <button type="button" class="button  button-secondary tiny"
                                ui-sref="admin.edit-mock({levelId: row.id})">
                            <i class="fa fa-pencil" aria-hidden="true"></i>
                        </button>
                    </td>
                </tr>
            </table>
        </div>
    </div>

The last point is adding link to a navigation menu on left side. Let's open file ``frontend/src/modules/admin.partials/templates/left-nav.html``
and add:

.. code-block:: html

      <li>
          <a href="#"><i class="fa fa-tachometer" aria-hidden="true"></i>{{ "nav.mock" | translate }}</a>
          <ul class="menu vertical nested">
              <li><a ui-sref="admin.mock-list">{{ "nav.mock" | translate }}</a></li>
          </ul>
      </li>
