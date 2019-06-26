.. index::
   single: acl

Access Control List (ACL) 
==========================

.. note::

    **Users roles and permissions (ACL settings) are related only with Admin Cockpit users**

Open Loyalty platform uses roles and permissions to create different levels of access to the Admin Cockpit. When your platform is first installed, you receive a **Super admin** role that has full permissions and give you full administrative access.

However, you can restrict the level of permissions for other admin users, who work with you. For example, a customer sevice can be given access to only the Customers, but not to areas with settings and earning rules.

.. note::

    To give someone restricted access to the Admin, the first step is to create a role that has the appropriate level of permissions.
    
    After the role is saved, you can add new users and assign the restricted role to grant them limited access to the Admin.


If an Admin user’s access is restricted to specific sections and/or elements, the sections and elements for which they are not authorized will either not be visible to them, or grayed-out as inactive.

.. image:: /userguide/_images/roles.PNG
   :alt:   Admin Roles

.. note::

    The grid lists all the existing roles. After first installed, **Super admin** is the only role available.


New role creation
-----------------------

To add new Role:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **ACL**. 

.. |settings| image:: /userguide/_images/icon.png

2. To add a new role, tap ``Add Role``

.. image:: /userguide/_images/roles_button.PNG
   :alt:   Add new role button

.. image:: /userguide/_images/new_role.PNG
   :alt:   Add new role
 
3. In the *Basic Information* section enter a descriptive role **Name**

4. To assigne resources and permissions level, do the following:

  - tap ``Add permission`` in **Permissions** field
  - set **Access** level of permissions to one of the following:
    
    - **Modify**
       user can do anything in platform specified sections and/or elements
      
    - **View**
       user can only read and display the platform specified sections and/or elements

  - in **Resource** field select from dropdown Admin Cockpit resource that the role can specified in previous step *Access*
  
.. image:: /userguide/_images/permissions.PNG
   :alt:   Assigne resources
  
5. Repeat *step 4* to add access for additional resources assigne to the Role

6. You can simply remove permission by clicking bin |bin| icon in a particular row 

.. |bin| image:: /userguide/_images/bin.png

7. When complete, tap ``SAVE``
 
The role now appears in the grid, and can be assigned to new user accounts.

+--------------------+-----------------------------------------------------------------------+
| ACCESS             | DESCRIPTION                                                           |
+====================+=======================================================================+
| View               | | Users can view resources and their properties, to which they are    |     
|                    | | assigned                                                            |
+--------------------+-----------------------------------------------------------------------+
| Modify             | | Users can view and modify resources and their properties, to which  | 
|                    | | they are assigned, including adding, deleting and edit option       |
+--------------------+-----------------------------------------------------------------------+
| Not listed         | | Specifies that the permission type is not granted for the object.   |
|                    |                                                                       |
|                    | | User can not view or make any changes to the resources, if they are |
|                    | | not assigne to him.                                                 |
+--------------------+-----------------------------------------------------------------------+

To learn more about Role resources please find :doc:`Role resources </userguide/getting_started/settings/role_resources>` section

.. warning::

    Remember that many resources are located in several sections within the Open Loyalty platform. 
    
    **For example**
    
    the level details and their creation is done in the "Levels" section, but in the "Customers" sections there is also the possibility of preview and editing the assigned level.


.. tip::

    **When assigning resources, be sure to include all sections containing resources to which user should have an access. Otherwise, users will not be able to modify or view them all.**


Users roles management
------------------------

To edit a Role:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /userguide/_images/role_edit.PNG
   :alt:   Role edition mode

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **ACL**. 

.. |settings| image:: /userguide/_images/icon.png

2.	In the Roles list, find the record to be edited and click **Edit** icon |edit|  in the Action column to open the role in edit mode.	

.. |edit| image:: /userguide/_images/edit.png

3. Make any necessary changes to role details. **If you change resources, make sure they have been assigned correctly**

   You can simply remove permission by clicking bin |bin| icon in a particular row 

.. |bin| image:: /userguide/_images/bin.png


To remove a Role:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also delete existing role from the Admin.

.. warning:: 

    Default **Super admin** role can not be deleted 
    

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **ACL**. 

.. |settings| image:: /userguide/_images/icon.png

2. In the Roles list, find the record to be deleted and click **Remove** icon |remove| in the Action column to delete the role

.. |remove| image:: /userguide/_images/remove.png

3. System display a message asked you to confirm the action. To confirm tap ``Yes``

.. image:: /userguide/_images/remove_role.PNG
   :alt:   Removing Role Action


4. When complete, tap ``SAVE``


.. warning::

    When removing role, be sure to don't delete role which is currently assigned to any user.  
    
    **Otherwise, user will not be able to login to Admin Cockpit** 
