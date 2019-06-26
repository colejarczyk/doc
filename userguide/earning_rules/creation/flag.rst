.. index::
   single: flag

Set rule as the last one
========================

.. note:: 

    **this feature is related ONLY with transactional rules**

**If there are more than one Earning Rule to be applied and one of them has a flag "stoppable", then this rule will be applied and stops any further rules according to sequence listed above**.

When customer registers a transaction, Open Loyalty checks for Earning Rules that can be applied. Then Open Loyalty starts executing each Earning Rule. When executed Earning Rule has a flag "stoppable" it should be the last Earning Rule executed for that transaction which means any next Earning Rules should be skipped.

Exceptional case
****************

By default only one of the following, the most "current" rule (edited as the last one) is used:

 - Multiply earned points,
 - Multiply earned points by product labels and
 - Instant reward 

But, if you add a "stoppable" flag to one of them and before points calculation you will also edited any of Multiply points rules or Instant reward (name, description, activity etc.), Open Loyalty recognize the edited one as the most "current"and use it before the rule with stoppable flag. The behavior is also related  with more than one this rule type.

In this exceptional case, the sequence of points calculation can be as follow:

1. **If applicable, General spending rule**
2. **Multiply earned points** - *rule edited today, the most "current"*  
3. **Multiply earned points by product labels** - *rule edited today, but before Multiply earned points rule edition*
4. **2nd Instant reward** - *rule edited yesterday*
5. **1st Instant reward** - *rule with stoppable flag added day before yesterday*   
