---
type: concept
aliases: [Backpropagation]
summary: A common algorithm for training Multi-Layer Perceptrons by iteratively processing mini-batches of data, using the chain rule to calculate and propagate error gradients backward through the network to update connection weights.
relationships:
  - target: stochastic-gradient-descent
    type: enables
  - target: deep-feedforward-network
    type: used_to_train
  - target: chain-rule
    type: is_an_application_of
  - target: multi-layer-perceptron
    type: is_training_method_for
tags: [neural-networks, training-algorithms, optimization, calculus]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Backpropagation

## Training Process
Backpropagation is an algorithm for training neural networks that operates by handling one mini-batch of instances at a time. The algorithm iterates through the full training set multiple times, with each complete pass being referred to as an epoch.

## Forward and Backward Passes
The algorithm is composed of two main phases. The first is the forward pass, where a mini-batch is fed to the input layer and the signal propagates forward through the network, layer by layer, until the output layer produces a prediction. All intermediate results from this pass are preserved. The second phase begins after the algorithm measures the network's output error using a loss function.

## Error Gradient Calculation
During the backward pass, the algorithm computes how much each connection in the output layer contributed to the total error by applying the calculus chain rule. It then works backward through the network, layer by layer, repeatedly using the chain rule to measure the error contributions from connections in the preceding layers. This reverse pass efficiently measures the error gradient across all connection weights, which is then used to update the weights in the network.

## Relationships

- **is_training_method_for**: [[multi-layer-perceptron|Multi Layer Perceptron]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*