.. index::
   single: loyalty

Loyalty
=======

In **Loyalty** section you can view Loyalty Points balance in the customer’s account. 

Depending on the :doc:`Configuration </userguide/getting_started/settings/Configuration/settings>` (whether level is calculated with points or transactions) different values will be displayed.


Level is calculated with transactions
-------------------------------------

.. image:: /userguide/_images/loyalty_transactions.png
   :alt:   Loyalty Points Balance 

1. **Total earned points**

   Total accumulated points assigned to the customer account thought various activity within the loyalty program based on Earning Rules. 
   
   Sum of active, locked, used and expired points.
   
2. **Active Points**

   Points that may be used to redeem a reward campaigns. 
   
   Depending on the :doc:`Configuration </userguide/getting_started/settings/Configuration/level_downgrade_settings>`, this value can be used to level recalculation instead Total points earned since last level recalculation amount.
   
3. **Used Points**

   Points redeemed by the Customer thought various Reward Campaigns  within the loyalty program

4. **Expired Points**

   Points expired due to non-redemption of assigned active points. 
   
   Points will expire after number of days from date of adding Point transfer. Points lifetime is set in :doc:`Open Loyalty Configuration </userguide/getting_started/settings/Configuration/settings>`

5. **Locked Points** 

   Points earned through various activity within the loyalty program that cannot be used after passing selected locked time. 
   
   Points will be locked for number of days set in :doc:`Open Loyalty Configuration </userguide/getting_started/settings/Configuration/settings>`, as a customer may return whole transaction or selected products. 
   
   Locked points are not used to calculate customer level. After passing selected locked time, points automatically get active. When points get active, a customer level will be recalculated.
   

Level is calculated with points
-------------------------------

When you set up in Open Loyalty configuration to use points for level recalculation additional information about level expiration date and earned points within specified period amount will be displayed.

.. image:: /userguide/_images/loyalty_points.png
   :alt:   Loyalty Points Balance    

1. **Total points earned since last level recalculation**

   Currently earned points from last downgrade date/level changed. 
   
   The displayed value is sum of all Active points earned within specified in :doc:`Level downgrade settings </userguide/getting_started/settings/Configuration/level_downgrade_settings>` period. 
   
   Depending on the Configuration, this value can be used to level recalculation instead Active points amount.

2. **Level will expire in**    

   Number of days until customer level recalculation. 
   
   It is calculated since registration date or last downgrade date plus configured in :doc:`Level downgrade settings </userguide/getting_started/settings/Configuration/level_downgrade_settings>` number of days
