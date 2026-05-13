---
type: entity
aliases: [Neural Autoregressive Density Estimator (NADE)]
summary: A specific type of neural autoregressive model where hidden units are organized into groups to efficiently compute conditional probabilities.
relationships:
  - target: neural-autoregressive-network
    type: is_an_implementation_of
tags: [generative-model, autoregressive-model, density-estimation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Neural Autoregressive Density Estimator (NADE)

## Overview
The Neural Autoregressive Density Estimator (NADE) is a specific architecture for a neural autoregressive network. It is designed to efficiently model the probability distribution of data by decomposing it into a product of conditionals.

## Architecture
NADE's key architectural feature is the organization of its hidden units into groups, denoted $h^{(i)}$. This structure imposes a specific connectivity pattern: only the inputs $x_1, \dots, x_i$ are involved in the computation of the hidden unit group $h^{(i)}$.

## Computation
This grouped structure allows for efficient computation of the conditional probabilities. The features computed in group $h^{(i)}$ are used to help predict all subsequent conditional probabilities $P(x_j | x_{j-1}, \dots, x_1)$ for all $j > i$. This distinguishes NADE from earlier neural autoregressive models.

## Relationships

- **is_an_implementation_of**: [[neural-autoregressive-network|Neural Autoregressive Network]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*