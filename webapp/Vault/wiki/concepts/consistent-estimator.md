---
type: concept
aliases: [Consistent Estimator]
summary: A statistical estimator whose value converges to the true value of the parameter being estimated as the sample size increases.
relationships:
  - target: likelihood-weighting
    type: is-a-property-of
tags: [statistics, estimation-theory, sampling]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Consistent Estimator

## Definition
In the context of sampling algorithms, an estimator is described as consistent if the estimated probability it produces becomes exact in the large-sample limit. This means that as the number of samples, N, approaches infinity, the estimate converges to the true value of the quantity being estimated.

## Application in Sampling
For approximate inference in Bayesian networks, consistency is a crucial property. An algorithm is consistent if the probability of an event, estimated as the fraction of samples matching that event, converges to the true probability as the number of samples grows. For example, the probability P(x1,...,xm) can be estimated by the ratio N_PS(x1,...,xm)/N, and this estimate is consistent.

## Significance
The property of consistency is used to formally prove the correctness of approximate inference algorithms. For instance, it is shown that likelihood weighting returns consistent estimates, meaning that given enough samples, it will provide an accurate approximation of the true posterior probability.

## Relationships

- **is-a-property-of**: [[likelihood-weighting|Likelihood Weighting]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*