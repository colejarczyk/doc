.. index::
   single: transfer_import

Import points transfers
=======================

If you have a customer list that you want to add points within your Loyalty Program, you can enter it into a Points transfer XML file and then import it in your Open Loyalty Admin. 

.. image:: /userguide/_images/points_import.png
   :alt:   Import Points Transfers

Importing a  XML file will create a points transfers for each customer:

 - email address 
 - phone number 
 - ID 
 - Loyalty card number
 
.. note:: 

    At least one, of the listed above value, must be provided to identify the customer and create points transfer for him. 

.. tip:: 

    **For example**, 
    
    in XML file you can provide only customer loyalty card number – if this number is unique and allow to identify him. 
    
    If not, provide e-mail or phone number for better authentication. 
    

If all informations are provided, platform uses them to assign your loyalty program participant with points transfer based on hard-coded priorities assigned to this value. **Priorities can’t be changed**.

Priorities are as follows: 

1. Customer ID 
2. Customer e-mail address
3. Customer Loyalty card number 
4. Customer phone number 

If any of this four listed value will not give a result an error message occurred. 
 
Mechanism of matching the customer with points transfer basing on priorities is the same like in :doc:`Identification factors </userguide/getting_started/settings/Configuration/identification_factors>` description (number 1 has the highest priority).

.. note:: 

    **For example**,
    
    if XML file includes customer ID and email address, customer ID is used for matching before the email address. 
    
    If there will be no clear result, email is verified. 


To import a points from a file:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Points transfers**. Then, choose **All points transfers**

2. Click ``Import`` at the top of the page, next to ``Add Transfer``

.. image:: /userguide/_images/add_transfer_button.png
   :alt:   Points Import Button

3. In the **Import points transfers** dialog, click ``Upload`` and then choose your customer XML file.

.. image:: /userguide/_images/import_points.png
   :alt:   Import Points Transfers

4. When file selected, click ``IMPORT``

The points transfers details of customers whose you've added to the XML file will appear in the **All points transfers** list in your Open Loyalty admin. 

