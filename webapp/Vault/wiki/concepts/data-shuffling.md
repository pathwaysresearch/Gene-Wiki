---
type: concept
aliases: [Data Shuffling]
summary: A data processing technique used in machine learning to randomize the order of instances in a training set, which is beneficial for optimization algorithms like Gradient Descent.
relationships:
  - target: tensorflow-data-api
    type: implemented_in
tags: [data-preprocessing, tensorflow, tf-data]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Data Shuffling

## Purpose in Machine Learning

Data shuffling is a critical step in preparing a training set for models optimized with Gradient Descent. The algorithm works best when the training instances are independent and identically distributed (IID). Shuffling the dataset is a simple and effective way to ensure this property, which helps the model converge more effectively.

## How It Works in TensorFlow

In the TensorFlow Data API, shuffling is performed using the `shuffle()` method on a dataset. This method operates by filling a buffer of a specified size with the initial items from the source dataset. When an item is requested for training, one is pulled randomly from the buffer. The vacated spot in the buffer is then filled with the next item from the source dataset. This process continues until the source dataset is exhausted, after which items are drawn randomly from the buffer until it is empty.

## Key Considerations

The effectiveness of the shuffle operation depends heavily on the buffer size. It is important to make the buffer large enough to ensure a thorough randomization of the data. However, the buffer size should not exceed the available RAM. There is no benefit to making the buffer significantly larger than the dataset itself.

## Relationships

- **implemented_in**: [[tensorflow-data-api|Tensorflow Data Api]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*