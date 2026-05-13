---
type: concept
aliases: [Manifold Learning]
summary: A class of dimensionality reduction algorithms that assume high-dimensional data lies on a lower-dimensional manifold, which they attempt to model and "unroll".
relationships:
  - target: representation-learning
    type: is_a_subfield_of
  - target: curse-of-dimensionality
    type: addresses
tags: [dimensionality-reduction, unsupervised-learning, non-linear]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Manifold Learning

## Definition
Manifold learning is an approach to dimensionality reduction that works by modeling the lower-dimensional manifold on which the training instances are assumed to lie. A d-dimensional manifold is a part of an n-dimensional space (where d < n) that locally resembles a d-dimensional hyperplane.

## The Manifold Hypothesis
This approach is based on the idea that many real-world high-dimensional datasets, like the "Swiss roll" example, are actually a lower-dimensional shape that has been bent and twisted in the higher-dimensional space. The goal is to find a low-dimensional representation that preserves the intrinsic structure of this manifold.

## Application in Dimensionality Reduction
Manifold learning algorithms aim to "unroll" the manifold to obtain a more useful, lower-dimensional representation of the data. This is contrasted with simpler techniques like direct projection, which can fail by squashing together distinct parts of the manifold, thereby losing important information.

## Relationships

- **addresses**: [[curse-of-dimensionality|Curse Of Dimensionality]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*