---
type: concept
aliases: [L1 Regularization]
summary: A regularization technique that adds a penalty equal to the absolute value of the magnitude of coefficients, encouraging sparsity in the model by pushing many weights to exactly zero.
relationships:
  - target: l2-regularization
    type: is_an_alternative_to
  - target: follow-the-regularized-leader
    type: is_used_with
tags: [regularization, sparsity, model-training]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# L1 Regularization

## Definition
L1 regularization is a method used during model training to prevent overfitting and to create sparse models. It works by adding a penalty term to the loss function that is proportional to the sum of the absolute values of the model's weights.

## Key Property: Sparsity
The primary characteristic of L1 regularization is its tendency to produce sparse models, meaning that many of the model's parameters (weights) are driven to be exactly zero. This happens because the L1 penalty pushes the optimizer to zero out as many weights as it can. This property is highly desirable when a model needs to be fast at runtime or take up less memory.

## Applications and Implementation
A common application is in training sparse models, where it can be a more effective technique than simply zeroing out tiny weights after training. In Keras, L1 regularization can be applied to a layer by using `keras.regularizers.l1()` as the `kernel_regularizer`. It can also be combined with L2 regularization using `keras.regularizers.l1_l2()`. For achieving even greater sparsity, L1 regularization is often used in conjunction with the FTRL optimization algorithm.

## Relationships

- **is_an_alternative_to**: [[l2-regularization|L2 Regularization]]
- **is_used_with**: [[follow-the-regularized-leader|Follow The Regularized Leader]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*