.. index::
   single: anniversary

Anniversary
===========

Segment of customers who have registration or birthday anniversary in specify number of days . 

**For example**, you can create segment of customers who have birthday within 14 days from today or register today. 


To create only Anniversary type segment:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Segments**. Then, choose **Add segment**. You can also add rule directly from **All segments** list by clicking ``Add segment`` at the top of the page 

.. image:: /userguide/_images/add_segment_button.png
   :alt:   Add Segment Options  


2. In **Basic informations** section, do the following:  

 - Enter a unique segment **Name** to identify the customer segment when working in the Admin
 - Enter a brief **Description** that explain purpose of the segment for internal reference
 - To activate the customer segment, in **Active** field select "**Active**" from the dropdown list

   
.. image:: /userguide/_images/basic_segment.png
   :alt:   Basic Informations Section

3. In **Segment Parts** set the conditions that must be met to assign the customer to *only* **Anniversary** segment. 

   During creation, you need to specify whether to include dates of birth or registration dates and number of **days** before anniversary occurs.

 - in **Type** field choose anniversary type. Options include: 
 
    - Birthday 
    - Registration
    
 - provide number of **days** before anniversary occurs

.. image:: /userguide/_images/anniversary.png
   :alt:   anniversary  


.. tip:: 

    **For example**
    
    if Days is equal 0 then all customers who e.g. have birthday today or register account today or at the same date like today but in previous years will be assign to this segment.
    
    If Days is equal 5 then all customers  who e.g. have birthday within 5 days (including today) or registered account within 5 days in previous years (including today) will be assign to the segment.     
   
   
.. note:: 

    One Segment consists of one or more conditions (types). Conditions can be combined through AND and OR logical operators.
    
     - **AND Condition** 
    
         is used to perform a logical conjuction on two conditions. Both conditions linked with this operator must be true. 
    
         **For example**, you can create segment with a list of customers who made purchase in specific POS and bought specific SKU. The list will contain customer who met both, 1st and 2nd condition.
     
     - **OR Condition** 
 
         is used to perform a logical disjunction on two conditions. At least one of conditions linked with this operator must be true. 
    
         **For example** you can create segment with a list of customers who made purchase in specific POS or bought specific SKU. List will contain customer who met only the 1st condition, who met only the 2nd condition and met both conditions.
  
To learn more about conditions type, see :doc:`Segment parts types </userguide/segments/creation/segment_type>`

4. You can simply **remove condition** by clicking **bin** icon |bin| in a particular row

.. |bin| image:: /userguide/_images/bin.png

5. When complete, tap ``SAVE``  

