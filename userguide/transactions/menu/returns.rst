.. index::
   single: returns

Returns
=======

If for any reason the customer returns the purchased products and claims a refund a Return transaction is created. Customer can request a return from both, online and offline stores and both, partial or full refund. 

Typically, customer contacts the merchant to request a refund. If merchant authorize the return and agree for refund, a unique document number of related sell transaction is required to identify the returned products and sell transaction, that caused the points earned. 

.. note:: 

    Open Loyalty prevent from: 
    
    - registering a return transaction for non-existing sell transaction 
    - making a return transaction which is not assigned to the same customer as sell transaction (which is returning).  


The **All transactions** menu lists all – return and sell transactions. **To see only returns, you have to filter the list**.


To display Return transactions:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Transactions**. Then, choose **All transactions**

2. In the field under **Document type** column header, click on the arrow

3. To see only returns, choose **Return** from dropdown list

.. image:: /userguide/_images/return.png
   :alt:   Return and Sell Transactions Filter

When Returns are enable (see :doc:`Configuration section </userguide/getting_started/settings/Configuration/settings>`), if the customer made a Return, in addition to subtracting the transaction value from the total value of transactions assigned to Customer, the number of earned points assigned to a given sell transaction is also reversed.

The reversed points will be listed in **All points transfers** menu with **Type spending**.  

.. image:: /userguide/_images/return_points.png
   :alt:   Points Transfer as a Result of Return Transaction

After the return, points are subtracted from the pool of Active points, according to the number of points earned within sell transaction and in proportion to the amount of transaction. 

.. note:: 

    **Points are not reversed according to points earned for bought specific products but in proportion to the all transaction amount (including all bought products)** 

For better understanding please see **Example** below


Example of customer points and profitability factors behavior after return 
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Your customer **transaction value is 40 €** and include following products: 
    
 - Product A – 10 €  
 - Product B – 10 € 
 - Product C – 20 € 
      
For following transaction and purchased of these products your customer has **earned the value of points as below**: 
    
 - Product A – 10 points (for bought specific product)  
 - Product B – 20 points (for bought specific product)
 - Product C – 0 points 
 - 40 points for total transaction value (1€ spend = 1 point earned)  
    
**So in total customer spent 40 € and earned 70 points**. 
    
Points were added to his Active points pool, and transaction value to total amount of his registered transaction value (CLV attribute).
    
For some reason, **he decided to return Product C, which cost 20 €**, which is a half of the total transaction value. 
    
And exactly in the same proportion will be calculated the value of points that will be subtracted. For this transaction he earned 70 points, so half of them – 35 points will be subtracted from the Active points pool. 

    
.. note:: 

    **Note, that the transaction value also affects to the Levels and Segments, which criteria are based on this value. Customer can return to previous level or not be included in a given segment when transaction, which caused this promotion, will be returned**


For more information please see :doc:`Levels </userguide/levels/index>` and :doc:`Segments </userguide/segments/index>` chapters.

     



