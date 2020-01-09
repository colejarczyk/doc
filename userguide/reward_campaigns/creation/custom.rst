.. index::
   single: custom

Custom campaign
===============

Receiving reward by customer may be linked with :doc:`geolocation </userguide/earning_rules/creation/geolocation>` or :doc:`QR code </userguide/earning_rules/creation/qrcode>` earning rule. Rule to which reward will be assigned is specified in **Connect type** field.

If customer redeemed reward, and conditions of linked rule will be met, additional points will be assign to his account. 

**For example**

- during reward creation, **geolocation** earning rule has been assigned, for which (when it is fulfilled) customer can get 10 points. 
  
  When during reward redeeming, customer is in specified in geolocation rule location (rule radius, latitude, longitude conditions are met), **except reward that he redeemed additional 10 points goes to his Active points pool**. If rule conditions are not fulfilled, customer receive only reward (without additional points). 

- during reward creation, **qr code** earning rule has been assigned, for which (when it is fulfilled) customer can get 15 points.  

  When during reward redeeming, customer will scan specified in qr code rule code (e.g. redeeming reward is done by scanning code), **except reward that he redeemed additional 15 points goes to his Active points pool**. If rule conditions are not fulfilled, customer receive only reward (without additional points). 

To create Custom campaign reward:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Reward campaigns**. Then, choose **Add reward campaign**. You can also add new reward directly from **All reward campaigns** list by clicking ``Add reward campaign`` at the top of the page 

.. image:: /userguide/_images/add_reward_button.png
   :alt:   Add Reward Options  

2. Scroll down to **Campaign type** section and select a **Custom campaign** reward type from a dropdown list (by default Discount code is displaying)

.. note:: 

    Depending on the selected **Campaign type**, a Basic information and next section - Campaign details, will display different fields to filled in.
    
    Different fields are required for *Cashback, Custom reward and Percentage discount code* , than for other types i.e. discount code, free delivery etc.     

.. image:: /userguide/_images/custom_basic.png
   :alt:   Custom Campaign Basic Information

3. When you choose *Custom campaign*, in the **Basic information** section related to the default language version do the following

 - Enter unique reward **Name**
 - If needed, provide a **Short description** of the reward campaign detail using rich media format 
 - If applicable, in **Condition description** field, provide a description of the conditions of getting a reward using rich media format
 - If needed, in **Brand name** field provide the name of the brand, that will be display in Client cockpit
 - If needed, provide a **Brand description** of the reward campaign using rich media format
 - If applicable, fulfill the same fields in other language version e.g. polish as on a screen above

.. image:: /userguide/_images/custom_details.png
   :alt:   Custom campaign details 

4. In the **Campaign details** section do the following

 - To make reward available for customer, in **Active** field select "**Active**" from the dropdown list
 - If needed, enter URL to the content page in **More information link field**, that explains your reward campaign or to external web with reward details 
 - If applicable, In **Reward value** field provide a monetary value of reward
 - If needed, enter **Tax** rate that applies to the reward and monetary value of tax for reward in **Tax value**
 - If applicable, mark **Featured** checkbox to differentiate campaign from the others. **Feature is used when you want to filter campaigns using API**
 - If applicable, mark **Public** checkbox to differentiate campaign from the others. **Feature is used when you want to filter campaigns using API** 

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
   
7. In the same **Campaign details** section, in **Connect type** field, set earning rule type that will be linked with this campaign, to one of the following:  

 - **Geolocation earning rule**   
      Customer could receive points for his location
 - **QRCode earning rule**  
      Customer could receive points for scanning define QR code 
 - **None**  
      Any earning rule linked 

   If you choose any other type than *None*, choose one of the **Earning rule** from a dropdown (related to the type choose in previous step)

.. image:: /userguide/_images/custom_rule.png
   :alt:   Earning rule

.. note:: 

    Displaying earning rule names will be related with type, chose in previous step.
    
    For example, if you set Connect type to Geolocation earning rule, only Geolocation earning rules will be listed.  

8. **Brand info** section allow to upload an image of the reward brand, that will be display in Client cockpit

.. image:: /userguide/_images/reward_brand.png
   :alt:   Brand info 

9. A reward can be extended to members of a specific customer group. In the **Target** section identify the customer group that qualifies to receive the reward

 - In **Target type** field, select from dropdown list Level or Segment to specify whether the reward will be available for customers assigned to particular level or segment
 - Depending on selected *Target type*, field **Segments** to specify segments or **Levels** to specify levels appear.  You can choose one or more levels/segments to used

.. image:: /userguide/_images/reward_target.png
   :alt:   Target


10. To make the reward *visible on the storefront for a limited period of time*, complete the **From and To dates** in **Visibility** section

 - In **Visible from** field set the first date the reward is visible. You can either enter the date or select it from the calendar
 - In **Visible to** field set the last date the reward is visible. You can either enter the date or select it from the calendar
 - If you want the reward to be visible all the time mark **All time visible** checkbox. When you choose that option *Visible from and Visible to fields will not be available*. 

.. image:: /userguide/_images/reward_visibility.png
   :alt:   Reward Visibility

.. note:: 

    **Visible to** and **Visible from** fields are available only when reward visibility is limited


11. **Activity** section define time boundaries when reward can be used by customers. To make the reward *available for a limited period of time*, complete the **From and To dates** in Activity section:  

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


12. When complete, tap ``SAVE``  


.. warning:: 

    Custom campaign is not visible for a customer in Available rewards section in Client Cockpit  
