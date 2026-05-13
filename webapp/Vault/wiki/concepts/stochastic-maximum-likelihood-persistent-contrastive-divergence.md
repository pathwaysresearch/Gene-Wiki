---
type: concept
aliases: [Stochastic Maximum Likelihood / Persistent Contrastive Divergence]
summary: A training method for undirected models that improves upon Contrastive Divergence by not re-initializing the MCMC chains at each gradient step. Instead, the chains persist across updates, allowing them to better explore the model's distribution.
relationships:
  - target: contrastive-divergence
    type: is_an_improvement_on
  - target: fast-persistent-contrastive-divergence
    type: is_a_basis_for
tags: [approximate-inference, mcmc, model-training, undirected-models]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Stochastic Maximum Likelihood / Persistent Contrastive Divergence

## Overview
Stochastic Maximum Likelihood (SML), independently rediscovered in the deep learning community as Persistent Contrastive Divergence (PCD), is an algorithm designed to resolve many of the problems associated with standard Contrastive Divergence (CD). The core idea is to maintain a persistent state for the Markov chains used to generate negative samples.

## How It Works
Unlike CD, which initializes a new Markov chain from a data point for each gradient calculation, PCD initializes the chains at each gradient step with their states from the end of the previous gradient step. This allows the chains to explore the model's state space more thoroughly over time, leading to a better approximation of the model's stationary distribution and a less biased estimate of the log-likelihood gradient, so long as the model parameters change slowly.

## Enhancements
The performance of SML/PCD can be further improved by incorporating more advanced MCMC techniques. For example, methods like parallel tempering can be used to enhance the mixing of the persistent Markov chains, leading to more effective training.

## Relationships

- **is_an_improvement_on**: [[contrastive-divergence|Contrastive Divergence]]
- **is_a_basis_for**: [[fast-persistent-contrastive-divergence|Fast Persistent Contrastive Divergence]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*