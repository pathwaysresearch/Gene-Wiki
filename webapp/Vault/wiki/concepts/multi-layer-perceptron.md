---
type: concept
aliases: [Multi-Layer Perceptron (MLP)]
summary: An artificial neural network architecture composed of an input layer, one or more hidden layers of Threshold Logic Units (TLUs), and an output layer, capable of solving non-linearly separable problems like XOR.
relationships:
  - target: perceptron
    type: extends
  - target: artificial-neural-network
    type: is_a_type_of
  - target: backpropagation
    type: is_trained_by
tags: [neural-networks, deep-learning, ann-architectures]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Multi-Layer Perceptron (MLP)

## Architecture
A Multi-Layer Perceptron (MLP) is an Artificial Neural Network formed by stacking multiple Perceptrons. Its structure consists of one passthrough input layer, one or more layers of Threshold Logic Units (TLUs) known as hidden layers, and a final layer of TLUs called the output layer.

## Overcoming Perceptron Limitations
The primary advantage of an MLP over a single Perceptron is its ability to solve more complex, non-linear problems. While a single Perceptron is limited to learning linearly separable patterns, an MLP can model non-linear relationships. A classic demonstration of this capability is its ability to solve the XOR problem, which a single Perceptron cannot.

## Solving the XOR Problem
The text illustrates how an MLP can solve the XOR classification problem. By using a hidden layer, the network can create a non-linear decision boundary. For inputs (0, 0) or (1, 1), the example network outputs 0, and for inputs (0, 1) or (1, 0), it outputs 1, correctly implementing the XOR function through a specific configuration of connection weights.

## Relationships

- **extends**: [[perceptron|Perceptron]]
- **is_a_type_of**: [[artificial-neural-network|Artificial Neural Network]]
- **is_trained_by**: [[backpropagation|Backpropagation]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*