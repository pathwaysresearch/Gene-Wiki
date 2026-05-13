---
type: concept
aliases: [Nesterov Accelerated Gradient]
summary: An optimization algorithm that improves upon standard Momentum by measuring the gradient after the momentum step, resulting in a more direct path to the minimum.
relationships:
  - target: yurii-nesterov
    type: is_named_for
tags: [optimization-algorithm, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Nesterov Accelerated Gradient

## Overview
Nesterov Accelerated Gradient (NAG), also known as Nesterov Momentum optimization, is an enhancement of the standard Momentum optimization algorithm. It will almost always speed up training compared to regular Momentum optimization.

## How It Works
Unlike regular Momentum, which first computes the gradient at the current position and then takes a large step in the direction of the momentum vector, NAG takes a slightly different approach. The Nesterov update first takes a step in the direction of the momentum vector and then measures the gradient at that new location. This adjusted gradient is then used to update the weights, which effectively corrects the course of the momentum vector. This correction helps the optimizer converge faster, especially in scenarios with elongated, valley-shaped cost functions, as it points more directly toward the global optimum.

## Implementation in Keras
In the Keras deep learning library, Nesterov Accelerated Gradient can be enabled when using the Stochastic Gradient Descent (SGD) optimizer. This is done by setting the `nesterov` parameter to `True` during the optimizer's instantiation, alongside the learning rate and momentum hyperparameters. For example: `optimizer = keras.optimizers.SGD(lr=0.001, momentum=0.9, nesterov=True)`.

## Relationships

- **is_named_for**: [[yurii-nesterov|Yurii Nesterov]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*