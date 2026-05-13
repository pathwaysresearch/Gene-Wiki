---
type: concept
aliases: [L2 Regularization]
summary: A regularization technique that adds a penalty equal to the square of the magnitude of coefficients, which discourages large weights and helps prevent overfitting.
relationships:
  - target: l1-regularization
    type: is_an_alternative_to
tags: [regularization, overfitting, model-training]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# L2 Regularization

## Definition
L2 regularization is a common technique used to combat overfitting in machine learning models. It adds a penalty term to the loss function that is proportional to the sum of the squares of the model's weights. Unlike L1 regularization, it does not typically result in sparse models but rather encourages smaller weight values throughout the model.

## How It Works
During each training step, the regularizer is called to compute the regularization loss based on the current weights. This regularization loss is then added to the final loss that the optimizer seeks to minimize. This process incentivizes the optimizer to keep the weights small, which can lead to a more generalized model. It is a recommended technique for deep networks that may be overfitting the training set.

## Implementation in Keras
In the Keras framework, L2 regularization can be applied to the weights of a layer, such as a `Dense` layer, by passing a regularizer instance to the `kernel_regularizer` argument. The `keras.regularizers.l2()` function is used to create this instance, typically with a factor that controls the strength of the regularization, for example, `kernel_regularizer=keras.regularizers.l2(0.01)`. It can also be combined with L1 regularization by using `keras.regularizers.l1_l2()`.

## Relationships

- **is_an_alternative_to**: [[l1-regularization|L1 Regularization]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*