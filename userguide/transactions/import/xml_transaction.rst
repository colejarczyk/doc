.. index::
   single: xml_transaction

XML file structure
==================

.. tip:: 

    If you don’t have or don’t want to import all this data, **remove all code line/section instead leave it blank**. 
   
    For example, if you don’t want to include posID remove all line from the code - don’t leave it with no value as below
    
    **Remember that some of them are required, so if you remove it Import will not be possible**


.. code-block:: bash

     WRONG FORMATTING
     
     <posId> </posId>
     <posId></posId>


.. tip:: 

    **If you don’t know POS ID you can include only POS Identifier**. POS Identifier is provided during POS creation and accessible from POS list


Example of complete Transaction XML file structure below

.. code-block:: json

      <?xml version="1.0" encoding="UTF-8"?>
      <transactions>
         <transaction>
            <documentNumber>R123/11</documentNumber>
            <purchasePlace>Wroclaw</purchasePlace>
            <purchaseDate>2018-08-15T15:52:01+00:00</purchaseDate>
            <documentType>sell</documentType>
            <posId>00000000-0000-474c-1111-b0dd880c07e2</posId>
            <posIdentifier>pos1</posIdentifier>
            <customer>
               <name>John Doe</name>
               <email> jdoe@example.com</email>
               <nip>123-12-22-123</nip>
               <phone>48231231232</phone>
               <loyaltyCardNumber>12982332</loyaltyCardNumber>
               <address>
                  <street> Main road</street>
                  <address1>123</address1>
                  <city>Wroclaw</city>
                  <country>PL</country>
                  <province>Dolnoslaskie</province>
                  <postal>45-123</postal>
               </address>
            </customer>
            <items>
               <item>
                  <sku>
                     <code>SKU1</code>
                  </sku>
                  <name>Item 1</name>
                  <quantity>1</quantity>
                  <grossValue>100</grossValue>
                  <category>category1</category>
                  <maker>maker</maker>
                  <labels>
                     <label>
                        <key>key1</key>
                        <value>value1</value>
                     </label>
                  </labels>
               </item>
               <item>
                  <sku>
                     <code>SKU2</code>
                  </sku>
                  <name>Item 2</name>
                  <quantity>3</quantity>
                  <grossValue>300</grossValue>
                  <category>category2</category>
                  <maker>maker</maker>
                  <labels>
                     <label>
                        <key>key3</key>
                        <value>value3</value>
                     </label>
                  </labels>
               </item>
            </items>
         </transaction>

