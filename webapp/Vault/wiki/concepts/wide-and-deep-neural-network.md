---
type: concept
aliases: [Wide and Deep Neural Network]
summary: A neural network architecture that combines a deep path (stacked layers) with a wide path that connects some inputs directly to the output layer.
relationships:
  - target: keras-functional-api
    type: implemented_using
  - target: relu
    type: uses
tags: [neural-network-architecture, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Wide and Deep Neural Network

## Architecture Overview
A Wide and Deep Neural Network is a hybrid architecture that processes information through two parallel paths. The "deep" path consists of a series of hidden layers (e.g., `Dense` layers with ReLU activation) that learn complex and abstract feature interactions. The "wide" path bypasses these hidden layers and connects some or all of the original input features directly to the final output layer, allowing the model to also learn simpler rules directly.

## Implementation
This architecture is well-suited for implementation with the Keras Functional API. The process involves creating an `Input` layer that is fed into the deep path. A `Concatenate` layer is then used to merge the output of the deep path with the original input layer. This combined tensor is subsequently fed into the final output layer to produce the prediction.

## Use Case Example
The text demonstrates building a Wide and Deep network to address the California housing regression problem. In this example, the model takes input features, passes them through two hidden `Dense` layers, and then concatenates the original input with the output of the second hidden layer before feeding the result to a single-neuron output layer.

## Relationships

- **implemented_using**: [[keras-functional-api|Keras Functional Api]]
- **uses**: [[relu|Relu]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*