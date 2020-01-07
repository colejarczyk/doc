.. index::
   single: level_delete

Deleting customer level
=======================

The levels created in OpenLoyalty are not supposed to change a lot, but if one or more of them is no longer needed,
there is a possibility to remove them.

To remove a level:

1. Navigate to the levels list. On the Admin sidebar, tap **Levels**.

2. Find the level to remove.

3. In the **Actions** column, use ``[x]`` button to show the delete level modal.

4. Confirm deletion by tapping ``YES``.

.. note::

    The level's data may still be present in the database (entity is soft deleted), but will not display in the admin panel or be returned from API.
    Currently there is no possibility to revert the deletion action without editing the database.
