.. index::
   single: general

General spending rule
=====================

Reward customer with defined amount of points for his order value. Allows to specify how many points customer can earn from 1 amount of currency. 

If needed, you can exclude certain products (with define SKUs or labels) and delivery costs from the points calculation.

To add new General spending rule:
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

.. image:: /userguide/_images/general.png
   :alt:   General Spending Rule 

3. In **Type details** section set rule **type** as General spending rule and complete details as follow:

 - In **Point value** enter ratio for calculating earned points based on purchased value. For example, if ratio is 2 then user get 2 points for every 1$ spent. 
   
 - SKU's provided in **Excluded SKUs** field will be excluded from the calculation of earned points
 
 - Points can be calculated for the purchase of products with defined labels. Set **Labels inclusion type** to one of following:
 
    - **None**
       product labels are not applicable. Points will be calculated for all purchased products (except excluded SKUs, if applicable) 
    - **Exclude**
       points will not be calculated for purchased products with defined labels 
    - **Include**  
       points will be calculated for purchased products with defined labels

 - Depending on the option chose in **Labels inclusion type** field, appropriate field will be display: 
   
    - **Has labels** – when *Include* is selected in previous step 
    - **Excluded labels** – when *Exclude* is selected in previous step
    - When *None* is selected in previous step, any field is not displayed
   
      Both fields, **Has labels** and **Excluded labels** are pair of Key and Value.

 - When **Excluded delivery costs** checkbox is selected then delivery cost will not be included in order value used for earned points calculation 
 
 - **Min order value** is currently not used
 
 - If you marked **Is last executed rule** checkbox, then you add a "stoppable" flag to this rule. 
   
   It means, that if more than this transactional rule can be applied, any next transactional Earning Rules will be skipped (other general spending rules, multiply points rules, product purchase rule). 
 
 
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
   

Exceptional case of stoppable flag
**********************************

**What if there are only general spending rules to be used and there are more than one?**

| All General spending rules have the same priority. It means, that to points calculation the most "current" rule is used. In that case, "current" means edited as the last one. 

| So, if you add a "stoppable" flag to 1st rule and before points calculation you will also edited 2nd and 3rd (name, description, activity etc.), Open Loyalty recognize the 2nd and 3rd as the more "current" and use them before the rule with stoppable flag.   

.. note:: 

    **Another words, any edited General spending rule will be used before that one with "stoppable" flag, if edition was made after you add a flag to the rule**. 

In this exceptional case, the sequence of points calculation can be as follow:

1. **3rd  General spending rule** - *rule edited today, the most "current"*
2. **2nd General spending rule** - *rule edited yesterday, more "current" than the flag rule*
3. **1st  General spending rule** - *rule with stoppable flag added day before yesterday*

     
