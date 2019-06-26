How to create a translatable field
==================================

Let’s say you want to add translatable field with named brand name. To form add translatable field type:

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


Next we need to create an mapping for entity translation. Because brandName is depend to campaign so we crete CampaignTranslation entity.

.. code-block:: yaml

    OpenLoyalty\Component\Campaign\Domain\CampaignTranslation:
      type: entity
      fields:
        brandName:
          type: text
          nullable: true
          column: brand_name

and entity class:

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

Next in \OpenLoyalty\Component\Campaign\Domain\Campaign class we need to modify setFromArray method

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

and add translation too set/get method

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

