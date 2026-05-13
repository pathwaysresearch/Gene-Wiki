---
type: concept
aliases: [Deep Belief Network]
summary: A generative model with multiple layers of latent variables, historically significant for being one of the first deep architectures to be trained successfully, sparking the modern deep learning renaissance.
relationships:
  - target: deep-boltzmann-machine
    type: related_to
  - target: generative-model
    type: is_a
tags: [generative-model, unsupervised-learning, historical-model]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Deep Belief Network

## Historical Significance
The introduction of Deep Belief Networks (DBNs) in 2006 is credited with beginning the current deep learning renaissance. Prior to DBNs, deep models were considered too difficult to optimize, and the research landscape was dominated by methods like kernel machines. DBNs demonstrated the success of deep architectures by outperforming kernelized support vector machines on the MNIST dataset. While now largely superseded by other models and rarely used, they hold an important place in deep learning history.

## Architecture
A DBN is a generative model composed of several layers of latent variables, which are typically binary. The visible units, which represent the data, can be binary or real. A key architectural feature is the absence of connections between units within the same layer (no intralayer connections). Typically, every unit in a given layer is connected to every unit in its neighboring layers.

## Approximate Inference
Exact inference in DBNs is intractable. A common approach uses a multi-layer perceptron (MLP) for approximate inference, which is a heuristic choice that propagates information upward from the visible units to the deepest hidden layer. This method is a simplification that ignores important interactions within the DBN's graphical model, such as "explaining away" effects among hidden units in the same layer and top-down influences from deeper layers. Consequently, the variational bound on the log-likelihood it provides may not be very tight.

## Relationships

- **related_to**: [[deep-boltzmann-machine|Deep Boltzmann Machine]]
- **is_a**: [[generative-model|Generative Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*