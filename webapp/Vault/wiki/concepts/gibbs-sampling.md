---
type: concept
aliases: [Gibbs Sampling]
summary: A Markov Chain Monte Carlo (MCMC) algorithm for approximate inference that generates a sequence of samples by iteratively sampling each variable from its conditional distribution given the current values of all other variables.
relationships:
  - target: markov-chain-monte-carlo-methods
    type: is_a
  - target: markov-chain-monte-carlo
    type: is-a-type-of
  - target: markov-blanket
    type: uses
tags: [bayesian-networks, approximate-inference, mcmc, algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Gibbs Sampling

## Definition
Gibbs sampling is a specific Markov Chain Monte Carlo (MCMC) algorithm used for obtaining a sequence of observations from a specified multivariate probability distribution when direct sampling is difficult. It is a common method for approximate inference in Bayesian networks.

## How It Works
The algorithm starts with a random assignment of values to all non-evidence variables. It then iterates through each non-evidence variable, one at a time, and resamples its value from its conditional probability distribution given the current values of all other variables (i.e., its Markov blanket). The process cycles through all non-evidence variables repeatedly. After many iterations, the state of the network can be treated as a fair sample from the posterior distribution, and counts are tallied to estimate probabilities.

## Theoretical Foundation
The correctness of Gibbs sampling relies on the property of detailed balance. The transition probability for each step of the sampler is constructed to be in detailed balance with the true posterior distribution. This property ensures that the stationary distribution of the Markov chain created by the sampling process is indeed the posterior distribution P(X|e) that is being sought, guaranteeing that the estimates will be consistent.

## Relationships

- **is-a-type-of**: [[markov-chain-monte-carlo|Markov Chain Monte Carlo]]
- **uses**: [[markov-blanket|Markov Blanket]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*