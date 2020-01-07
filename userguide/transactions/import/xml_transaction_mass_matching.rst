.. index::
   single: xml_transaction_mass_matching

XML file structure
==================

.. tip:: 

    If you don’t have or don’t want to import all this data, **remove all code lines/section instead leave it blank**. 
   
    For example, if you don’t want to include phone remove all line from the code - don’t leave it with no value as below
    
    **Remember that some of them are required, so if you remove it Import will not be possible**


.. code-block:: bash

     WRONG FORMATTING
     
     <phone> </phone>
     <phone></phone>


Example of completed mass matching transaction XML file structure below

.. code-block:: json

      <?xml version="1.0" encoding="UTF-8"?>
      <matchCustomers>
        <matchCustomer>
           <customerId>00000000-0000-474c-b092-b0dd880c07e33</customerId>
           <customerEmail>marek@example.com</customerEmail>
           <customerPhoneNumber>+48888888888</customerPhoneNumber>
           <customerLoyaltyCardNumber>936592735</customerLoyaltyCardNumber>
           <transactionDocumentNumber>t111</transactionDocumentNumber>
        </matchCustomer>
		<matchCustomer>
           <customerId>00000000-0000-474c-b092-b0dd880c07e44</customerId>
           <customerEmail>tomek@example.com</customerEmail>
           <customerPhoneNumber>+48888888889</customerPhoneNumber>
           <customerLoyaltyCardNumber>936592739</customerLoyaltyCardNumber>
           <transactionDocumentNumber>t190</transactionDocumentNumber>
        </matchCustomer>
      </matchCustomers>

