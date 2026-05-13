---
type: concept
aliases: [Momentum Optimization]
summary: An optimization algorithm that accelerates gradient descent by adding a fraction of the previous update vector to the current one, simulating physical momentum.
relationships:
  - target: stochastic-gradient-descent
    type: is_an_extension_of
  - target: boris-polyak
    type: created_by
tags: [optimization-algorithm, gradient-descent, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Momentum Optimization

## Core Idea

The central idea behind Momentum optimization is inspired by the physical concept of momentum, analogized to a bowling ball rolling down a gentle slope. The ball starts slowly but picks up momentum, allowing it to reach the bottom much faster than the small, regular steps taken by standard Gradient Descent. This method helps accelerate convergence, especially in areas with small but consistent gradients.

## Mechanism

Unlike regular Gradient Descent, which only considers the current local gradient to update weights, Momentum optimization incorporates information from previous gradients. It maintains a 'momentum vector' (m) that accumulates past gradients. At each iteration, the local gradient (multiplied by the learning rate) is subtracted from this momentum vector, and the weights are updated by adding the momentum vector. In this way, the gradient is used for acceleration rather than directly for speed.

## Historical Context

This optimization technique is not a recent invention. The text credits Boris Polyak with proposing Momentum optimization in 1964. It is presented as one of the most popular and foundational optimization algorithms, alongside more recent methods like AdaGrad, RMSProp, and Adam.

## Relationships

- **created_by**: [[boris-polyak|Boris Polyak]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*