---
type: concept
aliases: [Deep Boltzmann Machine]
summary: A deep generative model with multiple layers of hidden units where connections are undirected, unlike in Deep Belief Networks. It is a type of Boltzmann machine with a more complex structure than an RBM. A type of generative model using a layered network of symmetrically coupled stochastic units, often used for multimodal learning and modeling complex data distributions.
relationships:
  - target: deep-belief-network
    type: related_to
  - target: greedy-layer-wise-pretraining
    type: uses
  - target: mean-field-approximation
    type: uses
  - target: boltzmann-machine
    type: is_a
  - target: geoffrey-hinton
    type: developed_by
  - target: unsupervised-learning
    type: is_a_method_for
tags: [generative-model, unsupervised-learning, boltzmann-machine]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Deep Boltzmann Machine

## Overview and Structure
Deep Boltzmann Machines (DBMs) are deep generative models developed after Deep Belief Networks. A key difference is that in DBMs, all hidden units within a single layer are conditionally independent given the states of the other layers. This property simplifies the posterior distribution P(h|v) compared to DBNs, which counterintuitively allows for richer and more accurate approximations of this posterior.

## Training Challenges
Training a DBM from a random initialization using standard stochastic maximum likelihood is known to be difficult and often results in failure. The model may either fail to learn the data distribution adequately or converge to a state where it effectively functions as a single-layer Restricted Boltzmann Machine (RBM), with the weights in deeper layers being negligible.

## Training Strategies
The most popular and original method to train DBMs is greedy layer-wise pretraining, where each layer is trained sequentially as an RBM. After pretraining, the full model can be trained jointly. Alternatives to pretraining, such as joint training methods, have also been developed. One such technique is the multi-prediction DBM (MP-DBM), which trains the mean field inference process directly using back-propagation. Another helpful technique is the centering trick, which reparameterizes the energy function to improve the dynamics of stochastic gradient descent.

## Relationships

- **related_to**: [[deep-belief-network|Deep Belief Network]]
- **uses**: [[greedy-layer-wise-pretraining|Greedy Layer Wise Pretraining]]
- **uses**: [[mean-field-approximation|Mean Field Approximation]]
- **is_a**: [[boltzmann-machine|Boltzmann Machine]]
- **developed_by**: [[geoffrey-hinton|Geoffrey Hinton]]
- **is_a_method_for**: [[unsupervised-learning|Unsupervised Learning]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*