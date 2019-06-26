.. index::
   single: redeemed_rewards

Redeemed rewards
================

**Redeemed rewards** tab provides information about rewards (Reward Campaigns) that customer has redeemed, divided into used and delivered.

.. image:: /userguide/_images/redeemed_rewards.png
   :alt:   Redeemed Rewards

All rewards that customer redeemed appear in this tab as "**delivered**".

When reward coupon days inactive parameter will pass, an empty checkbox appears, to be marked when customer redeems coupon.

Only when a customer uses the reward/discount code during a purchase, reward is treated as "**used**".

On the Redeemed rewards list, **Used** rewards will have a marked checkbox in the column Use of coupon count, unlike to those **Delivered**, which will have an empty checkbox.

From the Admin Panel you can mark selected redeemed reward record as Used when customer used their coupon code during purchase, or you sent gift which customer selected from his cockpit etc.

.. note::

    You can mark selected reward/coupon record as used or unused only if its status is **Active**

    When coupon status changed to **Expired** none of the above operations is possible.



To mark coupon as used:
^^^^^^^^^^^^^^^^^^^^^^^

1. In the Redeemed reward list, find the reward you want to mark as Used and click checkbox in the **Use of coupons count** column 

.. image:: /userguide/_images/used_reward.png
   :alt:   Used/Delivered reward

To see the list of all redeemed rewards by customer within Loyalty Program click ``All Rewards`` below the tab.

To learn more about rewards, see :doc:`Redeemed rewards </userguide/reward_campaigns/redeemed_rewards>`

+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Field             | Description                                                                                                                 |
+===================+=============================================================================================================================+
| Name              | | Reward name, that is  display to customer                                                                                 |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Cost in points    | | Define how much points customer spent to redeem reward                                                                    |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Status            | | Reward campaign coupon status                                                                                             |
|                   | | **Option include: Active/Inactive/Expired**                                                                               |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Active from       | | Reward campaign start date from which customer can used reward, define during reward campaign creation in Activity section|
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Active to         | | Reward campaign end date until which customer can used reward, define during reward campaign creation in Activity section |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Purchased at      | | The date when reward was redeemed                                                                                         |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Coupon            | | Discount code that was used                                                                                               |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Use of coupon     | | Define whether customer already used the reward or it’s only delivered and can be used by him                             |
| count             |                                                                                                                             |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
