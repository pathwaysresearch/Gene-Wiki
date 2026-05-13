---
type: concept
aliases: [Greedy Layer-Wise Pretraining]
summary: A training methodology for deep generative models like DBMs, where each layer is trained sequentially and in isolation before the entire network is trained jointly.
relationships:
  - target: deep-boltzmann-machine
    type: is_method_for
  - target: restricted-boltzmann-machine
    type: uses
tags: [training-method, unsupervised-learning, pretraining]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Greedy Layer-Wise Pretraining

## Purpose
Greedy layer-wise pretraining is a technique developed to overcome the difficulties of jointly training deep models like Deep Boltzmann Machines (DBMs) from a random initialization. It provides a better starting point for the model's parameters before a final joint training or fine-tuning phase. It was the original and most popular method for training DBMs.

## Procedure
The method involves training the deep model one layer at a time. The first layer is trained in isolation as a Restricted Boltzmann Machine (RBM) to model the input data. Each subsequent layer is then trained as an RBM, but instead of using the raw data, it is trained to model samples drawn from the posterior distribution of the previously trained RBM layer. This process is repeated for all layers in the network.

## Limitations
A significant drawback of this approach is the difficulty in monitoring the performance of the complete, multi-layer model during the pretraining phase. Since only one layer is being trained at a time, it is hard to evaluate properties of the full DBM, which makes it challenging to set hyperparameters effectively for the final model.

## Relationships

- **is_method_for**: [[deep-boltzmann-machine|Deep Boltzmann Machine]]
- **uses**: [[restricted-boltzmann-machine|Restricted Boltzmann Machine]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*