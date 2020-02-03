.. index::
   single: redeemed_rewards

Redeemed rewards
================

Redeemed reward is an instance of reward that Customer has bought with Points or earned for performing specified action.

There is possibility to get:

 - virtual reward - as a Discount or Value Code, free delivery 
 - physical reward - which will be send to Customer, e.g. printed coupon, gift, etc.
 - cashback

.. note::

    When "buying" reward campaign using customer points, points that are expiring soon are used first

**Not enough points from Customer perspective**

In the Client Cockpit, if Customer does not have enough points to redeem reward then Redeem reward button will be disabled (greyed out).

When mouse hover over disabled button then tooltip will show "You must have <<reward cost - customer active points>> more points to get reward"


**Redeemed reward from Admin perspective**

Redeemed reward management could be performed only from Administrator Cockpit by user who has Admin privileges.

Redeemed rewards list grid provide an information about which customer and when redeemed and used given reward.

Moreover, you can check whether reward is **Delivered** (customer choose reward and spent points but he has not used it yet) or mark as **Used** (customer used coupon code during purchase, gift was sent to customer etc.)

.. note::

    You can mark selected reward/coupon record as Used or unmark if is not used only if it's status is **Active**

    When coupon status changed to **Expired** none of the above operations is possible.

By default all **Used** rewards receive the *Delivery status* **Ordered**. In the case of a *Used* Gift reward, additionally you can manage the status of its delivery to the customer.  More in :doc:`Gift fulfillment tracking process </userguide/reward_campaigns/creation/fulfillment_tracking>` section.

You can also see customer address on which reward will be sent by clicking **View**  |view|  icon in the Action column. This option is available for every reward types.

.. |view| image:: /userguide/_images/view.png

.. image:: /userguide/_images/redeemed2.PNG
   :alt:   Redeemed Rewards

Use the standard controls to filter the list by **Redeem date and time** and **Usage date and time**. You can also get a list of reward that are **Delivered** or **Used** by filter *Unused/used* column. By default Redeemed rewards grid show both – delivered and used rewards.

Moreover, you can sort and filter the list by redeemed rewards **Delivery status**.

Pagination controls appear if there are more redeemed rewards records than fit on the page, and are used to move from one page to the next.



To see all Redeemed rewards:
----------------------------
Tap ``Reward campaigns`` on the Admin sidebar and choose **Redeemed rewards** 


Field description
*****************

+---------------------------+------------------------------------------------------------------------------------------+
|   Field                   | Description                                                                              |
+===========================+==========================================================================================+
|   Redeem date and time    | | Date when reward was redeemed                                                          |
+---------------------------+------------------------------------------------------------------------------------------+
|   Usage date and time     | | Date when reward was used                                                              |
+---------------------------+------------------------------------------------------------------------------------------+
|   Cost in points          | | Number of points that customer spent for this reward                                   |
|                           | | (define during reward creation in *Cost in points* field)                              |
+---------------------------+------------------------------------------------------------------------------------------+
|   Tax value               | | monetary value of tax for reward                                                       |
+---------------------------+------------------------------------------------------------------------------------------+
|   Customer e-mail         | | Email address of customer who redeemed reward.                                         |
|                           | | E-mail address is used as an identification factor to verify                           |
|                           | | which customer choose particular reward.                                               |
+---------------------------+------------------------------------------------------------------------------------------+
|   Phone                   | | The customer’s phone number.                                                           |
|                           | | Can be used also as an identification factor.                                          |
+---------------------------+------------------------------------------------------------------------------------------+
|   Reward                  | | Name of the reward with coupon code number in round brackets                           |
+---------------------------+------------------------------------------------------------------------------------------+
|   Type                    | | Reward type.                                                                           |
|                           | | **Options include**:                                                                   |
|                           |                                                                                          |
|                           |   - Percentage discount code                                                             |
|                           |   - Cashback                                                                             |
|                           |   - Discount code                                                                        |
|                           |   - Free delivery                                                                        |
|                           |   - Gift                                                                                 |
|                           |   - Invitation for the event                                                             |
|                           |   - Value code                                                                           |
|                           |   - Custom campaign                                                                      |
|                           |                                                                                          |
|                           | | To learn more about the rule types, please see                                         |
|                           |   :doc:`Reward campaigns Types </userguide/reward_campaigns/creation/reward_type>`       |
+---------------------------+------------------------------------------------------------------------------------------+
|   Customer’s first name   | | First name of customer who redeemed reward                                             |
+---------------------------+------------------------------------------------------------------------------------------+
|   Customer’s surname      | | Last name of customer who redeemed reward                                              |
+---------------------------+------------------------------------------------------------------------------------------+
|   Customer active points  | | Amount of customer active points after he redeemed reward.                             |
|   amount                  | | From customer Active points pool, redeemed reward Cost in points value is deducted     |
+---------------------------+------------------------------------------------------------------------------------------+
|   Delivery status         | | Redeemed reward shipping process statuses                                              |
|                           | | For every *Used* reward type except *Gift* only status is **Ordered**                  |
|                           | | For **Gift** reward following statuses are possible:                                   |
|                           |                                                                                          |
|                           |   - Ordered                                                                              |
|                           |   - Shipped                                                                              |
|                           |   - Delivered                                                                            |
|                           |   - Canceled                                                                             |
|                           |                                                                                          |
|                           | | To learn more about the statuses, please see                                           |
|                           |   :doc:`Gift fulfillment </userguide/reward_campaigns/creation/fulfillment_tracking>`    |
|                           |   tracking process section                                                               |
+---------------------------+------------------------------------------------------------------------------------------+
|   Cashback status         | | Redeemed cashback rewards statuses                                                     |
|                           | | Rewards of types other than *Cashback* have a dash in this field.                      |
|                           | | For **Cashback** reward with PayTM provider, the following statuses are possible:      |
|                           |                                                                                          |
|                           |   - 0: INIT: INIT                                                                        |
|                           |   - 1: SUCCESS: SUCCESS                                                                  |
|                           |   - 2: (failure code): (failure message)                                                 |
|                           |   - 3: (code): (reason for pending)                                                      |
+---------------------------+------------------------------------------------------------------------------------------+
|   Unused / Used           | | Redeemed reward statuses.                                                              |
|                           | | **Options include**:                                                                   |
|                           |                                                                                          |
|                           |   - Delivered: *empty checkbox*                                                          |
|                           |   - Used: *marked checkbox*                                                              |
|                           |                                                                                          |
|                           | | To learn how to select reward as a used, see                                           |
|                           |   :doc:`Redeemed rewards </userguide/customers/profile_details/loyalty/redeemed_rewards>`|
|                           |   in profile detail section                                                              |
+---------------------------+------------------------------------------------------------------------------------------+
|   Actions                 | | The operations that can be applied to selected redeemed reward record.                 |
|                           | | **Options include**:                                                                   |
|                           |                                                                                          |
|                           |    - view customer address details used to reward delivery                               |
+---------------------------+------------------------------------------------------------------------------------------+

Content
^^^^^^^
- :doc:`Download redeemed rewards report </userguide/reward_campaigns/menu/reward_report>`
