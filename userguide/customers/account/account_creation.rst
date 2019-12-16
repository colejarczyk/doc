.. index::
   single: account_creation

Creating Customer account from admin
=====================================

Customer usually create their own accounts from your webshop or using Customer Cockpit. 

However, you can also create customer account directly from the Admin or POS Cockpit, which is useful when customers order by phone or at merchant location. 

.. note:: 

    **The Customer account created from the Admin or POS Cockpit has an active status instantly, so there is no need to activate its account by him** 

.. image:: /userguide/_images/add_customer.png
   :alt:   New Customer Account Information 


To create a New Customer Account:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Customers**. Then, choose **Add Customer**. You can also add customer directly from **All customers** list by clicking ``Add Customer`` at the top of the page 

.. image:: /userguide/_images/add_customer_button.png
   :alt:   Add Customer Options  
   
.. image:: /userguide/_images/basic_customer.png
   :alt:   Basic Information 

2. In the **Basic Information** section, complete the following required fields:   
  
 - First name 
 - Last name 
 - E-mail 

.. note:: 

    **For one email address only one Customer Account could be created**. 
    
    **You can change the email address associated with an account by editing a customer** 

3. In the same section, complete the optional fields as needed: 

 - Gender 
 - Birth date 
 - Phone (in one of acceptable format) 
 - Loyalty card number
 - Select level 
 - Select POS 
 - Select merchant

4. If applicable, create **Label(s)** you want refer to customer. Labels are intended to be used to specify identifying attributes of customer. 
  
   Labels can be used to organize and to select subsets of customers at customer segmentation process. To learn more about Customer segmentation, see :doc:`Segments </userguide/segments/index>`

 - To create Label, tap ``Add Label`` and do the following: 
    - Type label **Key**, which is a label name
    - Type label **Value**
      
     For example: Key – Customer type, Value – wholesale 
      
 - Repeat the process for all labels you want to used in your Loyalty Program

.. image:: /userguide/_images/customer_labels.png
   :alt:   Customer Labels 


.. note:: 

    **Labels can be added to customer during account creation and subsequently added and modified at any time** 

5. Mark **Company** checkbox, to define customer type if needed. 

6. Mark **Address** checkbox, to complete customer address information if needed.

.. image:: /userguide/_images/company_and_address.png
   :alt:   Company Data and Address Sections

7. **Company Data** section is available only when **Company** checkbox is selected. 
  
  All fields available in this section i.e. **Company name** and **Tax Identification Number** are required and need to be filled out. 

8. **Address** section is available only when **Address** checkbox is selected. Complete the following required fields: 

 - Street name 
 - Building name
 - Postal code
 - City
 - Country

 In the same section, complete the optional fields as needed:
   
 - Flat/Unit name 
 - State/Province

9. Mark the **Agreements** that customer has agreed to. **Legal agreement** is required and need to be filled out to set up an account. 

.. image:: /userguide/_images/agreements.png
   :alt:   Agreements

10. When complete, tap ``SAVE``

When the customer account is saved, it’s record appears at **All customers** list. 

The Customer Profile Details tab displays a summary of account activity and data provided during account creation. To learn more about Customer Profile, see :doc:`Profile details </profile_details/index>` 


Field description
*****************

+--------------------+-----------------------------------------------------------------------+
| FIELD              | DESCRIPTION                                                           |
+====================+=======================================================================+
| **BASIC INFORMATION**                                                                      |                 
+--------------------+-----------------------------------------------------------------------+
| First name*        | | The customer’s first name                                           |                               
+--------------------+-----------------------------------------------------------------------+
| Last name*         | | The customer’s last name                                            |
+--------------------+-----------------------------------------------------------------------+
| Gender             | | Identifies the customer’s gender as Male, Female or Not disclosed   |
+--------------------+-----------------------------------------------------------------------+
| Birth date         | | The customer’s date of birth.                                       |
|                    | | Information can be used to offer points for the birth anniversary   |                                         
+--------------------+-----------------------------------------------------------------------+
| Email*             | | The customer email address.                                         |
|                    | | Is used as a login name while logging to Customer Cockpit.          |                             
+--------------------+-----------------------------------------------------------------------+
| Phone              | | The customer’s phone number. Formatting is as on follow example:    |
|                    |                                                                       |
|                    |    - Country Code: +48/48                                             |
|                    |    - Subscriber number: 123456789                                     |
|                    |    - In total: +48123456789 / 123456789 / 48123456789                 |
+--------------------+-----------------------------------------------------------------------+
| Loyalty card       | | The customer loyalty card number                                    |
| number             |                                                                       |                                         
+--------------------+-----------------------------------------------------------------------+
| Labels             | | Internal tags you can use to refer your customer.                   |
|                    | | If applicable, can be used to segmentation to identify the customers|
|                    | | that this segment applies to                                        |
+--------------------+-----------------------------------------------------------------------+
| Select level       | | Starting level assigning to customer                                |
+--------------------+-----------------------------------------------------------------------+
| Select POS         | | POS which will be linked to the customer                            |
+--------------------+-----------------------------------------------------------------------+
| Select Merchant    | | Merchant account, which will be linked to the customer              |
+--------------------+-----------------------------------------------------------------------+
| Company            | | customer associated with company.                                   |
|                    | | If marked then additional sectionwill be shown.                     |                           
+--------------------+-----------------------------------------------------------------------+
| Address            | | customer address needed.                                            |
|                    | | If marked then additional section will be shown                     |                             
+--------------------+-----------------------------------------------------------------------+
| | **COMPANY DATA**                                                                         |
| | Visible only when **Company** checkbox is marked                                         |                 
+--------------------+-----------------------------------------------------------------------+
| Company name*      | | The company name, if applicable for this customer                   |
+--------------------+-----------------------------------------------------------------------+
| Tax Identification | | The company TAX / VAT number                                        |
| Number*            |                                                                       |                             
+--------------------+-----------------------------------------------------------------------+
| | **ADDRESS**                                                                              |
| | Visible only when **Address** checkbox is marked                                         |                 
+--------------------+-----------------------------------------------------------------------+
| Street name*       | | The street address of the customer                                  |
+--------------------+-----------------------------------------------------------------------+
| Building name*     | | The name/number of a building or property where the customer        |
|                    | | resides at this address                                             |                             
+--------------------+-----------------------------------------------------------------------+
| Flat/Unit name     | | The flat/unit name or number of the customer at this address        |
+--------------------+-----------------------------------------------------------------------+
| Postal code*       | | The postal code of the customer at this address                     |
+--------------------+-----------------------------------------------------------------------+
| City*              | | The city where the customer resides at this address                 |
+--------------------+-----------------------------------------------------------------------+
| State/Province     | | The state or province of the customer at this address               |
+--------------------+-----------------------------------------------------------------------+
| Country*           | | The country where customer resides at this address                  |
+--------------------+-----------------------------------------------------------------------+
| | **AGREEMENTS**                                                                           |                                         
+--------------------+-----------------------------------------------------------------------+
| | List of consents to which the customer can/has agreed.                                   |
| | Options include:                                                                         |
|                                                                                            |                         
|   - Legal agreement (required)                                                             |                  
|   - Marketing agreement                                                                    |
|   - Data processing agreement                                                              |
+--------------------+-----------------------------------------------------------------------+

