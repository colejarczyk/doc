.. index::
   single: role_resources

Role Resources 
================

Access to the following resources can be assigned to any admin user role. 

See the **Resources** linked page to learn more about the capabilities thyat are associated with. 

.. image:: /userguide/_images/resources.png
   :alt:   Resources list

.. note:: 

    Regardless of the permissions granted, User can edit his password and view the basic information of his account at any time

ACL 
^^^^^^

Defines access to the :doc:`ACL  </userguide/getting_started/settings/acl>` settings section and its individual elements

+----------------------------------------+----------------------------------------+
| VIEW                                   | MODIFY                                 |
+========================================+========================================+
|- Roles list preview                    | All **View** permissions, and more:    |     
|                                        |                                        |
|                                        | - Roles details preview                |
|                                        | - New role creation                    |
|                                        | - Existing roles edition               |
|                                        | - Existing role deletion               | 
+----------------------------------------+----------------------------------------+

.. warning:: 

    Default **Super admin** role can not be deleted 
    
.. warning:: 

    When assigning resources, be sure to don't give an any access to the **ACL** section if you are limiting access for a given role. 
    
    **Otherwise, users will be able to modify their own permissions** 


Admins 
^^^^^^

Defines access to the Admin :doc:`Users  </userguide/getting_started/settings/users>` settings section and its individual elements

+----------------------------------------+----------------------------------------+
| VIEW                                   | MODIFY                                 |
+========================================+========================================+
|- Users list preview                    | All **View** permissions, and more:    |     
|                                        |                                        |
|                                        | - New User account creation*           |
|                                        | - Existing user account edition*       |
+----------------------------------------+----------------------------------------+

.. note:: 

    To enable user edition and creation, you must have at least an **ACL View access** (*Roles* field is required). 
    
    If there is no ACL access, then you can not even see roles in the drop-down list. 

.. warning:: 

    Remember, that granting *View* access for ACL section (to enable new users account creation and edition), you give an access to the entire ACL section (in accordance with the permissions listed in the ACL table in *View* column) 
    

    

Audit
^^^^^^

Defines access to the :doc:`System logs  </userguide/getting_started/settings/system_logs>` settings section and its individual elements


+-------------------------------------------------+
| VIEW & MODIFY                                   |                                 
+=================================================+
|- System logs list preview                       |    
|- filter and sorting options of system logs list |
|- search logs from time period                   | 
+-------------------------------------------------+

.. tip:: 

    Regardless of access level, user has the same options in both - **View and Modify**
  
  

Customers
^^^^^^^^^^

Defines access to the :doc:`Customers  </userguide/customers/index>` section and its individual menu elements

+---------------------------------------------------------+
| VIEW                                                    | 
+=========================================================+
|- List of customers accounts preview*                    | 
|- Filter and sorting options of customers accounts list  |  
|- Referred customers list preview                        | 
|- Filter and sorting options of referred customers list  | 
|- Customer profile details: Profitability, Loyalty       | 
|  Profile details and Agreements sections (defualt)**    | 
|                                                         | 
+---------------------------------------------------------+

+--------------------------------------------------------+
| MODIFY                                                 |
+========================================================+
| All **View** permissions, and more:                    |     
|                                                        |
| - Customer account creation**                          |
| - Import customers list                                |
| - Updating Customer account**                          |
| - Deactivate a Customer’s account                      |
| - Level assigned manually mechanism**                  | 
+--------------------------------------------------------+


.. tip:: 

    **List of customers accounts preview***
    
    Even if User has no access to the Levels section, in All customers grid information about current level will be displayed

.. note:: 

    **Customer account creation & edition***
    
    To enable full customer account edition & creation, and display all Customer profile details, you must have at least an **View access** to the following: 
     - *Levels* - to assigne level and display in Profile details 
     - *POS* - to assigne POS and display in Profile details
     - *Merchants* - to assigne merchant and display in Profile details
     - *Segments* - to display segments to which customer belongs in Profile details 
     - *Transactions* - to display all customer registered transactions in Profile details 
     - *Points transfers* - to display all customer adding/spending points transfer in Profile details 
     - *Reward Campaign* - to display customer available and redeemed rewards in Profile details 
    
    If there is no access to any of this section, then you can not see options or tabs. 

.. image:: /userguide/_images/acl_customer.PNG
   :alt:   No levels, merchants and pos access 


.. warning:: 

    Remember, that granting *View* access for every section (to enable new users account creation and edition or display information in profile details), you give an access to the entire menu section (in accordance with the permissions listed in the particular tables in *View* column) 



Dashboard
^^^^^^^^^^

Defines access to the :doc:`Dashboard  </userguide/getting_started/admin/dashboard>` section and its individual elements

+-------------------------------------------------------------------------------+
| VIEW & MODIFY                                                                 |                                 
+===============================================================================+
|- Blocks with factors describing the current state of referral program preview |    
|- Chart shows the number of new customer accounts within last 30 days          |
|- Levels grid preview*                                                         | 
+-------------------------------------------------------------------------------+

.. tip:: 

    Regardless of access level, user has the same options in both - **View and Modify**

.. note:: 

    **Levels grid preview*** 
    
    To enable Levels grid preview you must have at least an **Levels View access**. 
    
    If there is no Levels access, then you can not see the grid. 

.. warning:: 

    Remember, that granting *View* access for Levels section (to enable levels grid preview), you give an access to the entire Levels menu section (in accordance with the permissions listed in the Levels table in *View* column) 



Earning rules
^^^^^^^^^^^^^^

Defines access to the :doc:`Earning rules  </userguide/earning_rules/index>` section and its individual menu elements

+----------------------------------------+----------------------------------------+
| VIEW                                   | MODIFY                                 |
+========================================+========================================+
|- Earning rules list preview            | All **View** permissions, and more:    |     
|- Sorting options of earning rules list |                                        |
|- Earning rules details preview*        | - Earning rules creation**             |
|                                        | - Updating earning rules**             |
|                                        | - Activate / Deactivate earning rule   |
+----------------------------------------+----------------------------------------+

.. tip:: 

    **Earning rules details preview***
    
    Even if User has no access to the Levels, Segments and POS sections, in *Earning rules details preview* information about assigne target and POS will be visible  

.. note:: 

    **Earning rule creation & edition****

    To enable earning rule edition and creation, you must have at least an **Levels and/or Segments View access** (*Target* section is required). 
    
    If there is no Levels or Segment access, then you can see *Target* but without possibility to change it
    
    To allow assign POS(es) to which rule will be applied, you should also give at least an **POS View access**  

.. warning:: 

    Remember, that granting *View* access for every section (to enable earning rule creation and edition), you give an access to the entire menu section (in accordance with the permissions listed in the particular tables in *View* column) 



Levels
^^^^^^^^^^^^^^

Defines access to the :doc:`Levels  </userguide/levels/index>` section and its individual menu elements

+--------------------------------------------+----------------------------------------+
| VIEW                                       | MODIFY                                 |
+============================================+========================================+
|- Levels list preview                       | All **View** permissions, and more:    |     
|- Special reward details preview            |                                        |
|- Customers assigned to level list preview* | - Creating customer level              |
|- Download the customers list**             | - Updating levels data                 |
|                                            | - Activate / Deactivate level          |
+--------------------------------------------+----------------------------------------+

.. note:: 

    **Customers assigned to level list preview*** 
    
    To enable customer assigned to particular level details preview you must have at least an **Customers View access**. 
    
    If there is no Customers access, then you can not see the ``Show`` button to preview customers details. You can only see customers account number assigned to this level.


.. note:: 

    **Download the customers list**** 
    
    To download a list of customers assigned to particular level you must have at least an **View access** to the following: 
     - *Customers* - to view customers details 
     - *Utilities* - to export the list of customers  
    
    If there is no Customers access, then you can not even see the download icon.


.. warning:: 

    Remember, that granting *View* access for Customers section (to enable customer details preview), you give an access to the entire Customers menu section (in accordance with the permissions listed in the Customers table in *View* column) 


Merchants
^^^^^^^^^^^^^^

Defines access to the :doc:`Merchants  </userguide/merchants/index>` section and its individual menu elements

+----------------------------------------------+-----------------------------------------+
| VIEW                                         | MODIFY**                                |
+==============================================+=========================================+
|- Merchants list preview*                     | All **View** permissions, and more:     |     
|- Filter and sorting options of merchant list |                                         |
|                                              | - Creating merchant account**           |
|                                              | - Updating merchant account**           |
|                                              | - Activate/Deactivate Merchant account**|
|                                              | - Remove merchant account**             | 
+----------------------------------------------+-----------------------------------------+

.. tip:: 

    **Merchants list preview***
    
    Even if User has no access to the POS sections, in *All merchants* grid information about assigne POS will be visible  

.. note:: 

    **Merchant Modify access**** 
    
    To enable all **Modify access** permissions you must have **POS Modify access**. 
    
    If there is no or only view POS access, then you have only Merchant *View* permissions. 

.. warning:: 

    Remember, that granting *Modify* access for POS section (to enable Merchant modify access), you give an access to the entire POS menu section (in accordance with the permissions listed in the POS table in *Modify* column) 

    

Points transfers
^^^^^^^^^^^^^^^^^^

Defines access to the :doc:`Points transfers  </userguide/points_transfers/index>` section and its individual menu elements

+------------------------------------------------------+----------------------------------------+
| VIEW                                                 | MODIFY                                 |
+======================================================+========================================+
|- Points transfers list preview*                      | All **View** permissions, and more:    |     
|- Filter and sorting options of points transfers list |                                        |
|- Points transfers details preview                    | - Creating Points transfer             |
|                                                      | - Import points transfers              |
|                                                      | - Canceling points transfer            |
+------------------------------------------------------+----------------------------------------+

.. tip:: 

    **Points transfers list preview***
    
    Even if User has no access to the *Customer* section, in *All points transfers* grid information about customer affected by the transfer will be visible



POS
^^^^^^^

Defines access to the :doc:`POS  </userguide/pos/index>` section and its individual menu elements

+----------------------------------------+----------------------------------------+
| VIEW                                   | MODIFY                                 |
+========================================+========================================+
|- POS list preview                      | All **View** permissions, and more:    |     
|- POS localization details              |                                        |
|                                        | - Adding new POS                       |
|                                        | - Updating POS information             |
+----------------------------------------+----------------------------------------+



Reward Campaign
^^^^^^^^^^^^^^^^^^

Defines access to the :doc:`Reward campaigns  </userguide/reward_campaigns/index>` section and its individual menu elements

+---------------------------------------------------------+
| VIEW                                                    | 
+=========================================================+
|- Reward campaign list preview                           | 
|- Filter and sorting options of reward campaign list     | 
|- Reward campaign details preview*                       | 
|- Redeemed rewards list preview**                        | 
|- Redeemed rewards details preview**                     | 
|- Filter and sorting options of redeemed rewards list    | 
|- Download redeemed rewards report                       |
|- Campaign categories list preview                       |
|- Filter and sorting options of Campaign categories list |
+---------------------------------------------------------+

.. tip:: 

    **Reward campaign details preview***
    
    Even if User has no access to the Levels or Segments, in *Reward campaign details preview* information about assigne target will be visible  

.. tip:: 

    **Redeemed rewards list and details preview****
    
    Even if User has no access to the Customers, in *Redeemed rewards* details and grid, information about customer who redeemed particular reward will be visible  


+------------------------------------------------------------+
| MODIFY                                                     |
+============================================================+
| All **View** permissions, and more:                        |     
|                                                            |
| - Reward campaigns creation*                               |
| - Updating reward data*                                    |
| - Activate / Deactivate reward campaign                    |
| - Buy reward campaign for customer**                       |
| - List of customers able to redeem reward preview***       | 
| - Mark reward as *Unused/used* on Redeemed rewards list    |
| - Change reward *Delivery status* on Redeemed rewards list |
| - New campaign category creation                           |
| - Updating campaign category                               |
| - Activate / Deactivate campaign category                  |
+------------------------------------------------------------+

.. note:: 

    **Reward campaign creation & edition***

    To enable reward campaign edition and creation, you must have at least an **Levels and/or Segments View access** (*Target* section is required). 
    
    If there is no Levels or Segment access, then you can see *Target* but without possibility to change it
    

.. note:: 

    **Buy reward campaign for customer****

    To enable manually assignment reward for customer, you must have at least a **Customers View access** (*E-mail or phone* field is required). 
    
    In case of *Percentage discount code* reward type, also at least a **Transactions View access** is required. 
    
    If there is no Customers (and Transactions) access, then you can not provide any value to find customer and assigne reward.  


.. note:: 

    **List of customers able to redeem reward preview***** 
    
    To enable customers who could redeem reward details preview you must have at least an **Customers View access**. 
    
    If there is no Customers access, then you can not see the ``Show`` button to preview customers details. You can see only number of customers who could redeem reward.


.. warning:: 

    Remember, that granting *View* access for every section (to enable creation and edition etc.), you give an access to the entire menu section (in accordance with the permissions listed in the particular tables in *View* column) 
    
    

Segments
^^^^^^^^^^^^^^^^^^

Defines access to the :doc:`Segments  </userguide/segments/index>` section and its individual menu elements

+---------------------------------------------+----------------------------------------+
| VIEW                                        | MODIFY                                 |
+=============================================+========================================+
|- Segments list preview                      | All **View** permissions, and more:    |     
|- Sorting options of segment list            |                                        |
|- Customers assigned to segment list preview*| - Creating customer segment            |
|- Download the customers list**              | - Updating segments data               |
|                                             | - Activate / Deactivate segment        |
|                                             | - Remove segment                       |
+---------------------------------------------+----------------------------------------+

.. note:: 

    **Customers assigned to segment list preview*** 
    
    To enable customer assigned to particular segment details preview you must have at least an **Customers View access**. 
    
    If there is no Customers access, then you can not see the ``Show`` button to preview customers details. You can only see customers account number assigned to this segment.


.. note:: 

    **Download the customers list**** 
    
    To download a list of customers assigned to particular segment you must have at least an **View access** to the following: 
     - *Customers* - to view customers details 
     - *Utilities* - to export the list of customers  
    
    If there is no Customers access, then you can not even see the download icon.


.. warning:: 

    Remember, that granting *View* access for Customers section (to enable customer details preview), you give an access to the entire Customers menu section (in accordance with the permissions listed in the Customers table in *View* column) 



Settings
^^^^^^^^^^^^^^^^^^

Defines access to the :doc:`Emails  </userguide/getting_started/settings/emails>` , :doc:`Translations  </userguide/getting_started/settings/translations>` and :doc:`Configuration  </userguide/getting_started/settings/Configuration/index>`  settings sections and its individual elements

+---------------------------------------------+----------------------------------------+
| VIEW                                        | MODIFY                                 |
+=============================================+========================================+
|- Translations list preview                  | All **View** permissions, and more:    |     
|- Emails list                                |                                        |
|                                             | - Create new translations              |
|                                             | - Updating translation                 |
|                                             | - Delete non-default translations      |
|                                             | - Updating an email template           |
|                                             | - Email template preview               |
|                                             | - Configuration section management     |
+---------------------------------------------+----------------------------------------+


Transactions
^^^^^^^^^^^^^^^^^^

Defines access to the :doc:`Transactions  </userguide/transactions/index>` section and its individual menu elements

+-------------------------------------------------+----------------------------------------+
| VIEW                                            | MODIFY                                 |
+=================================================+========================================+
|- Transactions list preview*                     | All **View** permissions, and more:    |     
|- Filter and sorting options of transactions list|                                        |
|- Transactions details preview*                  | - Match transaction with customer**    |
|                                                 | - Transaction labels ceation           |
|                                                 | - Transaction labels edition           |
|                                                 | - Importing transactions from a file   |
+-------------------------------------------------+----------------------------------------+

.. tip:: 

    **Transactions list and it's details preview***
    
    Even if User has no access to the *Customer* section, in *All transactions* grid and in transaction details, informations about customer related with transaction will be visible. 
  
  
.. note:: 

    **Match transaction with customer****

    To enable manually assignment transaction to customer, you must have at least a **Customers View access** (*E-mail or phone* field is required).  
    
    If there is no Customers access, then you can not provide any value to find customer and assigne transaction.   
  

Utilities
^^^^^^^^^^^^^^^^^^

Enable export options


+-------------------------------------------------+
| VIEW & MODIFY                                   |                                 
+=================================================+
|- download customer assigned to level list       |    
|- download customer assigned to segment list     |
+-------------------------------------------------+

.. tip:: 

    Regardless of access level, user has the same options in both - **View and Modify**
    
.. tip:: 

    To download redeemed rewards report *Utilities* resource is not needed - *Reward Campaign View access* is enough   
    
    
  
