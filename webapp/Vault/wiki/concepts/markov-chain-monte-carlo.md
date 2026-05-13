---
type: concept
aliases: [Markov Chain Monte Carlo (MCMC)]
summary: A class of algorithms for approximate inference that draws samples from a probability distribution by simulating a Markov chain whose stationary distribution is the desired distribution.
relationships:
  - target: markov-chain
    type: uses
  - target: gibbs-sampling
    type: is-a-type-of
  - target: approximate-inference
    type: is-a-method-for
tags: [bayesian-networks, approximate-inference, sampling, simulation, statistics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Markov Chain Monte Carlo (MCMC)

## Overview
Markov Chain Monte Carlo (MCMC) is a family of algorithms used for inference by simulation, particularly in complex probabilistic models like Bayesian networks. Instead of generating independent samples from scratch, MCMC methods generate a sequence of states where each state is sampled based on the previous one.

## Core Principle
The central idea is to construct a Markov chain over the state space of the network's variables. This chain is defined by a transition probability and is designed such that its stationary or equilibrium distribution is the true posterior probability distribution P(X|e) that is the target of the inference query. After running the chain for a sufficient number of steps, subsequent states can be treated as samples from this desired distribution.

## Application in Bayesian Networks
In the context of Bayesian networks, MCMC algorithms like Gibbs sampling provide a powerful method for approximate inference. They work by iteratively transitioning from one complete assignment of values to the network's variables to another, eventually producing a collection of samples that reflects the true posterior distribution, from which probabilities can be estimated by counting.

## Relationships

- **uses**: [[markov-chain|Markov Chain]]
- **is-a-type-of**: [[gibbs-sampling|Gibbs Sampling]]
- **is-a-method-for**: [[approximate-inference|Approximate Inference]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*