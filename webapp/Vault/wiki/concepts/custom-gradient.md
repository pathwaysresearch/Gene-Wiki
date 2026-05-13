---
type: concept
aliases: [Custom Gradient (@tf.custom_gradient)]
summary: A TensorFlow decorator (`@tf.custom_gradient`) that allows a user to define a custom, numerically stable gradient function for an operation where automatic differentiation might fail or be inefficient.
relationships:
  - target: tf-gradient-tape
    type: modifies_behavior_of
tags: [tensorflow, automatic-differentiation, numerical-stability]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Custom Gradient (@tf.custom_gradient)

## Definition
The `@tf.custom_gradient` decorator in TensorFlow allows a developer to override the standard gradient computation provided by automatic differentiation for a specific function. This is particularly useful when the analytical derivative of a function is known and is more numerically stable or efficient than what autodiff would compute.

## Problem Solved
Automatic differentiation can sometimes lead to numerical difficulties due to floating-point precision errors, especially for functions involving exponentials with large inputs. The text uses the `softplus` function as an example, where autodiff can compute infinity divided by infinity, resulting in a `NaN` (Not a Number) gradient. By providing a custom gradient, these numerical instabilities can be avoided.

## Implementation
To use this feature, a function is decorated with `@tf.custom_gradient`. This decorated function must return two values: first, its normal output, and second, a nested function that defines how to compute the gradients. This gradient function receives the upstream gradients (the gradients backpropagated so far) as an argument. According to the chain rule, it should multiply these upstream gradients by the local gradient of the function to correctly propagate the gradients backward.

## Relationships

- **modifies_behavior_of**: [[tf-gradient-tape|Tf Gradient Tape]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*