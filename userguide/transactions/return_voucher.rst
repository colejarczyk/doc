.. index::
   single: return_voucher

Return "Voucher" for a Customer
================================

.. note:: 

    **this feature is related ONLY with Percentage discount code campaign type**

**Percentage discount code** is a value discount, which customer received after purchase based on registered order amount. 
Discount will be equal percentage value of registered order amount - percentage value is provided in *Transaction percentage value* field during reward creation.

**For example**

If Customer total amount of transaction is **100 EUR**, and *Transaction percentage value* is equal **10** (i.e. 10% of registered transaction total amount) he will receive **10 EUR** discount for next purchase 

Received value code can be used for next purchase to reduce the value of the order. But what happens if the customer decides to return the transaction to which he used the value code?

.. image:: /userguide/_images/voucher_transactions.PNG
   :alt:   Transactions with Voucher

What will happen to customer's points and indicators of profitability is described in the :doc:`Return transactions </userguide/transactions/menu/returns>`.  

Used value code will be returned to Customer for next purchase, but it's value will depend on the return transaction value in propotion to the **registered order amount before reduction**. Returned value code will have **the same expiration date as the one used**   

For better understanding please see **Examples** below. 

1. Full refund
''''''''''''''''

**100% return - the full value of the coupon is returned**

Customer for his previous order recieved value code worth **100 EUR**, which he used for his next order to reduce it's value - Total order amount before reduction was **1000 EUR**

After few days, for some reason he decided to make full refund of transaction to which he used value code. After return transaction registration, customer: 

 - received *new value code worth the same as used* within transaction i.e. **100 EUR** 
 - returned coupon *expiration date* is the same as used within transaction 
 - returned coupon status is *Delivered*
 - the old coupon status remain *Used* (marked checkbox)
 
.. image:: /userguide/_images/full_refund.PNG	
   :alt:   Full refund voucher 

2. Partial refund
'''''''''''''''''''

**partial return - value of returned coupon is in propotion to the registered order amount before reduction**

Customer for his previous order recieved value code worth **100 EUR**, which he used for his next order to reduce it's value - Total order amount before reduction was **1000 EUR**

After few days, for some reason he decided to make a return transaction of **500 EUR**. Returned transaction is that one to which he used value code. 500 EUR is a half value of total order amount before reduction, so exactly in the same proportion will be calculated value of coupon that will be returned.  

After return transaction registration, customer: 

 - received *new value code worth 50% of the coupon previosly used* within transaction i.e. **50 EUR**  (50% of 100 EUR) 
 - returned coupon *expiration date* is the same as used within transaction 
 - returned coupon status is *Delivered*
 - the old coupon status remain *Used* (marked checkbox)


.. image:: /userguide/_images/partial_refund.PNG	
   :alt:   Partial refund voucher 
   
   
