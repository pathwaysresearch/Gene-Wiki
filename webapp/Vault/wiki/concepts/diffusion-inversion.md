---
type: concept
aliases: [Diffusion Inversion]
summary: A generative modeling training scheme based on non-equilibrium thermodynamics where a model learns to reverse a diffusion process that gradually destroys data structure.
relationships:
  - target: markov-chain-monte-carlo
    type: related_to
  - target: denoising-autoencoder
    type: related_to
tags: [generative-model, training-algorithm, thermodynamics]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Diffusion Inversion

## Overview and Origin
Diffusion inversion is a training scheme for learning a generative model, developed by Sohl-Dickstein et al. (2015). The approach is conceptually grounded in non-equilibrium thermodynamics and offers an alternative to more common generative approaches like MCMC or ancestral sampling.

## Mechanism
The core principle is to first define a diffusion process that gradually destroys the structure in a probability distribution, incrementally increasing its entropy until it becomes an unstructured distribution. A generative model is then trained to run this process in reverse. By iteratively applying a learned process that brings a distribution closer to the target data distribution, the model can start from an unstructured input and gradually restore the complex structure of the data, thereby generating a sample.

## Comparison to Other Methods
This iterative generation process resembles MCMC methods. However, a key distinction is that the model is defined to be the probability distribution produced by the final step of the chain, which means the iterative procedure does not introduce any approximation error. The text also notes that the diffusion inversion approach is conceptually very close to the generative interpretation of the denoising autoencoder, where noise is progressively removed to reconstruct a clean data point.

## Relationships

- **related_to**: [[markov-chain-monte-carlo|Markov Chain Monte Carlo]]
- **related_to**: [[denoising-autoencoder|Denoising Autoencoder]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*