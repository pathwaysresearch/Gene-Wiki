---
type: concept
aliases: [Nesterov Momentum]
summary: A variant of the momentum optimization algorithm that improves convergence by calculating the gradient at a projected future position, effectively adding a correction factor to the update.
relationships:
  - target: momentum-optimization
    type: is_a_variant_of
  - target: nesterov
    type: is_inspired_by
  - target: sutskever-et-al-2013
    type: was_introduced_by
tags: [optimization-algorithm, gradient-descent]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Nesterov Momentum

## Definition
Nesterov Momentum, introduced by Sutskever et al. (2013), is a modification of the standard momentum algorithm inspired by Nesterov's accelerated gradient method. It aims to improve the quality of the parameter updates by being more "prescient" about the next step.

## Core Mechanism
The critical difference between Nesterov momentum and standard momentum lies in where the gradient is evaluated. Standard momentum calculates the gradient at the current parameter position. In contrast, Nesterov momentum first applies a "look-ahead" step based on the current velocity (`theta + alpha * v`) and then evaluates the gradient at this new, temporary position. This allows the algorithm to correct its course if the anticipated step is poor.

## Convergence Properties
This "correction factor" provides significant theoretical benefits in certain settings. For convex batch gradient problems, Nesterov's original method was shown to improve the convergence rate of the excess error from O(1/k) to O(1/k^2). However, the text notes that this theoretical advantage does not carry over to the stochastic gradient case commonly used in deep learning.

## Relationships

- **is_a_variant_of**: [[momentum-optimization|Momentum Optimization]]
- **is_inspired_by**: [[nesterov|Nesterov]]
- **was_introduced_by**: [[sutskever-et-al-2013|Sutskever Et Al 2013]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*