.. index::
   single: import_customers

Import Customers list
=======================

If you have a customer list that you want to add to your Loyalty Program, you can enter it into a customer XML file and then import it in your Open Loyalty Admin. 

.. image:: /userguide/_images/customers_import.png
   :alt:   Customers import

Importing a XML file will create a customer in your Loyalty platform for each email address, phone number and loyalty card number in the file. 

**Any customers with duplicate email addresses, phone numbers or loyalty card number will be skipped** during an import

To import a Customer list from a file:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Customers**. Then, choose **All Customers**

2. Click ``Import`` at the top of the page, next to ``Add Customer``

.. image:: /userguide/_images/customer_import_button.png
   :alt:   Customers Import Button

3. In the **Import Customers** dialog, click ``Upload``, and then choose your customer XML file

.. image:: /userguide/_images/customer_import_window.png
   :alt:   Customers Import Button

4. When file selected, click ``IMPORT``

The customers whose records you've added to the XML file will appear in the **All customers** list in your Open Loyalty admin

.. note:: 

    For all imported customers (on the provided in XML file email addresses) **Welcome email** with temporary password is sent. 
    
    Customers accounts are **active** instantly, so after email receiving they can simply log in to theirs account using individual **e-mail** address (from XML file) and temporary **password** (from the Welcome email) 
