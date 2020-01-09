.. index::
   single: users 

Users
=====

When your store is first set up, you receive a set of login credentials for the Administrator role that has full permissions. If there are others on your team or service providers who need access, you can create a separate user account for each from this section.

Users list include both active and inactive Admin user’s – inactive are grayed-out. You can also see their status in Active column. Additionally, Users list grid provides basic information about users – name, surname, email address and authenticate method.

.. image:: /userguide/_images/users.png
   :alt:   All Users

   
New admin user creation
-----------------------

To add new user:
^^^^^^^^^^^^^^^^

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Users**. 

.. |settings| image:: /userguide/_images/icon.png

2. To add new user, tap ``Add``

.. image:: /userguide/_images/add_user.png
   :alt:   New User Account Information

3. In the **Create user** section, complete the following information:

  - Name
  - Surname
  - Phone
  - E-mail

  This email address must be different from the one that is associated with your original Admin account
	 
4. Then you have to decide which of the following user authentication method to choose:

  - To authenticate user via an **API key**, do the following:
  
    - Mark checkbox **External**
    - Enter an **API key**, received from Open Loyalty provider
   
  - To authenticate user via **Password**, do the following:
  
    - Leave **External** checkbox blank
    - Assign a **Password** to the account

5. Set **Active** field to "Active"

6. When complete, tap ``SAVE``

.. note::

    In case of API key authentication, you will authenticate the user and store that authentication in the session, so User will be automatically logged in for every subsequent request
	

Admin user edition
------------------

.. image:: /userguide/_images/edition.png
   :alt:   Admin User Editing
   

To edit an admin account:
^^^^^^^^^^^^^^^^^^^^^^^^^

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Users**. 

.. |settings| image:: /userguide/_images/icon.png

2.	In the Users list, find the record to be edited and click **Edit** icon |edit|  in the Action column to open the record in edit mode.	

.. |edit| image:: /userguide/_images/edit.png

3. Make any necessary changes to user account information. **If you change password/API key, make sure to inform user about changes**

4. When complete, tap ``SAVE``


Locked users
------------

Any user account that is currently inactive appears in the Users list as grayed-out. An account can be unlocked (set to active) by other Admin users.

To lock/unlock an admin account:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Users**. 

.. |settings| image:: /userguide/_images/icon.png

2.	In the Users list, find the record to be edited and click **Edit** icon |edit|  in the Action column to open the record in edit mode.	

.. |edit| image:: /userguide/_images/edit.png

3. Set **Active** field, to one of the following

  - **Active**  
      to unlock admin account. User can log in and have access to the Open Loyalty platform
  - **Inactive**  
      to lock an admin account. User will not be able to log in and have access to the Open Loyalty platform

  

.. tip::

    **Admin users can not be deleted from Open Loyalty platform**. 
	 
    To prevent any user from access to the platform, **set the Active field as Inactive**

