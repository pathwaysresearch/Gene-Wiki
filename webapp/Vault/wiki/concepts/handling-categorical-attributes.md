---
type: concept
aliases: [Handling Categorical Attributes]
summary: The process of converting non-numerical, categorical data, such as text labels, into a numerical format that can be used by most machine learning algorithms.
relationships:
  - target: data-preprocessing
    type: is_a_part_of
tags: [data-preprocessing, feature-engineering, encoding]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Handling Categorical Attributes

## The Need for Encoding
Most Machine Learning algorithms are designed to work with numbers, not text. Therefore, categorical attributes, such as the `ocean_proximity` feature in the housing dataset which contains text values like '<1H OCEAN' and 'INLAND', must be converted into a numerical representation before they can be fed into a model.

## Ordinal Encoding with Scikit-Learn
One method for this conversion is ordinal encoding, which maps each unique category to a different integer. The text demonstrates this using Scikit-Learn’s `OrdinalEncoder` class. An instance of the encoder is created, then its `fit_transform()` method is called on the categorical data. This process both learns the unique categories and transforms them into corresponding numerical values.

## Accessing Learned Categories
After the `OrdinalEncoder` has been fit to the data, it stores the list of unique categories it found. This mapping can be accessed via the `categories_` instance variable. This is useful for inspecting which integer corresponds to which original text category, allowing for better interpretation of the transformed data.

## Relationships

- **is_a_part_of**: [[data-preprocessing|Data Preprocessing]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*