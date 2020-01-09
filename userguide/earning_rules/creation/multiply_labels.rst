.. index::
   single: multiply_labels

Multiply earned points by product labels
========================================

Multiply points that customer receive for purchase products with specified labels. The rule is related to General spending rule. The rule defines for which purchased products, points (defined in rules above) are to be multiplied. 

Rule can contains more than one product label. Different **Labels** are linked with OR condition - at least one of labels linked with this rule must be true to let customer earn points. If more than one is true, points are multiply in order by all multipliers.

**For example**

if you have 2 labels assigned to this rule which are true, points gathered from purchases are multiply firstly by multiplier assigned to 1st label, and then again multiply by multiplier assigned to 2nd label. 

To add new Multiply earned points by product labels:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Earning rules**. Then, choose **Add earning rule**. You can also add rule directly from **All earning rules** list by clicking ``Add earning rule`` at the top of the page 

.. image:: /userguide/_images/add_rule_button.png
   :alt:   Add Rule Options  
   
.. image:: /userguide/_images/basic_rule.png
   :alt:   Add Earning Rule Form

2. In **Basic informations** section, do the following:  

 - Enter **Name** of the rule that will be displayed in views
 - Provide a brief **Description** of the rule that explains how to award points and information when the rule is active (thereby using to points calculation) 
 - To activate the rule, in **Active** field select "**Active**" from the dropdown list

.. image:: /userguide/_images/multiply_labels.png
   :alt:   Multiply earned points by product labels

3. In **Type details** section set rule **type** as Multiply earned points by product labels and complete details as follow: 

 - To create Label, tap ``Add label multiplier`` and do the following:
    - Type label **Key**, which is a product label name
    - Type label **Value**
      For example: Key – trousers, Value – jeans
    - Points gained for purchase product will be multiplied by factor provided in **Multiplier** field
 
      Repeat the process for all labels you want to use in your Loyalty Program
 
 - If you marked **Is last executed rule** checkbox, then you add a "stoppable" flag to this rule.
 
   The behavior of the flag is the same like in :doc:`Multiply earned points rule </userguide/earning_rules/creation/multiply>`

   See :doc:`Rule Types </userguide/earning_rules/creation/rule_type>` to learn more about Earning rules types
   
.. note:: 

    **Another words, only these rules that occur in the sequence before the Multiply earned points by product labels rule with a flag and the rule itself will be used – in that case, if applicable, General spending rule, Multiply earned points by product labels rule edited after added a flag and rule with a flag itself**. 

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

In exceptional case also Multiply earned points rule also can be used – please see Exceptional case box

Exceptional case of stoppable flag
**********************************

**When also Multiply earned points or Instant reward will be used?**

The same case as was described in Multiply earned points rule exception. If you add a "stoppable" flag to this rule and before points calculation you will also edited Multiply earned points (name, description, activity etc.), Open Loyalty recognize the second one as the most "current" and use it before the rule with stoppable flag.

In this exceptional case, the sequence of points calculation can be as follow:

1. **If applicable, General spending rule** 
2. **Multiply earned points** - *edited rule, the most "current"*
3. **Multiply earned points by product labels** - *rule with stoppable flag*  
