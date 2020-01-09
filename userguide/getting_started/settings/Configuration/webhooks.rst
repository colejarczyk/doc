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

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Configuration**

.. |settings| image:: /userguide/_images/icon.png

2. Scroll down to **Webhooks** section, and to enable mechanism do the following: 

  - In **Webhooks** field mark **Enable webhooks** checkbox
  - Enter configured **URL** address on which request will be sent
  - In **Request header name** as an additional security measure for webhooks batch provide a custom header that batches can be securely sent to your webhook endpoint(s). 
    This gives you the option of rejecting webhook batches if these custom headers and associated values are not included in the batch
  - In **Request header value** enter associated with header value

3. When complete, tap ``SAVE``

