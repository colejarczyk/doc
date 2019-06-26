.. index::
   single: transfer

Points transfers
================

**Points transfers** tab provide a view of latest points which customer gain or spend. Moreover, list contains information whether points are the result of Earning Rules (system) or they have been manually set by the Admin user (admin) and date until they will be locked.

.. image:: /userguide/_images/customer_transfer.png
   :alt:   Points Transfers Lists

To cancel points transfer click **Remove** icon |remove| in the Action column. System will display a message asked you to confirm the action.

.. |remove| image:: /userguide/_images/remove.png

.. image:: /userguide/_images/remove_ok.png
   :alt:   Removing Transfer Action

After canceling, no action to canceled transfer record will be longer available and the **Remove** icon background change color to blue. The same situation deal with Points transfers with "spending" type. 

To see the list of all your customer points transfers (not only the latest)  click ``All Points Transfer`` below the tab.

To add point transfer manually click ``Add new Points Transfer``

To learn more about Points transfers, see :doc:`Points transfer </userguide/points_transfers/index>`

Field description
*****************

+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Field             | Description                                                                                                                 |
+===================+=============================================================================================================================+
| Issuer            | | Define who create Transfer operation.                                                                                     |
|                   | | **Options include: system/admin**                                                                                         |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| State             | | Transferred points state:                                                                                                 |
|                   |                                                                                                                             |
|                   |    - **Active** : points are available to spend                                                                             |
|                   |    - **Expired** : points expired and cannot be used to redeem reward                                                       |
|                   |    - **Pending** : points are locked and cannot be used to redeem reward until locked time will be passing.                 |
|                   |                                                                                                                             |
|                   |      Locked time is set in :doc:`Open Loyalty Configuration </userguide/getting_started/settings/Configuration/settings>`   |
|                   |    - **Canceled** : points are subtracted from the pool of Active Points as a result of canceling the points transfer       |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Type              | | Transfer operation type.                                                                                                  |
|                   | | **Options include: Adding/Spending**                                                                                      |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Value             | | Amount of points earned/spent within the transfer                                                                         |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Comment           | | Show details about transfer, e.g. for what customer gets points, for what customer spend points                           |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Created at        | | Date when points transfer was made                                                                                        |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Points will be    | | Date until points with pending state will be locked.                                                                      |
| locked until      | | Locked time is set in :doc:`Open Loyalty Configuration </userguide/getting_started/settings/Configuration/settings>`      |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Expires at        | | Date when points will expire and cannot be used to redeem reward                                                          |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Actions           | | The remove operations that can be applied to selected, adding type, transfer record                                       |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
