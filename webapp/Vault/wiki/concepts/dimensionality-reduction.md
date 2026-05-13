---
type: concept
aliases: [Dimensionality Reduction]
summary: A data preprocessing technique used to simplify data by reducing the number of input variables or features without losing significant information.
relationships:
  - target: feature-extraction
    type: includes_method
tags: [machine-learning, data-preprocessing, unsupervised-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Dimensionality Reduction

## Goal
The primary goal of dimensionality reduction is to simplify data while retaining as much meaningful information as possible. This is often done before feeding the data into another machine learning algorithm, such as a supervised learning model.

## Methods
One common approach to dimensionality reduction is to merge several correlated features into a single new feature. For instance, a car's mileage and age, which are often highly correlated, could be combined into one feature representing the car's overall 'wear and tear'. This specific method is known as feature extraction.

## Practical Benefits
Applying dimensionality reduction can significantly improve the performance and efficiency of machine learning models. It leads to faster training times, and the reduced dataset takes up less disk and memory space.

## Relationships

- **includes_method**: [[feature-extraction|Feature Extraction]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*