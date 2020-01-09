.. index::
   single: qrcode

QR code
=======

Reward customer with defined amount of points for scanning QR code e.g. of product. Code for which customer can get points is defined in the Open Loyalty. 

If needed, you can also add repeatability limit to this rule type. 

This Earning rule could be call only with API. Every run of API function will reward Customer with defined points. 

To add new QR code rule:
^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Earning rules**. Then, choose **Add earning rule**. You can also add rule directly from **All earning rules** list by clicking ``Add earning rule`` at the top of the page 

.. image:: /userguide/_images/add_rule_button.png
   :alt:   Add Rule Options  
   
.. image:: /userguide/_images/basic_rule.png
   :alt:   Add Earning Rule Form

2. In **Basic informations** section, do the following:  

 - Enter **Name** of the rule that will be displayed in views
 - Provide a brief **Description** of the rule that explains how to award points and information when the rule is active (thereby using to points calculation) 
 - To activate the rule, in **Active** field select "**Active**" from the dropdown list

.. image:: /userguide/_images/qrcode.png
   :alt:   QR code

3. In **Type details** section set rule **type** as QRcode and complete details as follow:

 - QR **Code** (to be used with calling API function) 
 - Number of **Points** that will be added after earning rule has been triggered
 - You can limit how many times customer could be rewarded for the same action with the specified period of time. Mark **Usage limit active** checkbox to limit repeatability. Leave it blank to reward customer for this rule without limits.
 - **Period** field is visible and required if *Usage limit active* is marked.
   
   It defines period of time within customer can be rewarded for this rule. Option include: 
    - 1 day 
    - 1 week
    - 1 month
 - **Limit** field is visible and required if *Usage limit active* is marked. 

   Provided number defines how many times customer could be rewarded for this rule in specified period of time. 

   See :doc:`Rule Types </userguide/earning_rules/creation/rule_type>` to learn more about Earning rules types
   
.. note:: 

    If customer used the limit then rule will not be shown on available rules list in Customer cockpit

.. note:: 

    **once selected type can not be changed**

4. In **Activity of rule** section specify time boundaries when rule will be active

 - if you want the rule to be active all the time mark **All time active** checkbox 
 - if you want the rule to be limited in time in **Start at** and **End at** fields specify dates between rule will be active

5. In **POS** section, as an option you can assign an Earning rule to the existing POS. To do this, click **POS** field and choose store to which rule will be applied. 

   When a transaction comes from a specific POS, only earning rules assigned to this POS will be used to calculate points. 

.. image:: /userguide/_images/rule_pos.png
   :alt:   Earning rule assignment to POS
   
6. In **Target** section specify group of customers for which rule will be used. For example, Gold members will get 2 times more points than Bronze   

 - In **Target type** choose from dropdown list Level or Segment to specify whether the rule will be active for customers assigned to particular level or segment. 
 - Depending on the **Target type** field **Segments** to specify segments **or Levels** to specify levels appear.  You can choose one or more levels/segments to used

.. image:: /userguide/_images/rule_level.png
   :alt:   Earning rule target option
   
.. image:: /userguide/_images/rule_segment.png
   :alt:   Earning rule target option

7. If applicable, in **Earning rule photo** section upload image for Earning rule

.. image:: /userguide/_images/rule_photo.png
   :alt:   Earning rule photo option

8. When complete, tap ``SAVE``


.. note:: 

    Image size is limited to 2MB. Image dimensions could not be smaller than 600 x 600 px. Allowed file formats: png, gif, jpg.

