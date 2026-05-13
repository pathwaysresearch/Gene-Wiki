---
type: concept
aliases: [Variance Normalization]
summary: A heuristic technique used with the REINFORCE algorithm to stabilize training by adaptively rescaling the reinforcement signal based on its running standard deviation.
relationships:
  - target: reinforce-algorithm
    type: improves
  - target: variance-reduction
    type: is_a
tags: [training-heuristic, variance-reduction, reinforcement-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Variance Normalization

## Definition
Variance normalization is a heuristic used to improve the stability and performance of the REINFORCE algorithm. It is a form of variance reduction that acts as an adaptive learning rate for the reinforcement signal.

## How It Works
In REINFORCE, the gradient update often involves a term of the form \((J(y) - b(\omega))\), where \(J(y)\) is the cost and \(b(\omega)\) is a baseline used for variance reduction. The magnitude of this term can vary significantly during training. Variance normalization addresses this by dividing this term by its standard deviation. This standard deviation is typically estimated using a moving average calculated throughout the training process.

## Purpose
The primary goal of variance normalization is to counteract the effect of large fluctuations in the magnitude of the reinforcement signal. By normalizing this signal, the technique helps to stabilize the training process, preventing erratic updates and potentially leading to faster and more reliable convergence. Mnih and Gregor (2014) named this heuristic in their work on deep learning models.

## Relationships

- **improves**: [[reinforce-algorithm|Reinforce Algorithm]]
- **is_a**: [[variance-reduction|Variance Reduction]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*