---
type: concept
aliases: [Probabilistic Max Pooling]
summary: A pooling technique for energy-based models that constrains detector units so at most one can be active, making the normalization constant tractable.
relationships:
  - target: pooling
    type: is_a
  - target: energy-based-model
    type: used_in
tags: [pooling, convolutional-networks, energy-based-model]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Probabilistic Max Pooling

## Problem Addressed
In deep convolutional energy-based models, standard pooling operations like max pooling are difficult to generalize. A naive implementation, such as enforcing a pooling unit \(p = \max_i d_i\) by assigning infinite energy to constraint violations, is computationally intractable. For a small \(3 \times 3\) pooling region with \(n=9\) binary detector units, this would require evaluating \(2^9 = 512\) energy configurations just to compute the normalization constant for a single pooling unit.

## How It Works
Probabilistic max pooling, developed by Lee et al. (2009), solves this problem by constraining the detector units so that at most one may be active at any given time. This dramatically reduces the state space. For \(n\) detector units, there are only \(n+1\) possible states: one state for each of the \(n\) units being on individually, and one state where all units are off.

## Implementation
The pooling unit is defined to be 'on' if and only if one of the detector units is 'on'. The state where all detector units are off is assigned an energy of zero. This constraint simplifies the computation of the partition function, making pooling feasible within the energy-based model framework. It should not be confused with 'stochastic pooling,' which is a different technique.

## Relationships

- **is_a**: [[pooling|Pooling]]
- **used_in**: [[energy-based-model|Energy Based Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*