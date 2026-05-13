---
type: concept
aliases: [Autoencoder]
summary: A type of representation learning algorithm consisting of an encoder that converts input data into a new representation and a decoder that converts it back to the original format. A type of artificial neural network used for unsupervised learning of efficient data codings, typically for dimensionality reduction or feature learning, by learning to reconstruct its own input.
relationships:
  - target: representation-learning
    type: is_a
  - target: feedforward-network
    type: is_a
  - target: sparse-autoencoder
    type: has_subtype
  - target: denoising-autoencoder
    type: has_subtype
tags: [neural-network, representation-learning, unsupervised-learning, dimensionality-reduction, feature-learning, generative-model]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Autoencoder

## Definition
The autoencoder is described as the quintessential example of a representation learning algorithm. Its core purpose is to learn a compressed or different representation of input data automatically.

## Architecture
An autoencoder is composed of two main parts. It includes an encoder function that converts the input data into a different representation, often of a lower dimension. It also includes a decoder function that takes this new representation and converts it back into the original format.

## Training
While the provided text is cut short, it states that autoencoders are trained to perform this encoding-decoding process. The goal is typically to reconstruct the original input as accurately as possible, forcing the encoder to learn a useful and informative representation of the data.

## Relationships

- **is_a**: [[representation-learning|Representation Learning]]
- **is_a**: [[feedforward-network|Feedforward Network]]
- **has_subtype**: [[sparse-autoencoder|Sparse Autoencoder]]
- **has_subtype**: [[denoising-autoencoder|Denoising Autoencoder]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*