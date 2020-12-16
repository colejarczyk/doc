.. index::
   single: webhooks 

Webhooks
========

Webhooks is a mechanism allowing to send HTTP requests to the URL configured by Admin, triggered by some event, such as customer registration, transaction created, customer data edit etc. There is no need to be a request initiated on your end, data is sent whenever there’s new data available.

To setup a webhook all you have to do is register a URL with the company proving the service you’re requesting data from. That URL will accept data and can activate a workflow to turn the data into something useful. 

.. image:: /userguide/_images/webhooks.png
   :alt:   Webhooks Enable Option

   
To enable Webhook:
''''''''''''''''''

1. Tap the **Settings** icon |settings| in the upper-right corner and choose **Configuration** on the menu. 

.. |settings| image:: /userguide/_images/icon.png

2. Scroll down to **Webhooks** section, and to enable mechanism do the following: 

  - In **Webhooks** field mark **Enable webhooks** checkbox
  - Enter configured **URL** address on which request will be sent
  - In **Request header name** as an additional security measure for webhooks batch provide a custom header that batches can be securely sent to your webhook endpoint(s). 
    This gives you the option of rejecting webhook batches if these custom headers and associated values are not included in the batch
  - In **Request header value** enter associated with header value

3. When it is done, tap ``SAVE``

Available webhooks
''''''''''''''''''

onCustomerUpdate

.. code-block:: json

  {
     "type": "customer.updated",
      "data": {
              "customerId": "32c764d9-ddd5-401f-ac13-a7fcba0982ff"
           }
  }

onCustomerRegistered

.. code-block:: json

  {
     "type": "customer.registered",
     "data": {
         "customerId": "32c764d9-ddd5-401f-ac13-a7fcba0982ff",
         "data": {
             "firstName": "Jon",
             "lastName": "Doe",
             "gender": "not_disclosed",
             "email": "jdoe@example.com",
             "phone": 123456789,
             "levelAchievementDate": "2019-08-09T14:08:28+02:00",
             "createdAt": 1563363348,
              "address": {
                 "street": "Streets",
                 "address1": "12",
                 "address2": "3",
                 "postal": "41-222",
                 "city": "Glasgow",
                 "province": "Glasgow",
                 "country": "GB"
             },
             "company": {
                 "name": "Hydropol",
                 "nip": "123"
             },
             "loyaltyCardNumber": "444555666",
             "labels": [
                 {
                     "key": "labels_key",
                     "value": "5"
                 }
             ],
             "agreement1": true,
             "agreement2": false,
             "agreement3": false,
             "referral_customer_email": null,
             "levelId": "e82c96cf-32a3-43bd-9034-4df343e50000",
             "posId": "00000000-0000-474c-1111-b0dd880c07e3"
         }
     }
  }

onCustomerDeactivated

.. code-block:: json

  {
     "type": "customer.deactivated",
     "data": {
         "customerId": "32c764d9-ddd5-401f-ac13-a7fcba0982ff"
     }
  }

onCustomerLevelChangedAutomatically

.. code-block:: json

  {
     "type": "customer.level_changed_automatically",
     "data": {
         "customerId": "32c764d9-ddd5-401f-ac13-a7fcba0982ff",
         "levelId": "e82c96cf-32a3-43bd-9034-4df343e51111",
         "levelName": "level1",
         "levelMove": "up",
               "levelAchievementDate": "2019-08-09T14:08:28+02:00",
     }
  }

onCustomerLevelChanged

.. code-block:: json

  {
     "type": "customer.level_changed",
     "data": {
         "customerId": "32c764d9-ddd5-401f-ac13-a7fcba0982ff",
         "levelId": "e82c96cf-32a3-43bd-9034-4df343e50000",
         "levelName": "level0",
               "levelAchievementDate": "2019-08-09T14:08:28+02:00",
     }
  }

onTransactionRegistered

.. code-block:: json

  {
     "type": "transaction.registered",
     "data": {
         "transactionId": "cb4cc2f7-d897-4fe0-b5a6-9b67a91c0729",
         "transactionData": {
             "documentType": "sell",
             "documentNumber": "80",
             "purchasePlace": null,
             "purchaseDate": "2019-08-09T14:08:28+02:00"
         },
         "customerData": {
             "name": "Jon Doe",
             "email": "jdoe@example.com",
             "phone": null,
             "loyaltyCardNumber": null,
             "nip": "123",
             "address": {
                 "street": "Bridges",
                 "address1": "12",
                 "address2": “3”,
                 "postal": "41-222",
                 "city": "New york",
                 "province": "NY",
                 "country": "EN"
             }
         },
         "items": [
             {
                 "sku": {
                     "code": "sku1230"
                 },
                 "name": "product_name",
                 "quantity": 1,
                 "grossValue": 80,
                 "category": "Women",
                 "maker": "Exclusive",
                 "labels": []
             }
         ],
         "posId": null
     }
  }

onTransactionAssignedToCustomer

.. code-block:: json

  {
     "type": "transaction.assigned_to_customer",
     "data": {
         "transactionId": "cb4cc2f7-d897-4fe0-b5a6-9b67a91c0729",
         "customerId": "32c764d9-ddd5-401f-ac13-a7fcba0982ff",
         "grossValue": 80,
     }
  }

onAccountAvailablePointsAmountChanged

.. code-block:: json

  {
     "type": "account.available_points_amount_changed",
     "data": {
         "customerId": "32c764d9-ddd5-401f-ac13-a7fcba0982ff",
         "amount": 125,
         "amount_change": 25,
         "amount_change_type": "add”
     }
  }

