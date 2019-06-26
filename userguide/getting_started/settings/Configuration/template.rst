.. index::
   single: template 

Template
========

Template management determines the logo, as well as the other content elements e.g. fonts, headers, colors, that are used for all pages within Open Loyalty. 

.. image:: /userguide/_images/template.png
   :alt:   Template

The content is formatted with CSS, and can be easily edited and customizes by adding variables and another content element. You can make a color theme on the frontend using your primary color (Accent color). 
 
To customize your template:
'''''''''''''''''''''''''''

1. In the upper-right corner, tap the **Settings** icon |settings| . Then on the menu, choose **Configuration**. 

.. |settings| image:: /userguide/_images/icon.png


2. Scroll down to **Template** section and do the following:

  - In **Accent color**, define your primary color indicator. Accent color is the color displayed most frequently across your Loyalty Program screens and components. Only Hexadecimal color values are supported.
  - In the **CSS template** box, enter the CSS code as needed. The content consists of a combination of CSS directives, variables, and text

.. image:: /userguide/_images/content.png
   :alt:   Content management
  
| One of the first things you’ll want to do is to change the logo in the header above the menu. Your logo can be saved as either a **PNG, JPG, or JPEG** file type, and uploaded from the Admin of your Open Loyalty. 
| The default Open Loyalty logo in the sample data is a PNG file. During upload, Logo and Small logo images will be automatically resized to applicable versions. 

| In addition, you can also add an oversized banner image, called **Hero image**, that will be placed on a login page. Hero image is the first visual element a customer’s encounters on your site. 

.. image:: /userguide/_images/logo.png
   :alt:   Logo in Header Menu

.. note::

    **Images sizing and formats**:
    
     - The minimum and maximum image width is between 200-2560 pixels (except small logo)
     - The minimum and maximum image height is between 200 – 1440 pixels (except small logo)
     - The size of any one image must not exceed 2 MB 
     - Supported image formats: JPEG, JPG, PNG

   
To upload your logo:
''''''''''''''''''''

1. In the same **Template** section tap ``Upload`` on selected fields to do the following:

  - In **Logo** field, to import logo image that will be displayed on desktop version in Admin cockpit. Then choose the file from your computer- In **Big logo** field, to import logo image that will be displayed on desktop version in Client Cockpit. Then choose the file from your computer
  - In **Small logo** field, to import logo image that will be displayed on mobile version in Client Cockpit. Then choose the file from your computer
  - In **Hero image** field, to import an image that will be displayed as a banner on login page in Client Cockpit
  - You can simply remove uploaded logo by taping ``Remove``  
  
  
.. image:: /userguide/_images/logo2.png
   :alt:   Logo Updating
   
2. When complete, tap ``SAVE``

+--------------------------+-------------------------------------------------------------------------------------------------+
|   Field                  |  Description                                                                                    |
+==========================+=================================================================================================+
|   Logo                   | | Main logo image in the Admin cockpit placed in the header above the menu.                     |
|                          | | Image is display on desktop version of application.                                           |
|                          | | Applicable image size: 512 x 512 pixels                                                       |
+--------------------------+-------------------------------------------------------------------------------------------------+
|   Big logo               | | Big logo image in the Client cockpit placed above login credentials section on a login page.  |
|                          | | Image is display on desktop version of application in Client Cockpit.                         | 
|                          | | Applicable image size: 512 x 512 pixels                                                       |
+--------------------------+-------------------------------------------------------------------------------------------------+
|   Small logo             | | Small logo image in the Client cockpit placed above login credentials section on a login page.|
|                          | | Small image is display on mobile version of application in Client Cockpit.                    |
|                          | | It can be also used as an icon of the application on the mobile device.                       |
|                          | | Applicable image size: 192 x 192 pixels                                                       |
+--------------------------+-------------------------------------------------------------------------------------------------+
|   Hero image             | | Large web banner image placed on a Client Cockpit login page in the front.                    |
|                          | | Hero image is the first visual element a customer’s encounters on the site                    |
|                          | | and display on mobile and desktop versions.                                                   |
+--------------------------+-------------------------------------------------------------------------------------------------+ 
	
