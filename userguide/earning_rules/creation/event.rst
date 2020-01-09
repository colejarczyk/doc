.. index::
   single: event

Event rule
==========

Reward customer with defined amount of points for his action. Actions for which customer can get points are predefined in the Open Loyalty and related to events of your loyalty program. 

For example, create an account, first purchase etc.

To add new Event rule:
^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Earning rules**. Then, choose **Add earning rule**. You can also add rule directly from **All earning rules** list by clicking ``Add earning rule`` at the top of the page 

.. image:: /userguide/_images/add_rule_button.png
   :alt:   Add Rule Options  
   
.. image:: /userguide/_images/basic_rule.png
   :alt:   Add Earning Rule Form

2. In **Basic informations** section, do the following:  

 - Enter **Name** of the rule that will be displayed in views
 - Provide a brief **Description** of the rule that explains how to award points and information when the rule is active (thereby using to points calculation) 
 - To activate the rule, in **Active** field select "**Active**" from the dropdown list

.. image:: /userguide/_images/event.png
   :alt:   Event rule

3. In **Type details** section set rule **type** as Event rule and complete details as follow:

 - in **Event name** field select an event for which the customer will receive points. Options include:
    - Account created
    - Customer logged in 
    - First purchase
    - Newsletter subscription 
    
 - provide amount of **Points** that will be earned for this event rule
 
   See :doc:`Rule Types </userguide/earning_rules/creation/rule_type>` to learn more about Earning rules types

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

