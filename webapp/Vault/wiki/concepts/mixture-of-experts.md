---
type: concept
aliases: [Mixture of Experts]
summary: A neural network architecture where a "gater" network selects a combination of several specialized "expert" networks to compute the output for a given input.
relationships:
  - target: hard-mixture-of-experts
    type: has-variant
tags: [model-architecture, ensemble-methods]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Mixture of Experts

## Architecture
The Mixture of Experts (MoE) architecture involves multiple "expert" networks and a "gater" network. For a given input, the gater network determines how to combine the outputs of the various experts.

## How It Works
In the standard or "soft" version of MoE, the gater network uses a softmax nonlinearity to output a set of probabilities or weights, one for each expert. The final output of the entire system is a weighted combination of the outputs from all the expert networks, using the weights provided by the gater.

## Computational Cost
This standard implementation of MoE does not offer a reduction in computational cost compared to a single large model. Because the final output is a weighted sum of all expert outputs, every expert must be evaluated for every input example. This is in contrast to the "hard" mixture of experts, which does provide computational savings.

## Relationships

- **has-variant**: [[hard-mixture-of-experts|Hard Mixture Of Experts]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*