.. index::
   single: matching_transaction

Match transaction with customer
===============================

Usually, transaction come from your store system with information about customer related with. However, you can link transaction with Customer Account directly from the Admin in Open Loyalty, which is useful when you send to Open Loyalty only transactions. 

Depending on Matching transaction with customer identification factors priority (set up in Configuration) customer email, phone number or/and loyalty card number can be used. To remain about identification factors please see  :doc:`Configuration </userguide/getting_started/settings/Configuration/identification_factors>`

.. image:: /userguide/_images/match_transaction.png
   :alt:   Match Customer Account with Transaction

To match transaction with customer:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Transactions**. Then, choose **All transactions**

2. Tap ``Match with customer`` at the top of the page. Then, do the following:
   
 - Enter **E-mail or phone** to find customer, which you want to associate with the transaction
 - Enter transaction **Document number** (transaction ID), which you want to associate with the customer  
 - In the both fields: 
 
    - to find a close match, enter few letters/signs of what you want to find
    - to find an exact match, enter the exact word/number you want to find

3. When complete, tap ``SAVE`` 


.. image:: /userguide/_images/match_transaction2.png
   :alt:   Matching Customer List

