---
type: concept
aliases: [Partition Function]
summary: A normalization constant in many probabilistic models that ensures the total probability sums to one, but is often computationally intractable to compute or differentiate. The normalizing constant in an unnormalized probability model, often denoted Z(θ), which ensures the distribution sums or integrates to one. Its computation is often intractable, posing a major challenge in training and evaluating many deep learning models.
relationships:
  - target: positive-and-negative-phase
    type: is_central_to
  - target: contrastive-divergence
    type: is_approximated_by
  - target: noise-contrastive-estimation
    type: is_circumvented_by
  - target: score-matching
    type: is_circumvented_by
tags: [probabilistic-models, statistical-mechanics, machine-learning, undirected-models, normalization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Partition Function

## Definition and Role
The partition function is a normalizing constant that appears in the definition of many probabilistic models. Its purpose is to ensure that the probability distribution is valid by making the sum (or integral) over all possible configurations of the variables equal to one. This constant comes up during both inference and learning.

## Computational Intractability
A major challenge with many probabilistic models is that computing the partition function is intractable, as it requires summing over all possible values of certain variables. This intractability extends to the learning process, because training such models often requires computing the gradient of the logarithm of the partition function with respect to model parameters, a task that is generally as difficult as computing the function itself.

## Approaches to Handling Intractability
One way to confront the intractability of the partition function is to use approximation methods. Monte Carlo Markov chain (MCMC) methods are frequently used for this purpose, either to approximate the function or its gradient. However, MCMC methods have their own limitations, especially in high-dimensional spaces with numerous, well-separated modes. Another approach is to design models that avoid such intractable computations altogether.

## Relationships

- **is_central_to**: [[positive-and-negative-phase|Positive And Negative Phase]]
- **is_approximated_by**: [[contrastive-divergence|Contrastive Divergence]]
- **is_circumvented_by**: [[noise-contrastive-estimation|Noise Contrastive Estimation]]
- **is_circumvented_by**: [[score-matching|Score Matching]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*