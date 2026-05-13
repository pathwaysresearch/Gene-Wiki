---
type: concept
aliases: [Expectation-Maximization (EM) Algorithm]
summary: An iterative method for finding maximum likelihood estimates of parameters in statistical models, where the model depends on unobserved latent variables.
relationships:
  - target: latent-variable-models
    type: is_used_for_training
  - target: map-inference
    type: is_related_to
  - target: variational-inference
    type: is_related_to
  - target: gaussian-mixture-model
    type: used_by
  - target: k-means
    type: is_a_generalization_of
tags: [optimization-algorithm, machine-learning, statistics]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Expectation-Maximization (EM) Algorithm

## Overview
The Expectation-Maximization (EM) algorithm is an iterative method used to train probabilistic models like Gaussian Mixture Models. It has many similarities with the K-Means algorithm but is considered a generalization of it.

## How It Works
The algorithm begins by initializing the cluster parameters randomly. It then repeats two steps until it converges. The first is the 'expectation step,' where it assigns instances to clusters. The second is the 'maximization step,' where it updates the cluster parameters based on the new assignments. This two-step process is repeated until the model parameters stabilize.

## Comparison with K-Means
EM can be thought of as a more general version of K-Means. While K-Means only finds the cluster centers, EM also determines their size, shape, and orientation (covariance matrices), as well as their relative weights. A key distinction is that EM uses 'soft' cluster assignments, where it estimates the probability that an instance belongs to each cluster. In contrast, K-Means uses 'hard' assignments, definitively assigning each instance to a single cluster.

## Relationships

- **used_by**: [[gaussian-mixture-model|Gaussian Mixture Model]]
- **is_a_generalization_of**: [[k-means|K Means]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*