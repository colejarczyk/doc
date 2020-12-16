.. index::
   single: messages

Message Templates
=================

Message templates define the layout, content, and formatting of automated messages sent from Open Loyalty.

Open Loyalty includes a set of responsive email, SMS and Push Notification templates that are triggered by a variety of events that take place during the operation of your Loyalty Program. You will find a variety of prepared templates related to customer activities, admin actions, and system messages that you can customize.

.. image:: /userguide/_images/emails2.PNG
   :alt:   Message Templates


Customizing Message templates
-----------------------------

Open Loyalty includes a default message template for the body section of each message that is sent by the system. The template for the body content is formatted with HTML and CSS, and can be easily edited, and customized.

.. image:: /userguide/_images/email_preview.png
   :alt:   Preview of New Points Email

To edit an Message template:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Tap the **Settings** icon |settings| in the upper-right corner and choose **Message templates** on the menu.

.. |settings| image:: /userguide/_images/icon.png

2. In the **Messages list**, find the record to be edited and click **Edit** icon |edit| in the Action column to open the record in edit mode

.. |edit| image:: /userguide/_images/edit.png

.. image:: /userguide/_images/edit_email2.png
   :alt:   Template Information

3. Make any necessary changes to the following:

  - In **Target** choose to whom the message will be send
  - In **Channel** select what message you would like to send
  - In each message is **Event** field. Chose after what operation the message will be send
  - **Enabled** activates and deactivates the sending of messages
  - Enter new **Subject** of the message which will be displayed when the recipient gets an email.
  - Every event has predefined snippets added to content in **Snippets** field. The selection of available snippets depends on the event and can not be changed
  - The HTML code is used to define content of a message. In the **Content** box, modify the HTML as needed. Any changes of the content should be made by technical persons, who knows HTML to avoid further technical issues with templates.

.. note::

    **When working in the template code, be careful not to overwrite anything that is enclosed in double braces**


4. When you are ready to review your work, tap ``Preview``and make adjustments to the template as needed

5. When it is done, tap ``SAVE``


To stop/restart sending emails generated with a given template:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Tap the **Settings** icon |settings| in the upper-right corner and choose **Message templates** on the menu.

.. |settings| image:: /userguide/_images/icon.png

2. In the **Message list**, find the record to be disabled/enabled and click **Edit** icon |edit|  in the Action column to open the record in edit mode

.. |edit| image:: /userguide/_images/edit.png

.. image:: /userguide/_images/edit_email2.png
   :alt:   Template Information

3. Uncheck or check the **Enabled** box.

4. Tap ``SAVE``.


Email, SMS, Push Notification templates list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------------------------------+------------------------------------------------------------+
| Event                                        | Description                                                |
+==============================================+============================================================+
|  **Campaign has become available**                                                                        |
+----------------------------------------------+------------------------------------------------------------+
| | Message send when the new campaign         | | Message with information about new campaign              |
| | was created                                | |                                                          |
|                                              | |                                                          |
+----------------------------------------------+------------------------------------------------------------+
|  **Customer registered with temporary password**                                                          |
+----------------------------------------------+------------------------------------------------------------+
| | Message send after registering new Customer| | It contains temporary password to activate an account    |
| | Account using Admin Cocpit, POS Cockpit    | | and link to download Terms & Conditions file (.PDF)      |
| | and API                                    |                                                            |
+----------------------------------------------+------------------------------------------------------------+
|  **Customer registered and awaits activation**                                                            |
+----------------------------------------------+------------------------------------------------------------+
| | Message send after registering new Customer| | Message with activate the account                        |
| | Account using Client Cockpit               |                                                            |
+----------------------------------------------+------------------------------------------------------------+
|  **Earned points**                                                                                        |
+----------------------------------------------+------------------------------------------------------------+
| | Send after Customer earn points            | | It contains new points value and current amount of       |
|                                              | | all active points                                        |
+----------------------------------------------+------------------------------------------------------------+
|  **Email changed**                                                                                        |
+----------------------------------------------+------------------------------------------------------------+
| | Send after Customer change the email       | | It contains token to change the email address            |
| | in Client Cockpit                          |                                                            |
+----------------------------------------------+------------------------------------------------------------+
|  **Gained new level**                                                                                     |
+----------------------------------------------+------------------------------------------------------------+
| | Send after Customer reach next level       | | It contains information about customer new level and     |
|                                              | | new discount                                             |
+----------------------------------------------+------------------------------------------------------------+
|  **Issued Reward Campaign**                                                                               |
+----------------------------------------------+------------------------------------------------------------+
| | Send when a customer buys campaign         | | It contains rewards coupon and information               |
| | for accumulated points                     | | how to use it                                            |
+----------------------------------------------+------------------------------------------------------------+
|  **Customer used campaign reward**                                                                        |
+----------------------------------------------+------------------------------------------------------------+
| | Send when customer will use                | | Message with the information about used campaign         |
| | the campaign                               | |                                                          |
|                                              | |                                                          |
+----------------------------------------------+------------------------------------------------------------+
|  **User requested password reset**                                                                        |
+----------------------------------------------+------------------------------------------------------------+
| | Send when user click on Forgot password    | | Message with reset password link                         |
| | and provide email address                  | |                                                          |
|                                              | |                                                          |
+----------------------------------------------+------------------------------------------------------------+
|  **Phone number changed**                                                                                 |
+----------------------------------------------+------------------------------------------------------------+
| | Send after Customer change the phone       | | It contains basic information of the reward and customer |
| | number in Client Cockpit                   | | who used it and address assigned to his account to which |
|                                              | | the prize is to be sent                                  |
+----------------------------------------------+------------------------------------------------------------+
|  **Transaction labeled**                                                                                  |
+----------------------------------------------+------------------------------------------------------------+
| | Send when new transaction is added to      | | Message with the information about new transaction       |
|   list                                       | |                                                          |
+----------------------------------------------+------------------------------------------------------------+

Which events working for messages: email, Push Notification and SMS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Email - Customer registered with temporary password, Customer registered and awaits activation, Earned points, Email changed, Gained new level, Issued Reward Campaign, Password reset requested, Phone number changed, Transaction labeled

Push Notification - Campaign has become available

SMS - Customer registered with temporary password, Customer registered and awaits activation, Earned points, Email changed, Gained new level, Issued Reward Campaign, Password reset requested, Phone number changed, Transaction labeled
