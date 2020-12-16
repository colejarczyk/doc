Events
======

There are three types of events dispatched in Open Loyalty, commands, events and system events.

Commands
--------
It’s a user intention, it’s something that we want to happen but may be rejected on any reason, ie. because data
is not valid. To put it simply, it says “do something” to the software.

Events
------
Events have happened. It represents something that has happened and it cannot be rejected. It’s a consequence of
executing a command.

System events
-------------
Additional type of events that are thrown during execuing a command by command handler and may be used to trigger
another commands. They’re also useful to separate concerns.

List of all events
------------------

+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|  Module          |  Commands                          | Events                                | System events                                  |
+==================+====================================+=======================================+================================================+
|                  |  - AddPoints                       | - PointsWereAdded                     | - AccountCreatedSystemEvent                    |
|                  |  - CancelPointsTransfer            | - PointsTransferHasBeenCanceled       | - AvailablePointsAmountChangedSystemEvent      |
|  Account         |  - CreateAccount                   | - AccountWasCreated                   | - CustomEventOccurredSystemEvent               |
|                  |  - ExpirePointsTransfer            | - PointsTransferHasBeenExpired        |                                                |
|                  |  - SpendPoints                     | - PointsWereSpent                     |                                                |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|  ActivationCode  |  - CreateActivationCode            | - AccountWasCreated                   | - ActivationCodeCreatedSystemEvent             |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|  Audit           |  - CreateAuditLog                  | - AuditLogWasCreated                  | - CreatedAuditLogSystemEvent                   |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|                  |  - ChangeCampaignState             |                                       |                                                |
|                  |  - CreateCampaign                  |                                       |                                                |
|  Campaign        |  - RemoveCampaignPhoto             |                                       |                                                |
|                  |  - SetCampaignPhoto                |                                       |                                                |
|                  |  - UpdateCampaign                  |                                       |                                                |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|                  |  - ActivateCustomer                | - CustomerWasActivated                | - CustomerActivatedSystemEvent                 |
|                  |  - AssignPosToCustomer             | - PosWasAssignedToCustomer            | - CustomerAgreementsUpdatedSystemEvent         |
|  Customer        |  - BuyCampaign                     | - CouponWasBought                     | - CustomerLevelChangedSystemEvent              |
|                  |  - RedeemCoupon                    | - CouponWasRedeemed                   | - CustomerRemovedManuallyLevelSystemEvent      |
|                  |  - ReissueCoupon                   | - CouponWasReissued                   | - CustomerLoggedInSystemEvent                  |
|                  |  - CreateInvitation                | - InvitationWasCreated                | - CustomerRegisteredSystemEvent                |
|                  |  - DeactivateCustomer              | - CustomerWasDeactivated              | - CustomerUpdatedSystemEvent                   |
|                  |  - UpdateCustomerLoyaltyCardNumber | - PurchaseWasMadeForThisInvitation    | - CustomerDeactivatedSystemEvent               |
|                  |  - MoveCustomerToLevel             | - CustomerWasMovedToLevel             | - NewsletterSubscriptionSystemEvent            |
|                  |  - NewsletterSubscription          | - CustomerWasRegistered               | - CouponWasRedeemedSystemEvent                 |
|                  |  - RegisterCustomer                | - CustomerAddressWasUpdated           | - CouponWasReissuedSystemEvent                 |
|                  |  - RemoveManuallyAssignedLevel     | - CustomerDetailsWereUpdated          |                                                |
|                  |  - UpdateCustomerAddress           | - CustomerLoyaltyCardNumberWasUpdated |                                                |
|                  |  - UpdateCustomerCompanyDetails    |                                       |                                                |
|                  |  - UpdateCustomerDetails           |                                       |                                                |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|                  |  - ActivateEarningRule             |                                       |                                                |
|                  |  - CreateEarningRule               |                                       |                                                |
|  EarningRule     |  - DeactivateEarningRule           |                                       |                                                |
|                  |  - RemoveEarningRulePhoto          |                                       |                                                |
|                  |  - SetEarningRulePhoto             |                                       |                                                |
|                  |  - UpdateEarningRule               |                                       |                                                |
|                  |  - UseCustomEventEarningRule       |                                       |                                                |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|                  |  - ActivateLevel                   |                                       |                                                |
|                  |  - CreateLevel                     |                                       |                                                |
|  Level           |  - DeactivateLevel                 |                                       |                                                |
|                  |  - RemoveLevelPhoto                |                                       |                                                |
|                  |  - SetLevelPhoto                   |                                       |                                                |
|                  |  - UpdateLevel                     |                                       |                                                |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|  Messaging       |  - CreateMessage                   |                                       | - MessageCreatedSystemEvent                    |
|                  |  - UpdateMessage                   |                                       | - MessageUpdatedSystemEvent                    |
|                  |  - ActivateMessage                 |                                       | - MessageActivatedSystemEvent                  |
|                  |  - DeactivateMessage               |                                       | - MessageDeactivatedSystemEvent                |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|  Pos             |  - CreatePos                       |                                       | - PosUpdatedSystemEvent                        |
|                  |  - UpdatePos                       |                                       |                                                |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|                  |  - ActivateSegment                 |                                       |  - CustomerAddedToSegmentSystemEvent           |
|                  |  - CreateSegment                   |                                       |  - CustomerRemovedFromSegmentSystemEvent       |
|  Segment         |  - DeactivateSegment               |                                       |  - SegmentChangedSystemEvent                   |
|                  |  - DeleteSegment                   |                                       |                                                |
|                  |  - UpdateSegment                   |                                       |                                                |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|  Transaction     |  - AssignCustomerToTransaction     | - CustomerWasAssignedToTransaction    | - CustomerAssignedToTransactionSystemEvent     |
|                  |  - RegisterTransaction             | - TransactionWasRegistered            | - CustomerFirstTransactionSystemEvent          |
|                  |                                    |                                       | - TransactionRegisteredEvent                   |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
|  Webhook         |  - DispatchWebhook                 |                                       |                                                |
+------------------+------------------------------------+---------------------------------------+------------------------------------------------+
