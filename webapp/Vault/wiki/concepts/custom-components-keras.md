---
type: concept
aliases: [Custom Components (Keras)]
summary: A mechanism in Keras that allows developers to extend the framework by creating their own layers, loss functions, metrics, and other model components.
relationships:
  - target: keras
    type: feature_of
  - target: tensorflow-variable
    type: uses
tags: [keras, extensibility, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Custom Components (Keras)

## Overview
Keras provides a flexible framework for defining custom components when the built-in options are not sufficient. This allows for the implementation of novel research ideas or specialized business logic. Custom components can be created as simple functions or, for more complex stateful components, as classes that inherit from base Keras classes.

## Custom Functions and Metrics
Simple, stateless components like activation functions, initializers, regularizers, constraints, and basic loss functions can be implemented as plain Python functions that take and return tensors. For stateful metrics that need to be updated across batches (streaming metrics), one must create a class that inherits from `keras.metrics.Metric`, implementing `__init__`, `update_state`, and `result` methods to manage the metric's state using variables created with `add_weight`.

## Custom Layers
For creating new layers with trainable weights, developers must subclass `keras.layers.Layer`. The key methods to implement are `__init__` to define hyperparameters, `build` to create the layer's weights (variables) using `self.add_weight()`, and `call` to define the forward pass logic. To ensure the model can be saved and loaded, a `get_config` method should also be implemented to serialize the layer's hyperparameters.

## Relationships

- **feature_of**: [[keras|Keras]]
- **uses**: [[tensorflow-variable|Tensorflow Variable]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*