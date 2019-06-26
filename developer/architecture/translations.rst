Translations
============

Open Loyalty supports multi language in interface (admin, customer panel) and user data (levels, campaigns, campaign categories).

Languages
---------
Administrator has possibility to manages available languages in Translations settings. One of these languages should be marked as default. Default languages in used to translate interface.

Translatable data
-----------------
Some entities like levels, campaigns and category campaign have build-in multi language support. Administrator can translate some fields using Open Loyalty administrator panel or API.

By default API returns data using default language, but user may change current language in API using ``_locale`` parameter passing to request. If some data in given language is not defined then fallback to default language approach will be used.
