---
type: concept
aliases: [Sparse Coding]
summary: An unsupervised learning method that represents input data as a sparse linear combination of basis vectors, where the encoder is an optimization algorithm rather than a parametric function.
relationships:
  - target: linear-factor-model
    type: is_a
tags: [unsupervised-learning, feature-learning, sparse-representation, generative-model]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Sparse Coding

## Overview
Sparse coding is a linear factor model where the goal is to find a sparse representation (a 'code') for an input vector. Unlike models with a parametric encoder, the encoder in sparse coding is an optimization algorithm that solves for the most likely code value for a given input.

## Inference Process
The process of finding the code `h` for an input `x` involves solving an optimization problem. This problem is derived from maximizing the posterior probability `p(h|x)`, which is equivalent to minimizing a cost function. The cost function consists of two terms: a reconstruction error, `||x – Wh||_2^2`, and a sparsity penalty on the code, `λ||h||_1`. The use of the L1 norm as a penalty encourages most of the elements in the resulting code vector `h*` to be zero, thus making it sparse.

## Training the Model
Training the sparse coding model involves learning the weight matrix `W`. This is typically done through an iterative process that alternates between two steps. In the first step, the codes `h` are found for the input data while keeping `W` fixed. In the second step, the weight matrix `W` is updated to better reconstruct the data from the fixed codes `h`. The model includes hyperparameters, such as `λ` and `β`, which balance the trade-off between reconstruction accuracy and sparsity.

## Relationships

- **is_a**: [[linear-factor-model|Linear Factor Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*