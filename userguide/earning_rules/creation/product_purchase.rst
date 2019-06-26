.. index::
   single: product_purchase

Product purchase
================

Reward customer with defined amount of points for purchase specified products. Rule can be related to Multiply earned points rule and General spending rule. 

To add new Product purchase rule:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Earning rules**. Then, choose **Add earning rule**. You can also add rule directly from **All earning rules** list by clicking ``Add earning rule`` at the top of the page 

.. image:: /userguide/_images/add_rule_button.png
   :alt:   Add Rule Options  
   
.. image:: /userguide/_images/basic_rule.png
   :alt:   Add Earning Rule Form

2. In **Basic informations** section, do the following:  

 - Enter **Name** of the rule that will be displayed in views
 - Provide a brief **Description** of the rule that explains how to award points and information when the rule is active (thereby using to points calculation) 
 - To activate the rule, in **Active** field select "**Active**" from the dropdown list

.. image:: /userguide/_images/product_purchase.png
   :alt:   Product purchase

3. In **Type details** section set rule **type** as Product purchase and complete details as follow:

 - Rule will be applied only for listed products with selected **SKU**s
 
 - in **Points** field enter predefined amount of points that will be earned  
 
 - If you marked **Is last executed rule** checkbox, then you add a "stoppable" flag to this rule.
 
   It means, that if more than this transactional rule can be applied, next transactional Earning Rule will be skipped and Product purchase will be used as the last one (according to the sequence). 

   See :doc:`Rule Types </userguide/earning_rules/creation/rule_type>` to learn more about Earning rules types
   
.. note:: 

    **Another words, only these rules that occur in the sequence before the Product purchase rule with a flag and rule itself will be used – in that case, if applicable, General spending rule, both Multiply earned points rules, Product purchase rules edited after added a flag and rule with a flag itself**

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

In exceptional case also more than one product purchase rule can be used – please see Exceptional case box. 

Exceptional case of stoppable flag
**********************************

**What if there are more than one Product purchase rule to be used?**

All Product purchase rules have the same priority. It means, that to points calculation the most "current" rule is used. In that case, "current" means edited as the last one. 

So, if you add a "stoppable" flag to 1st rule and before points calculation you will also edited 2nd and 3rd (name, description, activity etc.), Open Loyalty recognize the 2nd and 3rd as the more "current" and use them before the rule with stoppable flag.  

.. note:: 

    **Another words, any edited Product purchase rule will be used before that one with "stoppable" flag, if edition was made after you add a flag to the rule** 

In this exceptional case, the sequence of points calculation can be as follow:

1. **If applicable, General spending rule** 
2. **If applicable, Multiply earned points** 
3. **3rd  Product purchase rule** - *rule edited today, the most "current"*
4. **2nd  Product purchase rule** - *rule edited yesterday, more "current" than the flag rule*    
5. **1st  Product purchase rule** - *rule with stoppable flag, added day before yesterday*
