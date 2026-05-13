---
type: concept
aliases: [Markov Chain Monte Carlo (MCMC) Methods]
summary: A class of algorithms for sampling from a probability distribution by constructing a Markov chain whose equilibrium distribution is the desired target distribution.
relationships:
  - target: monte-carlo-methods
    type: is_a
tags: [sampling-methods, mcmc, probabilistic-models, computational-statistics]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Markov Chain Monte Carlo (MCMC) Methods

## Rationale
MCMC methods are employed in situations where direct sampling from a target distribution $p_{\text{model}}(\mathbf{x})$ is intractable, and where it is also difficult to find a good, low-variance proposal distribution for importance sampling. This is a common scenario in deep learning, particularly with complex, high-dimensional models.

## How It Works
The core idea is to construct a Markov chain, a sequence of random states where the next state depends only on the current state. This chain is designed such that its stationary or equilibrium distribution is the target distribution $p_{\text{model}}(\mathbf{x})$. The process is defined by a transition operator $T$, which can be represented by a stochastic matrix $\boldsymbol{A}$. Repeatedly applying this operator causes the distribution over states to converge to the desired equilibrium, a property guaranteed by the Perron-Frobenius theorem for such matrices.

## Key Challenges
A major practical difficulty with MCMC is determining the **mixing time**—how many steps are needed for the chain to converge to its equilibrium distribution. Another significant problem is poor mixing between modes. If the target distribution has multiple modes of high probability separated by vast regions of low probability (high "energy barriers"), the chain can get stuck in one mode for a very long time, failing to explore the full distribution.

## Relationships

- **is_a**: [[monte-carlo-methods|Monte Carlo Methods]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*