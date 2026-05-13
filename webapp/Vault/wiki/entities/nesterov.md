---
type: entity
aliases: [Nesterov]
summary: A researcher who developed the accelerated gradient method that inspired the Nesterov Momentum algorithm used in deep learning.
relationships:
  - target: nesterov-momentum
    type: inspired
tags: [researcher, optimization-theory]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Nesterov

## Overview
Nesterov is a researcher known for his foundational work on accelerated gradient methods in convex optimization, with key publications cited from 1983 and 2004.

## Key Contribution
He developed what is known as Nesterov's accelerated gradient method. This method was shown to improve the rate of convergence for convex batch gradient problems, reducing the excess error from O(1/k) to O(1/k^2) after k steps, a significant theoretical improvement over standard gradient descent.

## Influence on Deep Learning
Nesterov's work directly inspired the Nesterov Momentum algorithm, which was introduced by Sutskever et al. (2013). This adaptation applied his ideas about accelerated gradients to the stochastic optimization setting commonly used for training deep neural networks.

## Relationships

- **inspired**: [[nesterov-momentum|Nesterov Momentum]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*