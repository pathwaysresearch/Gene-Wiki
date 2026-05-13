---
type: concept
aliases: [Vanishing and Exploding Gradient Problem]
summary: A difficulty found in training deep neural networks, especially RNNs, where gradients passed back through many layers either shrink to zero (vanish) or grow uncontrollably (explode).
relationships:
  - target: recurrent-neural-network
    type: is-a-challenge-for
tags: [optimization, deep-learning-challenges, rnn-training]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Vanishing and Exploding Gradient Problem

## Definition
The vanishing and exploding gradient problem refers to the issue where gradients, during back-propagation, can decrease or increase exponentially as a function of the number of layers or time steps they pass through. This phenomenon is particularly acute in recurrent neural networks due to the repeated application of the same weight matrix over many time steps. It was independently discovered by researchers including Hochreiter (1991) and Bengio et al. (1993, 1994).

## Cause in RNNs
In an RNN, the gradient signal is propagated backward through time. This process involves repeatedly multiplying by the Jacobian of the hidden-to-hidden transition. If the eigenvalues of this Jacobian matrix have magnitudes (spectral radius) greater than 1, the norm of the gradient will grow exponentially, leading to an 'exploding' gradient. Conversely, if the magnitudes are less than 1, the gradient norm will shrink exponentially, leading to a 'vanishing' gradient. This makes it extremely difficult for the model to learn dependencies between distant time steps.

## Consequences and Trade-offs
Exploding gradients can cause unstable updates to the weights, while vanishing gradients prevent the weights from being updated effectively, stopping the learning of long-term patterns. The text points out a fundamental dilemma: for an RNN to store memories in a way that is robust to small perturbations, it must operate in a region of its parameter space where gradients tend to vanish. This means that the very stability required for memory storage exacerbates the problem of learning long-term dependencies.

## Relationships

- **is-a-challenge-for**: [[recurrent-neural-network|Recurrent Neural Network]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*