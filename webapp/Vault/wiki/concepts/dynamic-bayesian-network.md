---
type: concept
aliases: [Dynamic Bayesian Network]
summary: A Bayesian network that models the evolution of a set of random variables over time, providing a general framework for temporal probabilistic models.
relationships:
  - target: kalman-filter
    type: is-a-generalization-of
  - target: hidden-markov-model
    type: is-a-generalization-of
tags: [probabilistic-reasoning, bayesian-networks, temporal-models]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Dynamic Bayesian Network

## Definition and Construction
A Dynamic Bayesian Network (DBN) is a framework for probabilistic reasoning over time. To construct a DBN, one must specify three components: the prior distribution over the state variables, P(X_0); the transition model, P(X_t+1|X_t), which describes how the system evolves from one time step to the next; and the sensor model, P(E_t|X_t), which describes how observations relate to the system's state.

## Generality and Flexibility
DBNs are a generalization of simpler temporal models like Hidden Markov Models and Kalman filters. While every Kalman filter can be represented as a DBN with continuous variables and linear Gaussian distributions, not every DBN can be represented by a Kalman filter. The key advantage of DBNs is their ability to model arbitrary distributions, whereas a Kalman filter is restricted to representing the state as a single multivariate Gaussian. This flexibility is essential for many real-world applications that involve a mix of discrete and continuous variables or multi-modal state distributions.

## Applications
The flexibility of DBNs allows them to model complex scenarios that are intractable for simpler models. For example, a DBN can model a sensor that has a persistent failure mode. By including a discrete state variable like `BMBroken`, the model can reason about whether an unusual reading (e.g., a battery meter reading 0) is due to the battery actually being empty or the sensor itself being faulty. This allows for more robust inference compared to a simple Gaussian error model, which might incorrectly conclude the battery is empty after a transient sensor failure.

## Relationships

- **is-a-generalization-of**: [[kalman-filter|Kalman Filter]]
- **is-a-generalization-of**: [[hidden-markov-model|Hidden Markov Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*