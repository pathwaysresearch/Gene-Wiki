---
type: concept
aliases: [Universal Approximation Theorem]
summary: A theorem stating that a feedforward network with one hidden layer containing a "squashing" activation function can approximate any continuous function to any desired degree of accuracy. A foundational theorem in neural network theory stating that a feedforward network with a single hidden layer can approximate any continuous function to an arbitrary degree of accuracy.
relationships:
  - target: feedforward-neural-network
    type: applies_to
tags: [neural-networks, deep-learning-theory, feedforward-networks, neural-network-theory, mathematical-foundations, approximation-theory]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Universal Approximation Theorem

## Definition
The universal approximation theorem states that a feedforward network with a linear output layer and at least one hidden layer using any “squashing” activation function (such as the logistic sigmoid) can approximate any Borel measurable function from one finite-dimensional space to another with any desired non-zero amount of error.

## Conditions and Scope
The theorem's guarantee holds provided that the network is given a sufficient number of hidden units. The concept of Borel measurability is broad and includes any continuous function on a closed and bounded subset of $\mathbb{R}^n$. While originally stated for squashing activation functions, the theorem has since been proven for a wider class of activation functions. The theorem also extends to the derivatives of the function, which can also be approximated arbitrarily well by the network's derivatives.

## Significance
This theorem provides a key theoretical foundation for the expressive power of neural networks, establishing them as a universal approximation framework. It gives assurance that, in principle, a sufficiently large shallow network can represent a vast range of functions, removing the need to design specialized models for every type of nonlinearity one wishes to learn.

## Relationships

- **applies_to**: [[feedforward-neural-network|Feedforward Neural Network]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*