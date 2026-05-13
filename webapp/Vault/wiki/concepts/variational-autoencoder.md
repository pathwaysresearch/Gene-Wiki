---
type: concept
aliases: [Variational Autoencoder]
summary: A deep generative model that uses a generator network paired with a learned approximate inference network, trainable with gradient-based methods. A generative model that learns a latent representation of data by combining an autoencoder architecture with principles from variational inference.
relationships:
  - target: differentiable-generator-network
    type: uses
  - target: deep-recurrent-attention-writer
    type: is_a_type_of
  - target: variational-rnn
    type: is_a_type_of
  - target: importance-weighted-autoencoder
    type: is_extended_by
  - target: autoencoder
    type: is_a
  - target: generative-model
    type: is_a
  - target: evidence-lower-bound
    type: uses
tags: [generative-models, autoencoders, approximate-inference, generative-model, unsupervised-learning, variational-inference]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Variational Autoencoder

## Definition
The Variational Autoencoder (VAE), developed by Kingma (2013) and Rezende et al. (2014), is a directed generative model that employs learned approximate inference. It is structured around a differentiable generator network that maps latent variables to data space, and it can be trained end-to-end using gradient-based optimization methods.

## Architecture and Generation Process
A VAE pairs a generator network with an inference network. To generate a sample, the model first draws a latent code $z$ from a prior distribution, $p_{\text{model}}(z)$. This code is then passed through the differentiable generator network $g(z)$ to produce the parameters for a distribution over the data space, from which the final sample $x$ is drawn.

## Key Properties and Extensions
A key advantage of the VAE framework is its flexibility and straightforward extensibility to a wide range of model architectures, unlike models like Boltzmann machines which require careful design for tractability. VAEs have been successfully combined with recurrent networks to create models like the Deep Recurrent Attention Writer (DRAW) and Variational RNNs for sequence generation. The framework has also been extended with objectives like the importance weighted autoencoder, which generalizes the standard variational lower bound. VAEs are effective at learning low-dimensional representations of high-dimensional data manifolds, as demonstrated by their ability to map faces and MNIST digits to 2-D latent spaces where axes correspond to meaningful variations like rotation or emotional expression.

## Relationships

- **uses**: [[differentiable-generator-network|Differentiable Generator Network]]
- **is_a_type_of**: [[deep-recurrent-attention-writer|Deep Recurrent Attention Writer]]
- **is_a_type_of**: [[variational-rnn|Variational Rnn]]
- **is_extended_by**: [[importance-weighted-autoencoder|Importance Weighted Autoencoder]]
- **is_a**: [[autoencoder|Autoencoder]]
- **is_a**: [[generative-model|Generative Model]]
- **uses**: [[evidence-lower-bound|Evidence Lower Bound]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*