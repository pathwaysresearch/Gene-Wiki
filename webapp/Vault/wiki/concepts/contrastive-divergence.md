---
type: concept
aliases: [Contrastive Divergence]
summary: An algorithm for training undirected probabilistic models that approximates the intractable negative phase of the log-likelihood gradient. It works by running a short Markov chain Monte Carlo (MCMC) simulation, initialized from a data point, to generate model samples.
relationships:
  - target: positive-and-negative-phase
    type: approximates
  - target: stochastic-maximum-likelihood-persistent-contrastive-divergence
    type: is_a_predecessor_to
  - target: score-matching
    type: is_related_to
tags: [approximate-inference, mcmc, model-training, undirected-models]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Contrastive Divergence

## How It Works
Contrastive Divergence (CD), specifically CD-k, provides an approximation to the negative phase gradient. Instead of running an MCMC chain until it converges to the model's stationary distribution, CD initializes the chain at a data point from the training set and runs it for only a small number of steps, k (e.g., 1-20 for an RBM). The sample obtained after k Gibbs steps is then used to compute an estimate of the negative phase gradient.

## Properties and Limitations
The CD update direction is not the gradient of any function, which means it is a biased estimator of the true log-likelihood gradient. This can lead to situations where the learning process could cycle, though this is not typically a serious problem in practice. The algorithm can be interpreted as penalizing the model for having a Markov chain that rapidly changes an input that comes from the data distribution, making it somewhat resemble autoencoder training.

## Applications
Despite its bias, CD is a useful training method, particularly for pretraining shallow models like Restricted Boltzmann Machines (RBMs) that will later be stacked to form a deep network. A side effect of CD training is that it encourages the initial layers to preserve more information from the input in their latent representations, which is beneficial for subsequent layers.

## Relationships

- **approximates**: [[positive-and-negative-phase|Positive And Negative Phase]]
- **is_a_predecessor_to**: [[stochastic-maximum-likelihood-persistent-contrastive-divergence|Stochastic Maximum Likelihood Persistent Contrastive Divergence]]
- **is_related_to**: [[score-matching|Score Matching]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*