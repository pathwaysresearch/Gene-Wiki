---
type: entity
aliases: [TensorFlow Feature Columns]
summary: A TensorFlow API (`tf.feature_column`) that provides a declarative way to represent and transform features, bridging raw data to the inputs required by a model.
relationships:
  - target: feature-bucketing
    type: implements
  - target: one-hot-encoding
    type: implements
  - target: embeddings-for-categorical-features
    type: implements
tags: [tensorflow, api, feature-engineering]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# TensorFlow Feature Columns

## Overview
The TensorFlow Feature Column API is a set of functions that serve as a bridge between raw data (such as columns in a CSV file or features in a dictionary) and the input layer of a model. They provide a declarative way to specify how each raw feature should be transformed before being fed into a neural network, handling common feature engineering tasks.

## Transforming Numerical Features
Feature columns can process numerical data directly using `tf.feature_column.numeric_column`. This function can also accept a `normalizer_fn` to apply transformations like standardization. Furthermore, continuous numerical features can be converted into categorical features through bucketization using `tf.feature_column.bucketized_column`, which groups values into predefined bins based on specified boundaries.

## Handling Categorical Features
The API offers several strategies for categorical data. For features with a small vocabulary, `tf.feature_column.indicator_column` can be used to generate one-hot encoded vectors. For features with a large vocabulary, such as those created by hash buckets, embeddings are a more suitable representation. Embeddings map categories to trainable, dense vectors, which is a more efficient representation for high-cardinality categorical features.

## Relationships

- **implements**: [[feature-bucketing|Feature Bucketing]]
- **implements**: [[one-hot-encoding|One Hot Encoding]]
- **implements**: [[embeddings-for-categorical-features|Embeddings For Categorical Features]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*