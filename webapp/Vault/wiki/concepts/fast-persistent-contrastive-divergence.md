---
type: concept
aliases: [Fast Persistent Contrastive Divergence (FPCD)]
summary: An enhancement to Persistent Contrastive Divergence (PCD) that accelerates the mixing of Markov chains during learning by using two sets of parameters: one that learns slowly and another that adapts rapidly.
relationships:
  - target: stochastic-maximum-likelihood-persistent-contrastive-divergence
    type: is_an_enhancement_of
tags: [mcmc, model-training, optimization, undirected-models]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Fast Persistent Contrastive Divergence (FPCD)

## Core Idea
Fast Persistent Contrastive Divergence (FPCD) is a technique designed to accelerate the mixing of the MCMC chains used in PCD. Instead of modifying the sampling technology itself, FPCD alters the model's parameterization and the cost function.

## How It Works
The model's parameters, θ, are replaced by the sum of two components: θ = θ(slow) + θ(fast). Both sets of parameters are learned, but the 'fast' parameters are trained with a much larger learning rate. This allows them to change rapidly in response to the negative phase of learning, effectively pushing the Markov chain into new regions of the state space and forcing it to mix more quickly.

## Implementation Details
Typically, the fast weights are regularized with significant weight decay. This encourages them to take on large values only transiently to aid mixing, before converging to small values. This rapid mixing effect is primarily active during the learning process while the fast weights are free to change.

## Relationships

- **is_an_enhancement_of**: [[stochastic-maximum-likelihood-persistent-contrastive-divergence|Stochastic Maximum Likelihood Persistent Contrastive Divergence]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*