---
type: concept
aliases: [Maximum-Likelihood Parameter Learning]
summary: A method for parameter learning with complete data that finds the parameter values that maximize the likelihood of the observed data, P(data|hypothesis).
relationships:
  - target: statistical-learning
    type: is-a
  - target: learning-bayesian-network-structures
    type: is-used-in
tags: [parameter-estimation, machine-learning, statistics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Maximum-Likelihood Parameter Learning

## Definition
Maximum-likelihood parameter learning is a technique used in density estimation for finding the numerical parameters of a probability model whose structure is fixed. It operates under the assumption of complete data, where each data point contains values for every variable in the model. The method works by selecting the parameter values (the hypothesis) that make the observed data most probable.

## How It Works
The process involves writing an expression for the likelihood of the data as a function of the model's parameters. To simplify calculation, the logarithm of the likelihood (log-likelihood) is typically used, which converts products into sums. The derivatives of this log-likelihood function with respect to each parameter are then calculated, set to zero, and solved. The resulting parameter values are those that maximize the log-likelihood, and therefore the likelihood itself.

## Applications and Examples
This method is widely applicable to both discrete and continuous models. For a discrete model, such as estimating the proportion $\theta$ of cherry candies in a bag, the maximum-likelihood estimate for $\theta$ is the observed fraction of cherry candies. For a continuous Gaussian density function, the maximum-likelihood estimates for the mean $\mu$ and variance $\sigma^2$ are the sample average and the sample variance of the data, respectively. These results confirm that the method often aligns with commonsense statistical practices.

## Relationships

- **is-a**: [[statistical-learning|Statistical Learning]]
- **is-used-in**: [[learning-bayesian-network-structures|Learning Bayesian Network Structures]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*