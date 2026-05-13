---
type: concept
aliases: [Denoising Autoencoder]
summary: An autoencoder trained to reconstruct a clean input from a stochastically corrupted version of it, forcing it to learn robust features that capture the data manifold.
relationships:
  - target: autoencoder
    type: subtype_of
tags: [autoencoder, unsupervised-learning, feature-learning, robustness, generative-model]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Denoising Autoencoder

## Definition
A denoising autoencoder (DAE) is a stochastic variant of the autoencoder. Its training process involves first corrupting an input data point `x` to get a noisy version `x̃` through a stochastic mapping `C(x̃|x)`. The DAE is then trained to take `x̃` as input and reconstruct the original, uncorrupted data point `x`.

## How It Works
By forcing the model to undo the corruption process, the DAE cannot simply learn an identity mapping. Instead, it must learn the underlying structure of the data distribution, often referred to as the data manifold. The model learns a vector field that effectively pulls corrupted data points away from low-probability regions and back towards the manifold of high-probability data. This process forces the DAE to capture robust and meaningful features.

## Training Objective
The DAE is trained by minimizing the reconstruction error, which can be formulated as minimizing the negative log-likelihood `-log p_decoder(x | h = f(x̃))`. This objective is an expectation over both the training data distribution and the corruption process. As long as the encoder `f` is deterministic, the DAE is a feedforward network and can be trained with standard techniques like stochastic gradient descent.

## Relationships

- **subtype_of**: [[autoencoder|Autoencoder]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*