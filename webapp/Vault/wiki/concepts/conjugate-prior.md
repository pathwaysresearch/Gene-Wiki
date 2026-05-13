---
type: concept
aliases: [Conjugate Prior]
summary: A family of prior distributions for a parameter where the posterior distribution also belongs to the same family after observing data, simplifying Bayesian updates.
relationships:
  - target: bayesian-learning
    type: is-a-technique-in
  - target: beta-distribution
    type: is-an-example-of
tags: [bayesian-statistics, probabilistic-models, prior-distribution]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Conjugate Prior

## Definition
A conjugate prior is a family of probability distributions that is "closed under update." This property means that if the prior distribution for a model's parameter belongs to a conjugate family, then the posterior distribution, after incorporating new data, will also belong to the same family. This significantly simplifies the process of Bayesian inference.

## Example: The Beta Distribution
The text highlights the Beta distribution as the conjugate prior for the family of distributions for a Boolean variable. For instance, if the parameter $\theta$ representing the proportion of cherry candies has a prior distribution beta$[a, b]$, then after observing a new candy, the posterior distribution for $\theta$ is also a Beta distribution, just with updated hyperparameters. The hyperparameters $a$ and $b$ can be thought of as representing prior beliefs or 'virtual' counts of observations.

## Significance in Bayesian Learning
The use of conjugate priors makes Bayesian updates computationally tractable. Instead of performing complex integration to find the posterior, the update simplifies to a straightforward algebraic manipulation of the distribution's hyperparameters. The text notes that other conjugate families exist, such as the Dirichlet family for discrete multivalued distributions and the Normal-Wishart family for the parameters of a Gaussian distribution.

## Relationships

- **is-a-technique-in**: [[bayesian-learning|Bayesian Learning]]
- **is-an-example-of**: [[beta-distribution|Beta Distribution]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*