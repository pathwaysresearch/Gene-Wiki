---
type: entity
aliases: [TensorFlow Data API]
summary: A TensorFlow API (`tf.data`) for building efficient, flexible, and scalable input pipelines for machine learning models. A TensorFlow API, accessed via `tf.data`, for building efficient, flexible, and scalable input pipelines for machine learning models.
relationships:
  - target: tensorflow-features-api
    type: works_with
  - target: data-shuffling
    type: provides
  - target: data-interleaving
    type: provides
  - target: data-prefetching
    type: provides
tags: [tensorflow, data-pipeline, data-preprocessing, api, etl]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# TensorFlow Data API

## Overview
The TensorFlow Data API, commonly referred to as `tf.data`, is a core TensorFlow library designed to handle the challenges of data loading and preprocessing for machine learning models. It provides a flexible and efficient way to build input pipelines, which is especially critical when working with datasets that are too large to fit into memory.

## Core Functionality
The primary purpose of the Data API is to create efficient data pipelines. It allows developers to read from various data sources and apply complex transformations to the data. This helps in preparing the data for consumption by a neural network in a streamlined and performant manner.

## Integration with Keras
The Data API is designed to integrate seamlessly with `tf.keras`. Models built with Keras can be trained directly on `tf.data.Dataset` objects, which are the central abstraction of the API. This tight integration simplifies the process of feeding large and complex datasets into Keras models for training and evaluation.

## Relationships

- **works_with**: [[tensorflow-features-api|Tensorflow Features Api]]
- **provides**: [[data-shuffling|Data Shuffling]]
- **provides**: [[data-interleaving|Data Interleaving]]
- **provides**: [[data-prefetching|Data Prefetching]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*