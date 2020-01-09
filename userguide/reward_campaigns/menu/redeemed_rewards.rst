.. index::
   single: redeemed_rewards

Redeemed rewards
================

Redeemed reward is an instance of reward that Customer has bought with Points or earned for performing specified action.

There is possibility to get:

 - virtual reward - as a Discount or Value Code, free delivery 
 - physical reward - which will be send to Customer, e.g. printed coupon, gift, etc.
 - cashback

**Not enough points**

If Customer does not have enough points to redeem reward then Redeem reward button will be disabled (greyed out).

When mouse hover over disabled button then tooltip will show "You must have <<reward cost - customer active points>> more points to get reward"


**Redeemed reward from Admin perspective**

Redeemed reward management could be performed only from Administrator Cockpit by user who has Admin privileges.

Redeemed rewards list grid provide an information about which customer and when redeemed given reward. 

Moreover, you can check whether reward is **Delivered** (customer choose reward and spent points but he has not used it yet) or **Used** (customer used coupon code during purchase, gift was sent to customer etc.)

.. image:: /userguide/_images/redeemed.png
   :alt:   Redeemed Rewards

Use the standard controls to sort the list by **Date and time** and filter list to get a register of reward that are **Delivered** or **Used**. By default Redeemed rewards grid show both – delivered and used reward.

Pagination controls appear if there are more redeemed rewards records than fit on the page, and are used to move from one page to the next.


To see all Redeemed rewards:
----------------------------
On the Admin sidebar, tap ``Reward campaigns``, then choose **Redeemed rewards** 


Field description
*****************

+----------------------------+----------------------------------------------------------------------------------------+
|   Field                    |  Description                                                                           |
+============================+========================================================================================+
|   Date and time            | | Date when reward was redeemed                                                        |
+----------------------------+----------------------------------------------------------------------------------------+
|   Cost in points           | | Number of points that customer spent for this reward                                 |
|                            | | (define during reward creation)                                                      |
+----------------------------+----------------------------------------------------------------------------------------+
|   Tax value                | | Value of tax for reward                                                              |
+----------------------------+----------------------------------------------------------------------------------------+
|   Customer e-mail          | | Email address of customer who redeemed reward.                                       |
|                            | | E-mail address is used as an identification factor to verify                         |
|                            | | which customer choose particular reward.                                             |   
+----------------------------+----------------------------------------------------------------------------------------+
|   Phone                    | | The customer’s phone number.                                                         |
|                            | | Can be used also as an identification factor.                                        |
+----------------------------+----------------------------------------------------------------------------------------+
|   Reward                   | | Name of the reward with coupon code number in round brackets                         |
+----------------------------+----------------------------------------------------------------------------------------+
|   Type                     | | Reward type.                                                                         |
|                            | | **Options include**:                                                                 |
|                            |                                                                                        |
|                            |   - Percentage discount code                                                           |
|                            |   - Cashback                                                                           |
|                            |   - Discount code                                                                      |
|                            |   - Free delivery                                                                      |
|                            |   - Gift                                                                               |
|                            |   - Invitation for the event                                                           |
|                            |   - Value code                                                                         |
|                            |   - Custom campaign                                                                    |
|                            |                                                                                        |
|                            | | To learn more about the rule types, please see                                       |
|                            |   :doc:`Reward campaigns Types </userguide/reward_campaigns/creation/reward_type>`     |
+----------------------------+----------------------------------------------------------------------------------------+
|   Customer’s first name    | | First name of customer who redeemed reward                                           |
+----------------------------+----------------------------------------------------------------------------------------+
|   Customer’s surname       | | Last name of customer who redeemed reward                                            |
+----------------------------+----------------------------------------------------------------------------------------+
|   Customer active points   | | Amount of customer active points after he redeemed reward.                           |
|   amount                   | | From customer Active points pool, redeemed reward Cost in points value is deducted   |
+----------------------------+----------------------------------------------------------------------------------------+
|   Delivered / Used         | | Redeemed reward statuses.                                                            |
|                            | | **Options include**:                                                                 |
|                            |                                                                                        |
|                            |   - Delivered                                                                          |
|                            |   - Used                                                                               |
|                            |                                                                                        |
|                            | | To learn how to select reward as a used, see                                           |
|                            | :doc:`Redeemed rewards </userguide/customers/profile_details/loyalty/redeemed_rewards>`|
|                            | in profile detail section                                                              |
+----------------------------+----------------------------------------------------------------------------------------+

Content
^^^^^^^
- :doc:`Download redeemed rewards report </userguide/reward_campaigns/menu/reward_report>`









