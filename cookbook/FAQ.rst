Open Loyalty FAQ 
====================

These are some of the most common questions and answers about Open Loyalty. If you couldn't find your question in the list below, please contact us `here <https://www.openloyalty.io/>`_.


1. I register with customer, but I lose my account activation code. How can I resend the code?
-----------------------------------------------------------------------------------------------------

**1. Account activation via SMS** 

After registration form fullfillment by customer from client cockpit, on the phone number provided in ther form activation code will be sent. If for some reason customer will lost this code he can simply resend a code. To do this, he need to go to the login page and click "Activate an account or resend a code", then click "Resend code" button and provide phone number. After that he will get another acitavtion code. 

Note, if you register customer from Admin or POS Cockpit activation code is not sent. Customer account is active instantly. 


**2. Account activation via email**

After registration form fullfillment by customer from client cockpit, on the email address provided in the form activation link will be sent. If for some reason customer will lost this link/email, his account can be activated manually by Admin on your side. Customer can send a message on help email or call to customer care department. 
 
Note, if you register customer from Admin or POS Cockpit activation link is not sent. Customer account is active instantly. 


2. We need to verify end-to-end earning mechanism is working properly. How can we emulate transaction without have a real POS in our testing environment?
-------------------------------------------------------------------------------------------------------------------------------------------------------------

**XML File Upload** 

The first option is to import transaction from XML file. In OL user guide please find chapter  "Import transaction" (p.107). Here you will find description of transaction import process and example of XML file structure.


3. In "Points Transfer" section, admin wants to batch import the "points transfer" list. What is the required format of the XML file? Is it the only supported file format, how about .csv file format?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CSV file format is not supported. 

In OL user guide please find chapter "Creating points transfer" (p.92). Here you will find description of points transfer import process and example of XML file structure.



4. In "Customers" section, admin wants to batch import the "customer" list. What is the required format of the XML file? Is it the only supported file format, how about .csv file format?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CSV file format is not supported. 

In OL user guide please find chapter "Creating customer account" (p.46). Here you will find description of customer import process and example of XML file structure.


5. Is there a way to 'preview' campaign before publishing to live view?
---------------------------------------------------------------------------
There is no possibility to “preview” campaign before publishing. 

From Admin cockpit you can create a new reward campaign, but with inactive status. In that case campaign will be not displaying on a storefront until it’s status will be change to active. Till this time you can edit all information related to this campaign e.g. description, photo, conditions etc. 

In OL user guide please find chapter “Creating reward campaign” (p. 177). Here you will find description of reward creation process. 



6. If the customer used available points to redeem a coupon, what would happen to the customer level?
--------------------------------------------------------------------------------------------------------

**Active Points**

As a customer, upon purchasing goods in a store (or other activity e.g. scanning a QR code), points will be earned. (Increase in active points)

The customer could use the earned points to redeem coupon or other rewards before the active points expired.

However, this use of points action (Decrease in active points) will not affect the customer "Level".

If the customer used up all the active points (Active points = 0) for coupon, the customer level will not down grade. (will remain in current level)

Active points will return to 0 upon:
- the customer used up all the points;
- all the points expired.


**Accumulated Points**

Level is the accumulation of earned points. It represents how the customer has achieved. 

Each level entitled the customer with specific rewards or benefits. (e.g. 20% off on every purchases.)

Upon the accumulation of earned points reached a certain amount, the customer level will be upgraded.


7. What is Open Loyalty approach for admin access right? Any preset admin account type?
-----------------------------------------------------------------------------------------
Single level access in current offering.



8. Admin wants to create birthday offer campaign which target for user who born on each months. How could the admin define those birthday segment for each 12 month?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
In current offering it's not possible to define a date range. 

OL standard gives an option to create a segment with customers whose have a birthday e.g. in 30 days from today. Segment will be recalculated dynamically - it means that customers will be associated and dissociated from a segment as they have a birthday in specified period. 



9. When customer visit an offline store, coupon may be used during transaction. Is there a way to view records of used coupon per POS?
-------------------------------------------------------------------------------------------------------------------------------------------
In current offering there is no option to see records of used coupon per POS. 

From All  reward campaigns view you can see how many times this reward was used by customers in general (sum from all POSes and website ) . For example, if you have "percentage discount code" you will be able to see in "Used by customers" column how many times this reward has been redeemed (delivered and used) 



10. Which one would be the expected bahviour of InstantRewards?
-------------------------------------------------------------------
1) the customer could get the reward coupon instantly.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**or** 

2) the customer is able to see the reward campaign and redeem the coupon manually.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The expected behaviour of Instant Reward is the 1st approach. When event is complete, for example GPS check in, customer will get reward instantly. Reward will appear in "Redeemed reward" section on client cockpit and Admin cockpit. 

From the Admin you will be able to see status of this reward: 

- delivered - customer get reward, reward is displaying in Redeemed reward section

- used - customer used reward 


11. I want to know how Earning points rule mechanism work, from developer perspective. Where can I find developer documentation?
------------------------------------------------------------------------------------------------------------------------------------
Open Loyalty  Developer Documentation is published for everyone `here <http://open-loyalty.readthedocs.io/en/latest/>`_. 

Documentation is updated after every new feature release. 



