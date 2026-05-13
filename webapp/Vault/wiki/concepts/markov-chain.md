---
type: concept
aliases: [Markov Chain]
summary: A mathematical model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event.
relationships:
  - target: markov-chain-monte-carlo
    type: is-a-foundation-of
tags: [stochastic-processes, probability-theory, simulation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Markov Chain

## Definition
A Markov chain is a process on a state space defined by a transition probability, denoted q(x -> x'), which gives the probability that the process makes a transition from state x to state x'. The core property is that the future state depends only on the current state, not on the sequence of states that preceded it.

## State Distribution Over Time
The state of the system at a given time can be described by a probability distribution. Let π_t(x) be the probability that the system is in state x at time t. The distribution at the next time step, π_{t+1}(x'), can be calculated by summing, over all possible previous states x, the probability of being in state x at time t multiplied by the transition probability from x to x'.

## Application in MCMC
Markov chains are the foundational component of Markov Chain Monte Carlo (MCMC) methods for approximate inference. Algorithms like Gibbs sampling construct a Markov chain over the state space of a model's variables. The chain is specifically designed so that its long-run, stationary distribution is the target posterior probability distribution, allowing one to generate samples from this distribution by simulating the chain.

## Relationships

- **is-a-foundation-of**: [[markov-chain-monte-carlo|Markov Chain Monte Carlo]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*