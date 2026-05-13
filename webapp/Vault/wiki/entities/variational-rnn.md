---
type: entity
aliases: [Variational RNN]
summary: An extension of the VAE framework that uses a recurrent encoder and decoder to generate sequences, introducing stochasticity at the latent variable level.
relationships:
  - target: variational-autoencoder
    type: is_an_implementation_of
tags: [generative-model, vae, recurrent-networks, sequence-generation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Variational RNN

## Overview
The Variational RNN (Chung et al., 2015b) is a model that extends the Variational Autoencoder (VAE) framework to generate sequences. It achieves this by incorporating recurrent neural networks (RNNs) into the VAE structure.

## Architecture
The model is defined by using a recurrent encoder and a recurrent decoder within the VAE framework. This allows it to process and generate data with sequential dependencies.

## Key Characteristics
A key difference between a Variational RNN and a traditional RNN lies in the source of stochasticity. In a traditional RNN, non-deterministic operations typically occur only at the output space to generate a sample. In contrast, a Variational RNN introduces random variability at a potentially more abstract level, specifically through the VAE's latent variables, allowing for more diverse and structured sequence generation.

## Relationships

- **is_an_implementation_of**: [[variational-autoencoder|Variational Autoencoder]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*