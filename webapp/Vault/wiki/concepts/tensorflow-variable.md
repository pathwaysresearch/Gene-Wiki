---
type: concept
aliases: [TensorFlow Variable]
summary: A special tensor-like object in TensorFlow used to hold mutable state, such as the weights and biases of a machine learning model.
relationships:
  - target: tensorflow
    type: core_component_of
  - target: tensor-tensorflow
    type: related_to
tags: [data-structure, tensorflow, model-parameters]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# TensorFlow Variable

## Definition and Purpose
A `tf.Variable` is a data structure that stores a value that can be changed during a computation. Unlike a regular `tf.Tensor`, which is immutable, a variable's primary purpose is to hold and update model parameters throughout training. It behaves like a tensor in most operations and is compatible with NumPy.

## In-Place Modification
The state of a `tf.Variable` can be modified in place using several methods. The `assign()` method replaces the variable's value entirely, while `assign_add()` and `assign_sub()` perform incremental updates. It is also possible to modify specific cells or slices of a variable using methods like `scatter_nd_update()` or by calling `assign()` on a slice.

## Usage in Keras
In practice, developers rarely create `tf.Variable` objects manually. High-level APIs like Keras manage them automatically. For example, when creating a custom layer, the `add_weight()` method is used within the `build` step to create the necessary trainable variables (weights and biases) for that layer. Optimizers then handle the process of updating these variables during training.

## Relationships

- **core_component_of**: [[tensorflow|Tensorflow]]
- **related_to**: [[tensor-tensorflow|Tensor Tensorflow]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*