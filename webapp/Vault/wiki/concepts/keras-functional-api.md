---
type: concept
aliases: [Keras Functional API]
summary: A way to create complex Keras models, such as those with multiple inputs or outputs, by connecting layers as if they were functions.
relationships:
  - target: keras
    type: is_part_of
  - target: wide-and-deep-neural-network
    type: enables
  - target: auxiliary-output
    type: enables
tags: [keras, api, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Keras Functional API

## Overview
The Keras Functional API is a powerful method for building neural network models that provides greater flexibility than the simpler Sequential API. It is essential for creating complex architectures, such as Wide & Deep networks, models with multiple inputs and outputs, or models with shared layers.

## How It Works
Building a model with the Functional API begins with creating an `Input` object, which defines the shape of the input data. Subsequent layers (e.g., `Dense`, `Concatenate`) are instantiated and then immediately called like functions, passing the output of a previous layer as their input. This process explicitly defines the graph of connections between layers. The model is finalized by creating a `keras.models.Model` instance and specifying its overall inputs and outputs.

## Key Feature
A defining characteristic of the Functional API is its declarative nature; it is used to describe how layers should be connected before any data is processed. This approach enables the construction of non-linear model topologies, which are not possible with a simple sequential stack of layers.

## Relationships

- **is_part_of**: [[keras|Keras]]
- **enables**: [[wide-and-deep-neural-network|Wide And Deep Neural Network]]
- **enables**: [[auxiliary-output|Auxiliary Output]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*