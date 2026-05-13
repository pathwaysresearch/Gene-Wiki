---
type: concept
aliases: [Generalized Denoising Autoencoder]
summary: A type of denoising autoencoder for which a specific Markov chain can be constructed to draw samples from the distribution it estimates.
relationships:
  - target: walk-back-training-procedure
    type: trained_with
  - target: denoising-autoencoder
    type: is_a
  - target: markov-chain-monte-carlo
    type: uses
tags: [generative-model, autoencoder, sampling-method]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Generalized Denoising Autoencoder

## Definition
Generalized denoising autoencoders are a specific class of autoencoder models. They are notable because, unlike many other autoencoder variants, they are associated with a well-defined procedure for drawing samples from the data distribution they have learned.

## Sampling Method
Bengio et al. (2013c) demonstrated how to construct a specific Markov chain that can sample from any generalized denoising autoencoder. This allows the model to be used for generation, which is a key task for deep generative models. The sampling process typically involves an iterative procedure, such as the one illustrated for a Generative Stochastic Network (GSN) where parts of an image are resampled at each step of the chain.

## Associated Training Procedures
To be effective as generative models, denoising autoencoders can be trained with specialized procedures. The walk-back training procedure, for instance, was proposed to accelerate the convergence of the generative training of such models. This highlights that the model architecture is closely tied to the methods used for both training and sampling.

## Relationships

- **trained_with**: [[walk-back-training-procedure|Walk Back Training Procedure]]
- **is_a**: [[denoising-autoencoder|Denoising Autoencoder]]
- **uses**: [[markov-chain-monte-carlo|Markov Chain Monte Carlo]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*