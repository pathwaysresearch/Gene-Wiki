---
type: concept
aliases: [Switching Kalman Filter]
summary: A hybrid dynamic model for continuous-state systems that switch unpredictably among a set of distinct behavioral 'modes.'
relationships:
  - target: kalman-filter
    type: is-a-variant-of
  - target: mixture-of-gaussians
    type: produces
tags: [hybrid-dynamic-model, filtering, state-estimation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Switching Kalman Filter

## Definition and Application
A switching Kalman filter is a Bayesian network model used to monitor a continuous-state system whose behavior switches unpredictably among a set of *k* distinct 'modes.' An example application is tracking an aircraft that executes a series of different maneuvers to evade a missile.

## Probabilistic Representation
The model's dynamics lead to a specific form for the state distribution. If the prior continuous state estimate is a multivariate Gaussian distribution, the predicted state after one time step becomes a mixture of Gaussians. Specifically, if there are *k* possible modes, the prediction will be a mixture of *k* Gaussians.

## Computational Complexity
A key challenge with switching Kalman filters is the unbounded growth of the posterior representation. If the state estimate at time *t* is a mixture of *m* Gaussians, the updated estimate at time *t+1* will generally be a mixture of *km* Gaussians. This exponential growth in the number of mixture components means the representation of the posterior grows without limit, making exact inference intractable over long time horizons.

## Relationships

- **is-a-variant-of**: [[kalman-filter|Kalman Filter]]
- **produces**: [[mixture-of-gaussians|Mixture Of Gaussians]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*