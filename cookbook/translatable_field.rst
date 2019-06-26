How to create a translatable field
==================================

Translatable fields let you store objects' data in several languages. If you have a translatable field and want to retrieve the data you saved in a given language you have to pass a request parameter named _locale to the API endpoint, with locale code given defined in the admin panel.

Let’s say you want to add a translatable field containing a brand name to the API. To do that, add a translatable field type to the form:

.. code-block:: php

    <?php
        $builder->add('translations', TranslationsType::class, [
            'required' => true,
            'fields' => [
                'brandName' => [
                    'field_type' => TextType::class,
                ],
            ],
        ]);


Next, we need to create a mapping for entity translation. Because brandName is a field of Campaign objects, we create a CampaignTranslation entity. Here is a Doctrine definition:

.. code-block:: yaml

    OpenLoyalty\Domain\Campaign\CampaignTranslation:
      type: entity
      fields:
        brandName:
          type: text
          nullable: true
          column: brand_name

and entity class body with FallbackTranslation trait:

.. code-block:: php
    <?php

    class CampaignTranslation
    {
        use FallbackTranslation;

        /**
         * @var string|null
         */
        private $brandName;

        /**
         * @return null|string
         */
        public function getBrandName(): ?string
        {
            return $this->brandName;
        }

        /**
         * @param null|string $brandName
         */
        public function setBrandName(?string $brandName): void
        {
            $this->brandName = $brandName;
        }
    }

Next we need to add FallbackTranslatable trait in the \OpenLoyalty\Domain\Campaign\Campaign class

.. code-block:: php
    class Campaign
    {
        use FallbackTranslatable;
    ...

and modify setFromArray method if it exists:

.. code-block:: php
    if (array_key_exists('translations', $data)) {
        foreach ($data['translations'] as $locale => $transData) {
            if (array_key_exists('brandName', $transData)) {
                $this->translate($locale, false)->setBrandName($transData['brandName']);
            }
        }
        /** @var CampaignTranslation $translation */
        foreach ($this->getTranslations() as $translation) {
            if (!isset($data['translations'][$translation->getLocale()])) {
                $this->removeTranslation($translation);
            }
        }
    }

You also need to add translation setters and getters, which will be responsible for modifying and returning the translated data

.. code-block:: php

    /**
     * @return string|null
     */
    public function getBrandName(): ?string
    {
        return $this->translateFieldFallback(null, 'brandName')->getBrandName();
    }

    /**
     * @param string|null $brandName
     */
    public function setBrandName(?string $brandName): void
    {
        $this->translate(null, false)->setBrandName($brandName);
    }

