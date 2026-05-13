---
type: entity
aliases: [Adaptive Linear Element (ADALINE)]
summary: A single-layer neural network model from the 1960s that could learn to predict a real-valued number from data using a special case of stochastic gradient descent.
relationships:
  - target: cybernetics
    type: is_a
tags: [neural-network-model, history-of-ai]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Adaptive Linear Element (ADALINE)

## Overview
The Adaptive Linear Element (ADALINE), which dates from around 1960, was developed by Bernard Widrow and Tedd Hoff. It was another key model from the early cybernetics era of neural network research.

## Functionality
Unlike the perceptron which was used for classification, ADALINE was designed to predict a real number. It did this by returning the value of the linear function $f(x)$ itself. Like the perceptron, it could also learn its predictive parameters from data.

## Learning Algorithm
The training algorithm used to adapt the weights of the ADALINE was a special case of an algorithm called stochastic gradient descent. This learning rule was highly influential and became a foundational component of modern machine learning and deep learning.

## Relationships

- **is_a**: [[cybernetics|Cybernetics]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*