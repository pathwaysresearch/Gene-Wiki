---
type: concept
aliases: [Kalman Filter]
summary: A recursive algorithm for estimating the state of a dynamic system from a series of noisy measurements, assuming linear dynamics and Gaussian noise. An optimal recursive algorithm for estimating the state of a linear dynamic system from a series of noisy measurements.
relationships:
  - target: extended-kalman-filter
    type: is-extended-by
  - target: dynamic-bayesian-network
    type: is-a-specific-type-of
  - target: particle-filtering
    type: related_to
tags: [probabilistic-reasoning, state-estimation, filtering, linear-gaussian-model, time-series-analysis, control-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Kalman Filter

## Definition and Assumptions
The Kalman filter is a model for temporal probabilistic reasoning over systems with continuous state variables. Its core assumptions are that the system's transition and sensor models are linear Gaussian distributions. This means the next state is a linear function of the current state plus Gaussian noise, and sensor readings are a linear function of the current state plus Gaussian noise. A key consequence of these assumptions is that the state distribution is always represented as a single multivariate Gaussian distribution.

## How It Works
The filter operates through a cycle of prediction and update. The general temporal model involves a linear transformation with additive Gaussian noise for both state transitions and sensor readings. The transition model is defined as P(X_t+1|X_t) = N(Fx_t, Σ_x)(x_t+1) and the sensor model as P(Z_t|X_t) = N(Hx_t, Σ_z)(z_t), where F and H are matrices for the linear transformations. The mathematical property that allows the filter to work is that the exponent of a Gaussian distribution is a quadratic form; multiplying and integrating Gaussians preserves this quadratic form, resulting in another Gaussian. This is often solved using a technique known as completing the square.

## Applications and Limitations
Kalman filtering is applied to problems like tracking the position and velocity of a moving object, such as a bird in flight. However, its assumptions are very strong and limit its applicability. Because it can only represent the state as a single Gaussian "bump," it cannot model multi-modal distributions. For example, it would be unsuitable for tracking the location of a set of keys that could be in one of several distinct places (e.g., pocket, table, car), as a single Gaussian covering all these locations would assign high probability to impossible intermediate locations, like in mid-air.

## Relationships

- **is-extended-by**: [[extended-kalman-filter|Extended Kalman Filter]]
- **is-a-specific-type-of**: [[dynamic-bayesian-network|Dynamic Bayesian Network]]
- **related_to**: [[particle-filtering|Particle Filtering]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*