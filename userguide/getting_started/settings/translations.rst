.. index::
   single: translations 

Translations
============

The Translations section allows defining many language versions used throughout the Open Loyalty platform in both, Client cockpit and Admin cockpit. All content elements will appear in the selected **default language**. 

Most of the text that appears to be hard-coded on pages throughout your loyalty platform can be instantly changed to a different language by changing the default language parameter. The Default language is selected at the translation creation process but can be changed at any time in edition mode.

Moreover, during Reward campaigns and Levels creation/edition processes admin can fulfill Basic Information section in every language version listed here. For example, if we have Polish and English translations, there is a possibility to provide Basic information of Levels and Reward Campaign in this both languages. 

Thanks to this,  changing the default language translate the text word-for-word and references a different translation table that provides the interface text that is used in the Admin and Client cockpit. The text that can be changed includes navigational titles, labels, buttons, and links such as "List of customers" and "Account", Reward campaigns and Levels name, description etc. 

**Currently, Open Loyalty is available in two languages: English and Polish**.  


.. image:: /userguide/_images/translation.png
   :alt:   Translations Lists

   
   
Create new translations
-----------------------

You can create and versions your loyalty platform in multiple languages. You can have only one default language at a time. 

.. tip::

    Before adding new translations, copy existing content in JSON and paste into new one. 
	 
    It helps you to include all content elements that should be translated and keep JSON format of a file.


To add new translation:
^^^^^^^^^^^^^^^^^^^^^^^

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Translations**. 

.. |settings| image:: /userguide/_images/icon.png

2. To add a new translation, tap ``Create new translations``

.. image:: /userguide/_images/button.png
   :alt:   Add new translation button

.. image:: /userguide/_images/add.png
   :alt:   New Translations Form

3. Enter a **Code (locale)** in lowercase characters to identify the language. For example: de

4. Enter a **Name** for the translations. For example: German

5. Enter a sort **Order** number to determine the sequence in which the translation is listed on a Translations list 

6. To set translation as a main language within the platform, mark **Default** checkbox

7. In **Content** field, for each text to be edited either paste or type the translated text into the field. The translated text is marked in green.
   Text in an editor must be valid JSON.
   
8. When complete, tap ``SAVE``

9. Repeat the process for all language version used in the Open Loyalty

.. code-block:: text

    Content field is available in two JSON format: 
   
    - Format JSON data, with proper indentation and line feeds 
    - Compact JSON data, remove all whitespaces 


Field description
*****************

+--------------------------+-------------------------------------------------------------------------------------+
|   Field                  |  Description                                                                        |
+==========================+=====================================================================================+
|   Code (locale)          | | Language identifier                                                               |
+--------------------------+-------------------------------------------------------------------------------------+
|   Name                   | | Language name                                                                     |
+--------------------------+-------------------------------------------------------------------------------------+
|   Updated at             | | Date of last language version modification                                        |
+--------------------------+-------------------------------------------------------------------------------------+
|   Default                | | Information which language is default.                                            |
|                          | | **Options include: Yes/No**                                                       |
+--------------------------+-------------------------------------------------------------------------------------+
|   Actions                | | The operations that can be applied to selected translations.                      |
|                          | | Options include:                                                                  |
|                          |                                                                                     |
|                          |     - Edit translation                                                              |
|                          |     - Remove translation                                                            |
|                          | | **Note** – there is not possible to remove default language version               |
+--------------------------+-------------------------------------------------------------------------------------+




Updating translation:
---------------------

You can edit all data provided during translation creation process (except Code locale), including change the default language to another. You can update translation data by selecting its record from **Translations list**.

.. image:: /userguide/_images/edit_translation.png
   :alt:   Translation Editing mode

To edit a translation:
^^^^^^^^^^^^^^^^^^^^^^

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Translations**

.. |settings| image:: /userguide/_images/icon.png

2.	In the **Translations list**, find the record to be edited and click **Edit** icon |edit|  in the Action column to open the record in edit mode	

.. |edit| image:: /userguide/_images/edit.png

3. Make any necessary changes to the translated text

4. When complete, tap ``SAVE``


.. note::

    Date of last translation modification will be displayed in the **Translations list** grid in the **Updated at** column


   
To change the default language:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Translations** 

.. |settings| image:: /userguide/_images/icon.png

2.	In the **Translations list**, find the language to be set as default and click **Edit** icon |edit|  in the Action column to open the record in edit mode	

.. |edit| image:: /userguide/_images/edit.png

3. Mark **Default** checkbox

4. When complete, tap ``SAVE``


.. note::

    Date of last translation modification and selected as default will be displayed in the **Translations list** grid. 
