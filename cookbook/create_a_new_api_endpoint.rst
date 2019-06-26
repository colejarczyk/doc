How to add a new API endpoint
=============================

Let’s say you want to add a new endpoint that will return just another list of earning points rules.
Here is a step-by-step guide how to achieve this.

First of all, you need to create a new controller in existing ``AppBundle`` in ``Controller`` directory.
Here is a sample code

.. code-block:: php

    <?php

    namespace AppBundle\Controller;
    use FOS\RestBundle\Controller\Annotations\Route;
    use FOS\RestBundle\View\View;
    use Nelmio\ApiDocBundle\Annotation\ApiDoc;
    use Sensio\Bundle\FrameworkExtraBundle\Configuration\Method;
    use Symfony\Component\HttpFoundation\Request;
    use FOS\RestBundle\Controller\FOSRestController;

    class EarningRuleController extends FOSRestController
    {
        /**
         * @Route(name="app.earning_rule.index", path="/earningRule/list")
         * @Method("GET")
         *
         * @ApiDoc(
         *     name="New earning rule list",
         *     section="Earning Rule",
         *     statusCodes={
         *       200="Returned when successful",
         *     }
         * )
         *
         * @param Request $request
         *
         * @return View
         */
        public function indexController(Request $request)
        {
            return $this->view(['data' => ['data']]);
        }
    }

@Route is an annotation to create a new route in Symfony Framework. The name is useful for creating links and redirection but not used as we’re implementing RESTful API. A path is an endpoint URI.

Route is an annotation to create a new route in Symfony Framework. The name is useful for creating links and redirection but not used as we’re implementing RESTful API. A path is an endpoint URI. <https://symfony.com/doc/3.4/routing.html>`_.

@Method is an annotation to specify which HTTP requests are allowed for this endpoint. Here we accept only GET requests.

@ApiDoc is an annotation from NelmioDocApi bundle to create a documentation for our API. This documentation is
automatically generated from this annotation and available at ``http://openloyalty.localhost/doc``

More information about this bundle you can find `here <https://symfony.com/doc/current/bundles/NelmioApiDocBundle/index.html>`_.

@param and @return are standard comments for developers and self-explaining.

Then we have an action in our controller ``indexAction`` that takes HTTP request as an argument and return a json response.

Now, when we have a new controller, the last thing to do is register it in the framework. To do that, add a follow
line in ``app/config/routing.yml``

.. code-block:: yaml

    app_bundle:
        resource: "@AppBundle/Controller/EarningRuleController.php"
        type: annotation
        prefix: /api

Note:
It’s important to define this route before open_loyalty_core, not after, as Open Loyalty has an
endpoint ``/api/earningRule/{earningRule}`` where ``{earningRule}`` is an variable and accepts any parameter,
including ``list`` from our route.

That’s it. Now you’ve got a new API endpoint registered in Open Loyalty. You can go to the
``http://openloyalty.localhost/doc`` and try to call this endpoint.
By default, all our ``/api`` endpoints are behind a firewall. So if you want to use ``/api`` endpoints, you need to
be logged in as an administrator and use authorization token.

To see how Symfony firewall is configured check ``backend/app/config/security.yml``
