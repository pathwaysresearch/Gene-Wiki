---
type: concept
aliases: [Importance Weighted Autoencoder]
summary: An extension of the Variational Autoencoder framework that uses a different training objective based on an average of multiple samples to provide a tighter bound on the log-likelihood.
relationships:
  - target: variational-autoencoder
    type: extends
tags: [generative-models, autoencoders, objective-functions]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Importance Weighted Autoencoder

## Definition
The Importance Weighted Autoencoder (Burda et al., 2015) is an extension of the Variational Autoencoder (VAE) framework. It is trained by maximizing a different objective function than the traditional variational lower bound.

## Objective Function
The objective function for the importance weighted autoencoder, denoted $\mathcal{L}_k$, is defined as the expectation over $k$ samples from the approximate posterior $q(z|x)$ of the log of an average of importance weights. The objective is given by: $\mathcal{L}_k(x, q) = \mathbb{E}_{z^{(1)},...,z^{(k)}\sim q(z|x)} \left[ \log \frac{1}{k} \sum_{i=1}^{k} \frac{p_{\text{model}}(x, z^{(i)})}{q(z^{(i)} | x)} \right]$.

## Relationship to VAEs
This objective provides a new way to train models within the VAE framework. When the number of samples $k$ is set to 1, the importance weighted objective $\mathcal{L}_1$ becomes equivalent to the traditional variational lower bound $\mathcal{L}$ used in standard VAEs. Using $k > 1$ generally provides a tighter bound on the true log-likelihood.

## Relationships

- **extends**: [[variational-autoencoder|Variational Autoencoder]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*