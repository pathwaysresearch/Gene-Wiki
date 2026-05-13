---
type: concept
aliases: [Wake-Sleep Algorithm]
summary: An algorithm for training a generative model and an associated inference network by alternating between a 'wake' phase that learns model parameters and a 'sleep' phase that trains the inference network.
tags: [generative-models, unsupervised-learning, approximate-inference]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Wake-Sleep Algorithm

## Problem Solved
The wake-sleep algorithm addresses a primary difficulty in training a model to infer latent variables $\boldsymbol{h}$ from visible variables $\boldsymbol{v}$: the lack of a supervised training set of $(\boldsymbol{v}, \boldsymbol{h})$ pairs. The mapping from $\boldsymbol{v}$ to $\boldsymbol{h}$ is unknown and changes as the model parameters $\boldsymbol{\theta}$ are learned.

## Algorithm Phases
The algorithm resolves this by generating its own training data. In what can be considered the 'sleep' phase, the generative model is used to draw samples of both $\boldsymbol{h}$ and $\boldsymbol{v}$, for example by performing ancestral sampling in a directed model. The inference network is then trained in a supervised manner to perform the reverse mapping: predicting the $\boldsymbol{h}$ that caused the sampled $\boldsymbol{v}$. The 'wake' phase (not detailed in the excerpts) would involve updating the generative model's parameters based on real data.

## Key Drawback
The main drawback of this approach is that the inference network is trained only on samples $\boldsymbol{v}$ that have high probability under the current generative model. Early in the learning process, the model's distribution will not resemble the true data distribution. Consequently, the inference network does not get an opportunity to learn how to perform inference on samples that are representative of the actual data.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*