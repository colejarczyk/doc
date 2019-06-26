.. index::
   single: all_transfers

All Points transfers
====================

The Points transfers lists gives you information about value of earned and spent points by particular customer with details regarding customers and transfer process. Moreover, list contains information whether points are the result of Earning Rules (system) or they have been manually set by the Admin user (admin).

To learn more about Earning Rules, see :doc:`Rules details </userguide/earning_rules/index>`

.. image:: /userguide/_images/points_transfers.png
   :alt:   Points Transfers List

Use the standard controls to sort the list, filter and search transfers by typing in the field under column header value you want to find, and apply actions to selected transfers records. 

Pagination controls appear if there are more transfer records than fit on the page, and are used to move from one page to the next.


Field description
*****************

+----------------------------+----------------------------------------------------------------------------------------+
|   Field                    |  Description                                                                           |
+============================+========================================================================================+
|   First name               | | The first name of customer referred to transfer                                      |
+----------------------------+----------------------------------------------------------------------------------------+ 
|   Last name                | | The last name of customer referred to transfer                                       |
+----------------------------+----------------------------------------------------------------------------------------+
|   Phone                    | | The customers referred to transfer phone number                                      |
+----------------------------+----------------------------------------------------------------------------------------+
|   Email                    | | The customers referred to transfer email address                                     |
+----------------------------+----------------------------------------------------------------------------------------+
|   State                    | | Transferred points state:                                                            |
|                            |                                                                                        |
|                            |    - **Active**                                                                        |
|                            |       points are available to spend                                                    |
|                            |    - **Expired**                                                                       |
|                            |       points expired and cannot be used to redeem reward                               |
|                            |    - **Pending**                                                                       |
|                            |       points are locked and cannot be used to redeem reward until locked time will     | 
|                            |       be passing. Locked time is set in                                                |
|                            |       :doc:`Configuration </userguide/getting_started/settings/Configuration/settings>`|
|                            |    - **Canceled**                                                                      |
|                            |       points are subtracted from the pool of Active Points as a result of              |
|                            |       canceling the points transfer                                                    |
+----------------------------+----------------------------------------------------------------------------------------+
|   Type                     | | Transfer operation type:                                                             |
|                            |                                                                                        |
|                            |    - **Adding**                                                                        |
|                            |       customer earn point for transaction or other activity                            |
|                            |    - **Spending**                                                                      |
|                            |       customer spent points for campaign reward                                        |
+----------------------------+----------------------------------------------------------------------------------------+
|   Value                    | | Amount of points earned/spent within the transfer                                    |
+----------------------------+----------------------------------------------------------------------------------------+
|   Comment                  | | Show details about transfer, e.g. for what Customer gets points, for what Customer   |
|                            |   spend points.                                                                        |
|                            | | Field is automatically filled in with the **reward campaign name** when the          |
|                            |   customer *spends points* for the reward using his account.                           |
|                            | | Field is automatically filled in with the **earning rule name**, used to             |
|                            |   *earn points* by customer.                                                           |
|                            | | If transfer is created manually by Admin user, field is filled in with information   |
|                            |   provided by the Admin during transfer creation.                                      |
+----------------------------+----------------------------------------------------------------------------------------+
|   Created at               | | Date when points transfer was made                                                   |
+----------------------------+----------------------------------------------------------------------------------------+ 
|   Loyalty card number      | | Customer loyalty card number linked with transfer.                                   |
|                            | | If there is no value assign "Not set" is displayed                                   |
+----------------------------+----------------------------------------------------------------------------------------+
|   POS                      | | Which of POS processed transaction upon which points were calculated.                |
|                            | | If there is no assignment "Not set" is displayed                                     |
+----------------------------+----------------------------------------------------------------------------------------+
|   Issuer                   | | Define who create Transfer operation.                                                |
|                            | | **Options include**: system/admin                                                    |
+----------------------------+----------------------------------------------------------------------------------------+
|   Actions                  | | The operations that can be applied to selected transfer record.                      |
|                            | | **Options include**:                                                                 |
|                            |                                                                                        |
|                            |    - cancel points transfer                                                            |
|                            |    - view points transfer details                                                      |
+----------------------------+----------------------------------------------------------------------------------------+


