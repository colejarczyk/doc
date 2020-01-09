.. index::
   single: rule_type

Earning rules types
===================

In general, Earning rules can be divided into two types: 

 - **Transactional rules** 
    related to transactions made by customer e.g. transaction total amount, purchased products etc.
 - **Non-transactional rules** 
    related to other customer data and his activity within loyalty program e.g. refer a friend, his friend registration/purchases, newsletter subscription, first purchase, account created etc. 

During creation of rule you must specify its type, describing conditions for awarding points. Every rule type has its own required fields (conditions) that must be filled. 

.. image:: /userguide/_images/rule_types.png
   :alt:   Rule Types

Transactional rules
-------------------
Open Loyalty offer following standard types: 

1. **General spending rule** 
    Customer could receive points for order value
    
    More information about rule creation :doc:`here </userguide/earning_rules/creation/general>`

2. **Multiply earned points**
    Customer could receive multiple points for product with specified SKU
    
    More information about rule creation :doc:`here </userguide/earning_rules/creation/multiply>`

3. **Multiply earned points by product labels**
    Customer could receive multiple points for product with specified labels
    
    More information about rule creation :doc:`here </userguide/earning_rules/creation/multiply_labels>`

4. **Instant reward**
    Customer could receive any reward campaign for his transaction registered within Loyalty Program
    
    More information about rule creation :doc:`here </userguide/earning_rules/creation/instant>`

5. **Product purchase**
    Customer could receive given amount of points for specified product
    
    More information about rule creation :doc:`here </userguide/earning_rules/creation/product_purchase>`



The sequence of points calculation is as following   
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

 1. Firstly, if applicable, customer receives points from **General spending rule**
 2. Secondly, if applicable, points are multiply based on **Multiply earned points** rule, or based on labels multipliers from **Multiply earned points by product labels**. Or  reward is assigned from **Instant reward** rule 
 3. Finally, if applicable, customer receives points from **Product purchase rule**
 
 
.. note::

    Rule from the 2nd step of sequence:
    
     - Multiply earned points,
     - Multiply earned points by product labels and
     - Instant reward
    
    have the same priority. It means, that to points calculation by default **only one of them, the most "current" rule is used**. 
    
    In that case, **"current" means edited as the last one**.
       
 


Non-transactional rules
-----------------------
Open Loyalty offer following standard types: 

1. **Custom event rule** 
    Customer could receive points for external actions
    
    More information about rule creation :doc:`here </userguide/earning_rules/creation/custom>`
   
2. **Customer referral**
    Referred and/or Referrer customer receive points for his action
    
    More information about rule creation :doc:`here </userguide/earning_rules/creation/referral>`
   
3. **Event rule**
    Customer could receive points for specified actions
    
    More information about rule creation :doc:`here </userguide/earning_rules/creation/event>`
      
4. **Geolocation**
    Customer could receive points for his location
    
    More information about rule creation :doc:`here </userguide/earning_rules/creation/geolocation>`
   
5. **QRcode**  
    Customer could receive points for scanning define QR codes 
    
    More information about rule creation :doc:`here </userguide/earning_rules/creation/qrcode>`

