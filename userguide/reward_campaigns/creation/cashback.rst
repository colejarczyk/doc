.. index::
   single: cashback

Cashback
========

During purchase customer can exchange earned points and get value discount to reduce order amount. Discount is calculated based on **Point value**. Each point will be exchanged for provided value in **Point value** field (regarding current currency)

**For example**

- local currency is EUR
- point value is equal 2 (i.e. 1 point = 2 EUR)
- customer has 50 points

Customer **total amount of transaction is 100 EUR**. Based on point value, if he exchanges all his points (50), he can get order for free.

If he exchanges part of his points e.g. 20, he will receive 40 EUR discount, and will have to pay 60 EUR for his order (instead of 100 EUR)

.. note::

    If more than one Cashback campaign is available and active only ONE of them will be used - the one with the best conversion rate at given time (better *Point value*)


To create Cashback reward:
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Reward campaigns**. Then choose **Add reward campaign**. You can also add new reward directly from **All reward campaigns** list by clicking ``Add reward campaign`` at the top of the page

.. image:: /userguide/_images/add_reward_button.png
   :alt:   Add Reward Options

2. In **Campaign type** section select a **Cashback** reward type from a dropdown list (by default Discount code is displayed)

.. image:: /userguide/_images/cashback_type.PNG
   :alt:   Cashback type

.. note::

    Depending on the selected **Campaign type**, Basic information section and the next one, **Campaign details**, will display different fields to be filled in.

    Different fields are required for *Cashback, Custom reward and Percentage discount code* than for other types, that is discount code, free delivery etc.

.. image:: /userguide/_images/cashback_basic.PNG
   :alt:   Cashback Basic Information

3. When you choose *Cashback*, in the **Basic information** section related to the default language version do the following

 - Enter unique reward **Name**
 - If needed, provide a **Short description** of the reward campaign detail using rich media format
 - If needed, in **Brand name** field provide the name of the brand, that will be display in Client cockpit
 - If needed, provide a **Brand description** of the reward campaign using rich media format
 - If applicable, fulfill the same fields in other language version e.g. polish as on a screen above

.. image:: /userguide/_images/cashback_details.PNG
   :alt:   Cashback Campaign Details

4. In the **Campaign details** section do the following

 - To make reward available for customer, in **Active** field select "**Active**" from the dropdown list
 - If needed, enter URL to the content page in **More information link field**, that explains your reward campaign or to external web with reward details
 - If applicable, in **Push notification text** provide a text message that will be displayed as a push notification for Customer, when reward become available for them
 - In **Point value** field, enter the monetary value of the points to define the number of points that can be applied as a refund towards the amount of order
 - If applicable, In **Reward value** field provide a monetary value of reward
 - If needed, enter **Tax** rate that applies to the reward and monetary value of tax for reward in **Tax value**
 - If applicable, mark **Featured** checkbox to differentiate campaign from the others. **Feature is used when you want to filter campaigns using API**
 - If applicable, mark **Public** checkbox to differentiate campaign from the others. **Feature is used when you want to filter campaigns using API**

.. note::

    If **Push notification text** is not provided, notification about new reward availability will not be sent.

    It does not change the fact that the reward will be available for customer and will be displayed in **Available rewards** section in Admin and Client cockpit.

5. In the same **Campaign details** section, if applicable, create **Label(s)** you want refer to reward. Labels are intended to be used to specify identifying attributes of reward campaign.

   Labels can be used only when you use API to organize subsets of rewards and make filtering/searching rewards campaign easier.  Through API you will be able to get list of all rewards with specified key or key and value.

 - To create a Label, tap ``Add Label`` and do the following:
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

6. In the same **Campaign details** section, in **Categories** field, select campaign category or categories to be assigned to this reward campaign. You can assign more than one campaign category.

.. image:: /userguide/_images/reward_category.png
   :alt:   Campaign category

7. **Brand info** section allows to upload an image of the reward brand, that will be displayed in Client cockpit

.. image:: /userguide/_images/reward_brand.png
   :alt:   Brand info

8. A reward can be extended to members of a specific customer group. In the **Target** section identify the customer group that qualifies to receive the reward

 - In **Target type** field, select from dropdown list Level or Segment to specify whether the reward will be available for customers assigned to particular level or segment
 - Depending on selected *Target type*, field **Segments** to specify segments or **Levels** to specify levels appear.  You can choose one or more levels/segments to used

.. image:: /userguide/_images/reward_target.png
   :alt:   Target

9. **Activity** section defines time boundaries when reward can be used by customers. To make the reward *available for a limited period of time*, complete the **From and To dates** in Activity section:

 - In **Active from** field set the first date the reward is available. You can either enter the date or select it from the calendar
 - In **Active to** field set the last date the reward is available. You can either enter the date or select it from the calendar
 - If you want the reward to be active all the time,please mark **All time active** checkbox. When you choose that option *Active from and Active to fields will not be available*.

.. image:: /userguide/_images/reward_activity.png
   :alt:   Activity

.. note::

    **Active to** and **Active from** fields are available only when reward activity (availability) is limited

.. note::

    Status of the Reward campaign (Active/Inactive) has higher priority than time boundaries from Active section.

    Even if time boundaries from Activity section are valid, changing Status to Inactive means that reward will not be available to customers.

10. When it is done, tap ``SAVE``

.. warning::

    Cashback is visible for a customer in Available rewards section in Client Cockpit but without possibility to redeem it 
