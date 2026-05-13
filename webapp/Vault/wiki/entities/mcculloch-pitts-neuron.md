---
type: entity
aliases: [McCulloch-Pitts Neuron]
summary: An early mathematical model of a biological neuron, proposed in 1943, that functions as a linear classifier with manually set weights.
relationships:
  - target: cybernetics
    type: is_a
tags: [neural-network-model, history-of-ai]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# McCulloch-Pitts Neuron

## Overview
The McCulloch-Pitts Neuron, developed by Warren McCulloch and Walter Pitts in 1943, was an early and influential model of brain function. It is considered a predecessor to modern neural networks.

## Functionality
This linear model was designed to recognize two different categories of inputs. It worked by computing a weighted sum of its inputs, $f(x, w)$, and testing whether the result was positive or negative to determine the category.

## Weight Configuration
A key characteristic of the McCulloch-Pitts Neuron was that its weights were not learned from data. Instead, the weights needed to be set correctly by a human operator for the model to correspond to the desired definition of the categories.

## Relationships

- **is_a**: [[cybernetics|Cybernetics]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*