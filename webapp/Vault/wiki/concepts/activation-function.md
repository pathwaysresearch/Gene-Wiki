---
type: concept
aliases: [Activation Function]
summary: In a neural network, a function `g` that is applied to the weighted sum of a unit's inputs to determine its output activation.
relationships:
  - target: feedforward-network
    type: component_of
  - target: artificial-neural-network
    type: is-a-component-of
  - target: perceptron
    type: is-used-by
  - target: logistic-regression
    type: is-used-by
tags: [neural-networks, non-linearity, function]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Activation Function

## Role in a Neural Network
The activation function is a core component of a neural network unit. After a unit computes the weighted sum of its inputs (`in_j`), the activation function `g` is applied to this sum to produce the unit's final output or activation: `a_j = g(in_j)`.

## Types
The text discusses two main types of activation functions. The first is a hard threshold, which results in a unit being called a perceptron. The second is a logistic function (or sigmoid), which creates a "soft" threshold and is used in models like sigmoid perceptrons and for logistic regression.

## Importance for Non-Linearity
The non-linearity of activation functions is what allows multi-layer neural networks to learn complex, non-linear patterns and decision boundaries. The text describes how nested non-linear soft threshold functions enable networks to perform non-linear regression by creating complex functional forms like ridges and bumps.

## Relationships

- **is-a-component-of**: [[artificial-neural-network|Artificial Neural Network]]
- **is-used-by**: [[perceptron|Perceptron]]
- **is-used-by**: [[logistic-regression|Logistic Regression]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*