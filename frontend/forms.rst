Forms
=====

We use forms to add, update and delete data that are provided by the API. For the purposes of this tutorial we create a form in 'admin.foo-bar' module template. We use backend validation, therefore we disable the default validation in the form by adding ``novalidate`` attribute to the form element. The ``ng-submit`` directive specifies a function to run when the form is submitted, which should be in the controller. If the form does not have an action ``ng-submit`` will prevent the form from being submitted. 

How to create a custom form
----------------------------

What is required:

submit method: ``FooBarCtrl.addFooBar(newFooBar)``

Open our custom module template ``src/modules/admin.foo-bar/templates/foo-bar.html`` and paste below lines of code:

.. code-block:: HTML

    <form novalidate ng-submit="FooBarCtrl.addFooBar(newFooBar)">
        <div class="box-content">
            <div class="row">
                <div class="columns medium-12">
                
                  // Input block
                  <fieldset class="fieldset">
                        <legend>{{ "fooBar.header" | translate }}</legend>
                        <div class="row">
                        
                            // Input label
                            <div class="small-3 medium-2 columns">
                                <label>{{ "fooBar.name" | translate }} <span class="required">*</span></label>
                            </div>
                            
                            // Input field
                            <div class="small-9 medium-10 columns" form-validation="validate.name.errors">
                                <input type="text" ng-model="newFooBar.name" required>
                                // Prompt container
                                <span class="prompt">{{ "fooBar.prompt" | translate }}</span>
                            </div>
                        </div>
                    </fieldset>
                </div>
            </div>
        </div>
        
        // Form footer
        <div class="box-footer" ng-init="FooBarCtrl.loaderStates.FooBarDetails=false">
            <div class="row">
                <div class="columns small-12">
                
                    // Submit buttom
                    <button class="button button-septenary-colorized  float-left m-r-1" type="submit">
                        {{ "global.save" | translate }}
                    </button>
                    
                    // Cancel buttom
                    <button type="button" ui-sref="admin.foo-bar" class="button button-default float-left" href="#">
                        {{ "global.cancel" | translate }}
                    </button>
                </div>
                <div style="clear:both;"></div>
            </div>
        </div>
    </form>
    
    
A quick overview of the main components
=============
  
Select copmponent
---------------

For select components we use angular directive named `Angular Selectize 2 <https://www.npmjs.com/package/angular-selectize2>`_
  
.. code-block:: HTML
  
      <div class="row">
        <div class="small-3 medium-2 columns">
            <label>{{ "fooBar.foo" | translate }} <span class="required">*</span></label>
        </div>
        <div class="small-9 medium-10 columns" form-validation="validate.foo[$index].bar.errors">
            <selectize 
                ng-model="newFooBar.foo[$index].bar" 
                options="fooBarCtrl.foo" 
                config="fooBarCtrl.fooConfig"
                required>
            </selectize>
            <span class="prompt">{{ "fooBar.prompt" | translate }}</span>
        </div>
    </div>
    
Radio component
---------------

.. code-block:: HTML

    <div class="row">
        <div class="medium-2 small-3 columns">
            <label>{{ "fooBar.foo" | translate }}</label>
        </div>
        <div class="medium-10 small-9 columns" form-validation="validate.fooBar.errors">
            <input type="radio" ng-model="fooBar.foo" value="foo" id="foo">
            <label for="foo">{{ "fooBar.foo" | translate }}</label>
            <input type="radio" ng-model="fooBar.bar" value="bar" id="bar">
            <label for="bar">{{ "fooBar.bar" | translate }}</label>
            <span class="prompt">{{ "fooBar.prompt" | translate }}</span>
        </div>
    </div>
    
Checkbox component
---------------

For checkboxes we use custom directive. Under this path you will find the code of the directive ``src\component\global\checkbox\templates\checkbox.html``
 
.. code-block:: HTML

    <div class="row">
        <div class="medium-2 small-3 columns">
            <label>{{ "fooBar.foo" | translate }}<span class="required">*</span></label>
        </div>
        <div class="medium-10 small-9 columns" form-validation="validate.fooBar.errors">
            <checkbox ng-model="fooBar.foo"></checkbox>
            <span class="prompt">{{ "fooBar.prompt" | translate }}</span>
        </div>
    </div>

DatePicker
----------

For selecting date we use custom directive. Under this path you will find the code of the directive ``src\component\global\datepicker\DatepickerDirective.js`` based on `jQuery Plugin Date and Time Picker <https://github.com/xdan/datetimepicker>`_

.. code-block:: HTML

    <div class="row">
        <div class="medium-2 small-3 columns">
            <label>{{ "fooBar.foo_date" | translate }}</label>
        </div>
        <div class="medium-10 small-9 columns" form-validation="validate.fooBar.errors">
            <input type="text" ng-model="fooBar.foo_date" datepicker required no-time="true">
            <span class="prompt">{{ "fooBar.prompt" | translate }}</span>
        </div>
    </div>
