---
type: concept
aliases: [Local Minima]
summary: A point in a non-convex cost function where the value is lower than at all nearby points, but not necessarily the lowest value globally, posing a potential obstacle for optimization.
relationships:
  - target: saddle-points
    type: related_to
tags: [optimization-challenge, non-convex-optimization, cost-function-landscape]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Local Minima

## Non-Problematic Local Minima
In neural networks, a vast number of local minima can arise from model non-identifiability. For example, in rectified linear or maxout networks, one can scale the incoming weights and biases of a unit by a factor α while scaling its outgoing weights by 1/α without changing the model's output. This creates entire families of equivalent parameter settings. These local minima are not considered a problematic form of non-convexity because they all share the same cost function value as each other.

## Problematic Local Minima
The primary concern for gradient-based optimization is the existence of local minima that have a high cost in comparison to the global minimum. If an algorithm becomes trapped in such a suboptimal minimum, the resulting model will have poor performance. The text notes that it is possible to construct small neural networks that possess these high-cost local minima, posing a serious potential problem for gradient-based methods.

## Relevance in Deep Learning
While theoretically possible, it remains an open question whether high-cost local minima are a common problem in practice for large, deep neural networks. Some theoretical work on shallow linear autoencoders showed that their loss functions have a global minimum and saddle points, but no local minima with higher cost. This suggests that for at least some classes of networks, other features of the optimization landscape, such as saddle points, may be a more significant obstacle.

## Relationships

- **related_to**: [[saddle-points|Saddle Points]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*