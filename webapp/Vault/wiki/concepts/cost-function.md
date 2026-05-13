---
type: concept
aliases: [Cost Function]
summary: A function that measures the performance of a machine learning model by quantifying the error between the model's predictions and the actual target values.
relationships:
  - target: model-based-learning
    type: is_used_by
tags: [machine-learning, optimization, model-training]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Cost Function

## Purpose in Training
A cost function is used to measure how 'bad' a model is performing on the training data. The primary goal of the training process in model-based learning is to find the set of model parameters that minimizes the value of this cost function.

## Application Example
For linear regression problems, a typical cost function measures the distance between the linear model’s predictions and the actual training data points. A lower cost signifies that the model's predictions are closer to the real values.

## Alternative Performance Measures
The cost function is one of two main ways to specify a performance measure. The alternative is a utility function, also known as a fitness function, which measures how 'good' a model is. In practice, minimizing a cost function is a more common approach.

## Relationships

- **is_used_by**: [[model-based-learning|Model Based Learning]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*