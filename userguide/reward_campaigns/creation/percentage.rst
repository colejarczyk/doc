.. index::
   single: percentage

Percentage discount code
========================

After purchase customer can receive value discount for next purchase base on registered order amount.
Discount is calculated based on **Transaction percentage value**.
Discount will be equal to percentage value of transaction provided in **Transaction percentage value** field.

.. note::

    If more than one Percentage discount code campaign is available and active all will be applied.

    So it is possible that the customer will receive several value codes of different value.

**For example**

- local currency is EUR 
- Transaction percentage value is equal to 10 (i.e. 10% of registered transaction total amount) 

If Customer total amount of transaction is **100 EUR**, he will receive **10 EUR** discount for next purchase 

If Customer total amount of transaction is **47 EUR**, he will receive **5 EUR** discount for next purchase 

If Customer total amount of transaction is **32 EUR**, he will receive **3 EUR** discount for next purchase 

.. note:: 

    **Percentage discount code must be match with specified customer transaction to be used**.
    
    It can be match manually by Admin from Reward campaign list or automatically assigned within Instant reward rule


To create Percentage discount code reward:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Reward campaigns** and choose **Add reward campaign**. You can also add new reward directly from **All reward campaigns** list by clicking ``Add reward campaign`` at the top of the page 

.. image:: /userguide/_images/add_reward_button.png
   :alt:   Add Reward Options  


2. In the **Campaign type** section select a **Percentage discount code** reward type from a dropdown list (Discount code is displayed by default)

.. image:: /userguide/_images/percentage_type.PNG
   :alt:   Percentage discount code type

.. note:: 

    Depending on the selected **Campaign type**, a Basic information and next section - Campaign details, will display different fields to filled in.
    
    Different fields are required for *Cashback, Custom reward and Percentage discount code* , than for other types i.e. discount code, free delivery etc.  

.. image:: /userguide/_images/cashback_basic.PNG
   :alt:   Percentage discount code Basic Information


3. When you choose *Percentage discount code*, in the **Basic information** section related to the default language version do the following

 - Enter unique reward **Name**
 - If needed, provide a **Short description** of the reward campaign detail using rich media format 
 - If needed, in **Brand name** field provide the name of the brand, that will be display in Client cockpit
 - If needed, provide a **Brand description** of the reward campaign using rich media format
 - If applicable, fulfill the same fields in other language version e.g. polish as on a screen above

.. image:: /userguide/_images/details_percentage.PNG
   :alt:   Percentage discount code campaign details


4. In the **Campaign details** section do the following

 - To make reward available for customer, in **Active** field select "**Active**" from the dropdown list

 - If needed, enter URL to the content page in **More information link field**, that explains your reward campaign or to external web with reward details 

 - If applicable, in **Push notification text** provide a text message that will be displayed as a push notification for Customer, when reward become available for him

 - In **Transaction percentage value** field provide a value of voucher which is calculated based on the transaction amount.  
 
   **For example**, if you enter 10, customer receive voucher worth 10% of the transaction value. 

 - If applicable, In **Reward value** field provide a monetary value of reward

 - If needed, enter **Tax** rate that applies to the reward and monetary value of tax for reward in **Tax value**

 - If applicable, mark **Featured** checkbox to differentiate campaign from the others. **Feature is used when you want to filter campaigns using API**

 - If applicable, mark **Public** checkbox to differentiate campaign from the others. **Feature is used when you want to filter campaigns using API**

.. note::

    If **Push notification text** is not provided, notification about new reward availability will not be displayed.

    It does not change the fact that the reward will be available for customer and display in **Available rewards** section in Admin and Client cockpit.


5. In the same **Campaign details** section, if applicable, create **Label(s)** you want refer to reward. Labels are intended to be used to specify identifying attributes of reward campaign. 
 
   Labels can be used only when you use API to organize subsets of rewards and make filtering/searching rewards campaign easier.  Through API you will be able to get list of all rewards with specified key or key and value. 
   
 - To create Label, tap ``Add Label`` and do the following: 
  - Type label **Key**, which is a label name
  - Type label **Value**
      
    For example: Key – Event, Value – Birthday. 
          
 - Repeat the process for all labels you want to used in your Loyalty Program
  
.. image:: /userguide/_images/reward_label.png
   :alt:   Reward Campaign Labels    
   
.. note:: 

    Filtering/Searching via API allows you to get list of all rewards related to events or (more specified) related to birthday event. 
    
.. note:: 

    Labels can be added to reward campaign during reward creation and subsequently added and modified at any time 


6. In the same **Campaign details** section, in **Categories** field, select campaign category or categories to be assign to this reward campaign. You can assign more than one campaign category. 

.. image:: /userguide/_images/reward_category.png
   :alt:   Campaign category      


7. **Brand info** section allow to upload an image of the reward brand, that will be display in Client cockpit

.. image:: /userguide/_images/reward_brand.png
   :alt:   Brand info 


8. A reward can be extended to members of a specific customer group. In the **Target** section identify the customer group that qualifies to receive the reward

 - In **Target type** field, select from dropdown list Level or Segment to specify whether the reward will be available for customers assigned to particular level or segment
 - Depending on selected *Target type*, field **Segments** to specify segments or **Levels** to specify levels appear.  You can choose one or more levels/segments to used

.. image:: /userguide/_images/reward_target.png
   :alt:   Target


9. In the **Coupons** section set the discount coupon expiration and inactive time boundaries

 - In **Days inactive** define number of days during which coupons assign to this campaign will be inactive since the transaction date.

   **If you want make coupons valid instantly, provide 0**

 - In **Days valid** specify number of days during which coupon assign to this campaign will be active since the inactive time boundaries finished. After provided here number of days voucher will expired.

   **If you want your coupons never expired, provide 0**

.. image:: /userguide/_images/coupon.PNG
   :alt:   Coupons


10. **Activity** section defines time boundaries when reward can be used by customers. To make the reward *available for a limited period of time*, complete the **From and To dates** in Activity section:

 - In **Active from** field set the first date the reward is available. You can either enter the date or select it from the calendar
 - In **Active to** field set the last date the reward is available. You can either enter the date or select it from the calendar
 - If you want the reward to be active all the time mark **All time active** checkbox. When you choose that option *Active from and Active to fields will not be available*.
 
.. image:: /userguide/_images/reward_activity.png
   :alt:   Activity

.. note:: 

    **Active to** and **Active from** fields are available only when reward activity (availability) is limited

.. note:: 

    Status of the Reward campaign (Active/Inactive) has higher priority than time boundaries from Active section.
    
    Even if time boundaries from Activity section will be valid,  changing Status to Inactive means that reward will not be available to customers.


11. When it is done, tap ``SAVE``


.. warning:: 

    Percentage discount code is not visible for a customer in Available rewards section in Client Cockpit
