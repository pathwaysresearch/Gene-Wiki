---
type: concept
aliases: [Differentiable Generator Network]
summary: A model that transforms samples of latent variables into data samples using a differentiable function, typically a neural network, forming the core of many deep generative models.
relationships:
  - target: variational-autoencoder
    type: is_a_component_of
  - target: generative-adversarial-network
    type: is_a_component_of
  - target: convolutional-generative-network
    type: is_a_specialization_of
tags: [generative-models, neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Differentiable Generator Network

## Definition
A differentiable generator network is a model that uses a differentiable function, $g(z; \theta^{(g)})$, to transform samples of latent variables $z$ into samples $x$ or distributions over $x$. This function is typically represented by a neural network, and the network's architecture defines the family of possible distributions while its parameters select a specific distribution from that family.

## How It Works
The network acts as a parametrized computational procedure for generating samples. For instance, a simple generator network can draw samples from a multivariate normal distribution by applying an affine transformation, $x = \mu + Lz$, to samples $z$ from a standard normal distribution, where $L$ is derived from the target covariance matrix's Cholesky decomposition. More complex models can use nonlinear transformations, such as inverse transform sampling.

## Role in Generative Modeling
Differentiable generator networks are a foundational component in many advanced generative models. They are paired with an inference network in Variational Autoencoders (VAEs), with a discriminator network in Generative Adversarial Networks (GANs), and can also be trained in isolation. Research has shown that contemporary generator networks possess sufficient capacity to be effective generative models, with the primary challenge lying in how to train them when the latent variables $z$ for each data point $x$ are unknown.

## Relationships

- **is_a_component_of**: [[variational-autoencoder|Variational Autoencoder]]
- **is_a_component_of**: [[generative-adversarial-network|Generative Adversarial Network]]
- **is_a_specialization_of**: [[convolutional-generative-network|Convolutional Generative Network]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*