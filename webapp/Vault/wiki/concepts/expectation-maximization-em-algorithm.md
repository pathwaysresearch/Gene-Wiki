---
type: concept
aliases: [Expectation-Maximization (EM) Algorithm]
summary: An iterative method for finding maximum likelihood estimates of parameters in probabilistic models, particularly when the model depends on unobserved latent variables.
relationships:
  - target: mixture-of-gaussians
    type: used-to-learn
  - target: learning-bayesian-network-structure-with-hidden-variables
    type: used-in
tags: [optimization-algorithm, machine-learning, statistical-inference, latent-variables]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Expectation-Maximization (EM) Algorithm

## Overview
The Expectation-Maximization (EM) algorithm is an iterative optimization technique used to find maximum likelihood parameters for statistical models with hidden or latent variables. It resembles a gradient-based hill-climbing algorithm but is distinct in that it has no "step size" parameter to tune.

## Key Properties
A fundamental property of the EM algorithm is that it increases the log likelihood of the observed data at every iteration, as illustrated in Figure 20.12. Under typical conditions, the algorithm is proven to converge to a local maximum in likelihood, although in rare cases it could find a saddle point or local minimum. The final learned model may have a slightly higher log likelihood than the true underlying model from which data was generated, which reflects the random nature of the data sample.

## How It Works
The algorithm alternates between two steps until convergence. In the Expectation (E) step, it calculates the expected values or counts of the hidden variables, given the current parameter estimates and the observed data. For instance, in a naive Bayes model with a hidden 'Bag' variable, this involves computing the probability that each observed candy came from a specific bag. In the Maximization (M) step, it updates the model parameters to maximize the likelihood of the data, using the expected counts of the hidden variables calculated in the E-step.

## Relationships

- **used-to-learn**: [[mixture-of-gaussians|Mixture Of Gaussians]]
- **used-in**: [[learning-bayesian-network-structure-with-hidden-variables|Learning Bayesian Network Structure With Hidden Variables]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*