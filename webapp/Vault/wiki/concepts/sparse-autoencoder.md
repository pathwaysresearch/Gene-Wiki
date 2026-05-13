---
type: concept
aliases: [Sparse Autoencoder]
summary: An autoencoder variant whose training criterion includes a sparsity penalty on the code layer, forcing the model to learn unique statistical features from the data.
relationships:
  - target: autoencoder
    type: subtype_of
tags: [autoencoder, unsupervised-learning, feature-learning, regularization, sparsity]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Sparse Autoencoder

## Definition
A sparse autoencoder is an autoencoder that is regularized by adding a sparsity penalty, `Ω(h)`, to its loss function. The total training objective becomes the sum of the reconstruction error and this sparsity penalty: `L(x, g(f(x))) + Ω(h)`. This encourages the hidden layer's activations (the code `h`) to be sparse, meaning most neurons are inactive.

## Purpose and Function
Sparse autoencoders are typically used to learn features for a subsequent task, such as classification. The sparsity constraint prevents the model from simply learning the identity function, where it would copy the input perfectly without extracting meaningful information. Instead, it must learn to capture unique statistical features of the dataset in a compressed, sparse representation. In this way, training to perform the copying task with a sparsity penalty yields a model that has learned useful features as a byproduct.

## Probabilistic Interpretation and Implementation
The sparsity penalty can be interpreted as corresponding to the log prior probability of the code, `log p_model(h)`, in a directed probabilistic model. A practical method for achieving true sparsity (i.e., actual zeros in the code layer) is to use rectified linear units (ReLUs) for the hidden layer's activation function, combined with a penalty like the absolute value penalty that actively pushes representations toward zero.

## Relationships

- **subtype_of**: [[autoencoder|Autoencoder]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*