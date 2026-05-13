---
type: concept
aliases: [Contractive Autoencoder]
summary: An autoencoder variant regularized to be insensitive to small perturbations in its input, thereby learning robust features that capture the local data manifold.
relationships:
  - target: manifold-learning
    type: is_a_method_for
tags: [autoencoder, regularization, unsupervised-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Contractive Autoencoder

## Definition
A Contractive Autoencoder (CAE) is a type of autoencoder that adds a regularization penalty to its reconstruction cost. This penalty is based on the Frobenius norm of the Jacobian matrix of the encoder's activations with respect to the input. The goal is to make the learned representation robust by training the model to resist small perturbations of its input data.

## The Contractive Property
The name "contractive" stems from the model's tendency to map a neighborhood of input points to a smaller neighborhood of output points. This contraction is a local property: all perturbations of a given training point `x` are mapped to a small region around its encoding `f(x)`. However, the global mapping may be expansive, meaning two distant points `x` and `x'` can be mapped to encodings that are even farther apart than the original points.

## Implementation and Behavior
When the contractive penalty is applied to hidden layers with sigmoidal activation units, one way the model minimizes the penalty is by pushing the units to saturate (i.e., approach values of 0 or 1). This encourages the CAE to learn encodings that resemble a binary code and utilize the full span of the representational space. To prevent a trivial solution where the encoder simply shrinks the code and the decoder learns to reverse it, the decoder's weights are often tied to be the transpose of the encoder's weights.

## Relationships

- **is_a_method_for**: [[manifold-learning|Manifold Learning]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*