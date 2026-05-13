---
type: concept
aliases: [Gradient Clipping]
summary: A technique used during the training of neural networks to mitigate the exploding gradients problem by capping the gradients at a certain threshold.
tags: [optimization, deep-learning, exploding-gradients]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
relationships:
  - target: exploding-gradients
    type: mitigates
  - target: recurrent-neural-network
    type: used-for
---

# Gradient Clipping

## Definition

Gradient Clipping is a technique designed to lessen the problem of exploding gradients in neural networks. It works by imposing a maximum value, or threshold, on the gradients during the backpropagation phase of training.

## Mechanism

The core mechanism of Gradient Clipping is to simply clip the gradients during backpropagation so that they never exceed a predefined threshold. If a gradient's norm exceeds this threshold, it is scaled down to match the threshold, thereby preventing the weight updates from becoming excessively large and destabilizing the training process.

## Primary Application

While it can be used in various neural network architectures, the text notes that this technique is most frequently employed in recurrent neural networks (RNNs), which are particularly susceptible to the exploding gradients problem due to their sequential nature and repeated application of weight matrices.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*