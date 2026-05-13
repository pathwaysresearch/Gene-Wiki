---
type: entity
aliases: [Sutskever et al. (2013)]
summary: A group of researchers who introduced a variant of the momentum algorithm inspired by Nesterov's accelerated gradient method in 2013.
relationships:
  - target: nesterov-momentum
    type: created
tags: [research-paper, authors]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Sutskever et al. (2013)

## Overview
Sutskever et al. are the researchers credited in a 2013 publication with introducing a specific and influential variant of the momentum optimization algorithm for use in deep learning.

## Contribution to Optimization
Their key contribution discussed in the text is the development of Nesterov Momentum. They adapted Nesterov's accelerated gradient method to create an update rule where the gradient is evaluated after the current velocity is applied, rather than before. This can be interpreted as adding a correction factor to the standard momentum update.

## Significance
This method provided a practical way to incorporate the ideas of Nesterov's accelerated gradient into the training of deep neural networks. While its theoretical convergence benefits from the convex case do not directly apply to stochastic optimization, it has been an empirically effective algorithm in many deep learning applications.

## Relationships

- **created**: [[nesterov-momentum|Nesterov Momentum]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*