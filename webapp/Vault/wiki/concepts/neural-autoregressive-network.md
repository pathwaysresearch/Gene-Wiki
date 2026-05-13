---
type: concept
aliases: [Neural Autoregressive Network]
summary: A class of generative models that models the joint distribution of variables by decomposing it into a product of conditional probabilities, where each variable is predicted from the preceding ones.
relationships:
  - target: neural-autoregressive-density-estimator
    type: is_a_type_of
tags: [generative-models, autoregressive-models, density-estimation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Neural Autoregressive Network

## Definition
A neural autoregressive network is a directed acyclic graphical model that predicts the $i$-th variable $x_i$ of a vector from the $i-1$ previous variables, $x_1, \dots, x_{i-1}$. It models the joint distribution $P(x)$ as a product of conditionals: $P(x) = \prod_i P(x_i | x_1, \dots, x_{i-1})$.

## Architecture
The model is parametrized such that features, represented by groups of hidden units $h_i$, are computed as functions of the preceding inputs $x_1, \dots, x_i$. These features can then be reused in the prediction of all subsequent variables $x_j$ where $j > i$. This structure allows for efficient computation and sharing of learned representations across the sequence of predictions.

## Comparison to Linear Models
Neural autoregressive networks are a powerful extension of linear auto-regressive networks. While linear autoregressive models can be trained with convex loss functions and sometimes have closed-form solutions, their capacity is limited. Neural autoregressive networks overcome this limitation by using the expressive power of neural networks to model the conditional distributions, allowing for much greater model capacity.

## Relationships

- **is_a_type_of**: [[neural-autoregressive-density-estimator|Neural Autoregressive Density Estimator]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*