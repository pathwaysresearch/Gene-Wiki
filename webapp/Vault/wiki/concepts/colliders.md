---
type: concept
aliases: [Colliders]
summary: A causal structure where two independent causes converge on a common effect (A → C ← B), which can induce a spurious correlation between the causes when conditioning on the effect.
relationships:
  - target: bayesian-networks
    type: is_a_structure_in
tags: [causality, graphical-models, selection-bias, collider-bias]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Colliders

## Definition

A collider is a junction in a causal diagram where two or more arrows point to the same node, such as A → C ← B. In this structure, A and B are independent causes of a common effect, C.

## The Explain-Away Effect

Conditioning on a collider (the common effect) can create a spurious negative correlation between its causes, a phenomenon also known as collider bias. If the effect is observed, a high value for one cause "explains away" the effect, making the other cause seem less likely. This happens even if the causes are unrelated in the population as a whole.

## Example

The text uses the example of Celebrity status being caused by Talent and Beauty (Talent → Celebrity ← Beauty). While talent and beauty may be unrelated in general, among the subpopulation of celebrities, they become negatively correlated. A celebrity with very low acting talent must possess great beauty to explain their success, and vice-versa.

## Relationships

- **is_a_structure_in**: [[bayesian-networks|Bayesian Networks]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*