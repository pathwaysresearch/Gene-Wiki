---
type: concept
aliases: [Annealed Importance Sampling]
summary: A method for estimating the ratio of two partition functions by using a sequence of intermediate distributions to bridge the gap between a simple and a complex distribution.
relationships:
  - target: importance-sampling
    type: is_an_extension_of
  - target: bridge-sampling
    type: is_an_alternative_to
  - target: partition-function
    type: is_used_to_estimate
tags: [approximate-inference, monte-carlo, sampling]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Annealed Importance Sampling

## Definition
Annealed Importance Sampling (AIS) is a strategy developed to estimate partition functions for complex, high-dimensional distributions. It is an advanced form of importance sampling designed to overcome the high variance that occurs when the proposal distribution and the target distribution are not close. It is particularly useful when a single distribution cannot effectively bridge the gap between a simple starting distribution and the complex target distribution.

## How It Works
AIS constructs a path of many intermediate distributions that gradually transition from a simple distribution $p_0$ (with a known partition function $Z_0$) to the complex target distribution $p_1$. It generates samples by starting from $p_0$ and using a Markov chain transition operator to move through the sequence of intermediate distributions. The final importance weight for each sample is calculated by chaining together the importance weights for the jumps between each consecutive intermediate distribution in the sequence.

## Estimating the Partition Function Ratio
With the importance weights $w^{(k)}$ calculated for a set of $K$ samples, the ratio of the partition functions $Z_1/Z_0$ is estimated by taking the average of these weights. To maintain numerical stability and avoid issues like overflow or underflow, it is recommended to compute the logarithm of the weights by adding and subtracting log probabilities rather than multiplying and dividing raw probabilities. The validity of AIS is established by showing it is equivalent to simple importance sampling on an extended state space.

## Relationships

- **is_an_extension_of**: [[importance-sampling|Importance Sampling]]
- **is_an_alternative_to**: [[bridge-sampling|Bridge Sampling]]
- **is_used_to_estimate**: [[partition-function|Partition Function]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*