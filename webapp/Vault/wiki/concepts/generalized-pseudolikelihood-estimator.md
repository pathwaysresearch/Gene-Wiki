---
type: concept
aliases: [Generalized Pseudolikelihood Estimator]
summary: An objective function for training probabilistic models that provides a trade-off between the computational complexity of full maximum likelihood and the statistical inefficiency of standard pseudolikelihood.
relationships:
  - target: maximum-likelihood-estimation
    type: is_an_alternative_to
tags: [model-training, objective-function, probabilistic-models, approximate-inference]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Generalized Pseudolikelihood Estimator

## Definition
The generalized pseudolikelihood estimator is an objective function that involves maximizing the sum of log conditional probabilities over different subsets of variables. The objective is given by Σᵢ log p(x_S(i) | x_-S(i)), where S(i) are different sets of variable indices. This formulation allows it to interpolate between two extremes: if there is only one set S containing all variables, it recovers the full log-likelihood; if there are n sets, each containing a single variable, it recovers the standard pseudolikelihood.

## Trade-offs
This method allows a user to trade computational complexity for a deviation from the behavior of maximum likelihood. By choosing the size and number of the index sets S, one can control the balance between computational cost and the quality of the model approximation.

## Performance and Applications
The performance of pseudolikelihood-based approaches is highly dependent on the intended use of the model. They tend to perform poorly on tasks requiring a good model of the full joint distribution, such as density estimation or sampling. However, they can outperform maximum likelihood on tasks that rely on the specific conditional distributions used during training, such as filling in small amounts of missing data. They are particularly powerful when the data has a regular structure that allows the index sets to be designed to capture the most important correlations.

## Relationships

- **is_an_alternative_to**: [[maximum-likelihood-estimation|Maximum Likelihood Estimation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*