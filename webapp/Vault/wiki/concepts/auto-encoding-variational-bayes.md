---
type: concept
aliases: [Auto-Encoding Variational Bayes]
summary: A deep generative model that combines an autoencoder architecture with Bayesian variational inference to learn a latent representation of data.
relationships:
  - target: diederik-p-kingma
    type: developed_by
  - target: max-welling
    type: developed_by
  - target: variational-inference
    type: uses
  - target: autoencoder
    type: related_to
tags: [deep-learning, generative-model, variational-inference, autoencoder]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Auto-Encoding Variational Bayes

## Definition
Auto-Encoding Variational Bayes, often referred to as the Variational Autoencoder (VAE), is a generative modeling framework introduced by Diederik P. Kingma and Max Welling in their 2014 paper. The text discusses this model in the context of deep generative models and inference, as indicated by the citations on pages 689 and 700.

## How It Works
The model leverages an autoencoder-like neural network structure for efficient, gradient-based inference. The paper by Kingma and Welling (2014a) details how this approach uses a recognition model (the encoder) to approximate the posterior distribution of latent variables, and a generative model (the decoder) to reconstruct the data. The citation of related work by the same authors (Kingma and Welling, 2014b; Kingma, 2013) on pages 689 and 696 suggests the text provides a thorough background on the inference techniques involved.

## Key Properties
A key aspect of this framework is its ability to perform efficient, amortized inference using gradient-based optimization. The citation of Opper and Archambeau (2009) on the variational Gaussian approximation (page 689) places the VAE within a broader context of variational inference methods, highlighting its connection to established principles in probabilistic machine learning.

## Relationships

- **developed_by**: [[diederik-p-kingma|Diederik P Kingma]]
- **developed_by**: [[max-welling|Max Welling]]
- **uses**: [[variational-inference|Variational Inference]]
- **related_to**: [[autoencoder|Autoencoder]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*