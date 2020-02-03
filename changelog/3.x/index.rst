3.x
===

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog` and this project adheres to `Semantic Versioning`.

[3.3.0] 22-03-2019
------------------

Added
^^^^^
 - (#2377) Send SMS when a transaction is matched
 - (#2384) [API][ADMIN] Added avatar for customers
 - (#1252) [DEV] Asynchronous email sending using RabbitMQ and worker
 - (#1253) [DEV] Asynchronous segments recalculation using RabbitMQ and worker
 - (#1254) [DEV] Asynchronous levels recalculation using RabbitMQ and worker
 - (#1684) [ADMIN] Added all Reward Campaign details to the view page
 - (#2101) [DEV] Added RabbitMQ for asynchronous jobs
 - (#2119) [DEV] Asynchronous points expiration using RabbitMQ and worker
 - (#2120) [DEV] Asynchronous points activation using RabbitMQ and worker
 - (#2121) [DEV] Asynchronous notification about expiring points using RabbitMQ and worker
 - (#2122) [DEV] Asynchronous coupons activation using RabbitMQ and worker
 - (#2123) [DEV] Asynchronous coupons expiration using RabbitMQ and worker
 - (#2124) [DEV] Asynchronous notification about expiring coupons using RabbitMQ and worker
 - (#2125) [DEV] Asynchronous notification about expiring levels using RabbitMQ and worker
 - (#2158) [API] GET /api/campaign sorting by createdAt
 - (#2158) [API] GET /api/customer/campaign/available by createdAt

Changed
^^^^^^^
 - (#1886) [API][CC] Show Custom Campaigns in CC
 - (#2134) [BC][API] GET /api/campaign/public/available changed SegmentNames type to object
 - (#2180) [DEV] Optimized consumers architecture
 - (#2386) [BC][API] GET /customer/{customerId}/status changed "pointsExpiringBreakdown" type to object
 - (#2386) [BC][API] GET /admin/customer/{customerId}/status changed "pointsExpiringBreakdown" type to object
 - (#2386) [BC][API] GET /seller/customer/{customerId}/status changed "pointsExpiringBreakdown" type to object
 - (#2031) [API][ADMIN] Disabled changing Reward Campaign's type after it's created
 - (#2036) [BC] Migrated Elastcisearch from 2.2 to 6.7
 - (#2109) [ADMIN] Moved "Days inactive" and "Days valid" from "Campaigns details" section to the "Coupons"
 - (#2116) [DEV] Upgraded to the latest Symfony version
 - (#2427) [ADMIN] Removed counter in the level list
 - (#2428) [ADMIN] Removed "no results" notification when permission denied as set in the ACL

Fixed
^^^^^
 - (#2013) A customer can register a return transaction to the other customer transaction
 - (#2153) [API] GET /api/customer/{customerId}/status wrong points expiration breakdown
 - (#2147) [API] GET /api/customer/campaign/available doesn't return all available campaigns
 - (#2157) [API][ADMIN] An admin with View permissions for Reward Campaigns is able to change Delivery status of redeemed rewards
 - (#2334) Point for referrer is released when the referred account is created, not when it's activated
 - (#2401) [API] POST /api/customer/campaign/coupons/mark_as_used misses "couponId" in the response
 - (#2444) [DEV] Missing configuration for sending SMS notification other than account activation or password reminder
 - (#2038) [API] POST /api/admin/campaign/cashback/redeem 500 Internal Server Error while calling
 - (#2038) [API] POST /api/admin/campaign/cashback/simulate 500 Internal Server Error while calling
 - (#2111) Customer's level name doesn't change after renaming
 - (#2112) [ADMIN] Logo doesn't scale in the left upper corner
 - (#2141) [API] POST /api/transaction/simulate 500 Internal Server Error while calling
 - (#2149) Fixed wrong round up transaction summary
 - (#2175) [API] GET /api/customer/{customerId} wrong calculation of pointsExpiringNextMonth
 - (#2178) [ADMIN] markdown for chinese language doesn't show
 - (#2183) [API] POST /api/customer/campaign/{campaign}/buy missing quantity in API DOC
 - (#2183) [API] POST /api/seller/customer/{customer}/campaign/{campaign}/buy missing quantity in API DOC
 - (#2198) [DEV] Segment with condition "Bought specific SKU" doesn't work when SKU contains special characters
 - (#2375) [DEV] Performance issue with a lot customers assigned to the segments
 - (#2390) [CC] Summary of available points shows wrong value
 - (#2412) [DEV] Losing connection between worker and RabbitMQ
 - (#2414) [DEV] Invalid snapshotting in Event Sourcing
 - (#2415) [DEV] 409 Conflict exception during many concurrent writes to the Elasticsearch
 - (#2422) [ADMIN] No info while logging without data to the admin panel
 - (#2434) [API] GET /api/admin/customer/{customer}/campaign/available wrong sorting
 - (#2434) [API] POST /api/transaction triggers a webhook with wrongly rounded transaction's total
 - (#1637) [ADMIN] Missing validation for labels in Earning Rules
 - (#2080) [API] GET GET /api/admin/customer/{customerId}/campaign/available?perPage=100&sort=campaignVisibility.visibleFrom&direction=desc wrong sorting

Note! In this version introduced a few features that breaks backward-compatibility.
Note2! Check UPGRADE-3.3.md to see how to upgrade.

[3.2.0] 14-01-2019
------------------

Changed
^^^^^^^
- Setting "Downgrade every X number of days" is now mandatory

Fixed
^^^^^
- The last row in the menu was half cut when the expanded menu is longer than the height of browser
- Fixed editing merchants

[3.1.1] 14-01-2019
------------------

Added
^^^^^
- Added User Guide to the documentation

[3.1.0] 14-01-2019
------------------

Note! In this version introduced a few features that breaks backward-compatibility.
Note2! Check UPGRADE-3.1.md to see how to upgrade.

Added
^^^^^
 - Added Snapshots for Event Sourcing to increase performance
 - Added new options for expiring points in Settings -> Configuration (all time active / after x number of days / at the end of the month / at the end of the year) (new feature)
 - Added User Guide at https://open-loyalty.readthedocs.io
 - Added new ACL for administration panel (new feature) (BC break)
 - Added return "Voucher" for a customer during registration a return transaction (new feature)
 - Added information about active and used points to the export in levels
 - GET /api/admin/customer/{customerId}/status added information about points going to expire in next month
 - GET /api/seller/customer/{customerId}/status added information about points going to expire in next month
 - GET /api/customer/{customerId}/status added information about points going to expire in next month
 - Added option "Fulfillment Tracking Process" to the Reward Campaign so an administration is able to change reward status (ordered / delivered / canceled / shipped) (new feature)
 - Added usage datetime of coupon in the GET /api/campaign/bought
 - Added an option at Settings -> Configuration to disable edit customer profile by himself except password change (new feature)
 - Added new filters "isFeatured", "hasSegment", "categoryId[]", "format" to GET /api/campaign/public/available
 - Added an integration with Pushy to send push notifications (new feature)
 - Added missing configuration to notify a customer a X number of days before level expires using Webhooks
 - GET /api/admin/customer/{customerId}/status added information about points expiration per day
 - GET /api/seller/customer/{customerId}/status added information about points expiration per day
 - GET /api/customer/{customerId}/status added information about points points expiration per day
 - Added limitation by POS, segments and levels in the Earning Rule with type "Geolocation"
 - Added sending information about rewards that became available for a customer using push notifications (new feature)
 - Added new types of "Usage limit active" for "Custom event rule" in Earning rule
 - Added an configuration (simple/advanced) in the app/config/parameters.yml to change password requirements
 - Added an configuration in the app/config/parameters.yml to change the length of activation code sent using SMS activation method
 - Added upload avatar for a customer profile (new feature)
 - Added support for IE 11 for an administration panel
 - Added POST /api/customer/earnRule/{eventName} to call "Custom event" Earning Rule with customer JWT Token
 - Added migration mechanism using Doctrine Migrations (new feature)

Changed
^^^^^^^
 - Prevent from registering a return transaction for non-existing transaction by documentNumber field
 - Prevent marking coupon as Unused by a customer
 - Changed Nginx version to 1.14.1
 - PUT /api/customer/{customer} works now as a partial update instead of full update (BC break)
 - Earning Rule with type "Geolocation" accepts now coordinates with five digits after decimal point
 - Increased php-fpm start processes to 5, min processes to 3 and max processes to 20
 - Increased php-fpm memory limit to 512MB
 - PHP-FPM is now configurable using docker/prod/php/conf/php-fpm-pool.conf
 - Changed translation in Settings - Notify user from "Days to level recalculation" to "Days before level recalculation to notify user"
 - Updated the documentation how to add a new segment
 - Disabled remove already redeemed coupons by a customer from Reward Campaign
 - Renamed GET /api/campaign/public/featured to GET /api/campaign/public/available
 - Removed filter "isPublic" from GET /api/campaign/public/available
 - Changed how projections to the Elasticsearch works by making them independent of each other
 - Changed ol__setings table by adding a unique constraint for setting_key column
 - Changed invitation process when SMS activation method is enabled POST /api/invitations/invite (BC break)
 - Changed crons by adding flock
 - Changed default sorting to "order" for categories of Reward Campaign in the administration panel
 - Removed "program_name" parameter from app/config/parameters.yml

Fixed
^^^^^
 - Fixed calling API endpoints starting with /api/customer by an administrator using X-AUTH-TOKEN
 - Fixed marking coupon as Used / Unused by an administrator
 - Fixed calculating level based on "Active points"
 - Fixed calculating level based on "Total points earned since last level recalculation"
 - Fixed automatically assign a birth date to the customer during update
 - Fixed PUT /api/customer/{customer} so it won't remove labels accidentally
 - Fixed translate level name on GET /api/customer/status?_locale={locale} according to the locale passed in the query parameter
 - Fixed 500 error while registering a new transaction when at least one Earning Rule has set option "All time active"
 - Fixed that an administrator see only "Example_coupon" on the Reward Campaign's edit page
 - Fixed adding points manually so it now has an impact on customer level
 - Fixed 500 error when now level with condition value equal zero is defined
 - Fixed activating and expiring coupons
 - Fixed 500 error during creating Reward Campaign with type "Instant Reward"
 - Fixed removing a language from the configuration
 - Fixed logo size on the administration panel sites
 - Fixed adding a new customer by an administrator in specific system configuration
 - Fixed using Earning Rule with type "QR code"
 - Fixed changing type of Earning Rule during creating a new one
 - Fixed forgot password when customers phone number was changed
 - Fixed usageLeftForCustomer value in GET /api/customer/campaign/available for single coupon
 - Fixed filtering by date in redeemed rewards table
 - Fixed remove field value while edit Reward Campaign in the administration panel
 - Fixed sorting GET /api/admin/customer/{customer}/campaign/available using sort=campaignVisibility.visibleFrom
 - Fixed GET /admin/analytics/points to show a correct number of spent points in loyalty program
 - Fixed 500 error while buy reward campaign in POST /api/admin/customer/{customer}/campaign/{campaign}/buy
 - Fixed crons for expire or activate coupons
 - Fixed 500 error when a transaction missed a required documentNumber field POST /api/transaction
 - Fixed supervisord in the production docker image
 - Fixed edit customer profile automatically set a manual level and disabled level change
 - Fixed selectbox shows only 10 segments while create Reward Campaign or Earning Rule
 - Fixed missing markdown for shortDescription in the Reward Campaign
 - Fixed unable to extend section with default language
 - Fixed showing a customer in the more than one level list at the same time GET /api/level/{levelId}/customers
 - Fixed import transaction using the same documentNumber more then once
 - Fixed mark coupon as used by an administrator POST /api/admin/campaign/coupons/mark_as_used (BC break)
 - Fixed 500 error while import transactions without or with invalid posId
 - Fixed Earning Rule with type "Account created" that was never called
 - Fixed "Timezone" setting at Settings -> Configuration
 - Fixed value of "usageLeftForCustomer" in GET /api/customer/campaign/available when single coupon used

[3.0.0] 15-10-2018
------------------

Added
^^^^^
 - multi photos for reward campaigns (new feature)
 - segments, levels and POS limits now available in the Geolocation Earning Rule (new feature)
 - Custom Reward Campaign that allows to link with Custom Earning Rule or QRCode Earning rule and reward customer with points (new feature)
 - QRCode Earning Rule (new feature)
 - new currency HDK to the settings
 - multi language for Levels, Reward Campaigns, Reward Campaigns Category (new feature)
 - new API endpoint /api/settings/css allowing to get custom CSS rules for Client Cockpit

Changed
^^^^^^^
 - importing transaction with POS information is now simplified, you can define posIdentifier or posId
 - size of textareas has been decreased

Fixed
^^^^^
 - data in Elastic Search was not always up to date
 - unable to add a points transfer when customer databases was large
 - a phone number was not copied from customer to transaction while matching transaction with customer
 - customer could register twice with the same phone number when activation method is SMS
 - a negative radius value in Geolocation Earning Rule caused 500 error
 - while creating Reward Campaign there was only first 10 reward categories to choose, now unlimited
 - buying a campaign when a customer has no phone number caused 500 error
 - fixed typos
 - missing translations

.. _`Keep a Changelog`: http://keepachangelog.com/en/1.0.0/
.. _`Semantic Versioning`: http://semver.org/spec/v2.0.0.html
