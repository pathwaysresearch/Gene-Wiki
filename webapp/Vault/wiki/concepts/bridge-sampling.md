---
type: concept
aliases: [Bridge Sampling]
summary: A method for estimating the ratio of partition functions between two distributions by introducing an intermediate 'bridge' distribution that has significant overlap with both.
relationships:
  - target: importance-sampling
    type: is_related_to
  - target: annealed-importance-sampling
    type: is_an_alternative_to
  - target: partition-function
    type: is_used_to_estimate
tags: [approximate-inference, monte-carlo, sampling]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Bridge Sampling

## Definition
Bridge sampling is a method for estimating the ratio of partition functions between two distributions, $p_0$ and $p_1$. It is particularly effective when the Kullback-Leibler divergence between the two distributions, $D_{KL}(p_0||p_1)$, is not too large, allowing a single intermediate 'bridge' distribution $p_*$ to effectively span the gap between them. If the distributions are too far apart, Annealed Importance Sampling (AIS) may be a more suitable choice.

## How It Works
The core strategy of bridge sampling is to choose a bridge distribution $p_*$ that has a large overlap of support with both $p_0$ and $p_1$. By using this intermediate distribution, bridge sampling can provide a more effective and lower-variance estimate of the partition function ratio compared to standard importance sampling, especially when the two target distributions are not very close.

## Optimal Bridge and Iterative Refinement
The optimal bridging distribution, $p_*^{(opt)}$, is a function of the unnormalized densities of $p_0$ and $p_1$ and the very ratio of partition functions, $r = Z_1/Z_0$, that one is trying to estimate. While this appears to be a circular dependency, it can be resolved through an iterative process. One can begin with a coarse estimate of the ratio $r$, use it to define a bridge distribution, and then use that bridge to generate a refined estimate of $r$. This process can be repeated to improve the estimate.

## Relationships

- **is_related_to**: [[importance-sampling|Importance Sampling]]
- **is_an_alternative_to**: [[annealed-importance-sampling|Annealed Importance Sampling]]
- **is_used_to_estimate**: [[partition-function|Partition Function]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*