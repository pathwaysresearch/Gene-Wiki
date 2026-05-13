---
type: concept
aliases: [Causal Chains]
summary: A fundamental causal structure in a diagram where one variable affects another through an intermediary variable, known as a mediator.
relationships:
  - target: bayesian-networks
    type: is_a_structure_in
tags: [causality, graphical-models, mediation]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Causal Chains

## Definition

A causal chain is a basic junction in a causal diagram represented as A → B → C. In this structure, the variable B is considered the mechanism or "mediator" that transmits the effect of A to C.

## Example

The text provides the example of Fire → Smoke → Alarm. The fire does not directly cause the alarm; it causes smoke, and the smoke, in turn, triggers the alarm. Smoke is the mediator in this chain. If the link between fire and alarm via smoke is disabled (e.g., by a fume hood), the fire will not cause an alarm.

## Key Property: Screening Off

A key property of a chain, first pointed out by Hans Reichenbach, is that the mediator B "screens off" information about A from C. Once the state of the mediator is known, information about the initial cause provides no additional information about the final effect. For instance, once we know there is smoke, knowing whether there is a fire does not change our belief about whether the alarm will sound.

## Relationships

- **is_a_structure_in**: [[bayesian-networks|Bayesian Networks]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*