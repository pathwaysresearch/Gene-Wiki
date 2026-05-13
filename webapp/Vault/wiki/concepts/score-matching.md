---
type: concept
aliases: [Score Matching]
summary: A method for fitting unnormalized statistical models by minimizing an objective function based on the gradient of the log-density (the score), thereby avoiding the need to compute the partition function.
relationships:
  - target: partition-function
    type: is_a_method_to_avoid
  - target: contrastive-divergence
    type: is_related_to
tags: [model-training, objective-function, unnormalized-models]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Score Matching

## How It Works
Score matching provides an alternative to likelihood-based training. Instead of maximizing the probability of the data, it aims to match the model's score function (the gradient of the log probability with respect to the input data x) to the data's score function. This objective does not depend on the partition function, as the derivative of log Z(θ) with respect to x is zero.

## Limitations
The method has several key limitations. Because it requires taking derivatives with respect to the input data x, it is not applicable to models of discrete data. Furthermore, it is not compatible with models where the unnormalized log probability, log p̃(x), cannot be evaluated directly or where its derivatives are unavailable. This means it cannot be applied to models with complicated interactions between hidden units, like deep Boltzmann machines, and has not been used for pretraining deeper layers which often contain discrete variables.

## Relationship to Contrastive Divergence
Score matching can be viewed as a specific form of Contrastive Divergence. It is equivalent to CD in the case where the MCMC method is not Gibbs sampling but a different approach that makes local moves guided by the gradient of the log probability, and the size of these moves approaches zero.

## Relationships

- **is_a_method_to_avoid**: [[partition-function|Partition Function]]
- **is_related_to**: [[contrastive-divergence|Contrastive Divergence]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*