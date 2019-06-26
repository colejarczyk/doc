.. index::
   single: emails

Emails
======

Email templates define the layout, content, and formatting of automated messages sent from Open Loyalty. 

Open Loyalty includes a set of responsive email templates that are triggered by a variety of events that take place during the operation of your Loyalty Program. You will find a variety of prepared email templates related to customer activities, admin actions, and system messages that you can customize.

.. image:: /userguide/_images/emails.png
   :alt:   Email Templates


Customizing Email templates
---------------------------

Open Loyalty includes a default email template for the body section of each message that is sent by the system. The template for the body content is formatted with HTML and CSS, and can be easily edited, and customized.

.. image:: /userguide/_images/email_preview.png
   :alt:   Preview of New Points Email
   
To edit an email template:
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Emails**. 

.. |settings| image:: /userguide/_images/icon.png

2. In the **Emails list**, find the record to be edited and click **Edit** icon |edit|  in the Action column to open the record in edit mode	

.. |edit| image:: /userguide/_images/edit.png

.. image:: /userguide/_images/edit_email.png
   :alt:   Template Information

3. Make any necessary changes to the following:	

  - Enter new **Subject** of the email message which will be displayed when the recipient gets an email. 
  
    For example OpenLoyalty – new points. The Template Subject appears also in the Subject column in **Emails list** grid 
  - In **Sender** name field enter the name which will be displayed when the recipient opens an email in the external email system, as the reference so that your recipient knows it was you who sent the message
  - In **Sender email** field  provide an email address which will be displayed when the recipient opens an email in the external system
  - Every template has predefined variables added to content in **Variables** field. The selection of available variables depends on the template and can not be changed
  - The HTML code is used to define content of an email. In the **Content** box, modify the HTML as needed. Any changes of the content should be made by technical persons, who knows HTML to avoid further technical issues with templates

.. note::

    **When working in the template code, be careful not to overwrite anything that is enclosed in double braces**

4. When you are ready to review your work, tap ``Preview``. Then, make adjustments to the template as needed

5. When complete, tap ``SAVE``

	
	 
Email templates
***************

+----------------------------------------------+------------------------------------------------------------+
| Event                                        | Description                                                | 
+==============================================+============================================================+
|  **Account created**                                                                                      |
+----------------------------------------------+------------------------------------------------------------+
| | E-mail send when Customer                  | | Email with link to activate account (password is entered |
| | register to program using Customer Cockpit | | by customer during filling out registration form)        |
|                                              | | and link to download Terms & Conditions file (.PDF)      |
+----------------------------------------------+------------------------------------------------------------+
|  **Account created**                                                                                      |
+----------------------------------------------+------------------------------------------------------------+
| | E-mail send after registering new Customer | | It contains temporary password to activate an account    | 
| | Account using Admin Cocpit, POS Cockpit    | | and link to download Terms & Conditions file (.PDF)      |
| | and API                                    |                                                            |
+----------------------------------------------+------------------------------------------------------------+
|  **Password reset requested**                                                                             |
+----------------------------------------------+------------------------------------------------------------+
| | Send when user click on Forgot password    | | E-mail with reset password link                          |  
| | and provide email address                  |                                                            |
+----------------------------------------------+------------------------------------------------------------+
|  **New reward**                                                                                           |
+----------------------------------------------+------------------------------------------------------------+
| | Send after Customer reward redemption      | | It contains coupon code and reward campaign name         |  
+----------------------------------------------+------------------------------------------------------------+
|  **New points**                                                                                           |
+----------------------------------------------+------------------------------------------------------------+
| | Send after Customer earn points            | | It contains new points value and current amount of       | 
|                                              | | all active points                                        |
+----------------------------------------------+------------------------------------------------------------+
|  **New level**                                                                                            |
+----------------------------------------------+------------------------------------------------------------+
| | Send after Customer reach next level       | | It contains information about customer new level and     |  
|                                              | | new discount                                             |
+----------------------------------------------+------------------------------------------------------------+
|  **Invitation**                                                                                           |
+----------------------------------------------+------------------------------------------------------------+
| | Send after Customer invite his friend to   | | It contains referrer customer name and registration      |
| | loyalty program (refer a friend)           | | link for his friend                                      |
+----------------------------------------------+------------------------------------------------------------+
