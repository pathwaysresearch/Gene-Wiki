---
type: concept
aliases: [Cybernetics]
summary: The first wave of neural networks research, characterized by simple linear models designed to associate a set of input values with an output by learning a set of weights.
relationships:
  - target: mcculloch-pitts-neuron
    type: includes_model
  - target: perceptron
    type: includes_model
  - target: adaline
    type: includes_model
  - target: connectionism
    type: preceded
tags: [history-of-ai, neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Cybernetics

## Overview
Cybernetics represents the earliest predecessors of modern deep learning and is the name given to the first wave of neural networks research. These early models were motivated from a neuroscientific perspective.

## Model Structure
Models from the cybernetics era were simple linear models. They were designed to take a set of n input values ($x_1, . . . , x_n$) and associate them with an output $y$. This was achieved by learning a set of weights ($w_1, . . . , w_n$) and computing their output as a weighted sum, $f(x, w) = x_1w_1 + \dots + x_nw_n$.

## Key Models
This first wave of research produced several foundational models. These include the McCulloch-Pitts Neuron, where weights were set by a human operator, and later models like the perceptron and the adaptive linear element (ADALINE), which could learn the weights from data.

## Relationships

- **includes_model**: [[mcculloch-pitts-neuron|Mcculloch Pitts Neuron]]
- **includes_model**: [[perceptron|Perceptron]]
- **includes_model**: [[adaline|Adaline]]
- **preceded**: [[connectionism|Connectionism]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*