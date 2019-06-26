.. index::
   single: settings2 

Settings
========

The Configuration section determines loyalty program and points details, customer earning and spending statuses, account activation, identification factors of a matching transaction with a customer and other settings that are used throughout the Open Loyalty system.

.. image:: /userguide/_images/settings2.PNG
   :alt:   Open Loyalty Settings

   
To configure Open Loyalty:
''''''''''''''''''''''''''

In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Configuration**. 

In the **Settings** section, do the following:

.. |settings| image:: /userguide/_images/icon.png

1. In the **Currency** list, select the currency to be used for the online and offline transaction, to one of the following:

  - EUR
  - HKD
  - PLN
  - USD

2. Select your **Timezone** from the list. Time zone is used for date time calculation 

3. Enter the **Program name** that you want to use in all communications  

4. If applicable, enter the URLs to the following: 

  - **Program URL**  
      URL to a page with Loyalty Program description
  - **Conditions URL**  
     URL to page with Loyalty Program Terms & Conditions description
  - **FAQ URL**  
      URL to page with Loyalty Program FAQ page

5. If applicable, in **Conditions File (PDF)** field you can upload Loyalty Program Terms & Conditions document in .pdf. After uploading and saving settings a link where a file is available appears. 
  
.. image:: /userguide/_images/condition_file.png
   :alt:   Conditions file uploaded

.. note::

    **The document will be attached as a link in the Welcome system e-mails footer. For more information please see system Emails**

6. In **Points singular** and **Points plural**, type a unit label of scoring in singular and plural, that you want to appear. 
  For example Point, Points

7. Set **Help e-mail**, where a customer can write to find help and support for your Loyalty Program

8. In **Expire points method** field define customers gathered *Active points* expiration time boundaries to one of following:

  - **After X days**  
      Points will expire, after a provided in **Points will expire after** field number of days, from the date of adding Points transfer
  - **All time active**
      Points accumulated by the participants of your loyalty program don’t expire
  - **At the end of the month**
      Points accumulated by the participant will expire at the end of the month when he got it i.e. points earned on January 22nd will expire at midnight on February 1st
  - **At the end of the year**
      Points accumulated by the participant will expire at the end of the year when he got it i.e. points earned in 2018 will expire at midnight on January 1st, 2019

.. image:: /userguide/_images/points_expiration.PNG
   :alt:   Expire points method
   
9. Mark the **Points are never locked** checkbox if you want to assign points to Active points pool and recalculate customer level instantly when his transaction will be registered in Open Loyalty

10. **Points will be locked for** field is available and required only when **Points are never locked** is *unselected*. 
  Points will be locked for a provided number of days from the date of transaction registration. After passing selected locked time points automatically will get active and customer level will be recalculated

.. image:: /userguide/_images/locked_points.png
   :alt:   Locked points options

.. note::

    **Date until points will be locked and amount of locked points is displaying in Customer profile details from the Admin and for customers via Client Cockpit**

11. If you marked **Returns** checkbox, then after Return process completed amount of points earned for a returned transaction will be subtracted

12. If you want to get a webhook notification about the customer earned points expiration you can define in **Days before expiring points to notify user** field number of days when notification will be sent.
  For proper operation, it **is necessary to activate the webhook** and provide the URL address to which the information will be sent (more in :doc:`Webhook section </userguide/getting_started/settings/Configuration/webhooks>`)

.. image:: /userguide/_images/webhook_notification.png
   :alt:   Webhook notification option – points expiration

.. note:: 

    **For example** 
    when you enter 10, it means that every day Open Loyalty will be checking if there is any customer who has points which will expire       in 10 days. 
    
    If **yes** webhook event will be sent (on the URL address provided by you in Webhooks section) with information about a customer, a     sum of his points which will expire in 10 days and points expiration date

   
13. If you want to get a webhook notification about the customer coupon expiration you can define in **Days before expiring coupons to notify user** field number of days when notification will be sent. 
   For proper operation, it **is necessary to activate the webhook** and provide the URL address to which the information will be sent (more in :doc:`Webhook section </userguide/getting_started/settings/Configuration/webhooks>`)

.. image:: /userguide/_images/webhook_notification2.png
   :alt:   Webhook notification option – coupons expiration 

.. note:: 

    **For example** 
    when you enter 10, it means that every day Open Loyalty will be checking if there is any coupon which will expire in 10 days. 
    
    If **yes** webhook event will be sent (on the URL address provided by you in Webhooks section) with information about: customer,         coupon code which will expire in 10 days, expiration date and coupon status (status is calculated based on days inactive and days       valid defined during reward campaign creation). 

14. Set the Levels will be calculated with a field to one of the following:

   - **Points** 
      current level assignment will be calculated on the basis of the sum of points earned from transactions (with use of earning rules)
   - **Transactions** 
      current level assignment will be calculated on the basis of the summary value of all transactions

   When **Points** is selected additional section appears below. Please see :doc:`Level downgrade settings </userguide/getting_started/settings/Configuration/level_downgrade_settings>` to learn how to configure reset points after a selected time period and level expiration

15. When **Delivery costs** checkbox is selected then delivery cost will not be included in order value used for earned points calculation

16. **Excluded SKUs of delivery cost** field is available and required only when **Delivery costs** checkbox is selected. 
  SKU's provided in this field will be excluded from the calculation of earned points

17. In the **SKUs excluded from levels** enter SKUs that will not be included in order value used for earned points calculation


When complete, tap ``SAVE``
