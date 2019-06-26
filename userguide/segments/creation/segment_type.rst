.. index::
   single: segment_type

Segment parts types
===================

The assignment process is carried out by the application based on defined rules. Customers who meet all criteria will be assigned to the segment. 

The criteria consist of conditions that can be combined through AND (conjuction of sets) and OR (disjunction of sets) logical operators.

During creation of Segment you must specify Segment parts type, describing conditions for assigning customer. Every type has its own required fields that must be filled, to specified condition. 

.. image:: /userguide/_images/segment_type.png
   :alt:   Segment Parts Types


Segments types
--------------
Open Loyalty offer following standard types: 

1. **Anniversary** 
    Customers  who have registration/birthday anniversary in specify number of days
    
    More information about segment creation :doc:`here </userguide/segments/creation/anniversary>`

2. **Average transaction amount**
    Customers whose average transaction value is between the limits 
    
    More information about segment creation :doc:`here </userguide/segments/creation/average_transaction>`

3. **Bought in specific POS**
    Customers who made purchase in selected POS
    
    More information about segment creation :doc:`here </userguide/segments/creation/pos>`

4. **Bought products with labels**
    Customers who bought products where label on product is one of the list
    
    More information about segment creation :doc:`here </userguide/segments/creation/product_labels>`

5. **Bought specific brands**
    Customers who bought products of a given brand
    
    More information about segment creation :doc:`here </userguide/segments/creation/brands>`

6. **Bought specific SKU** 
    Customers who bought specific products (on the basis of selected SKU) 
    
    More information about segment creation :doc:`here </userguide/segments/creation/sku>`

7. **Custom customer list**
    Any Customers selected by admin  
    
    More information about segment creation :doc:`here </userguide/segments/creation/custom_customer>`

8. **Customer who has such labels**
    Customers who made purchase in selected POS
    
    More information about segment creation :doc:`here </userguide/segments/creation/customer_labels>`

9. **Customers who has such labels value**
    Customers whose labels value on is one of the list
    
    More information about segment creation :doc:`here </userguide/segments/creation/customer_labels_value>`

10. **Last purchase was n days ago**
     Customers who have made their last purchase n-days ago 
    
     More information about segment creation :doc:`here </userguide/segments/creation/last_purchase>`

11. **Purchase period**
     Customers who made purchase (at least one) between the specified days  
    
     More information about segment creation :doc:`here </userguide/segments/creation/purchase_period>`

12. **Transaction count**
     Customers whose number of purchases is within the defined range 
    
     More information about segment creation :doc:`here </userguide/segments/creation/transaction_count>`
     
13. **Transaction percent in POS**
     Customers whose number of purchases in a specified POS is within defined percent amount 
    
     More information about segment creation :doc:`here </userguide/segments/creation/transaction_pos>`
     
14. **Transaction value**
     Customers whose overall amount of purchases is between the limits  
    
     More information about segment creation :doc:`here </userguide/segments/creation/transaction_value>`

