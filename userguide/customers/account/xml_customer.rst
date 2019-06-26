.. index::
   single: xml_customer

XML file structure
==================

.. tip:: 

    If you don’t have or don’t want to import all this data, **remove all code line/section instead leave it blank**. 
   
    For example, if you don’t want to include province remove all line from the code - don’t leave it with no value as below
    
    **Remember that some of them are required, so if you remove it Import will not be possible**


.. code-block:: bash

     WRONG FORMATTING
     
     <province> </province>
     <province></province>


Example of complete Customer XML file structure below

.. code-block:: json

      <?xml version="1.0" encoding="UTF-8"?>
      <customers>
         <customer>
            <active>true</active>
            <sendActivationMail>false</sendActivationMail>
            <address>
               <address1>Building name </address1>
               <address2>Flat/Unit name</address2>
               <city>Wroclaw</city>
               <country>PL</country>
               <postal>45-123</postal>
               <province>dolnoslaskie</province>
               <street>Main road</street>
            </address>
            <agreement1>true</agreement1>
            <agreement2>true</agreement2>
            <agreement3>true</agreement3>
            <birthDate>1985-02-03</birthDate>
            <company>
               <name>Company</name>
               <nip>123-12-22-123</nip>
            </company>
            <email>jdoe@example.com</email>
            <firstName>John</firstName>
            <lastName>Doe</lastName>
            <gender>male</gender>
            <labels>
               <label>
                <key>group</key>
                <value>wholesaler</value>
               </label>
            </labels>
            <loyaltyCardNumber>936592735</loyaltyCardNumber>
            <phone>+48231231233</phone>
            <levelID>000096cf-32a3-43bd-9034-4df343e5fd93</levelID>
            <posId>00000000-0000-474c-1111-b0dd880c07e2</posId>
            <sellerId>00000000-0000-474c-b092-b0dd880c07e4</sellerId>
         </customer>
      </customers>
