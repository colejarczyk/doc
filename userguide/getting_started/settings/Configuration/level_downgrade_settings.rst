.. index::
   single: level_downgrade_settings 

Level downgrade settings
========================

Section appears only when **Levels will be calculated with points option** is chosen and allows to specify if and when customer level should be recalculated. 

Here you also determine whether level recalculation should be combined with a customer points reset and define when and which points should be expired

   
To configure level downgrade options:
'''''''''''''''''''''''''''''''''''''

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Configuration**. 

.. |settings| image:: /userguide/_images/icon.png

2. Scroll down to **Level downgrade settings** section 

3. Set the **Mode** option to one of the following:
 
  - None
  - Automatic
  - Every x number of days
  
.. image:: /userguide/_images/mode.png
   :alt:   Mode options


+--------------------------+--------------------------------------------------------------------------------+
|   Type                   |  Description                                                                   |
+==========================+================================================================================+
|   None                   | | Customer level doesn’t decrease and his accumulated points are not reset     |
|                          | | No additional settings to configure here                                     |
+--------------------------+--------------------------------------------------------------------------------+
|   Automatic              | | Default Open Loyalty logic.                                                  |
|			   |										    | 
|                          | | The only scenarios when customer can return to previous level is when        | 
|                          | | transaction (order), which caused this promotion, will be returned           | 
|                          | | or his level will be changed manually by Admin.                              |
|			   |										    |
|                          | | His accumulated points are not reset – Loyalty points pool based on          |
|                          | | :doc:`Points transfers </userguide/points_transfers/index>`.                 |
|			   | 										    |
|                          | | No additional settings to configure here                                     |
+--------------------------+--------------------------------------------------------------------------------+
|   Every x number of days | | Customer level will be recalculated every provided number of days based      |
|                          | | on accumulated points counting from registration date/last downgrade date    |
|                          | | or last level change.                                                        |
|			   | 										    |
|                          | | If at the end of specified period                                            |
|                          | | (registration date/last downgrade date/last level change + number of days    |
|                          | | every which customer level is recalculated) customer won't reach enough      |
|                          | | points to stay at the same level, a customer will be relegated to level      |
|                          | | which his points determine                                                   |
+--------------------------+--------------------------------------------------------------------------------+


4. To set up level expiration after selected time period choose **Every x number of days** and do the following: 

  - In **Downgrade every** field define after how many days since registration date or last downgrade date (in next period) level will be recalculated. For example, provide 365 to recalculate level every year  
  - In **Downgrade based on** field choose which points should be used to level recalculation after defined X number of days 
       - Active points
       - Earned points within last X days
       - Earned points since last level change
       
	 
.. image:: /userguide/_images/downgrade.png
   :alt:   Level downgrade points pool options
   

+--------------------------+---------------------------------------------------------------------------------------------+
|   Type                   |  Description                                                                                |
+==========================+=============================================================================================+
| | Active points          | | Calculate a customer current level based on only his active points pool                   |
+--------------------------+---------------------------------------------------------------------------------------------+
| | Earned points within   | | Calculate a customer current level based on his earned points since last                  |
| | last X days            | | level recalculation date (registration date/las level recalulaction).                     |
|			   | 												 |
|                          | | It sums up added (Active) points. Used points won't affect on earned points.              | 
|                          | | Locked points are also excluded from earned points and will be added after unlocking them.|
|			   | 												 |
|                          | | Currently earned points from last downgrade date are displaying in **Customer Loyalty**   |
|                          | | balance as a **Total points earned since last level recalculation**.                      |
|			   |											         |
|                          | | At the of every defined period amount of collected within points is reset                 |
+--------------------------+---------------------------------------------------------------------------------------------+
| | Earned points since    | | Calculate a customer current level based on his earned points since last                  |
| | last level change      | | level change date (base on his activity within loyalty program).                          |
|			   |												 |
|                          | | **For example**, after registration customer is assigned to the basic level and from the  |
|                          | | registration date, days till level recalculation is counted. If in the middle time, 	 |
|                          | | customer will earn points that implicate promotion to the next level days are             |
|                          | | counted from the beginning starting from the date of promotion.                           |
|			   |												 |
|                          | | Currently earned points from last change are displaying in **Customer Loyalty**           |
|                          | | points balance as a **Total points earned since last level recalculation**.               |
|			   | 												 |
|                          | | At the end of every defined period, amount of collected within points is reset            |
+--------------------------+---------------------------------------------------------------------------------------------+



5. **Reset points** checkbox appears only when Active points are selected. When you mark it, Open Loyalty resets all Active and Locked points and move it to Expired points pool after specified **Downgrade every** number of days.     
  
.. image:: /userguide/_images/reset_points.png
   :alt:   Reset points checkbox


When complete, tap ``SAVE``


.. note::

    If you leave checkbox blank, Active points will not be reset and will pass to next period.  
	 The amount of Active points will be changing by Customer activity within Loyalty program – spending points for reward campaign, earning points for transaction, newsletter subscription, Admin adding/spending points transfer etc. 


.. warning::

    A customer level is recalculated and changing, before his points are reset. 
	 Points are reset after specified time period, counting from registration date, without customer level change.
   

Example of customer level downgrade base on earned points within last X days
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Your customer **points credentials to level promotion**: 
    
 - Level O - if a customer has no points 
 - Level 1 – if a customer has 10 points 
 - Level 2 – if customer has 30 points
 - Level 3 – if customer has 100 points 
      
You decided to *recalculate level every year* (365 days) since the customer registration date and to use for this Active points, which *will be reset* at the end of the year (after level recalculation). 
    
**Customer made a two transactions and get 10 points and 20 points**. 
    
After getting 10 points a customer leveled up to 1st level, after getting another 20 points a customer leveled up to 2nd level.
   
If at the end of year a customer:
   
 - has only **5 active points** then he is *downgraded* to the **Level 0**, and all his points are reset
 - has **10 active points** the he is *downgraded* to the **Level 1**, and all his points are reset
 - has **30 active points** the he stays in the same **Level 2**, and all his points are reset
