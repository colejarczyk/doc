2.x
===

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/en/1.0.0/>`
and this project adheres to `Semantic Versioning <http://semver.org/spec/v2.0.0.html>`.

[2.10.0] 24-09-2018
-------------------

Added
^^^^^
 - your points will expire soon (web hook)
 - you level will expire soon (web hook)
 - new level calculation mode
 - information about bought products in transfer points to avoid uneccesary calls
 - new logos in Settings -> Configuration
 - polish translation for backend validation
 - generating a manifest file from Settings -> Configuration
 - new web hook when a customer has been deactivated
 - added level name to the onCustomerLevelChangedAutomatically (web hook)
 - filter to /api/points/transfer to filter only active and expired points
 - filter to /api/points/transfer to filter points by expiration date
 - points transfer between customers (new feature)
 - brand icon for Reward Campaigns
 - categories for Reward Campaigns (new feature)
 - a new flag, feature for Reward Campaigns
 - coupon expiration (new feature)
 - your points will expire soon (web hook)
 - Earning Rule based on customer localization (new feature)
 - information how many points you need to earn to stay in the same level
 - added flag "public" to the Reward Campaign
 - buying many coupons at once (new feature)
 - an administrator can buy a campaign as a customer with or without using customer points (new feature)
 - resetting level after a certain time (new feature)
 - cancel coupon when a transaction has been fully returned (new feature)
 - using many coupons at once (new feature)
 - custom static segments (new feature)

Changed
^^^^^^^
 - import transfer points using customer email/phone number/loyalty card number
 - PUT /api/customer/{customer} is now a partial update, not full update
 - increased max_result_window for Elasticsearch to return more documents
 - removed column with template name from CSettings -> Emails table
 - removed redundant web hook onCustomerLevelChanged
 - logic how a customer will be downgraded or upgraded to next level
 - searching customers in POS by name or last name as a wildcard

Fixed
^^^^^
 - added missing translations
 - phone number validation (less restrict)
 - creating a new earning rule after changing it's type
 - matching transaction with customer using upper letters
 - table pagination
 - creating a reward campaign other than Cash Back
 - assign a new percent discount code to the customer

[2.9.0] 20-08-2018
------------------

Added
^^^^^
 - configurable e-mail content for referring a friend
 - markdown for campaign details
 - new earning rule "Instant Reward" to collect rewards instantly after a transaction
 - include/exclude labels for earning rule "General Spending Rule"
 - locking points for X number of days
 - assign earning rules to the POS
 - set earning rule as last

Changed
^^^^^^^
 - label value for the customer is not required anymore

Fixed
^^^^^
 - download level list as CSV file
 - translations
 - search client by first or last name in POS
 - upload button in firefox
 - upgrading read model
 - dashboard
 - points transfer list in client cockpit
 - creating Earning Rule without labels

[2.8.0] 20-07-2018
------------------

Added
^^^^^
 - configuring marketing automation tool in the administration panel
 - new command "phing migrate" to automate migration between versions
 - new development documentation
 - master key API token
 - filtering campaign through additional fields
 - seller can add or spend points for a customer
 - assign earning rule to the POS
 - resizing logos
 - added level ID to the endpoint /api/customer/level

Changed
^^^^^^^
 - changed Earning Points Rules to Earning Rules

Fixed
^^^^^
 - validation tags on Earning Rule "Multiply by labels"
 - fixed link to the terms and conditions file
 - fixed bug with Earning Rule "Custom event rule"
 - generating demo data

[2.7.0] 03-07-2018
------------------

Added
^^^^^
 - possibility to set an accent color for client cockpit
 - /api/customer/level to get list of possible levels for customers
 - added new earning points rule "Multiply by product label"
 - new configuration option to upload terms and condition file
 - labels to the transaction
 - labels to the reward campaigns

Changed
^^^^^^^
 - docker images
 - docker-compose settings, check updated README.md

Fixed
^^^^^
 - sorting for /api/customer/campaign/available
 - registering a refund transaction and subtracting points
 - saving settings with a various set of values
 - changing reward campaign photo
 - forgot password on client cockpit

[2.6.0] 05-06-2018
------------------

Added
^^^^^
 - upload customer from XML file
 - add Earning Points Rule name to the Transfer Points comment (https://github.com/DivanteLtd/open-loyalty/issues/79)

Changed
^^^^^^^
 - segment or level is now required in Earning Points Rules
 - only png/jpg/jpeg files are now supported for logo
 - updated Symfony to latest version 3.4.11 with security fixes

Fixed
^^^^^
 - generating demo data
 - updating administrator account
 - choosing different language in Settings -> Configuration (https://github.com/DivanteLtd/open-loyalty/issues/83)

[2.5.0] 25-05-2018
------------------

Added
^^^^^
 - added property hasPhoto to indicate a model has photo in campaigns, earning points rules and levels
 - added photo to Levels
 - added photo to Earning Points Rules
 - added uploading transactions from XML file
 - added new Reward Campaign "CashBack"
 - added a new property "Prize value" to the Reward Campaigns
 - added a new property "Tax" to the Reward Campaigns
 - added a new settings "Small logo"
 - added uploading points transfers from XML file
 - added a new sorting filter "manuallyAssignedLevel" to the customer list
 - added a method to unassign a customer from assigned manually level /api/customer/{customer}/remove-manually-level

Changed
^^^^^^^
 - upgraded minimum version of PHP from 7.0 to 7.1
 - changed campaignId object to string in response from /api/customer/campaign/bought
 - property "pointsEarned" is now always available in the /api/transaction response

[2.4.0] 23-04-2018
------------------

Added
^^^^^
 - added missing translations
 - added translatable program name in the title bar in browser
 - added list of redeemed rewards
 - added matching transaction with a customer using phone number
 - added new SMS gateway WorldText
 - added possibility to log in using phone number
 - added settings to change activation method (e-mail or sms)
 - added endpoint to match transactions by a customer

Fixed
^^^^^
 - fixed minor bugs with customer activation using SMS
 - fixed searching customers (/api/customer)

[2.3.1] 12-04-2018
------------------

Added
^^^^^
- added [API documentation](http://open-loyalty.readthedocs.io/en/latest/)

[2.3.0] 05-04-2018
------------------

Added
^^^^^
 - added API aliases to fix X-AUTH-TOKEN invalid credentials
 - added comment to the points transfer list
 - added missing translations
 - added a new feature to activate a customer using SMS

Fixed
^^^^^
 - fixed SQL Injection vulnerabilities

[2.2.0] 28-02-2018
------------------

Added
^^^^^
 - encryption parameter for Swiftmailer
 - logo validation
 - added APCu cache layer for mappings and query building in Doctrine ORM
 - better concurrency support for writings
 - increased performance
 - added makefile for common used commands

Changed
^^^^^^^
 - upgraded jquery to 3.x version to fix potential vulnerabilities
 - upgraded Symfony framework to version 3.4 LTS
 - upgraded Broadway library to version 2.0.1 (it's a BC break)
 - changed README.md

Fixed
^^^^^
 - changing merchant data in AC
 - searching a client in POSC
 - rounding points in emails

[2.1.0] 28-01-2018
------------------

Added
^^^^^
 - Added new customer account statuses (it's a BC break!)
 - Collect / spend points only when a customer has a defined status
 - Support GDPR
 - A new setting where you can change loyalty program logo
 - More information link field for a reward campaign
 - Display reward campaign's image in client cockpit

Fixed
^^^^^
 - Missing transactions in the POS cockpit
 - Remove transfer points in Admin Cockpit
 - Vagrant setup for Windows users
 - Fixes missing placeholders

[2.0.0] 2017-11-16
-------------------

Added
^^^^^
 - Kubernetes support

Changed
^^^^^^^
 - Docker files
 - Frontend migration from Gulp to the Webpack
 - Migration from Nodejs server to the Nginx

[1.4.0] 2017-11-07
------------------

Added
^^^^^
 - CLI command to restore read model using event store

Fixed
^^^^^
 - AC/POSC fixed transaction id
 - AC/POSC show points for each transaction
 - AC clear fields after changing event type
 - POSC fixed missing days from last order
 - CC fixed cancel button

[1.3.1] 2017-10-23
------------------

Added
^^^^^
 - Added change log file

Changed
^^^^^^^
 - API Documentation
 - Changed guide link in the admin cockpit

Fixed
^^^^^
 - Reload application after language change
 - Fixed renaming translation name

[1.3.0] 2017-10-09
------------------
Changed
^^^^^^^
 - Added new endpoints to the API documentation

Fixed
^^^^^
 - Fixed PHPUnit configuration
 - Changed label for Postgres from latest to version 9

[1.2.1] 2017-09-28
------------------

Added
^^^^^
 - Added API documentation

Fixed
^^^^^
 - Fixed wrong marketing agreement label
 - Fixed table width on the transaction details
 - View level & segment names instead of ID in the reward campaign view
 - Show newly added language in the settings

[1.2.0] 2017-09-08
------------------

Changed
^^^^^^^
 - Moved code to the vendor

Fixed
^^^^^
 - Fixed customer activation link
 - Fixed variables in the e-mail templates
 - Fixed link to the page "See rewards you have already redeemed"

[1.1.0] 2017-07-21
------------------

Changed
^^^^^^^
 - Allow decimal numbers for point value field in the general spending rule
 - Change default language from PL to EN

Fixed
^^^^^
 - Fixed loader look
