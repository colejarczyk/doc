.. index::
   single: xml_points

XML file structure
==================

.. tip:: 

    If you don’t have or don’t want to import all this data, **remove all code line/section instead leave it blank**. 
   
    For example, if you don’t want to include province remove all line from the code - don’t leave it with no value as below
    
    **Remember that some of them are required, so if you remove it Import will not be possible**


.. code-block:: bash

     WRONG FORMATTING
     
     <customerPhoneNumber> </customerPhoneNumber>
     <customerPhoneNumber></customerPhoneNumber>

Example of complete Points transfer XML file structure below

.. code-block:: json

      <?xml version="1.0" encoding="UTF-8"?>
      <pointsTransfers>
         <pointsTransfer>
            <customerId>00000000-0000-474c-b092-b0dd880c07e2</customerId>
            <customerEmail>john.doe@example.com</customerEmail>
            <customerPhoneNumber>+48888888888</customerPhoneNumber>
            <customerLoyaltyCardNumber>936592735</customerLoyaltyCardNumber>
            <points>12</points>
            <type>adding</type>
            <comment>reason of points transfer</comment>
            <validityDuration>30</ validityDuration >
         </pointsTransfer>
         <pointsTransfer>
            <customerEmail>jane.doe@example.com</customerEmail>
            <customerLoyaltyCardNumber>0123456789</customerLoyaltyCardNumber>
            <points>50</points>
            <type>spending</type>
            <comment>reason of points transfer</comment>
            <validityDuration>30</ validityDuration >
         </pointsTransfer>
      </pointsTransfers>
      
