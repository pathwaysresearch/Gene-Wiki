---
type: concept
aliases: [Regression MLP]
summary: A Multi-Layer Perceptron (MLP) architecture used for regression tasks to predict one or more continuous values.
relationships:
  - target: multi-layer-perceptron
    type: is_a
  - target: relu
    type: uses
tags: [neural-network-architecture, regression, mlp]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Regression MLP

## Definition
A Regression Multi-Layer Perceptron (MLP) is a neural network architecture configured for regression tasks, such as predicting the price of a house from its features. It is designed to predict continuous numerical values rather than discrete classes.

## Architecture
The structure of a regression MLP's output layer depends on the number of values being predicted. For univariate regression (predicting a single value), the network requires just a single output neuron. For multivariate regression, where multiple values are predicted simultaneously (e.g., 2D coordinates plus width and height for a bounding box), one output neuron is needed for each output dimension.

## Output Layer Configuration
In a typical regression MLP, the output neurons do not use any activation function. This allows them to be free to output any range of values, which is suitable for general regression problems. However, if the task requires the output to always be positive, the ReLU activation function can be used on the output layer to enforce this constraint.

## Relationships

- **is_a**: [[multi-layer-perceptron|Multi Layer Perceptron]]
- **uses**: [[relu|Relu]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*