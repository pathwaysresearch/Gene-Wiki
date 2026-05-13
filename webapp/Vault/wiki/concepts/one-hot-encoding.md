---
type: concept
aliases: [One-Hot Encoding]
summary: A method for representing categorical variables as binary vectors where only one element is 'hot' (1) and all others are 'cold' (0), indicating the presence of a specific category.
relationships:
  - target: embeddings-for-categorical-features
    type: alternative_to
  - target: tensorflow-feature-columns
    type: enabled_by
tags: [feature-engineering, data-preprocessing, tensorflow]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# One-Hot Encoding

## Definition

One-hot encoding is a process that converts categorical data into a numerical format that can be fed to a machine learning algorithm. It creates a binary vector for each category, with a length equal to the total number of categories in the vocabulary. The vector contains a '1' in the position corresponding to the specific category and '0's in all other positions.

## Implementation in TensorFlow

Within the TensorFlow Feature Column API, one-hot encoding is achieved by using `tf.feature_column.indicator_column`. This function takes a categorical column as input and produces the corresponding one-hot encoded vectors.

## Limitations and Use Cases

One-hot encoding is generally the recommended approach for categorical features with a small number of possible categories (e.g., fewer than 10). However, it becomes inefficient for large vocabularies. If a feature has many categories, the resulting one-hot vectors will be very high-dimensional and sparse (mostly zeros). This can lead to a neural network with an excessive number of weights to learn, which may hurt performance. In such cases, embeddings are a better alternative.

## Relationships

- **alternative_to**: [[embeddings-for-categorical-features|Embeddings For Categorical Features]]
- **enabled_by**: [[tensorflow-feature-columns|Tensorflow Feature Columns]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*