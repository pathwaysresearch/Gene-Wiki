---
type: concept
aliases: [Hidden Markov Model (HMM)]
summary: A statistical model where the system is a Markov process with unobserved (hidden) states, which are inferred from a set of observable variables. A statistical model where the system being modeled is assumed to be a Markov process with unobserved (hidden) states, which are inferred from a set of observations. A statistical model where the system is a Markov process with unobserved (hidden) states, commonly used for modeling sequential or time-series data.
relationships:
  - target: markov-process
    type: is-a
  - target: filtering-in-temporal-models
    type: uses-algorithm
  - target: smoothing-in-temporal-models
    type: uses-algorithm
  - target: most-likely-sequence-finding
    type: uses-algorithm
  - target: dynamic-bayesian-network
    type: is-a-specific-type-of
  - target: em-algorithm
    type: uses
  - target: forward-backward-algorithm
    type: uses
tags: [temporal-models, state-space-models, machine-learning, probabilistic-reasoning, state-estimation, robotics, probabilistic-models, time-series, nlp]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Hidden Markov Model (HMM)

## Definition
A Hidden Markov Model (HMM) is a specific type of temporal model characterized by a single, discrete state variable `X_t` that is not directly observable (it is hidden). The state of the system evolves according to a Markov process. The hidden state at time `t` influences an observable evidence variable `E_t`, from which the state must be inferred.

## Matrix Representation of Models
For HMMs, the transition and sensor models can be represented concisely using matrices. The transition model `P(X_t | X_{t-1})` is an `S x S` matrix `T`, where `S` is the number of states and the entry `T_ij` is the probability of transitioning from state `i` to state `j`. For the umbrella world example, this matrix is `[[0.7, 0.3], [0.3, 0.7]]`.

## Sensor Model Matrix
The sensor model is also represented by a matrix for a given observation `e_t`. It is an `S x S` diagonal matrix, denoted `O_t`, where the `i`-th diagonal entry is the probability of observing `e_t` given that the system is in state `i`, i.e., `P(e_t | X_t = i)`. All off-diagonal entries are zero. This matrix form simplifies the computations for inference algorithms like filtering and smoothing.

## Relationships

- **is-a**: [[markov-process|Markov Process]]
- **uses-algorithm**: [[filtering-in-temporal-models|Filtering In Temporal Models]]
- **uses-algorithm**: [[smoothing-in-temporal-models|Smoothing In Temporal Models]]
- **uses-algorithm**: [[most-likely-sequence-finding|Most Likely Sequence Finding]]
- **is-a-specific-type-of**: [[dynamic-bayesian-network|Dynamic Bayesian Network]]
- **uses**: [[em-algorithm|Em Algorithm]]
- **uses**: [[forward-backward-algorithm|Forward Backward Algorithm]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*