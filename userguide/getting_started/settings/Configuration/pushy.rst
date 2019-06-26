.. index::
   single: pushy

Push Notification Service
===========================

A push notification is a message that pops up on a mobile devices and websites. For better communication and to increase engagement for your loyalty program participants using mobile app you can integrate Open Loyalty platform with **PUSHY.ME** 

**Pushy** is push notification gateway, which can be used to send pursh notification to each user that install app version or visits your website and registers for push notifications. A unique device token token is assign to each customer to identify him and send personalized notification. 


.. warning::

    Customer, within first website visit, need to accept notification receiving. Then unique device token is assigned. 
    
    **Token assignement will fail if the user declines the Web Push permission dialog**. In that case notification will not be sent. 


You need to pass these device tokens to OpenLoyalty via /api/customer/{customer}/pushy-token endpoint. 

.. image:: /userguide/_images/pushy.PNG	
   :alt:   Push Notification Service

**Currently, Open Loyalty support one notification about new reward campaign available for customer** 

Text of displaying notification is provided by you during reward campaign creation. More information about reward campaigns you will find :doc:`here </userguide/reward_campaigns/index>`

.. note::

    **To integrate Open Loyalty platform with Pushy gateway firstly, you have to create an account in Pushy**. 
    
    **The data from your account will be needed to set up integration (API authentication section)** 


To set up integration with Pushy:
'''''''''''''''''''''''''''''''''''''''

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Configuration**. 

.. |settings| image:: /userguide/_images/icon.png

2. Scroll down to **Push Notification Service** section 

3. To integrate with Pushy in **Pushy API secret key** field provide your Pushy ApiSecret string (API authentication section from your Pushy account) 

4. When complete, tap ``SAVE``

.. warning::

    **To display push notification, only API key is not enough** 
    
    You have to put a code into your app or/and website application code. Documentations how to do this can be found on the official pushy website ``https://pushy.me/docs/web-push``

Below, you will find an example of code that can be paste to enable notification. 

.. code-block:: json

      <!DOCTYPE html>
      <html lang="pl" dir="ltr">
         <head>
            <meta charset="utf-8">
            <title></title>
         </head>
         <body>
            Hello!
            <script src="https://sdk.pushy.me/web/1.0.2/pushy-sdk.js"></script>
            <script>
               // Register device for push notifications
               Pushy.register({ appId: '%APP-ID%' }).then(function (deviceToken) {
                  // Print device token to console
                  console.log('Pushy device token: ' + deviceToken);

                  // Send the token to your backend server via an HTTP GET request
                  // $.post('%your-api%/api/customer/{customer}/pushy-token/', { 'customer': { 'pushyToken': deviceToken; }});

                  // Succeeded, optionally do something to alert the user
               }).catch(function (err) {
                  // Handle registration errors
                  console.error(err);
               });
            </script>
          </body>
         </html>
  
.. tip::

   **More information about PUSHY and push notification mechanism you will find on a official pushy website: ``https://pushy.me/docs/web-push``** 
    
