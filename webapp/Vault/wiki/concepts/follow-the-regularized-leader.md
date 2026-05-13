---
type: concept
aliases: [Follow The Regularized Leader (FTRL)]
summary: An optimization algorithm, proposed by Yurii Nesterov, that is particularly effective at producing very sparse models when combined with L1 regularization.
relationships:
  - target: l1-regularization
    type: is_used_with
  - target: yurii-nesterov
    type: created_by
tags: [optimization-algorithm, sparsity, model-training]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Follow The Regularized Leader (FTRL)

## Overview
Follow The Regularized Leader (FTRL), also known as Dual Averaging, is an optimization technique proposed by Yurii Nesterov. It is designed for training sparse models and serves as an alternative to more common optimizers like Adam or SGD when the primary goal is a model with a large number of zero-valued weights.

## Application for Sparsity
The key application of FTRL is in scenarios where model sparsity is critical, for example, to create a low-latency model or one that requires less memory. While strong L1 regularization with other optimizers can induce some sparsity, FTRL is often used when those methods are insufficient. The combination of FTRL with L1 regularization is particularly effective at driving many model weights to exactly zero.

## Implementation and Considerations
Keras provides an implementation of a variant of this technique called FTRL-Proximal in its `FTRL` optimizer. When choosing to use FTRL for sparsity, it's important to note that it can interfere with other architectural features. For instance, using FTRL will break the self-normalization property of networks using SELU activations, necessitating a switch to other techniques like Batch Normalization for deep networks.

## Relationships

- **is_used_with**: [[l1-regularization|L1 Regularization]]
- **created_by**: [[yurii-nesterov|Yurii Nesterov]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*