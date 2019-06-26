Points Expiration
=================

Points that are granted to the customer have an expiration date that can be adjusted in the :doc:`Admin Settings </api/settings>`. You can set after how many days the points are overdue and cannot be used by the customer.
To show the logic behind the expiration mechanism, let's see some use-case scenarios:

Scenario 1: What happens in the system with customer points when some of them expire
------------------------------------------------------------------------------------
The system updates the existing point transfers with new status *expired*. This is done automatically by the command set in the CRON job. This command fetches all point transfers that should be set as expired and updates their data.

.. code-block:: bash

    * * * * * /usr/local/bin/php /var/www/openloyalty/bin/console --env=prod ol:points:transfers:expire > /var/log/cron_ol_points_expire.log 2>&1


Scenario 2: From which transfer the system will subtract points if there is more than one active transfer for the customer
--------------------------------------------------------------------------------------------------------------------------
The system will create a new transfer with *subtract* type. OL only modifies Point Transfers when its status needs a change. In cases like adding or subtracting points from the Customer's Account, the system will create a new Point Transfer.

The subtracting action starts in :doc:`Spend customer points </api/settings>` action.
OL dispatches :code:`\OpenLoyalty\Component\Account\Domain\Command\SpendPoints` command along with :code:`\OpenLoyalty\Component\Account\Domain\Event\PointsWereSpent` event.

OL looks for points that are active on Customer's Account to sum them up and resolve total account points. If the amount is greater or equal the amount of subtracting points transfer, it proceeds further with logic.
