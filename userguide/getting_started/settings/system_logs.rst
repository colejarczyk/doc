.. index::
   single: system_logs 

Audit log list
==============

Logs grid allows monitoring every change on the customer data. The log file is accessible only to Admin users throughout the Admin Cockpit. Logs view allows you to check the date and time that change was made, type and unique ID of change and user name and his unique ID associated with this change. 

In addition, you can control logs results by filter and search option.

.. image:: /userguide/_images/logs.png
   :alt:   Audit Logs

System monitors and performs following events/operations:

1. **Create** –
	Customer and all elements related to the customer: transactions, transfers.
	For example: new points transfer to customer account creation
	
2. **Modify** - 
	Customer, all elements related to customer (transactions, transfers, redeemed rewards), operations that change customer data indirectly (segments and level assignment)
	For example: agreements updated
	
3. **Read** -
	Customer and all elements related to the customer: transactions, transfers, redeemed rewards
	For example: view customer
	
4. **Delete** -
	Customer, all elements related to customer (transactions, transfers, redeemed rewards), operations that change customer data indirectly (segments and level assignment)
	For example: delete points transfer to customer account

Search Audit Log by date range
------------------------------

You can search for audit logs by a certain time period using Search from time period search box. Date ranges can be specified with static start and end dates.

The date format is as follows: “YYYY-MM-DD HH:mm” and allows to display logs that have been placed from and up to the specified date.

.. image:: /userguide/_images/logs_search.png
   :alt:   Search box

To find a match:
^^^^^^^^^^^^^^^^

1. Tap the **Settings** icon |settings| in the upper-right corner and choose **Audit log** on the menu.

.. |settings| image:: /userguide/_images/icon.png
   :alt:   Settings icon

2. Set up the starting date in **From** field by selecting date and time from calendar grid

3. Set up the end date in **To** field by selecting date and time from calendar grid

4. When it is done, tap ``Search``


Search/Filter Logs
------------------

The filters in the header of each column can be used to limit the list to specific values. You can simply type the value you want to find and press Enter.

.. image:: /userguide/_images/logs_filter.png
   :alt:   Search/Filter Logs Results

To search the list:
^^^^^^^^^^^^^^^^^^^^^^^  

1. In the selected column in the field under column header type the value you want to find

  - to find a close match, enter the few letters/signs of what you want to find
  - to find an exact match, enter the exact word/number you want to find

2. You can put as many values under different columns headers as needed to describe the conditions that must be met for the search result. Search values from each column create an AND Condition rule. It means that in search results only records matching all entered values are displayed

Export Audit logs
-----------------

You can export audit logs to the csv file based on the for ie. selected time period for the logs.

To export audit logs:

1. Search logs based on the filters in the headers of each column and time period and click on the **Export to csv** icon.

.. image:: /userguide/_images/archives.png

After clicking, the list of exported audit logs will be downloaded in .CSV format.

Archive Audit logs
------------------

You can archive audit logs to the xml file from the previous year.

To archive audit logs:

1. Click on the **Archives** icon.

.. image:: /userguide/_images/archives.png

2. Select the date in **Archive before** field to which the logs will be archived

.. image:: /userguide/_images/archive.png

3. Click on the **Generate a new archive** icon.

.. image:: /userguide/_images/generate_archive.png

The archive audit log xml file will be visible in the "Archived files available for download:" section.