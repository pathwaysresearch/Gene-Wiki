---
type: concept
aliases: [Mixing Time]
summary: The number of steps a Markov chain must run to be sufficiently close to its stationary (equilibrium) distribution.
relationships:
  - target: markov-chain-monte-carlo-methods
    type: is_property_of
tags: [mcmc, markov-chains, computational-statistics]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Mixing Time

## Definition
In the context of Markov Chain Monte Carlo methods, the mixing time is the duration, or number of steps, required for the Markov chain to effectively converge to its equilibrium distribution. It represents the "burn-in" period after which samples drawn from the chain can be considered approximate samples from the target distribution.

## Theoretical Basis
The convergence of a Markov chain is governed by the eigenvalues of its transition matrix $\boldsymbol{A}$. The Perron-Frobenius theorem guarantees a unique largest eigenvalue of 1, corresponding to the stationary distribution. The mixing time is determined by the magnitude of the second-largest eigenvalue; the smaller this magnitude, the faster the chain converges or "mixes," as the influence of other eigenvalues diminishes exponentially with each step.

## Practical Challenges
In practice, especially for probabilistic models in deep learning, the state space is exponentially large, making it computationally infeasible to represent the transition matrix $\boldsymbol{A}$ or compute its eigenvalues. Consequently, the theoretical mixing time cannot be calculated. Practitioners must instead run the chain for a time they estimate to be sufficient and use heuristic methods, such as manually inspecting samples or measuring correlations between successive samples, to diagnose whether the chain appears to have mixed.

## Relationships

- **is_property_of**: [[markov-chain-monte-carlo-methods|Markov Chain Monte Carlo Methods]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*