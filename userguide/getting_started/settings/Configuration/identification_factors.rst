.. index::
   single: identification_factors 

Identification factors
======================

The identification factors determines the priority of factors used to match particular transaction with particular customer. 

Otherwise, these information are used to assign your loyalty program participant with transaction they making and transmitting relevant transaction data to Open Loyalty for completing or validating redemption-related transactions or re-wards, calculating associated rewards or identifying transaction matches.  


.. image:: /userguide/_images/identification_factors.png
   :alt:   Identification factors

   
To set up identification factors:
'''''''''''''''''''''''''''''''''

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Configuration**. 

.. |settings| image:: /userguide/_images/icon.png

2. Scroll down to **Matching transaction with customer** section. Fields in this section are used to prioritize which of factors will be taken first to calculate transaction to customer assignment.

.. image:: /userguide/_images/matching.png
   :alt:   Matching Factors with Priority 

3. The **Priority** field determines the order in which the calculation will be handled. Enter a number to determine the Priority of this factor in relation to other factors that might be active at the same time (number 1 has the highest priority).

.. note:: 

    **For example**
    
    If there are three factors, with a priority of one, two, and three, the one with the highest priority (number one) is calculated 	before the others. 
    
    If there will be no clear result, factor with the second highest priority is verified etc. 	  
	 
	 
4. Set the **Field** to one of the following: 

  - **email**  
      when matching transaction with the Customer email will be used (e.g. email provided in Loyalty Program and eCommerce must be the same)
  - **loyalty card number**  
      when matching transaction with the Customer loyalty card number will be used (e.g. Loyalty Card Number must be added to eCommerce account)
  - **phone**  
      when matching transaction with the Customer phone number will be used (e.g. phone number must be provided during  account in Loyalty Program creation)


5. You can simply remove factor rule by clicking bin |bin| icon in a particular row 

.. |bin| image:: /userguide/_images/bin.png


6. When complete, tap ``SAVE``




