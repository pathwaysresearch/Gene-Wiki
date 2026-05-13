---
type: entity
aliases: [TensorFlow Features API]
summary: A TensorFlow API designed to facilitate the conversion of various types of raw features, such as text and categorical data, into numerical formats suitable for neural networks.
relationships:
  - target: tensorflow-data-api
    type: works_with
tags: [tensorflow, feature-engineering, data-preprocessing]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# TensorFlow Features API

## Overview
The TensorFlow Features API is a component of the TensorFlow ecosystem that helps manage and preprocess diverse types of input features. It addresses the common need to convert raw data, which is often not in a purely numerical format, into a representation that can be fed into a neural network.

## Feature Conversion
The API provides tools to handle various feature types. For example, it can process text features and categorical features. A key capability highlighted in the text is its ability to handle categorical features with a large number of categories (e.g., cities or words) by encoding them using embeddings. An embedding is a trainable, dense vector that represents a specific category, allowing the model to learn meaningful relationships between categories.

## Ecosystem Integration
The Features API is designed to work in concert with other parts of TensorFlow. It complements the TensorFlow Data API, which handles the efficient loading and streaming of data, by providing the tools to perform the necessary feature-specific transformations within the data pipeline. This allows for a complete and robust solution for handling real-world data.

## Relationships

- **works_with**: [[tensorflow-data-api|Tensorflow Data Api]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*