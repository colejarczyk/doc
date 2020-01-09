.. index::
   single: product_labels

Bought products with labels
===========================

Segment of customers who bought products where label on product is one of the list. Labels are key-value pairs that you can attach to a products.  

**For example**, you can create segment of customers who bought trousers (key) - jeans (value) or leggins (value) 

To create only Bought products with labels type segment:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the Admin sidebar, tap **Segments**. Then, choose **Add segment**. You can also add rule directly from **All segments** list by clicking ``Add segment`` at the top of the page 

.. image:: /userguide/_images/add_segment_button.png
   :alt:   Add Segment Options  


2. In **Basic informations** section, do the following:  

 - Enter a unique segment **Name** to identify the customer segment when working in the Admin
 - Enter a brief **Description** that explain purpose of the segment for internal reference
 - To activate the customer segment, in **Active** field select "**Active**" from the dropdown list

   
.. image:: /userguide/_images/basic_segment.png
   :alt:   Basic Informations Section

3. In **Segment Parts** set the conditions that must be met to assign the customer to *only* **Bought products with labels** segment.   

   Each of list element has two values – **Key**, which is a label name, and **Value**, which is a label value. Both field need to be filled out.  
   
   Enter your key and value to add a product label. To apply additional labels, click ``Add label``

.. image:: /userguide/_images/segment_product_labels.png
   :alt:   Bought Labels Type

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
 
   
   
