---
type: concept
aliases: [Hard Mixture of Experts]
summary: A variation of the Mixture of Experts model where a gater network selects only a single expert network to process each input, significantly reducing computational cost.
relationships:
  - target: mixture-of-experts
    type: is-variation-of
tags: [model-architecture, efficiency, inference]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Hard Mixture of Experts

## Definition
The hard mixture of experts is a variant of the mixture of experts architecture. Unlike the standard "soft" mixture, where all experts contribute to the output via a weighted average, the hard mixture involves a gater network that selects only a single expert to compute the output for each given input.

## Key Advantage
The primary benefit of this approach is a considerable acceleration in both training and inference time. By activating only one expert per example, the computational load is significantly reduced compared to evaluating the entire ensemble of experts.

## Limitations
This strategy works well when the number of gating decisions is small. However, when the goal is to select different subsets of units or parameters, the problem becomes combinatorial. In such cases, it is not possible to use a "soft switch" that smoothly approximates the hard decision, because it would require enumerating and computing outputs for all possible configurations of the gater.

## Relationships

- **is-variation-of**: [[mixture-of-experts|Mixture Of Experts]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*