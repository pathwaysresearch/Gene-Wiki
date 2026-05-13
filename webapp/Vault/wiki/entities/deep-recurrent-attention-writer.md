---
type: entity
aliases: [Deep Recurrent Attention Writer (DRAW)]
summary: A sophisticated Variational Autoencoder model that uses recurrent networks and an attention mechanism to generate images sequentially.
relationships:
  - target: variational-autoencoder
    type: is_an_implementation_of
tags: [generative-model, vae, recurrent-networks, attention-mechanism]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Deep Recurrent Attention Writer (DRAW)

## Overview
The Deep Recurrent Attention Writer (DRAW) model (Gregor et al., 2015) is a particularly sophisticated implementation of the Variational Autoencoder (VAE) framework. It is designed for image generation and demonstrates the flexibility of the VAE architecture.

## Architecture
The DRAW model is built with a recurrent encoder and a recurrent decoder. A key feature of its architecture is the inclusion of an attention mechanism.

## Generation Process
The generation process in a DRAW model is sequential and iterative. Instead of generating the entire image at once, the model sequentially visits different small patches of the image canvas. At each step, guided by the attention mechanism, it draws the values of the pixels at those specific points, gradually constructing the final image.

## Relationships

- **is_an_implementation_of**: [[variational-autoencoder|Variational Autoencoder]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*